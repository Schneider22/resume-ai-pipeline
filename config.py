"""
config.py

Central configuration for the Resume AI Pipeline.

This module loads environment variables and exposes a single
Settings class used throughout the application.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv

# Load .env file
load_dotenv()


class Settings:
    """
    Central application settings.

    Reads all configuration from environment variables.
    """

    def __init__(self) -> None:

        # --------------------------------------------------
        # Provider
        # --------------------------------------------------

        self.provider: str = os.getenv(
            "LLM_PROVIDER",
            "GEMINI"
        ).upper()

        # --------------------------------------------------
        # Gemini
        # --------------------------------------------------

        self.gemini_api_key: str = os.getenv(
            "GEMINI_API_KEY",
            ""
        )

        self.gemini_model: str = os.getenv(
            "GEMINI_MODEL",
            "gemini-2.5-flash"
        )

        # --------------------------------------------------
        # OpenAI
        # --------------------------------------------------

        self.openai_api_key: str = os.getenv(
            "OPENAI_API_KEY",
            ""
        )

        self.openai_model: str = os.getenv(
            "OPENAI_MODEL",
            "gpt-5"
        )

        # --------------------------------------------------
        # Future Providers
        # --------------------------------------------------

        self.bedrock_model: str = os.getenv(
            "BEDROCK_MODEL",
            ""
        )

        # --------------------------------------------------
        # Generation
        # --------------------------------------------------

        self.temperature: float = float(
            os.getenv(
                "TEMPERATURE",
                "0.2"
            )
        )

        self.max_tokens: int = int(
            os.getenv(
                "MAX_TOKENS",
                "4000"
            )
        )

        # --------------------------------------------------
        # Logging
        # --------------------------------------------------

        self.log_level: str = os.getenv(
            "LOG_LEVEL",
            "INFO"
        ).upper()

        # --------------------------------------------------
        # Validation
        # --------------------------------------------------

        self._validate()

    # ==================================================

    def _validate(self) -> None:
        """
        Validate configuration.
        """

        supported = {
            "GEMINI",
            "OPENAI",
            "BEDROCK"
        }

        if self.provider not in supported:
            raise ValueError(
                f"Unsupported LLM provider: {self.provider}"
            )

        if self.provider == "GEMINI" and not self.gemini_api_key:
            raise ValueError(
                "GEMINI_API_KEY is not configured."
            )

        if self.provider == "OPENAI" and not self.openai_api_key:
            raise ValueError(
                "OPENAI_API_KEY is not configured."
            )

    # ==================================================

    @property
    def model(self) -> str:
        """
        Returns the active model according to the provider.
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
            f"Settings("
            f"provider='{self.provider}', "
            f"model='{self.model}', "
            f"log_level='{self.log_level}')"
        )