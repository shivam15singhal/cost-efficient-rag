from app.config import settings
from app.schemas import RetrievalResult, RetrievedChunk
from app.vector_store import get_vector_store


def retrieve(question: str) -> RetrievalResult:
    

    vector_store = get_vector_store()

    results = vector_store.similarity_search_with_relevance_scores(
        question,
        k=settings.top_k,
    )

    retrieved_chunks = []

    for document, score in results:
        from app.logger import logger
        logger.info(
    f"Retrieved score: {score:.4f}"
)

        if score < settings.similarity_threshold:
            continue

        retrieved_chunks.append(
            RetrievedChunk(
                content=document.page_content,
                source=document.metadata.get("source", "Unknown"),
                page=document.metadata.get("page"),
                score=score,
            )
        )

    return RetrievalResult(
        has_context=len(retrieved_chunks) > 0,
        chunks=retrieved_chunks,
    )