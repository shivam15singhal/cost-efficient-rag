from typing import List


def recall_at_k(relevant_found: int, total_relevant: int) -> float:
    if total_relevant == 0:
        return 0.0
    return relevant_found / total_relevant


def hit_rate(found: bool) -> float:
    return 1.0 if found else 0.0


def reciprocal_rank(rank: int | None) -> float:
    if rank is None:
        return 0.0
    return 1 / rank


def dcg(relevances: List[int]) -> float:
    score = 0

    for i, rel in enumerate(relevances):
        score += rel / __import__("math").log2(i + 2)

    return score


def ndcg(relevances: List[int]) -> float:

    ideal = sorted(relevances, reverse=True)

    actual = dcg(relevances)

    ideal_score = dcg(ideal)

    if ideal_score == 0:
        return 0.0

    return actual / ideal_score


def context_precision(
    relevant_chunks: int,
    retrieved_chunks: int,
) -> float:

    if retrieved_chunks == 0:
        return 0.0

    return relevant_chunks / retrieved_chunks