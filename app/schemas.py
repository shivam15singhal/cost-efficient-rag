from pydantic import BaseModel


class RetrievedChunk(BaseModel):
    

    content: str
    source: str
    page: int | None
    score: float


class RetrievalResult(BaseModel):
    has_context: bool
    chunks: list[RetrievedChunk]
    retrieved_count: int