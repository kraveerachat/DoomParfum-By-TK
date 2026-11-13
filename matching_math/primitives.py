"""Exact, pure mathematical primitives tested only with SYNTHETIC inputs.

These functions do not establish rights, source approval, real-data eligibility,
accepted completeness, confidence or pairwise evidence. The application adapter
must establish those gates before any future separately authorized scorer.
No default weights, Mode A/B1/B2 behavior or percentage conversion is supplied.
"""
from collections.abc import Mapping
from dataclasses import dataclass
from fractions import Fraction
from uuid import UUID


def _identifier(value):
    if type(value) is not str:
        raise TypeError("Identifiers must be strings")
    if not value or value != value.strip():
        raise ValueError("Identifiers must be nonempty and already canonical")


def _number(value):
    if type(value) not in (int, Fraction):
        raise TypeError("Use exact int/Fraction values; floats, booleans and expressions are refused")
    return Fraction(value)


def _unit(value):
    result = _number(value)
    if not 0 <= result <= 1:
        raise ValueError("Value is outside the unit interval")
    return result


def _metadata(complete, *identifiers):
    if type(complete) is not bool:
        raise TypeError("Completeness must be explicit Boolean")
    for value in identifiers:
        _identifier(value)


@dataclass(frozen=True)
class SetInput:
    members: frozenset[str]
    complete: bool
    domain_id: str

    def __post_init__(self):
        _metadata(self.complete, self.domain_id)
        if type(self.members) is not frozenset:
            raise TypeError("Supply an explicit canonical frozenset, not raw source occurrences")
        for key in self.members:
            _identifier(key)


@dataclass(frozen=True)
class VectorInput:
    values: tuple[tuple[str, Fraction | int | None], ...]
    complete: bool
    domain_id: str
    scale_id: str

    def __post_init__(self):
        _metadata(self.complete, self.domain_id, self.scale_id)
        if type(self.values) is not tuple:
            raise TypeError("Supply finite immutable vector pairs")
        keys = []
        for pair in self.values:
            if type(pair) is not tuple or len(pair) != 2:
                raise TypeError("Vector pair must be a two-item tuple")
            key, value = pair
            _identifier(key)
            keys.append(key)
            if value is not None:
                _unit(value)
        if keys != sorted(keys) or len(set(keys)) != len(keys):
            raise ValueError("Vector keys must be unique and sorted")


@dataclass(frozen=True)
class Measure:
    value: Fraction | None
    reason: str

    def __post_init__(self):
        if self.value is not None:
            if type(self.value) is not Fraction or self.reason != "computed":
                raise ValueError("Computed measure must be exact Fraction with computed reason")
            _unit(self.value)
        elif self.reason not in {
            "missing_input", "incomplete_input", "domain_mismatch", "scale_mismatch",
            "empty_union", "unknown_value",
        }:
            raise ValueError("Undefined measure needs an explicit reason")


def _profile(value, expected):
    if value is not None and type(value) is not expected:
        raise TypeError("Unexpected mathematical input type")


def set_jaccard(left: SetInput | None, right: SetInput | None) -> Measure:
    _profile(left, SetInput)
    _profile(right, SetInput)
    if left is None or right is None:
        return Measure(None, "missing_input")
    if not left.complete or not right.complete:
        return Measure(None, "incomplete_input")
    if left.domain_id != right.domain_id:
        return Measure(None, "domain_mismatch")
    union = left.members | right.members
    if not union:
        return Measure(None, "empty_union")
    return Measure(Fraction(len(left.members & right.members), len(union)), "computed")


def weighted_jaccard(left: VectorInput | None, right: VectorInput | None) -> Measure:
    _profile(left, VectorInput)
    _profile(right, VectorInput)
    if left is None or right is None:
        return Measure(None, "missing_input")
    if not left.complete or not right.complete:
        return Measure(None, "incomplete_input")
    if left.domain_id != right.domain_id:
        return Measure(None, "domain_mismatch")
    if left.scale_id != right.scale_id:
        return Measure(None, "scale_mismatch")
    if tuple(key for key, _ in left.values) != tuple(key for key, _ in right.values):
        return Measure(None, "domain_mismatch")
    if any(value is None for _, value in left.values + right.values):
        return Measure(None, "unknown_value")
    pairs = [(_unit(a), _unit(b)) for (_, a), (_, b) in zip(left.values, right.values)]
    denominator = sum((max(a, b) for a, b in pairs), Fraction(0))
    if not denominator:
        return Measure(None, "empty_union")
    numerator = sum((min(a, b) for a, b in pairs), Fraction(0))
    return Measure(numerator / denominator, "computed")


def _weighted_inputs(values, weights, *, allow_unknown):
    if not isinstance(values, Mapping) or not isinstance(weights, Mapping):
        raise TypeError("Explicit finite mappings required")
    if not weights or set(values) != set(weights):
        raise ValueError("Values and nonempty weights must have identical explicit keys")
    converted_values, converted_weights = {}, {}
    for key in weights:
        _identifier(key)
        weight = _number(weights[key])
        if weight <= 0:
            raise ValueError("Every supplied weight must be positive")
        converted_weights[key] = weight
        value = values[key]
        converted_values[key] = None if value is None and allow_unknown else _unit(value)
    return converted_values, converted_weights


def weighted_mean(values, weights) -> Measure:
    """Complete-input mean only. Missing-component renormalization is not a policy here."""
    values, weights = _weighted_inputs(values, weights, allow_unknown=True)
    if any(value is None for value in values.values()):
        return Measure(None, "unknown_value")
    total = sum(weights.values(), Fraction(0))
    result = sum((weights[key] * values[key] for key in weights), Fraction(0)) / total
    return Measure(result, "computed")


def coverage(reliabilities, weights) -> Fraction:
    """Explicit known reliability values with original total-weight denominator."""
    values, weights = _weighted_inputs(reliabilities, weights, allow_unknown=False)
    return sum((weights[key] * values[key] for key in weights), Fraction(0)) / sum(
        weights.values(), Fraction(0))


@dataclass(frozen=True)
class RankItem:
    candidate_id: str
    value: Fraction | int | None

    def __post_init__(self):
        _identifier(self.candidate_id)
        if str(UUID(self.candidate_id)) != self.candidate_id:
            raise ValueError("Candidate ID must be a canonical lowercase UUID")
        if self.value is not None:
            _unit(self.value)


def stable_order(rows: tuple[RankItem, ...]) -> tuple[RankItem, ...]:
    """Known exact values descending, canonical UUID ties; undefined values last.

    No currentness/coverage/method grouping, eligibility or real-data ranking is
    established. Future callers must supply their independently approved gates.
    """
    if type(rows) is not tuple or any(type(row) is not RankItem for row in rows):
        raise TypeError("Supply a finite immutable tuple of RankItem")
    if len({row.candidate_id for row in rows}) != len(rows):
        raise ValueError("Duplicate candidate IDs require reconciliation, not silent suppression")
    return tuple(sorted(rows, key=lambda row: (
        row.value is None, -_unit(row.value) if row.value is not None else Fraction(0),
        row.candidate_id,
    )))
