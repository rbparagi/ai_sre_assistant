# Script to embed and load Q&A into Milvus
from pymilvus import Collection, connections, FieldSchema, CollectionSchema, DataType
from sentence_transformers import SentenceTransformer

# Connect to Milvus
connections.connect("default", host="localhost", port="19530")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Define schema if collection doesn't exist
def create_collection():
    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384),
        FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=500)
    ]
    schema = CollectionSchema(fields, description="Infra Knowledge Base")
    collection = Collection("infra_agent", schema=schema)
    return collection

# Initialize or load existing collection
try:
    collection = Collection("infra_agent")
except:
    collection = create_collection()

# Sample Q&A list
qa_data = [
    "how to restart a pod in kubernetes",
    "check cpu usage in linux",
    "create s3 bucket using aws cli",
    "what is CrashLoopBackOff in k8s",
    "check disk usage in linux"
]

# Convert to vectors
embeddings = model.encode(qa_data).tolist()

# Insert data
collection.insert([embeddings, qa_data])

# ✅ Create index before loading/searching
collection.create_index(
    field_name="embedding",
    index_params={
        "index_type": "IVF_FLAT",
        "metric_type": "IP",
        "params": {"nlist": 128}
    }
)

collection.flush()
print("✅ Q&A data loaded and indexed into Milvus.")
