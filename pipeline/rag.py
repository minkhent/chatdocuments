import pathlib
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import TokenTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()


class RAGPipeline:
    def __init__(self) -> None:
        self.emb_model_path = os.getenv("EMBEDDING_MODEL")
        self.emb_model = self.get_embedding_model(self.emb_model_path)
        self.vector_store_path = os.getenv("VECTOR_STORE")

    def load_documents(self, path: str) -> str:
        "Select document loader by document types."

        file_type = pathlib.Path(path).suffix

        if file_type == ".txt":
            loader = TextLoader(path)
        elif file_type == ".pdf":
            loader = PyPDFLoader(path)
        elif file_type == ".csv":
            loader = CSVLoader(path)

        pages = loader.load_and_split()
        return pages

    def get_embedding_model(self, emb_model) -> HuggingFaceBgeEmbeddings:
        model_kwargs = {"device": "cpu"}
        encode_kwargs = {
            "normalize_embeddings": True
        }  # set True to compute cosine similarity
        embeddings_model = HuggingFaceBgeEmbeddings(
            model_name=emb_model,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs,
        )
        return embeddings_model

    def split_docs(self, docs) -> list:
        "Split document text to chunks"

        text_splitter = TokenTextSplitter(chunk_size=250, chunk_overlap=0)
        documents = text_splitter.split_documents(docs)
        return documents

    def create_vector_db(self, file_path: str) -> None:
        "Create vector DB from file content."

        self.doc = self.load_documents(file_path)
        self.documents = self.split_docs(self.doc)
        db = Chroma.from_documents(
            self.documents,
            embedding=self.emb_model,
            persist_directory=self.vector_store_path,
        )

        db.persist()

    def load_vector_db(self) -> Chroma:
        "Load back the embeddings from disk"

        db = Chroma(
            persist_directory=self.vector_store_path, embedding_function=self.emb_model
        )
        return db

    def create_retriever(self, path: str):
        "Create semantic reteriver from vector DB"

        self.create_vector_db(path)
        docsearch = self.load_vector_db()
        retriever = docsearch.as_retriever(search_type="mmr", search_kwargs={"k": 1})
        return retriever
