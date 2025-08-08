import google.generativeai as genai
from config import GOOGLEAPI
from vector_db_searching import get_relevent_chunks


#LLM Model
genai.configure(api_key=GOOGLEAPI)
model = genai.GenerativeModel("gemini-1.5-flash")

def LLM_query_response(query):

    search = get_relevent_chunks(query)

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
