🎯 Goal of the Project
To build a local chatbot powered by a large language model (LLM) like LLaMA 2, running through Ollama, with the following features:

🧠 Answer user questions using a local LLM (no OpenAI API required)

📄 Log conversations to a file

🌐 Provide a web interface to chat using Gradio

💬 Maintain chat history context for better responses

🔍 Ask questions about a PDF — and the chatbot will answer based only on what’s inside that PDF.
------------------------------------------------------------
✅ How it works (in concept):
Upload a PDF file (e.g., a textbook, article, report).

The app extracts and processes the text from that PDF.

You ask questions like:

"What does the author say about photosynthesis on page 4?"

The chatbot uses the extracted text to generate answers based on that content only — not general internet knowledge.


🛠 To make this work, we’ll:
Let the user upload a PDF via the Gradio web UI.

Extract the text (e.g. with PyMuPDF, pdfplumber, or PyPDF2).

Optionally split the text into chunks and use embeddings to find relevant context for each question (this is called RAG – Retrieval-Augmented Generation).

Feed the most relevant chunks + user question into the LLM.
------------------------------------------------------------
✅ What we’ve done so far:
Installed & ran LLaMA 2 locally using Ollama.

Created a CLI-based chatbot (mistral_chat.py).

Logged messages to chat_log.txt.

Pushed the project to a GitHub repo.

Created a web-based chat UI with Gradio (web_chat.py).

Integrated message history for multi-turn chat (so it remembers what you said).

# 🧠 LLM Project Steps

## ✅ Setup
- Installed Ollama
- Pulled LLaMA 2 model: `ollama run llama2`
- Created Python virtual environment and activated it
- Installed required Python packages (`ollama`, `openai`, etc.)

## 🧪 CLI Chatbot
- Created `mistral_chat.py`
- Used `Ollama` to run local LLM chat
- Added chat logging to `chat_log.txt`

## 🌐 Web Interface
- Created `web_chat.py` using Gradio
- Implemented chatbot interface with history
- Used `Gradio` to run chat at `localhost:7860`

## 📝 Git
- Created GitHub repo
- Added `.gitignore`
- Tracked everything with `git add .`, `git commit -m ""`, `git push`

## 🚧 Next Features
- Add PDF upload + question-answering
- Chunking + embedding for RAG

