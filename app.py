import streamlit as st
import os
import tempfile

from ingest import create_vector_store
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM


# ------------------------
# Page Config
# ------------------------

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

# ------------------------
# Custom Styling
# ------------------------

st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

h1 {
    color: white;
}

.stChatMessage {
    padding: 10px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# ------------------------
# Header
# ------------------------

st.title("🤖 AI Research Assistant")

st.write("Upload PDFs and ask questions using a local AI model.")

# ------------------------
# Sidebar
# ------------------------

with st.sidebar:

    st.header("📂 Document Upload")

    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        file_paths = []

        for uploaded_file in uploaded_files:

            temp_dir = tempfile.mkdtemp()

            path = os.path.join(temp_dir, uploaded_file.name)

            with open(path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            file_paths.append(path)

        if st.button("Process Documents"):

            create_vector_store(file_paths)

            st.success("Documents processed successfully!")

    st.divider()

    if st.button("Generate Document Summary"):

        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        db = FAISS.load_local(
            "vectorstore",
            embeddings,
            allow_dangerous_deserialization=True
        )

        retriever = db.as_retriever(search_kwargs={"k":5})

        docs = retriever.get_relevant_documents("summarize")

        context = " ".join([doc.page_content for doc in docs])

        llm = OllamaLLM(model="llama3")

        prompt = f"""
Summarize this document into bullet points:

{context}
"""

        response = llm.invoke(prompt)

        st.write(response)


# ------------------------
# Chat Memory
# ------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ------------------------
# User Input
# ------------------------

prompt = st.chat_input("Ask a question about your documents...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Load vector DB
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = db.as_retriever()

    docs = retriever.get_relevant_documents(prompt)

    context = " ".join([doc.page_content for doc in docs])

    llm = OllamaLLM(model="llama3")

    query_prompt = f"""
You are an AI research assistant.

Answer the question based on the context below.

Context:
{context}

Question:
{prompt}
"""

    response = llm.invoke(query_prompt)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )