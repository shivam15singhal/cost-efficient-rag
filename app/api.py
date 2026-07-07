from fastapi import FastAPI
from pydantic import BaseModel

from app.rag_service import answer_question

app = FastAPI(
    title="Cost Efficient RAG API",
    version="1.0.0",
)


class QueryRequest(BaseModel):
    question: str
    filename: str | None = None


@app.post("/query")
def query(request: QueryRequest):

    return answer_question(
    request.question,
    request.filename,
)