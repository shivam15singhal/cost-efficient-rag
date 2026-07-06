from app.config import settings
from app.ingest import load_documents


documents = load_documents(
    settings.raw_data_directory
)

print(f"\nLoaded {len(documents)} documents\n")

for document in documents[:3]:
    print("-" * 50)
    print(document.metadata)