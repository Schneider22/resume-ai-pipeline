"""
llm_client.py

LLM client for Resume AI Pipeline.

Supports multiple providers:

- Google Gemini
- OpenAI

Future:

- Amazon Bedrock
- Anthropic
"""

from __future__ import annotations

from google import genai
from openai import OpenAI

from config import Settings


class LLMClient:
    """
    Generic LLM client.
    """

    def __init__(self, settings: Settings) -> None:

        self.settings = settings
        self.provider = settings.provider.upper()

        if self.provider == "GEMINI":

            self.client = genai.Client(
                api_key=settings.gemini_api_key
            )

        elif self.provider == "OPENAI":

            self.client = OpenAI(
                api_key=settings.openai_api_key
            )

        else:

            raise NotImplementedError(
                f"Provider '{self.provider}' is not implemented."
            )

    # ==================================================

    def generate(self, prompt: str) -> str:
        """
        Generate text using the configured provider.
        """

        if self.provider == "GEMINI":
            return self._generate_gemini(prompt)

        if self.provider == "OPENAI":
            return self._generate_openai(prompt)

        raise RuntimeError("Unknown provider.")

    # ==================================================

    def _generate_gemini(self, prompt: str) -> str:
        """
        Generate using Gemini.
        """

        response = self.client.models.generate_content(
            model=self.settings.gemini_model,
            contents=prompt,
        )

        return response.text.strip()

    # ==================================================

    def _generate_openai(self, prompt: str) -> str:
        """
        Generate using OpenAI.
        """

        response = self.client.responses.create(
            model=self.settings.openai_model,
            input=prompt,
            max_output_tokens=self.settings.max_tokens,
        )

        return response.output_text.strip()