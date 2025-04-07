# FastAPI app with /ask endpoint
from fastapi import FastAPI
from pydantic import BaseModel
from pymilvus import Collection, connections
from sentence_transformers import SentenceTransformer

app = FastAPI()

# Connect to Milvus and load model
connections.connect("default", host="localhost", port="19530")
model = SentenceTransformer("all-MiniLM-L6-v2")
collection = Collection("infra_agent")
collection.load()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_agent(query: Query):
    question = query.question
    embedding = model.encode([question])[0].tolist()

    results = collection.search(
        data=[embedding],
        anns_field="embedding",
        param={"metric_type": "IP", "params": {"nprobe": 10}},
        limit=1,
        output_fields=["text"]
    )

    if results and results[0]:
        return {"reply": results[0][0].entity.get("text")}
    else:
        return {"reply": "Sorry, I don't know that yet."}