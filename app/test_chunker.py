from app.chunker import chunk_documents
from app.config import settings
from app.ingest import load_documents

documents = load_documents(
    settings.raw_data_directory
)

chunks = chunk_documents(documents)

print()

print(f"Total Chunks: {len(chunks)}")

print()

first_chunk = chunks[0]

print("Metadata")

print(first_chunk.metadata)

print()

print("Content")

print("-" * 50)

print(first_chunk.page_content)