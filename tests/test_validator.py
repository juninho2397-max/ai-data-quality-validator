from app.validator import validate_records


def test_clean_dataset_is_valid():
    result = validate_records(
        [{"id": 1, "text": "hello"}, {"id": 2, "text": "world"}],
        ["id", "text"],
    )
    assert result["valid"] is True
    assert result["duplicate_count"] == 0
    assert result["missing_total"] == 0


def test_missing_and_duplicates_are_detected():
    records = [
        {"id": 1, "text": ""},
        {"id": 1, "text": ""},
        {"id": 2, "text": "ok"},
    ]
    result = validate_records(records, ["id", "text"])
    assert result["valid"] is False
    assert result["duplicate_count"] == 1
    assert result["missing_by_field"]["text"] == 2
