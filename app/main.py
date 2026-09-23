from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.validator import validate_records

app = FastAPI(title="AI Data Quality Validator", version="1.0.0")


class ValidationRequest(BaseModel):
    records: list[dict[str, Any]] = Field(min_length=1)
    required_fields: list[str] = Field(default_factory=list)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/validate")
def validate(payload: ValidationRequest) -> dict[str, Any]:
    return validate_records(payload.records, payload.required_fields)
