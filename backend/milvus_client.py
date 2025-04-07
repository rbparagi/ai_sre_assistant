# Milvus connection test script
from pymilvus import connections

def connect_to_milvus():
    connections.connect("default", host="localhost", port="19530")
    print("✅ Connected to Milvus")

if __name__ == "__main__":
    connect_to_milvus()