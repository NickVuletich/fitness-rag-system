"""
EMBEDDING MODULE

Purpose:
Convert text into vector embeddings using a local model.

Responsibilities:
- Load a sentence transformer model
- Provide a function that takes in text and returns an embedding

Steps to Implement:

1. Import the sentence transformer library

2. Load a pre-trained model
   - Use a lightweight model suitable for semantic search
   - Store it in a variable at the top level (so it only loads once)

3. Create a function (e.g., embed_text)

   Input:
   - text (string)

   Output:
   - embedding (list of floats)

4. Inside the function:
   - Pass the text into the model
   - Get the embedding output
   - Convert it to a Python list (important for storage later)

5. Return the embedding

Notes:
- Do NOT handle file reading here
- Do NOT store anything here
- This file ONLY converts text → embedding

Test Idea:
- Call your function with a short sentence
- Print the length of the embedding vector
"""

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text):
    