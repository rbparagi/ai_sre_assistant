# Infra Knowledge Base Agent

This project is a FastAPI-based application that uses Milvus, a vector database, to provide answers to user queries. It leverages a pre-trained SentenceTransformer model to encode questions into embeddings and performs similarity searches in the Milvus database.

## Features

- **FastAPI API**: Provides an `/ask` endpoint to handle user queries and return relevant answers.
- **Milvus Integration**: Uses Milvus as a vector database to store and search embeddings.
- **SentenceTransformer**: Encodes user questions into embeddings for similarity search.
- **Knowledge Base Loader**: A script to load Q&A data into Milvus.



## Prerequisites

- Python 3.8 or higher
- Docker and Docker Compose

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>

2. Install Python dependencies:
    pip install -r requirements.txt

3. Start the Milvus database and its dependencies using Docker Compose:
    docker-compose up -d

4. Load the knowledge base into Milvus:
    python kb_loader/load_markdown.py

Running the Application

    1. Navigate to the backend directory:
        cd backend
        uvicorn main:app --reload
    2. The API will be available at http://127.0.0.1:8000.

API Endpoints
/ask (POST)
    Description: Accepts a user query and returns the most relevant answer from the knowledge base.
    Request Body:
        {
            "question": "Your question here"
        }

Configuration
    The application connects to Milvus on localhost:19530. Update the connection settings in backend/main.py or backend/milvus_client.py if needed.

Dependencies
    FastAPI
    Uvicorn
    SentenceTransformers
    PyMilvus
Development
    To add new features or modify the application:
        Update the FastAPI logic in backend/main.py.
        Add or modify scripts in the kb_loader directory to manage the knowledge base.



Extra steps
    
    pip install "sentence-transformers==2.2.2" "transformers==4.25.1" "huggingface_hub==0.10.1"

