from app.llm import generate_answer
from app.retriever import retrieve


def answer_question(question: str,filename: str | None = None,) -> dict:
    

    retrieval_result = retrieve(
    question,
    filename,
)

    answer = generate_answer(
        question,
        retrieval_result,
    )

    return {
        "question": question,
        "answer": answer,
        "retrieved_chunks": retrieval_result.retrieved_count,
        "sources": [
            chunk.source
            for chunk in retrieval_result.chunks
        ],
    }