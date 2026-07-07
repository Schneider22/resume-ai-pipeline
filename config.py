"""
=====================================================================
Resume AI Pipeline
---------------------------------------------------------------------
File        : config.py
Author      : Jose Schneider Londoño Gonzalez
Description : Global configuration manager for the Resume AI Pipeline.
Version     : 1.0.0
Python      : 3.12+
=====================================================================
"""

from pathlib import Path
from dotenv import load_dotenv
import os

class Settings:
    """Centralized application settings."""

    def __init__(self) -> None:
        load_dotenv()

        # ==========================
        # Project Root
        # ==========================
        self.root_dir = Path(__file__).resolve().parent

        # ==========================
        # Directories
        # ==========================
        self.input_dir = self.root_dir / "input"
        self.output_dir = self.root_dir / "output"
        self.logs_dir = self.output_dir / "logs"
        self.data_dir = self.root_dir / "data"
        self.prompts_dir = self.root_dir / "prompts"
        self.schemas_dir = self.root_dir / "schemas"
        self.modules_dir = self.root_dir / "modules"
        self.tests_dir = self.root_dir / "tests"

        # ==========================
        # Files
        # ==========================
        self.master_cv_file = self.data_dir / "master_cv.json"
        self.job_schema_file = self.schemas_dir / "job_schema.json"
        self.job_prompt_file = self.prompts_dir / "job_parser_prompt.txt"
        self.system_prompt_file = self.prompts_dir / "system_prompt.txt"
        self.job_output_file = self.output_dir / "job_description.json"

        # ==========================
        # LLM
        # ==========================
        #self.provider = os.getenv("LLM_PROVIDER", "OPENAI")
        #self.model = os.getenv("OPENAI_MODEL", "gpt-5")
        self.provider = os.getenv("LLM_PROVIDER", "GEMINI")
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.gemini_model = os.getenv("GEMINI_MODEL","gemini-2.5-flash")
        self.openai_model = os.getenv("OPENAI_MODEL", "gpt-5")
        self.temperature = float(os.getenv("TEMPERATURE", "0.2"))
        self.max_tokens = int(os.getenv("MAX_TOKENS", "4000"))

        # ==========================
        # Logging
        # ==========================
        self.log_level = os.getenv("LOG_LEVEL", "INFO")

    def create_directories(self) -> None:
        """Create project directories if they do not exist."""

        directories = [
            self.input_dir,
            self.output_dir,
            self.logs_dir,
            self.data_dir,
            self.prompts_dir,
            self.schemas_dir,
            self.modules_dir,
            self.tests_dir,
        ]

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)