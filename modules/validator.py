"""
validator.py

JSON schema validator for Resume AI Pipeline.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import validate
from jsonschema.exceptions import ValidationError


class SchemaValidator:
    """
    Validates dictionaries against a JSON Schema.
    """

    def __init__(self, schema_path: str | Path) -> None:

        self.schema_path = Path(schema_path)

        if not self.schema_path.exists():
            raise FileNotFoundError(
                f"Schema not found: {self.schema_path}"
            )

        with open(
            self.schema_path,
            "r",
            encoding="utf-8",
        ) as file:

            self.schema = json.load(file)

    # ==================================================

    def validate(
        self,
        data: dict[str, Any],
    ) -> bool:
        """
        Validate data against the loaded schema.
        """

        try:

            validate(
                instance=data,
                schema=self.schema,
            )

            return True

        except ValidationError as ex:

            raise ValueError(
                f"JSON validation failed:\n{ex.message}"
            ) from ex


# ------------------------------------------------------
# Backward compatibility
# ------------------------------------------------------

JsonValidator = SchemaValidator