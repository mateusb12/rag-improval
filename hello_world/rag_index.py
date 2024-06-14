from transformers import AutoTokenizer, AutoModel
import faiss
import numpy as np

# Load pretrained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
model = AutoModel.from_pretrained('bert-base-uncased')

# Sample documents
documents = [
    "TechGadget offers a refund within 30 days of purchase. The product must be in its original condition and "
    "packaging. Customers should provide proof of purchase to be eligible for a refund.",
    "SuperShop allows returns within 45 days of purchase, given the item is unused and in its original packaging."
    " Customers need to present a receipt or proof of purchase.",
    "QuickMart provides a refund within 15 days of purchase. Items should be unopened and accompanied by the"
    " original receipt."
]


# Encode documents
def embed_text(text):
    inputs = tokenizer(text, return_tensors='pt')
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()


doc_embeddings = np.vstack([embed_text(doc) for doc in documents])

# Build FAISS index
index = faiss.IndexFlatL2(doc_embeddings.shape[1])
index.add(doc_embeddings)

# Encode query
query = "What is the maximum amount of days for the refund policy of TechGadget?"
query_embedding = embed_text(query)

# Retrieve relevant documents
k = 1
distances, indices = index.search(query_embedding, k)
retrieved_docs = [documents[idx] for idx in indices[0]]

print("Retrieved Document:", retrieved_docs)

# Use a generative model (like GPT) to generate the final answer
# Here we just return the retrieved document as a simplified example
answer = retrieved_docs[0]
print("Generated Answer:", answer)
