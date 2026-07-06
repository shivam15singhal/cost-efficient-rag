from app.config import settings

print("Chunk Size:", settings.chunk_size)
print("Overlap:", settings.chunk_overlap)
print("Top K:", settings.top_k)
print("Database:", settings.chroma_path)