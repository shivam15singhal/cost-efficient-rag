from app.llm import generate_answer
from app.retriever import retrieve


def main():

    while True:

        question = input("\nQuestion (or exit): ")

        if question.lower() == "exit":
            break

        retrieval = retrieve(question)

        answer = generate_answer(
            question,
            retrieval,
        )

        print()

        print(answer)

        print()


if __name__ == "__main__":
    main()