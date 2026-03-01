from sentence_transformers import SentenceTransformer
import faiss
import os
import pickle
import os
from sentence_transformers import SentenceTransformer
import faiss
import pickle

# Automatically find the project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Absolute paths
data_folder = os.path.join(BASE_DIR, "data")
vectorstore_path = os.path.join(BASE_DIR, "vectorstore")
os.makedirs(vectorstore_path, exist_ok=True)

# Load all text files
docs = []
for file_name in os.listdir(data_folder):
    if file_name.endswith(".txt"):
        with open(os.path.join(data_folder, file_name), "r", encoding="utf-8") as f:
            docs.append(f.read())

# Convert documents to embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')  # free, local
embeddings = model.encode(docs)

# Create FAISS index
dimension = embeddings[0].shape[0]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index and documents
os.makedirs("../vectorstore", exist_ok=True)
faiss.write_index(index, "../vectorstore/index.faiss")
with open("../vectorstore/docs.pkl", "wb") as f:
    pickle.dump(docs, f)

print("Index created successfully!")