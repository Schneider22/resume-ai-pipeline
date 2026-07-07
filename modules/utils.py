"""
utils.py

Common utility functions for Resume AI Pipeline.
"""

from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime
from typing import Any


def ensure_directory(directory: Path) -> None:
    """
    Create a directory if it does not exist.

    Parameters
    ----------
    directory : Path
        Directory to create.
    """
    directory.mkdir(parents=True, exist_ok=True)


def read_text_file(file_path: Path) -> str:
    """
    Read a UTF-8 text file.

    Parameters
    ----------
    file_path : Path

    Returns
    -------
    str
    """
    return file_path.read_text(encoding="utf-8")


def write_text_file(file_path: Path, content: str) -> None:
    """
    Write a UTF-8 text file.

    Parameters
    ----------
    file_path : Path
    content : str
    """
    file_path.write_text(content, encoding="utf-8")


def load_json(file_path: Path) -> dict[str, Any]:
    """
    Load a JSON file.

    Parameters
    ----------
    file_path : Path

    Returns
    -------
    dict
    """
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_json(file_path: Path, data: dict[str, Any]) -> None:
    """
    Save a dictionary as JSON.

    Parameters
    ----------
    file_path : Path
    data : dict
    """
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False,
        )


def file_exists(file_path: Path) -> bool:
    """
    Check if a file exists.

    Parameters
    ----------
    file_path : Path

    Returns
    -------
    bool
    """
    return file_path.exists()


def current_timestamp() -> str:
    """
    Returns current timestamp.

    Returns
    -------
    str
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def current_date() -> str:
    """
    Returns current date.

    Returns
    -------
    str
    """
    return datetime.now().strftime("%Y-%m-%d")


def current_time() -> str:
    """
    Returns current time.

    Returns
    -------
    str
    """
    return datetime.now().strftime("%H:%M:%S")