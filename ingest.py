from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from utils import load_documents, split_documents
import os

def create_vector_store(files):

    documents = load_documents(files)

    chunks = split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(chunks, embeddings)

    vectorstore.save_local("vectorstore")

    print("Vector database created")