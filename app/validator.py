from collections import Counter
from typing import Any


def validate_records(
    records: list[dict[str, Any]], required_fields: list[str]
) -> dict[str, Any]:
    missing = {field: 0 for field in required_fields}

    for record in records:
        for field in required_fields:
            value = record.get(field)
            if value is None or (isinstance(value, str) and not value.strip()):
                missing[field] += 1

    fingerprints = [repr(sorted(record.items())) for record in records]
    counts = Counter(fingerprints)
    duplicates = sum(count - 1 for count in counts.values() if count > 1)
    total_missing = sum(missing.values())

    return {
        "row_count": len(records),
        "duplicate_count": duplicates,
        "missing_by_field": missing,
        "missing_total": total_missing,
        "valid": duplicates == 0 and total_missing == 0,
    }
