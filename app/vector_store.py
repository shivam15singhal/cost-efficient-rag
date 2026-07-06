from langchain_chroma import Chroma

from app.config import settings
from app.embeddings import get_embedding_model


def get_vector_store():

    return Chroma(
        collection_name="documents",
        embedding_function=get_embedding_model(),
        persist_directory=str(settings.chroma_directory),
    )