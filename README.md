# RAG System with Guardrails

This is a Retrieval-Augmented Generation (RAG) system I built from scratch, mostly as a way to actually learn how these things work under the hood instead of just reading about them.

In plain words: you give it some documents, and then you can ask it questions about them. Instead of just guessing an answer from general knowledge, it first searches your documents for the relevant bits, then asks an AI model to answer using only that information. On top of that, it has four safety checks (guardrails) running in the background to keep things safe and honest.

## What it actually does

1. You send it a question
2. It checks the question isn't trying to manipulate the AI (prompt injection check)
3. It checks the question is actually relevant to the documents it knows about (topic check)
4. It hides any personal info in the question, like emails or phone numbers (PII redaction)
5. It searches your documents for the most relevant pieces of text
6. It sends those pieces + your question to Google Gemini, which writes an answer
7. It double-checks the answer actually matches the documents, instead of being made up (groundedness check)
8. It sends back the answer, along with which documents it came from

## Tech used

- **Python + FastAPI** — the web server
- **ChromaDB** — stores and searches documents
- **sentence-transformers** — turns text into numbers so we can compare meaning, not just keywords
- **Google Gemini (free tier)** — writes the actual answers
- **Presidio** — detects and hides personal information

## Before you start

You'll need:
- Windows with PowerShell (these instructions are written for that)
- A free Google account, to get a Gemini API key
- About 15–20 minutes for the first-time setup (mostly downloading things)

## Setup, step by step

### 1. Install Python 3.11

Newer Python versions (like 3.14) currently cause install errors with some of the tools this project uses, so 3.11 is the safe choice.

Using the Python Install Manager:

```powershell
py install 3.11
py list
```

You should see `3.11` in the list of installed versions.

### 2. Create the project folder

```powershell
mkdir rag_system
cd rag_system
code .
```

That last command opens the folder in VS Code.

### 3. Create the subfolders

```powershell
mkdir app
mkdir app/core
mkdir app/guardrails
mkdir data
```

### 4. Create a virtual environment

A virtual environment keeps this project's tools separate from anything else on your computer.

```powershell
py -3.11 -m venv venv
```

Then turn it on:

```powershell
venv\Scripts\Activate.ps1
```

If PowerShell blocks this with a permissions error, run this once:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Type `Y` when it asks, then try activating again.

You'll know it worked when you see `(venv)` at the start of your terminal line.

### 5. Install the required tools

Make sure `requirements.txt` (included in this repo) is in your project folder, then run:

```powershell
pip install -r requirements.txt
```

This installs FastAPI, ChromaDB, sentence-transformers, Gemini's library, and a few others. It'll take a few minutes and download a fair amount — that's normal.

### 6. Get a free Gemini API key

1. Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. Sign in with any Google account
3. Click **Create API key**
4. Copy it somewhere safe

No credit card needed for the free tier.

### 7. Set your API key

Every time you open a new terminal, tell it your key:

```powershell
$env:GEMINI_API_KEY="paste_your_key_here"
```

Or, to set it permanently so you never have to do this again:

```powershell
[System.Environment]::SetEnvironmentVariable("GEMINI_API_KEY", "paste_your_key_here", "User")
```

(Close and reopen your terminal for this to take effect.)

## Running it

Start the server:

```powershell
uvicorn app.main:app --reload
```

Then open this in your browser:

```
http://127.0.0.1:8000/docs
```

This gives you an interactive page to test the `/ask` endpoint. Click it, click **Try it out**, and send something like:

```json
{
  "question": "What is your refund policy?"
}
```

## Adding your own documents

Put a `.txt` or `.pdf` file into the `data` folder, then run:

```powershell
python -m app.ingest data/yourfile.txt
```

This reads the file, splits it into small overlapping chunks, and saves it so it can be searched later.

## Project structure

```
rag_system/
├── app/
│   ├── main.py              → the API server, wires everything together
│   ├── config.py            → all settings in one place
│   ├── ingest.py            → loads documents into the system
│   ├── core/
│   │   ├── chunker.py       → splits text into small pieces
│   │   ├── vector_store.py  → stores and searches document chunks
│   │   └── llm.py           → talks to Gemini
│   └── guardrails/
│       ├── pii.py           → hides personal info
│       ├── injection.py     → blocks prompt injection attempts
│       ├── topic.py         → blocks off-topic questions
│       └── groundedness.py  → checks answers aren't made up
├── data/                    → your documents go here
└── requirements.txt
```

## A few things I learned building this

- Environment variables like your API key only last for the terminal window they were set in, unless you make them permanent
- Newer Python versions don't always have ready-made installs for every tool yet — sticking to a stable version like 3.11 avoids a lot of headaches
- Comparing "meaning" instead of exact words is what makes search actually smart — it's why asking "how many days to return something" can correctly find a document that says "refund policy," even without sharing a single word
- Model names for AI APIs change over time, so it's worth using a "latest" alias where available instead of hardcoding an exact version

## What's not included (yet)

- A proper frontend — right now you interact with it through `/docs` or direct API calls
- Authentication — anyone who can reach the server can use it
- Smarter prompt injection detection — the current version checks for known phrases, not sneakier rewordings
