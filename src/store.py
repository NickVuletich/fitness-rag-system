"""
STORAGE MODULE

Purpose:
Store embeddings and their associated text in a vector database.

Responsibilities:
- Initialize a local vector database
- Store embeddings along with original text and identifiers

Steps to Implement:

1. Import the vector database library (Chroma)

2. Initialize a client
   - This should run once when the file is loaded

3. Create or get a collection
   - Give it a clear name (e.g., "fitness_logs")

4. Create a function (e.g., store_embedding)

   Input:
   - id (string, usually filename or date)
   - text (original document)
   - embedding (list of floats)

   Output:
   - none (just stores data)

5. Inside the function:
   - Add the data to the collection:
     - documents → original text
     - embeddings → vector
     - ids → unique identifier

Important:
- Always store BOTH the embedding AND the original text
- IDs must be unique per document

Notes:
- Do NOT generate embeddings here
- Do NOT read files here
- This file ONLY handles storing data

Test Idea:
- Manually call your function with a fake embedding and text
- Ensure no errors occur when adding to the collection
"""

import chromadb

