import time

from google import genai

from app.config import settings
from app.logger import logger
from app.prompts import SYSTEM_PROMPT


client = genai.Client(api_key=settings.gemini_api_key)


def generate_answer(question: str, retrieval_result) -> str:
    """
    Generate a grounded answer using Gemini based only on the retrieved context.
    """

    if not retrieval_result.has_context:
        return "I couldn't find enough information in the provided documents."

    
    context_parts = []

    for chunk in retrieval_result.chunks:
        context_parts.append(
            f"""Source: {chunk.source}
Page: {chunk.page if chunk.page is not None else "N/A"}

{chunk.content}
"""
        )

    context = "\n\n".join(context_parts)

   
    prompt = SYSTEM_PROMPT.format(
        context=context,
        question=question,
    )

   
    start_time = time.perf_counter()

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

    except Exception as error:
        logger.exception(f"Gemini API Error: {error}")
        return "An error occurred while generating the answer."

    latency = time.perf_counter() - start_time

    logger.info(f"LLM latency: {latency:.2f} seconds")

    
    usage = getattr(response, "usage_metadata", None)

    if usage:

        logger.info(f"Prompt Tokens: {usage.prompt_token_count}")
        logger.info(f"Completion Tokens: {usage.candidates_token_count}")
        logger.info(f"Total Tokens: {usage.total_token_count}")

    
    answer = response.text.strip()

    citations = []
    seen = set()

    for chunk in retrieval_result.chunks:

        citation = (
            f"- {chunk.source} "
            f"(page {chunk.page if chunk.page is not None else 'N/A'})"
        )

        if citation not in seen:
            seen.add(citation)
            citations.append(citation)

    answer += "\n\nSources:\n"
    answer += "\n".join(citations)

    return answer