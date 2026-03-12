FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Download model
RUN ollama pull llama3

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]