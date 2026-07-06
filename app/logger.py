import logging
from pathlib import Path

from app.config import settings


def setup_logger() -> logging.Logger:
   
   
    settings.logs_directory.mkdir(parents=True, exist_ok=True)

    log_file = settings.logs_directory / "application.log"

    logger = logging.getLogger("cost-efficient-rag")

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


logger = setup_logger()