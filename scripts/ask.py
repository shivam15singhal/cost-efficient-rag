from app.rag_service import answer_question


def main():

    while True:

        question = input("\nQuestion (or exit): ")

        if question.lower() == "exit":
            break

        result = answer_question(question)

        print()

        print(result["answer"])

        print()


if __name__ == "__main__":
    main()