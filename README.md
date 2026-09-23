# AI Data Quality Validator

A lightweight FastAPI service for validating tabular records before they enter machine-learning or analytics pipelines.

## Features
- Required-field completeness checks
- Duplicate-record detection
- Typed request validation with Pydantic
- Health and validation endpoints
- Automated tests with Pytest
- GitHub Actions CI

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs`.

## Example
POST `/validate`
```json
{
  "records": [
    {"id": 1, "text": "hello"},
    {"id": 2, "text": "world"}
  ],
  "required_fields": ["id", "text"]
}
```

## Tests
```bash
pytest -q
```
