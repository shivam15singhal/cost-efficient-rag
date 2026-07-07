import json
from pathlib import Path

from google import genai

from app.config import settings
from app.rag_service import answer_question

client = genai.Client(api_key=settings.gemini_api_key)

QUESTIONS_FILE = Path("evaluation/questions.json")
OUTPUT_FILE = Path("evaluation/results/answer_report.json")

JUDGE_PROMPT = """
You are an evaluator for Retrieval-Augmented Generation (RAG).

Evaluate the generated answer.

Score both metrics from 1-5.

Faithfulness:
5 = Completely supported by retrieved context.
1 = Hallucinated or unsupported.

Answer Relevance:
5 = Fully answers the question.
1 = Doesn't answer the question.

Return ONLY valid JSON.

{{
    "faithfulness": 5,
    "answer_relevance": 5,
    "reason": "short explanation"
}}

Question:
{question}

Answer:
{answer}
"""


def evaluate_answers():

    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        questions = json.load(f)

    reports = []

    faithfulness_scores = []
    relevance_scores = []

    for item in questions:

        question = item["question"]

        rag_result = answer_question(question)

        prompt = JUDGE_PROMPT.format(
            question=question,
            answer=rag_result["answer"],
        )

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        try:
            result = json.loads(response.text)
        except Exception:
            continue

        faithfulness_scores.append(result["faithfulness"])
        relevance_scores.append(result["answer_relevance"])

        reports.append(
            {
                "question": question,
                "answer": rag_result["answer"],
                "faithfulness": result["faithfulness"],
                "answer_relevance": result["answer_relevance"],
                "reason": result["reason"],
            }
        )

    summary = {
        "Average Faithfulness": round(
            sum(faithfulness_scores) / len(faithfulness_scores),
            2,
        ),
        "Average Answer Relevance": round(
            sum(relevance_scores) / len(relevance_scores),
            2,
        ),
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(
            {
                "summary": summary,
                "reports": reports,
            },
            f,
            indent=4,
        )

    print(summary)


if __name__ == "__main__":
    evaluate_answers()