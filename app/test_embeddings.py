from app.embeddings import get_embedding_model

embedding_model = get_embedding_model()

vector = embedding_model.embed_query(
    "What is Retrieval-Augmented Generation?"
)

print()

print(f"Embedding Dimension : {len(vector)}")

print()

print(vector[:10])