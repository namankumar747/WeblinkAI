import requests
from newspaper import Article
from config import SERPAPI

# Web search function
def search_web(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI,
        "num": 5
    }
    response = requests.get("https://serpapi.com/search", params=params)
    results = response.json()
    return [res["link"] for res in results.get("organic_results", [])]

# Fetch article content
def fetch_article_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except:
        return ""
    

def web_search_results(query):
    urls = search_web(query)
    texts = [fetch_article_text(url) for url in urls]
    texts = [t for t in texts if t.strip()]
    if not texts:
        return {"error": "No valid content fetched."}
    
    combined = " ".join(texts)
    return combined
