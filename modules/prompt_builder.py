"""
prompt_builder.py

Builds the final prompt that will be sent to the LLM.
"""

from pathlib import Path

from modules.utils import read_text_file


class PromptBuilder:
    """
    Builds prompts from template files.

    The prompt template must contain the placeholder:

        {{JOB_DESCRIPTION}}

    which will be replaced with the extracted job description.
    """

    PLACEHOLDER = "{{JOB_DESCRIPTION}}"

    def __init__(self, prompt_file: Path) -> None:
        self.prompt_file = prompt_file

    def build(self, job_description: str) -> str:
        """
        Build the final prompt.

        Parameters
        ----------
        job_description : str
            Extracted text from the job offer.

        Returns
        -------
        str
            Final prompt ready to send to the LLM.
        """

        template = read_text_file(self.prompt_file)

        if self.PLACEHOLDER not in template:
            raise ValueError(
                f"Placeholder '{self.PLACEHOLDER}' was not found in the prompt template."
            )

        return template.replace(
            self.PLACEHOLDER,
            job_description.strip()
        )