# Cost Comparison

## Assumptions

- Vector Database: ChromaDB (self-hosted)
- Embedding Model: BAAI/bge-small-en-v1.5
- Embedding Dimension: 384
- Single replica
- Approximate embedding storage only
- Small cloud VM (~$6/month) for self-hosting
- Managed comparison based on Pinecone Serverless pricing assumptions

| Vectors | ChromaDB | Managed Vector DB | Notes |
|---------:|---------:|------------------:|------|
|100K|~$6/month|~$19/month|Small corpus|
|1M|~$6/month|~$70/month|Storage grows|
|10M|~$12/month|~$450/month|Managed costs dominate|

## Discussion

ChromaDB provides significantly lower infrastructure costs for small-to-medium RAG applications because there are no always-on managed vector database charges. The trade-off is that deployment, backups, scaling, and monitoring must be managed manually. For production workloads requiring high availability, automatic scaling, and enterprise SLAs, a managed vector database would become preferable.