import os

OLLAMA_BASE = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")
DEFAULT_COLLECTION = "finance_kb"
DEFAULT_EMBED_MODEL = "nomic-embed-text"
DEFAULT_LLM_MODEL = "qwen3:8b"
CHROMA_HOST = "chromadb"
CHROMA_PORT = 8000
