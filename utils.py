from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

def load_documents(files):
    documents = []

    for file in files:
        loader = PyPDFLoader(file)
        docs = loader.load()
        documents.extend(docs)

    return documents


def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    return text_splitter.split_documents(documents)