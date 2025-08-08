import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from web_search import web_search_results

#Chunk the text
def chunk_text(text, chunk_size=100):
    words = text.split()
    return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

#embedding Model
embeder = SentenceTransformer("all-MiniLM-L6-v2")

def vector_db_formation(query):
    search_result = web_search_results(query)

    #chunks formation
    chunks = chunk_text(search_result)
    #generate embeddings
    embeddings = embeder.encode(chunks)

    #create FAISS db index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    return chunks, index

def get_relevent_chunks(query):
    #get chunks and vector_db
    chunks, index = vector_db_formation(query)

    #encodeing User Input
    query_embedding = embeder.encode([query])

    #Semantic Searching
    distances, indices = index.search(np.array(query_embedding), k=3)

    #Relevant Chunks in List
    matched_chunks = [chunks[i] for i in indices[0]] 

    return matched_chunks
