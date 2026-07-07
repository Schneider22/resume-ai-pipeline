"""
detector.py

Detects the type of the input file.
"""

from pathlib import Path


class FileDetector:
    """
    Detects the file type based on its extension.
    """

    SUPPORTED_TYPES = {
        ".txt": "TEXT",
        ".pdf": "PDF",
        ".docx": "DOCX",
        ".png": "IMAGE",
        ".jpg": "IMAGE",
        ".jpeg": "IMAGE",
    }

    @classmethod
    def detect(cls, file_path: Path) -> str:
        """
        Detect file type.

        Parameters
        ----------
        file_path : Path

        Returns
        -------
        str

        Raises
        ------
        ValueError
            If the file extension is not supported.
        """

        extension = file_path.suffix.lower()

        if extension not in cls.SUPPORTED_TYPES:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        return cls.SUPPORTED_TYPES[extension]