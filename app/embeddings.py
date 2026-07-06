from langchain_huggingface import HuggingFaceEmbeddings

from app.logger import logger

_embedding_model = None


def get_embedding_model():
    

    global _embedding_model

    if _embedding_model is None:

        logger.info("Loading embedding model...")

        _embedding_model = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en-v1.5",
            model_kwargs={
                "device": "cpu"
            },
            encode_kwargs={
                "normalize_embeddings": True
            }
        )

        logger.info("Embedding model loaded.")

    return _embedding_model