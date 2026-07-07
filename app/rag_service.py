from app.llm import generate_answer
from app.retriever import retrieve


def answer_question(question: str) -> dict:
    

    retrieval_result = retrieve(question)

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