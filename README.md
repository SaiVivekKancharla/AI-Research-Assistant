# AI Research Assistant

An AI-powered research assistant that allows users to upload PDF documents and ask questions about their content using natural language. The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant document sections and generate accurate responses using a local LLM.

This project demonstrates how to build a **document-based AI chatbot** using modern LLM engineering tools while running completely **locally without external APIs**.

---

## 🚀 Live Demo

Public demo (via ngrok):

https://urijah-attritional-carrol.ngrok-free.dev/

---

# ✨ Features

- Upload and analyze PDF documents  
- Ask natural language questions about documents  
- Retrieval-Augmented Generation (RAG) pipeline  
- Semantic search using vector embeddings  
- Chat-style conversational interface  
- Document summarization  
- Source citation from retrieved document chunks  
- Fully local AI inference using Ollama

---

# 🛠 Tech Stack

### Frontend
- Streamlit

### AI / ML
- LangChain  
- HuggingFace Embeddings  
- FAISS Vector Database  
- Local LLM using Llama3 via Ollama

### Backend
- Python

### Deployment
- Local deployment with ngrok for public access

---

# 🧠 System Architecture

```
User Query
   ↓
Streamlit Chat Interface
   ↓
LangChain RAG Pipeline
   ↓
Vector Search (FAISS)
   ↓
Relevant Document Chunks
   ↓
LLM Response Generation
   ↓
Answer Returned to User
```

---

# 📂 Project Structure

```
AI-Research-Assistant
│
├── app.py                # Streamlit chatbot interface
├── ingest.py             # Document ingestion and vector store creation
├── utils.py              # Helper functions
├── requirements.txt      # Python dependencies
├── vectorstore/          # FAISS vector database
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/SaiVivekKancharla/AI-Research-Assistant.git
cd AI-Research-Assistant
```

Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🦙 Install Ollama

Install Ollama from:

https://ollama.com

Pull the Llama3 model:

```bash
ollama pull llama3
```

---

# ▶️ Run the Application

Start the Ollama server:

```bash
ollama serve
```

Run the Streamlit app:

```bash
streamlit run app.py
```

The application will open at:

```
http://localhost:8501
```

---

# 🔍 How It Works

1. Users upload PDF documents.  
2. Documents are split into smaller chunks.  
3. Each chunk is converted into vector embeddings.  
4. Embeddings are stored in a FAISS vector database.  
5. When a user asks a question:
   - Relevant document chunks are retrieved
   - Context is passed to the LLM
   - The LLM generates an answer.

---

# 💡 Example Use Cases

- Research paper analysis  
- Document Q&A systems  
- Knowledge base assistants  
- AI-powered document summarization  
- Internal company document search

---

# 🚧 Future Improvements

- Multi-document knowledge base  
- Persistent chat history  
- PDF sentence highlighting for answers  
- Docker deployment  
- Cloud deployment with GPU inference  
- Authentication and user workspaces

---

# 👨‍💻 Author

**Vivek Kancharla**

GitHub:  
https://github.com/SaiVivekKancharla

---

# 📄 License

This project is open-source and available under the **MIT License**.
