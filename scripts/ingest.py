import time

from app.chunker import chunk_documents
from app.config import settings
from app.ingest import load_documents
from app.logger import logger
from app.store_chunks import store_chunks
from app.vector_store import get_vector_store

logger.info(
    f"Chunk Size={settings.chunk_size}, "
    f"Overlap={settings.chunk_overlap}, "
    f"Top-K={settings.top_k}"
)

def main():

    start_time = time.perf_counter()

    logger.info("=" * 60)
    logger.info("Starting document ingestion")

    documents = load_documents(
        settings.raw_data_directory
    )

    logger.info(f"Loaded {len(documents)} document pages.")

    chunks = chunk_documents(documents)

    logger.info(f"Generated {len(chunks)} chunks.")

    inserted, skipped = store_chunks(chunks)

    vector_store = get_vector_store()

    vector_count = len(vector_store.get()["ids"])

    elapsed = time.perf_counter() - start_time

    logger.info("-" * 60)

    logger.info(f"Inserted : {inserted}")
    logger.info(f"Skipped  : {skipped}")
    logger.info(f"Total vectors : {vector_count}")
    logger.info(f"Elapsed : {elapsed:.2f} seconds")

    logger.info("=" * 60)

    print()

    print("Ingestion Summary")

    print("----------------------------")

    print(f"Documents Loaded : {len(documents)}")

    print(f"Chunks Generated : {len(chunks)}")

    print(f"Inserted Chunks  : {inserted}")

    print(f"Skipped Chunks   : {skipped}")

    print(f"Vector Count     : {vector_count}")

    print(f"Time Taken       : {elapsed:.2f} seconds")


if __name__ == "__main__":
    main()