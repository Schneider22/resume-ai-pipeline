"""
logger.py

Centralized logging configuration for Resume AI Pipeline.
"""

from pathlib import Path
import logging

import colorlog


class LoggerManager:
    """
    Creates and configures the application logger.
    """

    def __init__(self, logs_directory: Path, level: str = "INFO") -> None:
        self.logs_directory = logs_directory
        self.level = getattr(logging, level.upper(), logging.INFO)

        self.logs_directory.mkdir(parents=True, exist_ok=True)

    def get_logger(self, name: str = "ResumeAI") -> logging.Logger:
        """
        Returns a configured logger instance.

        Parameters
        ----------
        name : str
            Logger name.

        Returns
        -------
        logging.Logger
        """

        logger = logging.getLogger(name)

        if logger.handlers:
            return logger

        logger.setLevel(self.level)

        # ---------------------------------------------------------
        # Console Handler
        # ---------------------------------------------------------

        console_handler = logging.StreamHandler()

        console_formatter = colorlog.ColoredFormatter(
            "%(log_color)s%(asctime)s | %(levelname)-8s | %(message)s",
            datefmt="%H:%M:%S",
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            },
        )

        console_handler.setFormatter(console_formatter)

        # ---------------------------------------------------------
        # File Handler
        # ---------------------------------------------------------

        log_file = self.logs_directory / "resume_ai.log"

        file_handler = logging.FileHandler(
            log_file,
            encoding="utf-8",
        )

        file_formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler.setFormatter(file_formatter)

        # ---------------------------------------------------------
        # Register Handlers
        # ---------------------------------------------------------

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        return logger