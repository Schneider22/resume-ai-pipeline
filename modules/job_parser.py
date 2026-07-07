"""
job_parser.py

Main Job Parser module for Resume AI Pipeline.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from config import Settings
from modules.logger import LoggerManager
from modules.prompt_builder import PromptBuilder
from modules.llm_client import LLMClient
from modules.validator import SchemaValidator
from modules.utils import (
    read_text_file,
    save_json,
)


class JobParser:
    """
    Parses a job description into a validated JSON structure.
    """

    def __init__(self, settings: Settings) -> None:

        self.settings = settings

        self.logger = LoggerManager(
            settings.logs_dir,
            settings.log_level
        ).get_logger()

        self.prompt_builder = PromptBuilder(
            settings.job_prompt_file
        )

        self.llm_client = LLMClient(settings)

        self.validator = SchemaValidator(
            settings.job_schema_file
        )

    # =====================================================

    def parse(
        self,
        input_file: Path
    ) -> dict[str, Any]:
        """
        Parse a job description.

        Parameters
        ----------
        input_file : Path

        Returns
        -------
        dict
        """

        self.logger.info("Starting Job Parser...")

        # -----------------------------------------------
        # Read input file
        # -----------------------------------------------

        self.logger.info("Reading job description...")

        from modules.extractor import TextExtractor

        ...

        self.extractor = TextExtractor()

        ...

        job_description = self.extractor.extract(
            input_file
        )

        # -----------------------------------------------
        # Build prompt
        # -----------------------------------------------

        self.logger.info("Building prompt...")

        prompt = self.prompt_builder.build(
            job_description
        )

        # -----------------------------------------------
        # Call LLM
        # -----------------------------------------------

        self.logger.info("Calling LLM...")

        response = self.llm_client.generate(
            prompt
        )

        # -----------------------------------------------
        # Convert response to JSON
        # -----------------------------------------------

        self.logger.info("Parsing JSON response...")

        try:

            result = json.loads(response)

        except json.JSONDecodeError as ex:

            self.logger.error(
                "LLM returned invalid JSON."
            )

            raise ValueError(
                "Invalid JSON received from LLM."
            ) from ex

        # -----------------------------------------------
        # Validate schema
        # -----------------------------------------------

        self.logger.info("Validating schema...")

        self.validator.validate(result)

        # -----------------------------------------------
        # Save output
        # -----------------------------------------------

        self.logger.info("Saving output JSON...")

        save_json(
            self.settings.job_output_file,
            result
        )

        self.logger.info("Job Parser completed successfully.")

        return result