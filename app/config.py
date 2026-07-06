from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()


@dataclass(frozen=True)
class Settings:
    """
    Stores all application configuration in one place.
    """

    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")

    chunk_size: int = int(os.getenv("CHUNK_SIZE", 500))
    chunk_overlap: int = int(os.getenv("CHUNK_OVERLAP", 100))

    top_k: int = int(os.getenv("TOP_K", 5))

    similarity_threshold: float = float(
        os.getenv("SIMILARITY_THRESHOLD", 0.35)
    )

    project_root: Path = Path(__file__).resolve().parent.parent

    data_directory: Path = project_root / "data"
    raw_data_directory: Path = data_directory / "raw"
    processed_data_directory: Path = data_directory / "processed"

    chroma_directory: Path = project_root / "chroma_db"

    logs_directory: Path = project_root / "logs"


settings = Settings()