from newspaper import Article
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
from config import GOOGLEAPI

# Fetch article content
def fetch_article_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except:
        return ""
    
#Chunk the text
def chunk_text(text, chunk_size=100):
    words = text.split()
    return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

#embedding Model
embeder = SentenceTransformer("all-MiniLM-L6-v2")

#Processing Link to get chunks and vector_db
def vector_db_chunks_formation(url):
    search_result = fetch_article_text(url)

    #chunks formation
    chunks = chunk_text(search_result)
    #generate embeddings
    embeddings = embeder.encode(chunks)

    #create FAISS db index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    return chunks, index


def get_relevent_chunks(query, chunks, index):
    #encodeing User Input
    query_embedding = embeder.encode([query])

    #Semantic Searching
    distances, indices = index.search(np.array(query_embedding), k=3)

    #Relevant Chunks in List
    matched_chunks = [chunks[i] for i in indices[0]] 

    return matched_chunks

#LLM Model
genai.configure(api_key=GOOGLEAPI)
model = genai.GenerativeModel("gemini-1.5-flash")

def LLM_link_response(query, chunks, index):

    search = get_relevent_chunks(query, chunks, index)

    prompt = f"""
                You are a knowledgeable and trustworthy AI assistant. Your task is to answer the user's query as accurately and clearly as possible using the context provided below, which is derived from recent web search results.

                Primary Objective:
                - Use the information in the provided context to generate a detailed, relevant, and accurate response to the query.

                If Needed:
                - If the context is insufficient, partially relevant, or unclear, you may draw upon your own general knowledge to provide a complete and helpful response. In such cases, clearly distinguish between what is taken from the context and what is supplemented from your own understanding.

                Instructions:
                1. Prioritize using facts and details from the given context when formulating your answer.
                2. You may enhance or expand your answer using your own trained knowledge **only if necessary** to clarify, elaborate, or fill in gaps.
                3. Do not fabricate facts. If an answer cannot be confidently provided, say that the context and available knowledge are insufficient.
                4. If the context contains conflicting data, summarize both sides neutrally and indicate uncertainty.
                5. Present the final answer in a clear, natural tone without referring explicitly to the “context” or “search results.”
                6. Maintain coherence, structure, and relevance throughout your answer.

                ---

                Context (from web search results):
                {search}

                ---

                User Query:
                {query}

            """
    
    
    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.8,
            "max_output_tokens": 500  # Use this instead of max_tokens
        }
    )
    return response.text