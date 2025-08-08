from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from LLM_response import LLM_query_response
from web_search import search_web
from link_fetch import vector_db_chunks_formation, LLM_link_response
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or use specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/web_search_result/")
def web_search_result(query: str = Form(...)):
    
    search_response = LLM_query_response(query)
    urls = search_web(query)

    result = {
        "search_result": search_response,
        "urls": urls
    }

    return result

stored_chunks_index = [] #Global variable to store link informations

@app.post("/process_link/", response_class=PlainTextResponse)
def process_link(url: str = Form(...)):
    global stored_chunks_index
    try:
        chunks, index = vector_db_chunks_formation(url)
        if not chunks or not index:
            raise ValueError("Invalid or unprocessable link.")
        stored_chunks_index = [{"index": index, "chunks": chunks}]
        return "🔗 Link processed"
    except Exception as e:
        stored_chunks_index = []  # Reset in case of error
        return f"❌ Error: Enter a valid link ({str(e)})"


@app.post("/link_response/", response_class=PlainTextResponse)
def process_link(query: str = Form(...)):
    if not stored_chunks_index:
        return "Enter Link first"
    index = stored_chunks_index[0].get("index")
    chunks = stored_chunks_index[0].get("chunks")

    response = LLM_link_response(query, chunks, index)

    return response


if __name__ == "__main__":
    uvicorn.run("main:app")