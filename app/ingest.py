from pathlib import Path

from langchain_community.document_loaders import (
    PyMuPDFLoader,
    TextLoader,
    UnstructuredHTMLLoader,
)

from app.logger import logger
from app.config import settings


SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".md",
    ".html",
    ".htm",
}


def load_documents(data_directory: Path):
    

    documents = []

    for file_path in data_directory.rglob("*"):

        if not file_path.is_file():
            continue

        extension = file_path.suffix.lower()

        if extension not in SUPPORTED_EXTENSIONS:
            continue

        logger.info(f"Loading {file_path.name}")

        try:

            if extension == ".pdf":
                loader = PyMuPDFLoader(str(file_path))

            elif extension == ".md":
                loader = TextLoader(
                    str(file_path),
                    encoding="utf-8"
                )

            else:
                loader = UnstructuredHTMLLoader(str(file_path))

            docs = loader.load()

            documents.extend(docs)

        except Exception as error:

            logger.exception(
                f"Failed to load {file_path.name}: {error}"
            )

    for doc in docs:
        doc.metadata["source"] = str(file_path.relative_to(settings.raw_data_directory))

    return documents