from app.logger import logger
from app.vector_store import get_vector_store


def store_chunks(chunks):
   

    vector_store = get_vector_store()

    existing_ids = set(vector_store.get()["ids"])

    new_chunks = []
    new_ids = []

    skipped = 0

    for chunk in chunks:

        chunk_id = chunk.metadata["chunk_id"]

        if chunk_id in existing_ids:
            skipped += 1
            continue

        new_chunks.append(chunk)
        new_ids.append(chunk_id)

    if new_chunks:

        vector_store.add_documents(
            documents=new_chunks,
            ids=new_ids
        )

        logger.info(
            f"Inserted {len(new_chunks)} chunks."
        )

    else:

        logger.info("No new chunks inserted.")

    return len(new_chunks), skipped