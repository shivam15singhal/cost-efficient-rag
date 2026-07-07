import json
import time
from pathlib import Path
import statistics

from app.retriever import retrieve
from evaluation.metrics import (
    recall_at_k,
    hit_rate,
    reciprocal_rank,
    ndcg,
    context_precision,
)

QUESTIONS_FILE = Path("evaluation/questions.json")
OUTPUT_FILE = Path("evaluation/results/report.json")


def evaluate():

    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        questions = json.load(f)

    results = []

    retrieval_latencies = []

    recall_scores = []
    hit_scores = []
    mrr_scores = []
    ndcg_scores = []
    context_scores = []

    for item in questions:

        question = item["question"]
        expected_source = item["relevant_source"]

        start = time.perf_counter()

        retrieval = retrieve(question)

        latency = (time.perf_counter() - start) * 1000

        retrieval_latencies.append(latency)

        retrieved_sources = [
            chunk.source
            for chunk in retrieval.chunks
        ]

        found = expected_source in retrieved_sources

        relevant_found = 1 if found else 0

        try:
            rank = retrieved_sources.index(expected_source) + 1
        except ValueError:
            rank = None

        relevances = [
            1 if s == expected_source else 0
            for s in retrieved_sources
        ]

        recall = recall_at_k(relevant_found, 1)
        hit = hit_rate(found)
        mrr = reciprocal_rank(rank)
        ndcg_score = ndcg(relevances)
        precision = context_precision(
            relevant_found,
            len(retrieved_sources),
        )

        recall_scores.append(recall)
        hit_scores.append(hit)
        mrr_scores.append(mrr)
        ndcg_scores.append(ndcg_score)
        context_scores.append(precision)

        results.append(
            {
                "question": question,
                "expected": expected_source,
                "retrieved": retrieved_sources,
                "latency_ms": round(latency, 2),
                "recall": recall,
                "hit_rate": hit,
                "mrr": round(mrr, 3),
                "ndcg": round(ndcg_score, 3),
                "context_precision": round(precision, 3),
            }
        )

    summary = {
        "questions": len(results),
        "Recall@k": round(sum(recall_scores) / len(recall_scores), 3),
        "HitRate": round(sum(hit_scores) / len(hit_scores), 3),
        "MRR": round(sum(mrr_scores) / len(mrr_scores), 3),
        "nDCG": round(sum(ndcg_scores) / len(ndcg_scores), 3),
        "ContextPrecision": round(sum(context_scores) / len(context_scores), 3),
        "RetrievalLatencyMean": round(
            sum(retrieval_latencies) / len(retrieval_latencies),
            2,
        ),
        "RetrievalLatencyP50": round(
    statistics.median(retrieval_latencies),
    2,
),
"RetrievalLatencyP95": round(
    sorted(retrieval_latencies)[
        int(0.95 * len(retrieval_latencies)) - 1
    ],
    2,
),
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

        json.dump(
            {
                "summary": summary,
                "results": results,
            },
            f,
            indent=4,
        )

    print("\nEvaluation Complete\n")

    for key, value in summary.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    evaluate()