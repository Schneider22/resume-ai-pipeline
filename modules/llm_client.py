"""
llm_client.py

LLM client for Resume AI Pipeline.
Supports:
- Google Gemini
- OpenAI
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
        self.provider = settings.provider

        if self.provider == "GEMINI":

            self.client = genai.Client(
                api_key=settings.gemini_api_key
            )

        elif self.provider == "OPENAI":

            self.client = OpenAI(
                api_key=settings.openai_api_key
            )

        else:

            raise ValueError(
                f"Unsupported provider: {self.provider}"
            )

    # --------------------------------------------------

    def generate(self, prompt: str) -> str:
        """
        Generate text using the configured provider.
        """

        if not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        if self.provider == "GEMINI":
            return self._generate_gemini(prompt)

        if self.provider == "OPENAI":
            return self._generate_openai(prompt)

        raise ValueError(
            f"Unsupported provider: {self.provider}"
        )

    # --------------------------------------------------

    def _generate_gemini(self, prompt: str) -> str:

        response = self.client.models.generate_content(
            model=self.settings.gemini_model,
            contents=prompt,
        )

        if not response.text:
            raise RuntimeError("Empty response from Gemini.")

        return response.text.strip()

    # --------------------------------------------------

    def _generate_openai(self, prompt: str) -> str:

        response = self.client.responses.create(
            model=self.settings.openai_model,
            input=prompt,
            max_output_tokens=self.settings.max_tokens,
        )

        if not response.output_text:
            raise RuntimeError("Empty response from OpenAI.")

        return response.output_text.strip()