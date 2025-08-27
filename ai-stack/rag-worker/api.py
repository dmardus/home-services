from fastapi import FastAPI, Request
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain.chat_models import ChatOllama
from langchain.schema import Document
from datetime import datetime
import os
import re
from config import OLLAMA_BASE, DEFAULT_EMBED_MODEL, DEFAULT_LLM_MODEL

app = FastAPI()

@app.post("/query")
async def query_doc(request: Request):
    try:
        body = await request.json()
        question = body.get("question")
        collection = body.get("collection", "support_kb")
        model_name = body.get("model", DEFAULT_LLM_MODEL)

        if not question:
            return {"error": "Missing question"}

        print(f"📥 Received query: '{question}' on collection '{collection}' using model '{model_name}'")

        persist_directory = os.path.join("chroma_db", collection)

        embeddings = OllamaEmbeddings(model=DEFAULT_EMBED_MODEL, base_url=OLLAMA_BASE)
        vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
        llm = ChatOllama(model=model_name, base_url=OLLAMA_BASE, temperature=0.2)

        # Try direct incident ID match
        incident_id_match = re.search(r"INC-\d{8}-\d{4}", question)
        incident_id = incident_id_match.group(0) if incident_id_match else None

        documents = []

        if incident_id:
            print(f"🔎 Attempting exact metadata match for incident ID: {incident_id}")
            raw_docs = vectordb.get()
            all_docs = [
                Document(page_content=content, metadata=metadata)
                for content, metadata in zip(raw_docs['documents'], raw_docs['metadatas'])
            ]
            documents = [doc for doc in all_docs if doc.metadata.get("incident_id") == incident_id]

        if not documents:
            print("🌀 Falling back to similarity search...")
            documents = vectordb.similarity_search(question, k=5)

        if not documents:
            return {
                "answer": f"The incident with ID **{incident_id}** is not found in the knowledge base." if incident_id else "No relevant information was found.",
                "sources": [],
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }

        # Return raw context to Open WebUI, let prompt do formatting
        context = "\n\n".join(doc.page_content for doc in documents)
        sources = sorted(set(doc.metadata.get("source", "unknown") for doc in documents))

        return {
            "answer": context,
            "sources": sources,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

    except Exception as e:
        print(f"❌ Error: {e}")
        return {"error": str(e)}

@app.get("/health")
def health():
    return {"status": "ok"}
