"""Pure, exact synthetic B1-PD-TYPED-1 revision 2 operation.

Synthetic caller declarations establish no real source rights, completeness,
eligibility, smell similarity, confidence, or direct-pair evidence. This module
implements only the separately accepted synthetic pyramid positive-domain method.
"""
from dataclasses import dataclass, fields
from fractions import Fraction
import hashlib
import re

from matching_math.primitives import SetInput


@dataclass(frozen=True)
class B1Query:
    clauses: tuple["B1Clause", ...]


@dataclass(frozen=True)
class B1Clause:
    note_id: str
    selector: str
    role: str
    weight: int | None


@dataclass(frozen=True)
class B1Profile:
    perfume_id: str
    top: "B1Layer | None"
    heart: "B1Layer | None"
    base: "B1Layer | None"


@dataclass(frozen=True)
class B1Layer:
    notes: SetInput
    completeness_assertion_id: str | None
    selected_claim_id: str
    capture_id: str
    revision_id: str
    selection_snapshot_id: str
    scope_id: str


@dataclass(frozen=True)
class B1LayerDomain:
    layer: str
    domain_id: str


@dataclass(frozen=True)
class B1Vocabulary:
    vocabulary_version: str
    vocabulary_fingerprint: str
    domain_version: str
    transform_version: str
    alias_version: str
    normalization_version: str
    selection_snapshot_id: str
    scope_id: str
    layer_domains: tuple[B1LayerDomain, ...]
    note_ids: frozenset[str]


@dataclass(frozen=True)
class B1Config:
    method_id: str
    config_id: str
    schema_id: str
    role_policy_id: str
    selector_policy_id: str
    clause_weight_policy_id: str
    closure_policy_id: str
    assignment_policy_id: str
    focus_domain_policy_id: str
    positive_minimum: int
    formula_weights: tuple[int | Fraction, ...]
    max_raw_clauses: int
    max_normalized_clauses: int
    max_candidates: int
    max_memberships_per_candidate: int
    max_vocabulary_notes: int
    min_positive_weight: int
    max_positive_weight: int
    max_identifier_chars: int
    max_numeric_bits: int
    max_total_memberships: int


@dataclass(frozen=True)
class B1ContextKey:
    vocabulary_version: str
    vocabulary_fingerprint: str
    domain_version: str
    transform_version: str
    alias_version: str
    normalization_version: str
    selection_snapshot_id: str
    scope_id: str
    layer_domains: tuple[B1LayerDomain, ...]


@dataclass(frozen=True)
class B1QueryKey:
    config: B1Config
    context: B1ContextKey
    clauses: tuple[B1Clause, ...]


@dataclass(frozen=True)
class B1Lineage:
    completeness_assertion_id: str | None
    selected_claim_id: str
    capture_id: str
    revision_id: str
    selection_snapshot_id: str
    scope_id: str


@dataclass(frozen=True)
class B1LayerStatus:
    layer: str
    state: str
    declared_complete: bool | None
    domain_compatible: bool | None
    domain_id: str | None
    lineage: B1Lineage | None


@dataclass(frozen=True)
class B1Occurrence:
    note_id: str
    layer: str


@dataclass(frozen=True)
class B1ClauseEvaluation:
    clause: B1Clause
    domain_layers: tuple[str, ...]
    state: str
    witness: B1Occurrence | None
    unverified_domains: tuple[str, ...]


@dataclass(frozen=True)
class B1GateSummary:
    required: str
    excluded: str
    positive_domain: str
    positive_minimum: str


@dataclass(frozen=True)
class B1PartitionKey:
    query_key: B1QueryKey
    positive_layer_mask: tuple[str, ...]
    strict_layer_mask: tuple[str, ...]
    relevant_layer_mask: tuple[str, ...]
    layer_domains: tuple[B1LayerDomain, ...]


@dataclass(frozen=True)
class B1CandidateResult:
    method_id: str
    config_id: str
    schema_id: str
    candidate_id: str
    query_key: B1QueryKey
    reason: str
    fit: Fraction | None
    query_coverage: Fraction | None
    focus: Fraction | None
    query_weight_denominator: int
    verified_matched_weight: int
    verified_matched_positive_count: int
    verified_matched_occurrence_count: int
    positive_domain_size: int | None
    positive_layer_mask: tuple[str, ...]
    strict_layer_mask: tuple[str, ...]
    relevant_layer_mask: tuple[str, ...]
    closure_mask: tuple[str, ...]
    unique_positive_note_count: int
    gates: B1GateSummary
    clauses: tuple[B1ClauseEvaluation, ...]
    layers: tuple[B1LayerStatus, ...]
    partition_key: B1PartitionKey | None
    query_fit_percent_display: str | None
    confidence_state: str
    pair_evidence_state: str


@dataclass(frozen=True)
class B1PartitionResult:
    key: B1PartitionKey
    results: tuple[B1CandidateResult, ...]


@dataclass(frozen=True)
class B1BatchResult:
    method_id: str
    config_id: str
    schema_id: str
    query_key: B1QueryKey
    raw_clause_count: int
    normalized_clause_count: int
    positive_clause_count: int
    query_weight_denominator: int
    unique_positive_note_count: int
    positive_layer_mask: tuple[str, ...]
    strict_layer_mask: tuple[str, ...]
    relevant_layer_mask: tuple[str, ...]
    groups: tuple[B1PartitionResult, ...]
    unranked: tuple[B1CandidateResult, ...]


_LAYERS = ("top", "heart", "base")


def _exact(value, expected):
    if type(value) is not expected:
        raise TypeError("Invalid typed input")


def _record(value, expected):
    _exact(value, expected)
    for field in fields(expected):
        _get(value, field.name)


def _get(value, name):
    try:
        return getattr(value, name)
    except AttributeError:
        raise ValueError("Invalid typed input shape") from None


def _bound(condition):
    if not condition:
        raise ValueError("Input bound exceeded")


def _text(value):
    _exact(value, str)
    _bound(len(value) <= 128)


def _integer(value):
    _exact(value, int)
    _bound(value.bit_length() <= 128)


def _token(value):
    if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:-]*", value, re.ASCII) is None:
        raise ValueError("Invalid identifier")


def _uuid(value, namespace):
    if (re.fullmatch(namespace + r"-0000-4000-8000-[0-9a-f]{12}", value, re.ASCII) is None
            or value[-12:] == "000000000000"):
        raise ValueError("Invalid identifier")


def _config(value):
    # Types and bit caps precede policy comparisons or Fraction arithmetic.
    for field in fields(B1Config):
        item = getattr(value, field.name)
        if field.name == "formula_weights":
            _exact(item, tuple)
            if len(item) != 2:
                raise ValueError("Unsupported configuration")
        elif field.name.endswith("_id"):
            _text(item)
        else:
            _integer(item)
    for item in value.formula_weights:
        if type(item) is int:
            _integer(item)
        elif type(item) is Fraction:
            numerator, denominator = _get(item, "_numerator"), _get(item, "_denominator")
            _integer(numerator)
            _integer(denominator)
            if denominator <= 0:
                raise ValueError("Unsupported configuration")
        else:
            raise TypeError("Invalid typed input")
    expected = ("mc-b1-pyramid-positive-domain-p1", "b1-pd-typed-config-1", "b1-pd-typed-schema-1",
                "required-all-optional-soft-b1-v1", "pyramid-exact-any-b1-v1",
                "positive-int-1-5-excluded-none-b1-v1", "synthetic-closed-domains-b1-v1",
                "one-to-one-top-heart-base-b1-v1", "positive-layers-only-b1-v1", 1,
                (Fraction(4, 5), Fraction(1, 5)), 30, 30, 64, 512, 512, 1, 5, 128, 128, 32768)
    if tuple(getattr(value, f.name) for f in fields(value)) != expected:
        raise ValueError("Unsupported configuration")
    # Reconstruct declared metadata; forged extra attributes never enter results.
    return B1Config(*expected)


def _shapes(query, candidates, vocabulary):
    """Check all record/container shapes and counts before scanning any tokens."""
    _exact(vocabulary.layer_domains, tuple)
    _exact(vocabulary.note_ids, frozenset)
    _bound(len(vocabulary.note_ids) <= 512)
    # Fixed table size is a context policy, checked before scanning its records.
    if len(vocabulary.layer_domains) != 3:
        raise ValueError("Unsupported fixture context")
    for domain in vocabulary.layer_domains:
        _record(domain, B1LayerDomain)
    total = 0
    for candidate in candidates:
        _record(candidate, B1Profile)
        count = 0
        for name in _LAYERS:
            layer = getattr(candidate, name)
            if layer is None:
                continue
            _record(layer, B1Layer)
            _record(layer.notes, SetInput)
            _exact(layer.notes.members, frozenset)
            _exact(layer.notes.complete, bool)
            count += len(layer.notes.members)
            _bound(count <= 512)
            total += len(layer.notes.members)
            _bound(total <= 32768)
    for clause in query.clauses:
        _record(clause, B1Clause)


def _token_shapes(query, candidates, vocabulary):
    """After global count checks, bound every token and clause numeric field."""
    for field in fields(B1Vocabulary):
        if field.name not in ("layer_domains", "note_ids"):
            _text(getattr(vocabulary, field.name))
    for domain in vocabulary.layer_domains:
        _text(domain.layer)
        _text(domain.domain_id)
    for note in vocabulary.note_ids:
        _text(note)
    for candidate in candidates:
        _text(candidate.perfume_id)
        for name in _LAYERS:
            layer = getattr(candidate, name)
            if layer is None:
                continue
            _text(layer.notes.domain_id)
            for field in fields(B1Layer):
                if field.name == "notes":
                    continue
                item = getattr(layer, field.name)
                if item is not None or field.name != "completeness_assertion_id":
                    _text(item)
            for note in layer.notes.members:
                _text(note)
    for clause in query.clauses:
        _text(clause.note_id)
        _text(clause.selector)
        _text(clause.role)
        if clause.weight is not None:
            _integer(clause.weight)
        elif clause.role in ("required", "optional"):
            raise TypeError("Invalid typed input")


def _context(vocabulary):
    expected = ("synth-notes-b1-v1", "synth-pyramid-domains-b1-v1", "canonical-set-fixture-b1-v1",
                "canonical-id-only-b1-v1", "canonical-clause-set-b1-v1", "synth-selection-b1-v1", "synth-scope-b1-v1")
    names = ("vocabulary_version", "domain_version", "transform_version", "alias_version",
             "normalization_version", "selection_snapshot_id", "scope_id")
    domains = tuple(B1LayerDomain(name, f"synth-{name}-b1-v1") for name in _LAYERS)
    if (tuple(getattr(vocabulary, name) for name in names) != expected
            or vocabulary.layer_domains != domains):
        raise ValueError("Unsupported fixture context")
    fingerprint = hashlib.sha256("\n".join(sorted(vocabulary.note_ids)).encode("ascii")).hexdigest()
    if fingerprint != vocabulary.vocabulary_fingerprint:
        raise ValueError("Invalid fixture vocabulary")
    return B1ContextKey(vocabulary.vocabulary_version, fingerprint, vocabulary.domain_version,
                        vocabulary.transform_version, vocabulary.alias_version, vocabulary.normalization_version,
                        vocabulary.selection_snapshot_id, vocabulary.scope_id, domains)


def _syntax(query, candidates, vocabulary):
    """Complete token syntax checks before context hashing or membership checks."""
    for field in fields(B1Vocabulary):
        if field.name not in ("note_ids", "layer_domains", "vocabulary_fingerprint"):
            _token(getattr(vocabulary, field.name))
    if re.fullmatch(r"[0-9a-f]{64}", vocabulary.vocabulary_fingerprint, re.ASCII) is None:
        raise ValueError("Invalid identifier")
    for domain in vocabulary.layer_domains:
        _token(domain.layer)
        _token(domain.domain_id)
    for note in vocabulary.note_ids:
        _uuid(note, "20000000")
    for candidate in candidates:
        _uuid(candidate.perfume_id, "10000000")
        for name in _LAYERS:
            layer = getattr(candidate, name)
            if layer is None:
                continue
            for note in layer.notes.members:
                _uuid(note, "20000000")
            _token(layer.notes.domain_id)
            for field in fields(B1Layer):
                item = getattr(layer, field.name)
                if field.name != "notes" and item is not None:
                    _token(item)
    for clause in query.clauses:
        _uuid(clause.note_id, "20000000")


def _memberships(query, candidates, vocabulary):
    for candidate in candidates:
        for name in _LAYERS:
            layer = getattr(candidate, name)
            if layer is not None and any(note not in vocabulary.note_ids for note in layer.notes.members):
                raise ValueError("Invalid fixture vocabulary")
    for clause in query.clauses:
        if clause.note_id not in vocabulary.note_ids:
            raise ValueError("Invalid fixture vocabulary")


def _candidate_semantics(candidates, vocabulary):
    seen = set()
    for candidate in candidates:
        if candidate.perfume_id in seen:
            raise ValueError("Invalid identifier")
        seen.add(candidate.perfume_id)
        for name in _LAYERS:
            layer = getattr(candidate, name)
            if layer is None:
                continue
            if (layer.scope_id != vocabulary.scope_id
                    or layer.selection_snapshot_id != vocabulary.selection_snapshot_id
                    or layer.notes.complete != (layer.completeness_assertion_id is not None)):
                raise ValueError("Invalid fixture lineage")


def _clauses(query):
    for clause in query.clauses:
        if clause.selector not in (*_LAYERS, "any_pyramid") or clause.role not in ("required", "optional", "excluded"):
            raise ValueError("Invalid query")
        if clause.role == "excluded":
            if clause.weight is not None:
                raise ValueError("Invalid query")
        elif clause.weight < 0 or clause.weight > 5:
            raise ValueError("Invalid query")
    positives = tuple(c for c in query.clauses if c.role != "excluded")
    if not positives or all(c.weight == 0 for c in positives):
        raise ValueError("Invalid empty positive query")
    if any(c.weight == 0 for c in positives):
        raise ValueError("Invalid query")
    normalized = []
    for clause in query.clauses:
        for prior in normalized:
            if prior.note_id != clause.note_id:
                continue
            if prior.selector == clause.selector:
                if (prior.role, prior.weight) != (clause.role, clause.weight):
                    raise ValueError("Invalid query")
            elif "any_pyramid" in (prior.selector, clause.selector):
                raise ValueError("Invalid query")
        clean = B1Clause(clause.note_id, clause.selector, clause.role, clause.weight)
        if clean not in normalized:
            normalized.append(clean)
    selectors = (*_LAYERS, "any_pyramid")
    roles = ("required", "optional", "excluded")
    return tuple(sorted(normalized, key=lambda c: (c.note_id, selectors.index(c.selector),
                        roles.index(c.role), 0 if c.weight is None else c.weight)))


def _search(clause):
    return _LAYERS if clause.selector == "any_pyramid" else (clause.selector,)


def _mask(clauses):
    return tuple(name for name in _LAYERS if any(name in _search(c) for c in clauses))


def _status(candidate, context):
    statuses = []
    for name, domain in zip(_LAYERS, context.layer_domains):
        layer = getattr(candidate, name)
        if layer is None:
            statuses.append(B1LayerStatus(name, "missing", None, None, None, None))
        else:
            compatible = layer.notes.domain_id == domain.domain_id
            state = "domain_mismatch" if not compatible else "complete" if layer.notes.complete else "incomplete"
            lineage = B1Lineage(*(getattr(layer, f.name) for f in fields(B1Lineage)))
            statuses.append(B1LayerStatus(name, state, layer.notes.complete, compatible, layer.notes.domain_id, lineage))
    return tuple(statuses)


def _evaluate(candidate, clauses, statuses):
    evaluations = []
    for clause in clauses:
        searched = _search(clause)
        unavailable = tuple(s.layer for s in statuses if s.layer in searched and s.state != "complete")
        observed = tuple(s.layer for s in statuses if s.layer in searched and s.domain_compatible
                         and clause.note_id in getattr(candidate, s.layer).notes.members)
        witness = None
        if clause.role == "excluded":
            if observed:
                state, witness = "excluded_present", B1Occurrence(clause.note_id, observed[0])
            else:
                state = "unverified" if unavailable else "excluded_absent"
        elif unavailable:
            state = "unverified"
        elif observed:
            state, witness = "matched", B1Occurrence(clause.note_id, observed[0])
        else:
            state = "unmatched"
        evaluations.append(B1ClauseEvaluation(clause, searched, state, witness, unavailable))
    return tuple(evaluations)


def _gate(evaluations, role, failure):
    selected = tuple(e.state for e in evaluations if e.clause.role == role)
    return "failed" if failure in selected else "unverified" if "unverified" in selected else "passed"


def _score(candidate, key, positive, strict, relevant, denominator, specificity):
    statuses = _status(candidate, key.context)
    evaluations = _evaluate(candidate, key.clauses, statuses)
    matched = tuple(e for e in evaluations if e.clause.role != "excluded" and e.state == "matched")
    weight = sum(e.clause.weight for e in matched)
    positive_closed = all(s.state == "complete" for s in statuses if s.layer in positive)
    minimum = ("passed" if matched else "unverified" if any(e.state == "unverified"
               for e in evaluations if e.clause.role != "excluded") else "failed")
    gates = B1GateSummary(_gate(evaluations, "required", "unmatched"),
                          _gate(evaluations, "excluded", "excluded_present"),
                          "complete" if positive_closed else "unverified", minimum)
    reason = "computed"
    for condition, label in ((gates.excluded == "failed", "rejected_excluded"),
            (gates.required == "failed", "rejected_missing_required"),
            (gates.required == "unverified", "unverified_required_domain"),
            (gates.excluded == "unverified", "unverified_exclusion_domain"),
            (not positive_closed, "unverified_positive_domain"),
            (minimum == "failed", "rejected_no_positive_match")):
        if condition:
            reason = label
            break
    size = sum(len(getattr(candidate, name).notes.members) for name in positive) if positive_closed else None
    coverage = Fraction(weight, denominator) if positive_closed else None
    focus = (Fraction(len(matched), size) if size else Fraction(0)) if positive_closed else None
    fit = key.config.formula_weights[0] * coverage + key.config.formula_weights[1] * focus if reason == "computed" else None
    partition, display = None, None
    if fit is not None:
        partition = B1PartitionKey(key, positive, strict, relevant,
                                  tuple(d for d in key.context.layer_domains if d.layer in relevant))
        scaled = 1000 * fit + Fraction(1, 2)
        tenths = scaled.numerator // scaled.denominator
        display = f"{tenths // 10}.{tenths % 10}"
    return B1CandidateResult(key.config.method_id, key.config.config_id, key.config.schema_id,
        candidate.perfume_id, key, reason, fit, coverage, focus, denominator, weight, len(matched),
        len(matched), size, positive, strict, relevant,
        tuple(s.layer for s in statuses if s.layer in relevant and s.state == "complete"),
        specificity, gates, evaluations, statuses, partition, display,
        "not_evaluated_policy_pending", "not_evaluated_synthetic_only")


def score_synthetic_b1(query: B1Query, candidates: tuple[B1Profile, ...], *,
                       vocabulary: B1Vocabulary, config: B1Config) -> B1BatchResult:
    """Validate the entire bounded call, then score only its synthetic candidates."""
    _exact(query, B1Query)
    _exact(candidates, tuple)
    _exact(vocabulary, B1Vocabulary)
    _exact(config, B1Config)
    _exact(_get(query, "clauses"), tuple)
    _bound(len(query.clauses) <= 30)
    _bound(len(candidates) <= 64)
    _record(config, B1Config)
    clean_config = _config(config)
    _record(vocabulary, B1Vocabulary)
    _shapes(query, candidates, vocabulary)
    _token_shapes(query, candidates, vocabulary)
    _syntax(query, candidates, vocabulary)
    context = _context(vocabulary)
    _memberships(query, candidates, vocabulary)
    _candidate_semantics(candidates, vocabulary)
    clauses = _clauses(query)
    key = B1QueryKey(clean_config, context, clauses)
    positives = tuple(c for c in clauses if c.role != "excluded")
    positive = _mask(positives)
    strict = _mask(tuple(c for c in clauses if c.role in ("required", "excluded")))
    relevant = tuple(name for name in _LAYERS if name in positive or name in strict)
    denominator = sum(c.weight for c in positives)
    specificity = len({c.note_id for c in positives})
    results = tuple(_score(c, key, positive, strict, relevant, denominator, specificity) for c in candidates)
    ranked = tuple(sorted((r for r in results if r.fit is not None), key=lambda r: (-r.fit, r.candidate_id)))
    unranked = tuple(sorted((r for r in results if r.fit is None), key=lambda r: r.candidate_id))
    groups = (B1PartitionResult(ranked[0].partition_key, ranked),) if ranked else ()
    return B1BatchResult(clean_config.method_id, clean_config.config_id, clean_config.schema_id,
        key, len(query.clauses), len(clauses), len(positives), denominator, specificity,
        positive, strict, relevant, groups, unranked)
