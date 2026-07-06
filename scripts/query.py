from app.retriever import retrieve


def main():

    while True:

        question = input("\nQuestion (or 'exit'): ")

        if question.lower() == "exit":
            break

        result = retrieve(question)

        if not result.has_context:

            print("\nNo relevant context found.\n")
            continue

        print("\nRetrieved Chunks\n")

        for chunk in result.chunks:

            print("-" * 60)

            print(f"Source : {chunk.source}")

            print(f"Page   : {chunk.page}")

            print(f"Score  : {chunk.score:.3f}")

            print()

            print(chunk.content)

            print()


if __name__ == "__main__":
    main()