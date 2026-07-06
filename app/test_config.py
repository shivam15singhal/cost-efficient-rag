from app.config import settings

print("=" * 50)
print("Configuration Loaded")
print("=" * 50)

print(f"Chunk Size           : {settings.chunk_size}")
print(f"Chunk Overlap        : {settings.chunk_overlap}")
print(f"Top K                : {settings.top_k}")
print(f"Similarity Threshold : {settings.similarity_threshold}")

print()
print("Directories")

print(settings.raw_data_directory)
print(settings.processed_data_directory)
print(settings.chroma_directory)
print(settings.logs_directory)