"""Pinned five-record Scento adapter for private, unselected offline review.

No application, database, scorer or transport dependency is used. Synthetic
parser/extractor helpers cannot bypass the publisher's six immutable byte pins.
Local publication assumes no hostile process can replace directory ancestors
during an operation. Existing symlinks and Windows reparse points are rejected.
An interrupted publisher can leave a lock: inspect it manually, never auto-steal.
File fsync and atomic pointer replacement protect process interruption; this is
not a promise of directory-entry durability through machine/power failure.
"""
from __future__ import annotations

from contextlib import contextmanager
import csv
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import stat
import uuid


REVISION = '086769ecf1add770ea6646bd4d88d39f0e7cddeb'
TRANSFORM = 'enr-pinned-scento-preview-1'
SCHEMA = 'enr-pinned-scento-preview-schema-1'
PRIVATE_RELATIVE = Path('.local/imp-enr-01/preview-private')


@dataclass(frozen=True)
class Pin:
    name: str
    size: int
    sha256: str


@dataclass(frozen=True)
class Table:
    header: tuple[str, ...]
    fields: tuple[str, ...]
    count: int


@dataclass(frozen=True)
class Selection:
    file: str
    key: str
    ordinal: int


@dataclass(frozen=True)
class Artifact:
    name: str
    data: bytes


@dataclass(frozen=True)
class Snapshot:
    revision: str
    artifacts: tuple[Artifact, ...]


@dataclass(frozen=True)
class Publication:
    bundle_name: str
    payload_sha256: str


PINS = (
    Pin('perfumes.csv',780683,'726a1a2af8aef42d801b424b086415b50f6ca33dd2189d6fbd2bcbcb442bf8e5'),
    Pin('houses.csv',29765,'f076db1629fc1c07fe417811a55891bbfe70991319bf5c520766253f80cc9c18'),
    Pin('materials.csv',87027,'9b342c803f0b370e96106a4dff0ae56f1f5340bdc82c6e32d180473a9f31764c'),
    Pin('LICENSE',188,'7be5a0aac3f6a1803ae0a950624941a74b4a17c54ab3c9272ef8f61ebb8efc84'),
    Pin('README.md',2799,'c925d4b50cefde8038706125e9296d07270ca98bd6bcafd079ced9a77cf5c688'),
    Pin('datapackage.json',4845,'c4f072d7486a9f64b24502b7b53862e9fad61a2d79943d0ae6525d97f3f30bc2'),
)
TABLES = (
    ('perfumes.csv',Table(
        ('id','name','house_id','house','year','perfumers','concentration','family','secondary_family','character',
         'seasons','times_of_day','top_notes','heart_notes','base_notes','notes','description','popularity_rank','url'),
        ('id','name','house_id','house','year','concentration','family','secondary_family',
         'top_notes','heart_notes','base_notes','notes','url'),1479)),
    ('houses.csv',Table(('id','name','country','founded','type','portrait','perfume_count','url'),
                        ('id','name','country','founded','type','url'),160)),
    ('materials.csv',Table(('id','name','aliases','material_family','origin','smell','url'),
                           ('id','name','aliases','material_family','origin','smell','url'),420)),
)
SELECTIONS = (
    Selection('perfumes.csv','afnan-9-am',644),
    Selection('perfumes.csv','afnan-9-am-dive',645),
    Selection('houses.csv','afnan',3),
    Selection('materials.csv','mint',257),
    Selection('materials.csv','bergamot',46),
)


class PreviewError(ValueError):
    """Sanitized classification only: never include raw fields or private paths."""

    def __init__(self, code: str):
        self.code = code
        super().__init__(code)


def _is_reparse(info: os.stat_result) -> bool:
    return stat.S_ISLNK(info.st_mode) or bool(getattr(info,'st_file_attributes',0) & stat.FILE_ATTRIBUTE_REPARSE_POINT)


def _safe_path(path: Path, *, must_exist: bool = True) -> Path:
    path = Path(path)
    if not path.is_absolute() or '..' in path.parts or path.drive.startswith(('\\\\','//')):
        raise PreviewError('UNSAFE_PATH')
    for part in reversed((path,) + tuple(path.parents)):
        try:
            info = os.lstat(part)
        except FileNotFoundError:
            if must_exist:
                raise PreviewError('UNSAFE_PATH') from None
            continue
        except OSError:
            raise PreviewError('UNSAFE_PATH') from None
        if _is_reparse(info):
            raise PreviewError('UNSAFE_PATH')
    return path


def _read_regular(path: Path) -> bytes:
    _safe_path(path)
    try:
        # O_NOFOLLOW is available on POSIX. Windows reparse checks above and
        # descriptor metadata checks below supplement the local trust boundary.
        descriptor = os.open(path,os.O_RDONLY | getattr(os,'O_BINARY',0) | getattr(os,'O_NOFOLLOW',0))
        with os.fdopen(descriptor,'rb') as handle:
            if not stat.S_ISREG(os.fstat(handle.fileno()).st_mode):
                raise PreviewError('UNSAFE_PATH')
            data = handle.read()
        _safe_path(path)
        return data
    except OSError:
        raise PreviewError('SOURCE_READ_FAILED') from None


def _verify_snapshot(snapshot: Snapshot) -> None:
    if snapshot.revision != REVISION:
        raise PreviewError('SOURCE_REVISION')
    if tuple(a.name for a in snapshot.artifacts) != tuple(p.name for p in PINS):
        raise PreviewError('ARTIFACT_SCOPE')
    for artifact,pin in zip(snapshot.artifacts,PINS):
        if type(artifact.data) is not bytes or len(artifact.data) != pin.size or hashlib.sha256(artifact.data).hexdigest() != pin.sha256:
            raise PreviewError('PIN_MISMATCH')


def load_snapshot(source: Path, revision: str = REVISION) -> Snapshot:
    """Read all six exact files once, verify all pins before any parsing."""
    if revision != REVISION:
        raise PreviewError('SOURCE_REVISION')
    root = _safe_path(source)
    if not root.is_dir():
        raise PreviewError('UNSAFE_PATH')
    snapshot = Snapshot(revision,tuple(Artifact(pin.name,_read_regular(root/pin.name)) for pin in PINS))
    _verify_snapshot(snapshot)
    return snapshot


def parse_csv(name: str, raw: bytes, expected_count: int) -> tuple[dict[str,str], ...]:
    """Strict literal parser; count override exists only for synthetic controls."""
    tables = dict(TABLES)
    if name not in tables:
        raise PreviewError('ARTIFACT_SCOPE')
    try:
        text = raw.decode('utf-8',errors='strict')
    except UnicodeError:
        raise PreviewError('CSV_ENCODING') from None
    _validate_csv_quotes(text)
    try:
        records = csv.reader(io.StringIO(text,newline=''),strict=True)
        if tuple(next(records,())) != tables[name].header:
            raise PreviewError('CSV_HEADER')
        rows: list[dict[str,str]] = []
        identifiers: set[str] = set()
        for values in records:
            if len(values) != len(tables[name].header):
                raise PreviewError('CSV_SHAPE')
            row = dict(zip(tables[name].header,values))
            if row['id'] == '':
                raise PreviewError('CSV_MISSING_ID')
            if row['id'] in identifiers:
                raise PreviewError('CSV_DUPLICATE_ID')
            identifiers.add(row['id'])
            rows.append(row)
    except csv.Error:
        raise PreviewError('CSV_SYNTAX') from None
    if len(rows) != expected_count:
        raise PreviewError('CSV_COUNT')
    return tuple(rows)


def _validate_csv_quotes(text: str) -> None:
    """Reject bare quotes/NULs accepted permissively by csv.reader.

    Newlines inside quoted fields stay literal; csv.reader remains responsible
    for logical record boundaries, field decoding and exact row shape.
    """
    state = 'start'
    for character in text:
        if character == '\x00':
            raise PreviewError('CSV_SYNTAX')
        if state == 'quoted':
            if character == '"':
                state = 'closed'
        elif state == 'closed':
            if character == '"':
                state = 'quoted'
            elif character in ',\r\n':
                state = 'start'
            else:
                raise PreviewError('CSV_SYNTAX')
        elif character in ',\r\n':
            state = 'start'
        elif character == '"':
            if state != 'start':
                raise PreviewError('CSV_SYNTAX')
            state = 'quoted'
        else:
            state = 'unquoted'
    if state == 'quoted':
        raise PreviewError('CSV_SYNTAX')


def parse_snapshot(snapshot: Snapshot) -> tuple[tuple[str,tuple[dict[str,str], ...]], ...]:
    _verify_snapshot(snapshot)
    artifacts = {artifact.name:artifact.data for artifact in snapshot.artifacts}
    return tuple((name,parse_csv(name,artifacts[name],table.count)) for name,table in TABLES)


def select_records(tables: tuple[tuple[str,tuple[dict[str,str], ...]], ...],
                   selections: tuple[Selection, ...] = SELECTIONS) -> tuple[tuple[Selection,dict[str,str]], ...]:
    """Select by both immutable source key and logical data ordinal."""
    if selections != SELECTIONS:
        raise PreviewError('SELECTION_SCOPE')
    sources = dict(tables)
    selected = []
    for selection in SELECTIONS:
        try:
            row = sources[selection.file][selection.ordinal-1]
        except (KeyError,IndexError):
            raise PreviewError('LOCATOR_MISMATCH') from None
        if row.get('id') != selection.key:
            raise PreviewError('LOCATOR_MISMATCH')
        selected.append((selection,row))
    return tuple(selected)


def field_evidence(selection: Selection, field: str, raw: str) -> dict:
    """Literal extraction only; no stripping, normalization or interpretation."""
    domains = {'top_notes':'Top','heart_notes':'Heart','base_notes':'Base','notes':'General','aliases':'Aliases'}
    pin = next((p for p in PINS if p.name == selection.file),None)
    if (pin is None or selection not in SELECTIONS or field not in dict(TABLES)[selection.file].fields
            or not isinstance(raw,str)):
        raise PreviewError('FIELD_INPUT')
    present = raw != ''
    return {
        'source_dataset':'Scento Perfume Database','source_revision':REVISION,
        'source_file':selection.file,'file_sha256':pin.sha256,'data_ordinal':selection.ordinal,
        'source_key':selection.key,'field_locator':field,
        'original_value_state':'PRESENT' if present else 'MISSING',
        'raw_value':raw if present else None,
        'domain':domains.get(field),'closure':'UNKNOWN',
        'occurrences':[{'ordinal':i,'raw_token':token} for i,token in enumerate(raw.split(';'),1)]
                      if present and field in domains else None,
        'mapping':'UNMAPPED','selection':'UNSELECTED','review_outcome':'UNKNOWN','reviewed_at':None,
        'transform_version':TRANSFORM,'schema_version':SCHEMA,
    }


def transform_snapshot(snapshot: Snapshot) -> dict:
    """Revalidate immutable bytes, then emit exactly five records / 46 slots."""
    rows = parse_snapshot(snapshot)
    records = []
    for selection,row in select_records(rows):
        fields = dict(TABLES)[selection.file].fields
        records.append({'source_file':selection.file,'source_key':selection.key,'data_ordinal':selection.ordinal,
                        'canonical_id':None,'matching_eligibility':'NOT_AUTHORIZED',
                        'fields':[field_evidence(selection,field,row[field]) for field in fields]})
    return {
        'contract':'ENR-PINNED-SCENTO-1','contract_revision':1,'transform_version':TRANSFORM,'schema_version':SCHEMA,
        'source_revision':REVISION,'source_population':{name:table.count for name,table in TABLES},
        'source_artifacts':[{'name':p.name,'bytes':p.size,'sha256':p.sha256} for p in PINS],
        'rights':{'license':'CC BY 4.0','license_url':'https://creativecommons.org/licenses/by/4.0/',
                  'attribution':'Scento — https://www.scento.com/perfume-database',
                  'audience':'PRIVATE_LOCAL_REVIEW_ONLY','linked_content':'NO_RIGHTS_GRANTED','images':'NO_RIGHTS_GRANTED',
                  'transformation_notice':'Bounded raw-field candidate extraction; source files unchanged.'},
        'current_database_status':'NOT_QUERIED_UNKNOWN',
        'effects':{'canonical_writes':False,'normalization_promotion':False,'hold_release':False,'database_mutation':False},
        'records':records,
    }


def build_preview(source: Path, revision: str = REVISION) -> dict:
    return transform_snapshot(load_snapshot(source,revision))


def canonical(payload: dict) -> bytes:
    """UTF-8, sorted object keys, manifest array order, fixed separators, no BOM."""
    return json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode('utf-8')


def payload_hash(payload: dict) -> str:
    return hashlib.sha256(canonical(payload)).hexdigest()


def _private_root(workspace: Path) -> Path:
    workspace = _safe_path(workspace)
    if not (workspace/'.git').exists():
        raise PreviewError('UNSAFE_PATH')
    root = _safe_path(workspace/PRIVATE_RELATIVE,must_exist=False)
    try:
        root.mkdir(parents=True,exist_ok=True)
    except OSError:
        raise PreviewError('PUBLICATION_FAILED') from None
    return _safe_path(root)


def _write_closed(path: Path, data: bytes) -> None:
    _safe_path(path,must_exist=False)
    with path.open('xb') as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())


@contextmanager
def _publication_lock(root: Path):
    lock = _safe_path(root/'publisher.lock',must_exist=False)
    try:
        handle = lock.open('xb')
    except FileExistsError:
        raise PreviewError('PUBLICATION_LOCKED') from None
    except OSError:
        _failure(root)
        raise PreviewError('PUBLICATION_FAILED') from None
    try:
        try:
            with handle:
                handle.write(b'IMP-ENR-01 exclusive local publisher\n')
                handle.flush()
                os.fsync(handle.fileno())
        except OSError:
            _failure(root)
            raise PreviewError('PUBLICATION_FAILED') from None
        yield
    finally:
        # Cleanup failure after a successful pointer commit must not turn a
        # committed operation into a reported failed publication. A retained
        # lock fails closed on the next attempt and needs manual inspection.
        try:
            _safe_path(lock)
            lock.unlink()
        except (OSError,PreviewError):
            pass


def _failure(root: Path) -> None:
    # Best-effort diagnostics must not replace the initial failure or expose it.
    try:
        path = root/('failure-'+uuid.uuid4().hex+'.json')
        with path.open('xb') as handle:
            handle.write(b'{"classification":"PUBLICATION_FAILED"}')
            handle.flush()
            os.fsync(handle.fileno())
    except OSError:
        pass


def _transition(root: Path, bundle: str | None, digest: str | None) -> None:
    pointer = _safe_path(root/'active.json',must_exist=False)
    candidate = root/('pointer-'+uuid.uuid4().hex+'.tmp')
    _write_closed(candidate,canonical({'bundle':bundle,'payload_sha256':digest,'schema_version':SCHEMA}))
    _safe_path(root)
    _safe_path(pointer,must_exist=False)
    os.replace(candidate,pointer)


def publish_preview(source: Path, workspace: Path, *, execution_time: str | None = None) -> Publication:
    """Build from pins; retain unique bundles; replace only the active pointer.

    This is private local pointer publication, not distribution or acceptance.
    All candidates and pointer files share the destination volume. No caller
    payload or expected-pins parameter is accepted.
    """
    root = _private_root(workspace)
    with _publication_lock(root):
        try:
            payload = build_preview(source)
            data = canonical(payload)
            digest = payload_hash(payload)
            if hashlib.sha256(data).hexdigest() != digest or canonical(json.loads(data)) != data:
                raise PreviewError('REPLAY_MISMATCH')
            name = 'bundle-'+uuid.uuid4().hex
            candidate = root/('candidate-'+uuid.uuid4().hex)
            _safe_path(candidate,must_exist=False)
            candidate.mkdir()
            _write_closed(candidate/'payload.json',data)
            _write_closed(candidate/'manifest.json',canonical({'payload_sha256':digest,'payload_bytes':len(data),'schema_version':SCHEMA}))
            _write_closed(candidate/'run.json',canonical({'execution_time':execution_time if execution_time is not None
                                                        else datetime.now(timezone.utc).isoformat()}))
            if _read_regular(candidate/'payload.json') != data:
                raise PreviewError('REPLAY_MISMATCH')
            _safe_path(root)
            candidate.rename(root/name)
            _transition(root,name,digest)
        except BaseException as error:
            _failure(root)
            if not isinstance(error,Exception):
                raise
            raise PreviewError('PUBLICATION_FAILED') from None
    return Publication(name,digest)


def rollback_preview(source: Path, workspace: Path, bundle_name: str | None) -> None:
    """Restore/withdraw only local pointer, retaining all candidates/history."""
    if bundle_name is not None and (len(bundle_name) != 39 or not bundle_name.startswith('bundle-')
                                    or any(c not in '0123456789abcdef' for c in bundle_name[7:])):
        raise PreviewError('UNSAFE_PATH')
    root = _private_root(workspace)
    with _publication_lock(root):
        try:
            digest = None
            if bundle_name is not None:
                bundle = _safe_path(root/bundle_name)
                data = _read_regular(bundle/'payload.json')
                expected = canonical(build_preview(source))
                manifest = json.loads(_read_regular(bundle/'manifest.json'))
                digest = hashlib.sha256(data).hexdigest()
                if data != expected or manifest != {'payload_sha256':digest,'payload_bytes':len(data),'schema_version':SCHEMA}:
                    raise PreviewError('REPLAY_MISMATCH')
            _transition(root,bundle_name,digest)
        except BaseException as error:
            _failure(root)
            if not isinstance(error,Exception):
                raise
            raise PreviewError('PUBLICATION_FAILED') from None
