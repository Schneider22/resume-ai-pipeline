"""
config.py

Central configuration for Resume AI Pipeline.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

# ==========================================================
# Load environment variables
# ==========================================================

load_dotenv()


class Settings:
    """
    Central configuration class.

    Every module in the application must obtain its
    configuration from this class.
    """

    def __init__(self) -> None:

        # ==================================================
        # Project Root
        # ==================================================

        self.project_root = Path(__file__).resolve().parent

        # ==================================================
        # Directories
        # ==================================================

        self.input_dir = self.project_root / "input"

        self.output_dir = self.project_root / "output"

        self.logs_dir = self.project_root / "logs"

        self.prompts_dir = self.project_root / "prompts"

        self.schemas_dir = self.project_root / "schemas"

        self.data_dir = self.project_root / "data"

        self.tests_dir = self.project_root / "tests"

        # ==================================================
        # Files
        # ==================================================

        self.job_input_file = (
            self.input_dir / "job_offer.txt"
        )

        self.job_output_file = (
            self.output_dir / "job_description.json"
        )

        self.job_prompt_file = (
            self.prompts_dir / "job_parser_prompt.txt"
        )

        self.job_schema_file = (
            self.schemas_dir / "job_schema.json"
        )

        # ==================================================
        # Provider
        # ==================================================

        self.provider = os.getenv(
            "LLM_PROVIDER",
            "GEMINI"
        ).upper()

        # ==================================================
        # Gemini
        # ==================================================

        self.gemini_api_key = os.getenv(
            "GEMINI_API_KEY",
            ""
        )

        self.gemini_model = os.getenv(
            "GEMINI_MODEL",
            "gemini-2.5-flash"
        )

        # ==================================================
        # OpenAI
        # ==================================================

        self.openai_api_key = os.getenv(
            "OPENAI_API_KEY",
            ""
        )

        self.openai_model = os.getenv(
            "OPENAI_MODEL",
            "gpt-5"
        )

        # ==================================================
        # Amazon Bedrock
        # ==================================================

        self.bedrock_model = os.getenv(
            "BEDROCK_MODEL",
            ""
        )

        # ==================================================
        # Generation
        # ==================================================

        self.temperature = float(
            os.getenv(
                "TEMPERATURE",
                "0.2"
            )
        )

        self.max_tokens = int(
            os.getenv(
                "MAX_TOKENS",
                "4000"
            )
        )

        # ==================================================
        # Logging
        # ==================================================

        self.log_level = os.getenv(
            "LOG_LEVEL",
            "INFO"
        ).upper()

        # ==================================================
        # Create project directories
        # ==================================================

        self.create_directories()

        # ==================================================
        # Validate configuration
        # ==================================================

        self._validate()

    # ==================================================

    def create_directories(self) -> None:
        """
        Creates all required directories.
        """

        directories = [

            self.input_dir,

            self.output_dir,

            self.logs_dir,

            self.prompts_dir,

            self.schemas_dir,

            self.data_dir,

            self.tests_dir,

        ]

        for directory in directories:

            directory.mkdir(
                parents=True,
                exist_ok=True
            )

    # ==================================================

    def _validate(self) -> None:
        """
        Validate configuration.
        """

        providers = {

            "GEMINI",

            "OPENAI",

            "BEDROCK",

        }

        if self.provider not in providers:

            raise ValueError(
                f"Unsupported provider: {self.provider}"
            )

        if (
            self.provider == "GEMINI"
            and not self.gemini_api_key
        ):

            raise ValueError(
                "GEMINI_API_KEY is missing."
            )

        if (
            self.provider == "OPENAI"
            and not self.openai_api_key
        ):

            raise ValueError(
                "OPENAI_API_KEY is missing."
            )

    # ==================================================

    @property
    def model(self) -> str:
        """
        Returns the active model.
        """

        if self.provider == "GEMINI":
            return self.gemini_model

        if self.provider == "OPENAI":
            return self.openai_model

        if self.provider == "BEDROCK":
            return self.bedrock_model

        raise ValueError(
            f"Unknown provider: {self.provider}"
        )

    # ==================================================

    def __repr__(self) -> str:

        return (
            "Settings("
            f"provider='{self.provider}', "
            f"model='{self.model}', "
            f"log_level='{self.log_level}')"
        )