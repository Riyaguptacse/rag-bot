import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Load saved index
index = faiss.read_index("../vectorstore/index.faiss")

# Load saved documents
with open("../vectorstore/docs.pkl", "rb") as f:
    docs = pickle.load(f)

#  Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def retrieve(query, k=1):
    """
    Returns top k most relevant documents for the query
    """
    # Convert query to embedding
    query_vec = model.encode([query])

    # Search in FAISS
    distances, indices = index.search(query_vec, k)

    # Retrieve documents
    results = [docs[i] for i in indices[0]]
    return results

# Test
if __name__ == "__main__":
    question = "Who founded Tesla?"
    top_docs = retrieve(question, k=2)
    print("Top documents:")
    for doc in top_docs:
        print("-", doc)