from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import settings
from app.logger import logger
from app.utils import generate_chunk_id


def chunk_documents(documents):
   

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            "",
        ],
    )

    chunks = splitter.split_documents(documents)

    logger.info(f"Generated {len(chunks)} chunks.")

    for index, chunk in enumerate(chunks):

        chunk.metadata["chunk_id"] = generate_chunk_id(
            chunk.page_content
        )

        chunk.metadata["chunk_index"] = index

    return chunks