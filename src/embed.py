
from sentence_transformers import SentenceTransformer

# https://pypi.org/project/sentence-transformers/

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text):
   embedding = model.encode(text)
   embedding = embedding.tolist()
   return embedding