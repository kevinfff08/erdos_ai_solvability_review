#!/usr/bin/env python3
"""Reference helpers retained to document V2 validation and atomic output."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def safe_number(number: str) -> str:
    return number.replace("-", "_")


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    staged = path.with_suffix(path.suffix + ".tmp")
    staged.write_text(text, encoding="utf-8", newline="\n")
    staged.replace(path)


def atomic_write_json(path: Path, payload: Any) -> None:
    atomic_write_text(
        path, json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    )


def validate_schema(instance: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    """Validate the JSON-Schema subset used by deep_review.schema.json."""

    errors: list[str] = []
    expected = schema.get("type")
    type_ok = {
        "object": lambda value: isinstance(value, dict),
        "array": lambda value: isinstance(value, list),
        "string": lambda value: isinstance(value, str),
        "integer": lambda value: isinstance(value, int) and not isinstance(value, bool),
        "number": lambda value: isinstance(value, (int, float))
        and not isinstance(value, bool),
        "boolean": lambda value: isinstance(value, bool),
        "null": lambda value: value is None,
    }
    if expected and not type_ok[expected](instance):
        return [f"{path}: expected {expected}, got {type(instance).__name__}"]

    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: value {instance!r} is not in enum")

    if isinstance(instance, str) and len(instance) < schema.get("minLength", 0):
        errors.append(f"{path}: string is shorter than {schema['minLength']}")
    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0):
            errors.append(f"{path}: array has fewer than {schema['minItems']} items")
        item_schema = schema.get("items")
        if item_schema:
            for index, item in enumerate(instance):
                errors.extend(validate_schema(item, item_schema, f"{path}[{index}]"))
    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            errors.append(f"{path}: value is below {schema['minimum']}")
        if "maximum" in schema and instance > schema["maximum"]:
            errors.append(f"{path}: value is above {schema['maximum']}")
    if isinstance(instance, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in instance:
                errors.append(f"{path}: missing required property {key!r}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in instance:
                if key not in properties:
                    errors.append(f"{path}: unexpected property {key!r}")
        for key, value in instance.items():
            if key in properties:
                errors.extend(
                    validate_schema(value, properties[key], f"{path}.{key}")
                )
    return errors


def source_status_conflicts(source_status: str, audited_status: str) -> bool:
    """Conservative source-vs-audit conflict used for recheck selection."""

    unresolved_source = {"open", "falsifiable", "verifiable", "decidable"}
    meta_source = {"not disprovable", "not provable", "independent"}
    open_audit = {"confirmed_open", "likely_open"}
    meta_audit = {"meta_mathematical", "ambiguous", "insufficient_evidence"}
    if source_status in unresolved_source:
        return audited_status not in open_audit
    if source_status in meta_source:
        return audited_status not in meta_audit
    return False


def core_signature(review: dict[str, Any]) -> tuple[Any, ...]:
    statement = review.get("statement_audit") or {}
    return (
        review.get("current_status"),
        review.get("status_confidence"),
        review.get("actionability"),
        statement.get("ambiguity_severity"),
        statement.get("easy_counterexample_status"),
    )
