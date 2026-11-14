"""M1-NL-TYPED-1: bounded, exact, synthetic-only layered-note comparison.

The Owner accepted this typed contract for IMP-MATCH-08. Fixture lineage is
caller-declared metadata, not real-source rights, completeness or eligibility
verification. This module performs no I/O and has no application integration.
"""
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import re
from typing import Literal

from matching_math.primitives import SetInput, set_jaccard

LayerName = Literal['top', 'heart', 'base']
_LAYERS = ('top', 'heart', 'base')
_WEIGHTS = (Fraction(1, 4), Fraction(3, 8), Fraction(3, 8))
_COUNT_FIELDS = (('min_comparable_layers', 2), ('max_candidates', 64),
                 ('max_memberships_per_profile', 512), ('max_vocabulary_notes', 512),
                 ('max_identifier_chars', 128), ('max_numeric_bits', 128),
                 ('max_total_memberships', 33280))
_CONTEXT = (('vocabulary_version', 'synth-notes-m1-v1'),
            ('domain_version', 'synth-pyramid-domains-m1-v1'),
            ('transform_version', 'canonical-set-fixture-m1-v1'),
            ('selection_snapshot_id', 'synth-selection-m1-v1'),
            ('scope_id', 'synth-scope-m1-v1'))


@dataclass(frozen=True)
class M1Config:
    method_id: str
    config_id: str
    schema_id: str
    layer_weights: tuple[Fraction | int, ...]
    min_comparable_layers: int
    note_support_budget: Fraction | int
    max_candidates: int
    max_memberships_per_profile: int
    max_vocabulary_notes: int
    max_identifier_chars: int
    max_numeric_bits: int
    max_total_memberships: int


@dataclass(frozen=True)
class FixtureVocabulary:
    vocabulary_version: str
    vocabulary_fingerprint: str
    domain_version: str
    transform_version: str
    selection_snapshot_id: str
    scope_id: str
    note_ids: frozenset[str]


@dataclass(frozen=True)
class FixtureProfile:
    perfume_id: str
    top: 'FixtureLayer | None'
    heart: 'FixtureLayer | None'
    base: 'FixtureLayer | None'


@dataclass(frozen=True)
class FixtureLayer:
    notes: SetInput
    completeness_assertion_id: str | None
    selected_claim_id: str
    capture_id: str
    revision_id: str
    selection_snapshot_id: str
    scope_id: str


@dataclass(frozen=True)
class FixtureLineage:
    completeness_assertion_id: str | None
    selected_claim_id: str
    capture_id: str
    revision_id: str
    selection_snapshot_id: str
    scope_id: str


@dataclass(frozen=True)
class LayerSide:
    state: str
    declared_complete: bool | None
    domain_id: str | None
    lineage: FixtureLineage | None


@dataclass(frozen=True)
class LayerExplanation:
    layer: LayerName
    left: LayerSide
    right: LayerSide
    reason: str
    jaccard: Fraction | None
    intersection_count: int | None
    union_count: int | None
    original_weight: Fraction


@dataclass(frozen=True)
class LayerDomain:
    layer: LayerName
    domain_id: str


@dataclass(frozen=True)
class PartitionKey:
    method_id: str
    config_id: str
    schema_id: str
    component_mask: tuple[str, ...]
    comparable_layer_mask: tuple[LayerName, ...]
    vocabulary_version: str
    vocabulary_fingerprint: str
    domain_version: str
    transform_version: str
    selection_snapshot_id: str
    scope_id: str
    layer_domains: tuple[LayerDomain, ...]


@dataclass(frozen=True)
class PairResult:
    method_id: str
    config_id: str
    schema_id: str
    reference_id: str
    candidate_id: str
    fit: Fraction | None
    reason: str
    scoring_coverage: Fraction
    observed_layer_support: Fraction
    note_score_denominator: Fraction | None
    comparable_layer_mask: tuple[LayerName, ...]
    partition_key: PartitionKey | None
    structural_fit_percent_display: str | None
    confidence_state: str
    pair_evidence_state: str
    layers: tuple[LayerExplanation, ...]


@dataclass(frozen=True)
class PartitionResult:
    key: PartitionKey
    results: tuple[PairResult, ...]


@dataclass(frozen=True)
class M1BatchResult:
    method_id: str
    config_id: str
    schema_id: str
    reference_id: str
    vocabulary_version: str
    vocabulary_fingerprint: str
    domain_version: str
    transform_version: str
    selection_snapshot_id: str
    scope_id: str
    groups: tuple[PartitionResult, ...]
    unranked: tuple[PairResult, ...]


def _exact(value, declared):
    if type(value) is not declared:
        raise TypeError('Invalid typed input')


def _token_bound(value):
    _exact(value, str)
    if not 1 <= len(value) <= 128:
        raise ValueError('Identifier bound exceeded')


def _token(value):
    _token_bound(value)
    if re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._:-]*', value, flags=re.ASCII) is None:
        raise ValueError('Invalid identifier')


def _numeric(value):
    if type(value) not in (int, Fraction):
        raise TypeError('Invalid numeric type')
    numerator = value if type(value) is int else value.numerator
    denominator = 1 if type(value) is int else value.denominator
    if numerator.bit_length() > 128 or denominator.bit_length() > 128:
        raise ValueError('Numeric bound exceeded')
    result = Fraction(value)
    if not 0 <= result <= 1:
        raise ValueError('Invalid numeric value')
    return result


def _config(config):
    # Check exact numeric types and bit lengths before equality or arithmetic.
    for name in ('method_id', 'config_id', 'schema_id'):
        _token(getattr(config, name))
    for name, _ in _COUNT_FIELDS:
        value = getattr(config, name)
        _exact(value, int)
        if value.bit_length() > 128:
            raise ValueError('Numeric bound exceeded')
    _exact(config.layer_weights, tuple)
    if len(config.layer_weights) != 3:
        raise ValueError('Invalid configuration shape')
    weights = tuple(_numeric(value) for value in config.layer_weights)
    budget = _numeric(config.note_support_budget)
    if (config.method_id != 'mc-a-notes-layered-p1' or config.config_id != 'm1-nl-typed-config-1'
            or config.schema_id != 'm1-nl-typed-schema-1' or weights != _WEIGHTS
            or budget != Fraction(1, 2)
            or any(getattr(config, name) != expected for name, expected in _COUNT_FIELDS)):
        raise ValueError('Unsupported configuration')


def _profile_shape(profile):
    """Check every set size before collecting member values for later validation."""
    _exact(profile, FixtureProfile)
    total = 0
    for name in _LAYERS:
        layer = getattr(profile, name)
        if layer is None:
            continue
        _exact(layer, FixtureLayer)
        _exact(layer.notes, SetInput)
        _exact(layer.notes.complete, bool)
        _exact(layer.notes.members, frozenset)
        total += len(layer.notes.members)
    if total > 512:
        raise ValueError('Profile membership bound exceeded')
    return total


def _profile_tokens(profile):
    values = [profile.perfume_id]
    for name in _LAYERS:
        layer = getattr(profile, name)
        if layer is None:
            continue
        values.extend((layer.notes.domain_id, layer.selected_claim_id, layer.capture_id,
                       layer.revision_id, layer.selection_snapshot_id, layer.scope_id))
        if layer.completeness_assertion_id is not None:
            values.append(layer.completeness_assertion_id)
        values.extend(layer.notes.members)
    return values


def _fixture_uuid(value, prefix):
    # _token_bound has already refused wrong types and unbounded strings.
    if (len(value) != 36 or not value.startswith(prefix)
            or re.fullmatch(r'[0-9a-f]{12}', value[-12:]) is None
            or value[-12:] == '000000000000'):
        raise ValueError('Invalid synthetic identity')


def _validate(reference, candidates, vocabulary, config):
    _exact(reference, FixtureProfile)
    _exact(candidates, tuple)
    _exact(vocabulary, FixtureVocabulary)
    _exact(config, M1Config)
    if len(candidates) > 64:
        raise ValueError('Candidate bound exceeded')
    _config(config)
    _exact(vocabulary.note_ids, frozenset)
    if len(vocabulary.note_ids) > 512:
        raise ValueError('Vocabulary bound exceeded')
    profiles = (reference,) + candidates
    total = sum(_profile_shape(profile) for profile in profiles)
    if total > 33280:
        raise ValueError('Total membership bound exceeded')
    # All container bounds above precede member scans, hashing, sorting or set math.
    tokens = [getattr(vocabulary, name) for name, _ in _CONTEXT]
    tokens.append(vocabulary.vocabulary_fingerprint)
    tokens.extend(vocabulary.note_ids)
    for profile in profiles:
        tokens.extend(_profile_tokens(profile))
    for value in tokens:
        _token_bound(value)
    for value in tokens:
        _token(value)
    for name, expected in _CONTEXT:
        if getattr(vocabulary, name) != expected:
            raise ValueError('Unsupported fixture context')
    for value in vocabulary.note_ids:
        _fixture_uuid(value, '20000000-0000-4000-8000-')
    fingerprint = vocabulary.vocabulary_fingerprint
    if re.fullmatch(r'[0-9a-f]{64}', fingerprint) is None:
        raise ValueError('Invalid vocabulary fingerprint')
    actual = sha256('\n'.join(sorted(vocabulary.note_ids)).encode('ascii')).hexdigest()
    if actual != fingerprint:
        raise ValueError('Vocabulary fingerprint mismatch')
    identities = set()
    for profile in profiles:
        _fixture_uuid(profile.perfume_id, '10000000-0000-4000-8000-')
        if profile.perfume_id in identities:
            raise ValueError('Duplicate or self identity')
        identities.add(profile.perfume_id)
        for name in _LAYERS:
            layer = getattr(profile, name)
            if layer is None:
                continue
            if layer.scope_id != vocabulary.scope_id or layer.selection_snapshot_id != vocabulary.selection_snapshot_id:
                raise ValueError('Fixture lineage mismatch')
            if layer.notes.complete != (layer.completeness_assertion_id is not None):
                raise ValueError('Completeness assertion mismatch')
            for value in layer.notes.members:
                _fixture_uuid(value, '20000000-0000-4000-8000-')
                if value not in vocabulary.note_ids:
                    raise ValueError('Note outside fixture vocabulary')


def _side(layer):
    if layer is None:
        return LayerSide('missing', None, None, None)
    lineage = FixtureLineage(layer.completeness_assertion_id, layer.selected_claim_id, layer.capture_id,
                             layer.revision_id, layer.selection_snapshot_id, layer.scope_id)
    return LayerSide('complete' if layer.notes.complete else 'incomplete', layer.notes.complete,
                     layer.notes.domain_id, lineage)


def _layer_explanation(name, left, right, weight):
    measure = set_jaccard(None if left is None else left.notes, None if right is None else right.notes)
    intersection = union = None
    if measure.reason in ('computed', 'empty_union'):
        intersection = len(left.notes.members & right.notes.members)
        union = len(left.notes.members | right.notes.members)
    return LayerExplanation(name, _side(left), _side(right), measure.reason, measure.value,
                            intersection, union, weight)


def _display(value):
    scaled = 1000 * value + Fraction(1, 2)
    tenths = scaled.numerator // scaled.denominator
    return f'{tenths // 10}.{tenths % 10}'


def _pair(reference, candidate, vocabulary, config):
    layers = tuple(_layer_explanation(name, getattr(reference, name), getattr(candidate, name), weight)
                   for name, weight in zip(_LAYERS, _WEIGHTS))
    comparable = tuple(layer for layer in layers if layer.jaccard is not None)
    mask = tuple(layer.layer for layer in comparable)
    support = sum((layer.original_weight for layer in comparable), Fraction(0))
    fit = key = denominator = display = None
    coverage = Fraction(0)
    if len(comparable) >= config.min_comparable_layers:
        fit = sum((layer.original_weight * layer.jaccard for layer in comparable), Fraction(0)) / support
        denominator = support
        coverage = Fraction(config.note_support_budget) * support
        display = _display(fit)
        key = PartitionKey(config.method_id, config.config_id, config.schema_id, ('notes',), mask,
                           vocabulary.vocabulary_version, vocabulary.vocabulary_fingerprint, vocabulary.domain_version,
                           vocabulary.transform_version, vocabulary.selection_snapshot_id, vocabulary.scope_id,
                           tuple(LayerDomain(layer.layer, layer.left.domain_id) for layer in comparable))
    return PairResult(config.method_id, config.config_id, config.schema_id, reference.perfume_id,
                      candidate.perfume_id, fit, 'computed' if fit is not None else 'insufficient_layers',
                      coverage, support, denominator, mask, key, display, 'not_evaluated_policy_pending',
                      'not_evaluated_synthetic_only', layers)


def _group_order(key):
    bits = sum(1 << _LAYERS.index(name) for name in key.comparable_layer_mask)
    return (bits, key.method_id, key.config_id, key.schema_id, key.component_mask, key.vocabulary_version,
            key.vocabulary_fingerprint, key.domain_version, key.transform_version, key.selection_snapshot_id,
            key.scope_id, tuple((domain.layer, domain.domain_id) for domain in key.layer_domains))


def score_synthetic_notes_layered(reference: FixtureProfile, candidates: tuple[FixtureProfile, ...], *,
                                  vocabulary: FixtureVocabulary, config: M1Config) -> M1BatchResult:
    """Validate all bounded declared fixtures, then return exact partitioned results.

    All four arguments are required. No coercion, default policy, hidden fallback,
    real-data eligibility or cross-partition ranking is provided.
    """
    try:
        _validate(reference, candidates, vocabulary, config)
    except AttributeError:
        # An exact dataclass type can still be forged without its required fields.
        # Refuse the malformed shape without leaking attribute names or payloads.
        raise ValueError('Invalid typed input shape') from None
    grouped = {}
    unranked = []
    for candidate in candidates:
        result = _pair(reference, candidate, vocabulary, config)
        if result.partition_key is None:
            unranked.append(result)
        else:
            grouped.setdefault(result.partition_key, []).append(result)
    groups = tuple(PartitionResult(key, tuple(sorted(grouped[key], key=lambda row: (-row.fit, row.candidate_id))))
                   for key in sorted(grouped, key=_group_order))
    return M1BatchResult(config.method_id, config.config_id, config.schema_id, reference.perfume_id,
                         vocabulary.vocabulary_version, vocabulary.vocabulary_fingerprint, vocabulary.domain_version,
                         vocabulary.transform_version, vocabulary.selection_snapshot_id, vocabulary.scope_id,
                         groups, tuple(sorted(unranked, key=lambda row: row.candidate_id)))
