# WeblinkAI - LLM-based Intelligent Web Assistant

> An AI-powered web assistant that answers queries by searching and summarizing content from multiple websites using NLP and LLMs. Supports querying specific URLs, parsing and analyzing their content to provide accurate, contextual responses.

## ✨ Features

- 🤖 AI-Powered Query Handling – Answers user queries using advanced web search and NLP techniques.
- 🌐 Multi-Source Summarization – Gathers and summarizes content from multiple websites for accurate, contextual responses.
- 💬 Chatbot-Style Interface – Interactive, user-friendly conversation experience.
- 🔗 URL-Specific Querying – Allows users to input a specific URL and ask questions about its content.
- ⚡ Dynamic Content Parsing – Extracts, processes, and analyzes web content in real time.
- 🧠 LLM Integration – Uses large language models for semantic understanding, summarization, and contextual reasoning.

## 🔧 Tech Stack

### 🧠 AI / Language Processing
- Google Gemini API – Powers semantic understanding, summarization, and contextual reasoning
- NLP Techniques – Used for query parsing, keyword extraction, and meaningful response generation
- SentenceTransformer (all-MiniLM-L6-v2) – Converts text into semantic vector embeddings for similarity search

### 📦 Vector Database
- FAISS – Efficient similarity search and retrieval of relevant content using vector embeddings

### 💻 Backend
- Python – Core programming language for backend logic and AI integration
- FastAPI – High-performance Python framework for building and serving APIs

### 🌐 Web Search & Data Retrieval
- SerpAPI – Fetches search results from multiple sources for accurate, real-time information retrieval

### 🖥️ Frontend
- HTML – Structures the chatbot-style web interface
- CSS – Styles and formats the frontend for a responsive and user-friendly experience
- JavaScript – Enables interactive features and API communication between frontend and backend


## 📂 Project Structure

```planetext

WeblinkAI/
├── frontend/                          # HTML, CSS, JavaScript based chatbot interface
│   ├── index.html
│   ├── link_mode.html
│   ├── script.js
│   └── style.css
│
├── config.py                          # Contain API Keys
├── link_fetch.py                      # Fetches and parses content from given URLs
├── LLM_response.py                    # Generates responses using LLMs
├── main.py                            # FastAPI application entry point
├── requirements.txt                   # Python dependencies
├── vector_db_searching.py             # FAISS vector DB search with SentenceTransformer
├── web_search.py                      # Web search integration using SerpAPI
└── README.md                          # Project documentation
```
## Getting Started

## 🛠️ Project Setup
Follow the steps below to set up the project on your local machine.

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/WeblinkAI.git
cd WeblinkAI
```

### 2. Create a Python Virtual Environment
In VS code Terminal
```bash
# Create virtual environment
python -m venv weblink_env

# Activate virtual environment
# On Windows:
weblink_env/Scripts/activate
# On macOS/Linux:
source weblink_env/bin/activate
```

### 3. Install Required Libraries
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## ▶️ Starting the Project

### Step 1. Add your Google Generative AI API and SerpAPI keys to `config.py`
```python
GOOGLEAPI = "YOUR_GOOGLE_AI_API_KEY" #replace with your API Key
SERPAPI = "YOUR_SERP_API_KEY"  #replace with your API Key
```

### Step 2. Activate Virtual Environment & Run Backend
In VS code Terminal
```bash
# Activate virtual environment
# On Windows:
weblink_env/Scripts/activate
# On macOS/Linux:
source weblink_env/bin/activate

# Run backend server
python main.py
```

### Step 3. Launch Frontend
- Open `frontend/index.html` in Live Server (VS Code extension)
- The chatbot interface will now be accessible in your browser.

## 📝 Notes
- Make sure all dependencies from requirements.txt are installed before starting the backend.
- If using Live Server, ensure it’s set to open on a port different from the backend port (e.g., 5500 for frontend, 8000 for backend).
- The backend must be running before opening the frontend; otherwise, queries will not work.
