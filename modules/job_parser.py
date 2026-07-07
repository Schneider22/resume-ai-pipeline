"""
job_parser.py

Main Job Parser module for Resume AI Pipeline.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from config import Settings
from modules.extractor import TextExtractor
from modules.llm_client import LLMClient
from modules.logger import LoggerManager
from modules.prompt_builder import PromptBuilder
from modules.utils import (
    save_json,
    write_text_file,
)
from modules.validator import JsonValidator


class JobParser:
    """
    Parses a job description into a validated JSON structure.
    """

    def __init__(self, settings: Settings) -> None:

        self.settings = settings

        self.logger = LoggerManager(
            settings.logs_dir,
            settings.log_level,
        ).get_logger()

        self.extractor = TextExtractor()

        self.prompt_builder = PromptBuilder(
            settings.job_prompt_file
        )

        self.llm_client = LLMClient(settings)

        self.validator = JsonValidator(
            settings.job_schema_file
        )

    # =====================================================

    def _clean_llm_response(
        self,
        response: str
    ) -> str:
        """
        Removes Markdown code fences from LLM responses.
        """

        response = response.strip()

        if response.startswith("```json"):
            response = response[7:]

        elif response.startswith("```"):
            response = response[3:]

        if response.endswith("```"):
            response = response[:-3]

        return response.strip()

    # =====================================================

    def parse(
        self,
        input_file: Path
    ) -> dict[str, Any]:
        """
        Parse a job description into structured JSON.

        Parameters
        ----------
        input_file : Path

        Returns
        -------
        dict[str, Any]
        """

        self.logger.info("Starting Job Parser...")

        # --------------------------------------------------
        # Read input file
        # --------------------------------------------------

        self.logger.info("Reading job description...")

        job_description = self.extractor.extract(
            input_file
        )

        # --------------------------------------------------
        # Build prompt
        # --------------------------------------------------

        self.logger.info("Building prompt...")

        prompt = self.prompt_builder.build(
            job_description
        )

        # --------------------------------------------------
        # Call LLM
        # --------------------------------------------------

        self.logger.info("Calling LLM...")

        response = self.llm_client.generate(
            prompt
        )

        # --------------------------------------------------
        # Save raw LLM response
        # --------------------------------------------------

        raw_response_file = (
            self.settings.logs_dir
            / "raw_llm_response.txt"
        )

        write_text_file(
            raw_response_file,
            response
        )

        # --------------------------------------------------
        # Clean Markdown
        # --------------------------------------------------

        response = self._clean_llm_response(
            response
        )

        # --------------------------------------------------
        # Parse JSON
        # --------------------------------------------------

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

        # --------------------------------------------------
        # Validate Schema
        # --------------------------------------------------

        self.logger.info("Validating schema...")

        self.validator.validate(result)

        # --------------------------------------------------
        # Save Output
        # --------------------------------------------------

        self.logger.info("Saving output...")

        save_json(
            self.settings.job_output_file,
            result
        )

        self.logger.info(
            "Job Parser completed successfully."
        )

        return result