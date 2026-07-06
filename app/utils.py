from hashlib import sha256


def generate_chunk_id(text: str) -> str:
    """
    Generate a stable SHA256 hash for a chunk.

    This hash is later used to prevent duplicate vectors
    during re-ingestion.
    """
    return sha256(text.encode("utf-8")).hexdigest()