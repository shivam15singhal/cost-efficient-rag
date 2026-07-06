from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import settings
from app.logger import logger
from app.utils import generate_chunk_id
from pathlib import Path


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

  

    for index, chunk in enumerate(chunks):
        source = Path(
        chunk.metadata.get("source", "unknown")
        )
        chunk.metadata["chunk_id"] = generate_chunk_id(chunk.page_content)
        chunk.metadata["chunk_index"] = index
        chunk.metadata["filename"] = source.name
        chunk.metadata["document_type"] = source.suffix.lower()
        chunk.metadata["page"] = chunk.metadata.get("page", 0)
        chunk.metadata["content_length"] = len(chunk.page_content)

    return chunks