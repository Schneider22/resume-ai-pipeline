"""
extractor.py

Extracts text from supported file types.
"""

from pathlib import Path

import fitz
import pytesseract

from PIL import Image
from docx import Document

from modules.detector import FileDetector


class TextExtractor:
    """
    Extracts text from TXT, PDF, DOCX and image files.
    """

    def extract(self, file_path: Path) -> str:

        file_type = FileDetector.detect(file_path)

        if file_type == "TEXT":
            return self._extract_txt(file_path)

        if file_type == "PDF":
            return self._extract_pdf(file_path)

        if file_type == "DOCX":
            return self._extract_docx(file_path)

        if file_type == "IMAGE":
            return self._extract_image(file_path)

        raise ValueError(f"Unsupported file type: {file_type}")

    # --------------------------------------------------

    def _extract_txt(self, file_path: Path) -> str:

        return file_path.read_text(
            encoding="utf-8"
        )

    # --------------------------------------------------

    def _extract_pdf(self, file_path: Path) -> str:

        text = []

        pdf = fitz.open(file_path)

        for page in pdf:
            text.append(page.get_text())

        pdf.close()

        return "\n".join(text)

    # --------------------------------------------------

    def _extract_docx(self, file_path: Path) -> str:

        document = Document(file_path)

        paragraphs = [
            paragraph.text
            for paragraph in document.paragraphs
            if paragraph.text.strip()
        ]

        return "\n".join(paragraphs)

    # --------------------------------------------------

    def _extract_image(self, file_path: Path) -> str:

        image = Image.open(file_path)

        return pytesseract.image_to_string(image)