import argparse
import os
import re
from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from config import OLLAMA_BASE, DEFAULT_EMBED_MODEL
from utils import validate_directory

def extract_incident_id_from_text(text):
    match = re.search(r"INC-\d{8}-\d{4}", text)
    return match.group(0) if match else None

def extract_metadata(filepath, content):
    filename = os.path.basename(filepath)
    incident_id = extract_incident_id_from_text(content)
    return {
        "source": filename,
        "incident_id": incident_id,
    }

def ingest_documents(collection_name, data_path, embed_model_name=DEFAULT_EMBED_MODEL, delete_collection=False):
    validate_directory(data_path)

    print(f"📂 Loading documents from {data_path}...")
    loader = DirectoryLoader(data_path, glob="**/*.md", loader_cls=TextLoader)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=100)
    docs = []
    for doc in documents:
        incident_id = extract_incident_id_from_text(doc.page_content)
        metadata = extract_metadata(doc.metadata.get("source", ""), doc.page_content)
        chunks = splitter.split_documents([doc])
        for chunk in chunks:
            chunk.metadata.update(metadata)
            docs.append(chunk)
            print(f"📎 Ingesting chunk with metadata: {chunk.metadata}")

    embeddings = OllamaEmbeddings(base_url=OLLAMA_BASE, model=embed_model_name)
    persist_directory = os.path.join("chroma_db", collection_name)

    if delete_collection and os.path.exists(persist_directory):
        import shutil
        print(f"🧹 Deleting existing collection at {persist_directory}...")
        shutil.rmtree(persist_directory)

    print(f"📦 Ingesting into Chroma collection '{collection_name}'...")
    Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=persist_directory,
    )
    print(f"✅ Successfully ingested {len(docs)} chunks into '{collection_name}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest documents into ChromaDB via LangChain")
    parser.add_argument("--collection", required=True, help="ChromaDB collection name")
    parser.add_argument("--data_path", required=True, help="Path to incident markdown files")
    parser.add_argument("--embed_model", default="nomic-embed-text", help="Embedding model to use")
    parser.add_argument("--delete_collection", action="store_true", help="Delete existing Chroma collection")
    args = parser.parse_args()

    ingest_documents(
        collection_name=args.collection,
        data_path=args.data_path,
        embed_model_name=args.embed_model,
        delete_collection=args.delete_collection
    )
