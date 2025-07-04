# Home Services

A collection of Docker Compose files for self-hosting various services at home.

## Table of Contents

- [About](#about)
- [Services](#services)
  - [AI Services](#ai-services)
  - [Media Services](#media-services)
  - [NVIDIA SMI](#nvidia-smi)
  - [Productivity Services](#productivity-services)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About

This repository contains Docker Compose files that allow you to easily deploy and manage various services on your home server or local machine. The goal is to simplify the setup and maintenance of self-hosted applications for personal use.

## Services

This repository is organized into several categories of services, each with its own directory containing the relevant `docker-compose.yml` file and any necessary configuration files.

### AI Services

This directory contains Docker Compose files for running AI-related services.

*   **[Ollama](https://github.com/ollama/ollama):** A service for running large language models locally.
*   **[Open WebUI](https://github.com/open-webui/open-webui):** An extensible, feature-rich, and user-friendly self-hosted AI platform designed to operate entirely offline.
*   **[SearXNG](https://github.com/searxng/searxng):** A free internet metasearch engine which aggregates results from various search services and databases.
*   **[Chroma DB](https://github.com/chroma-core/chroma):** A document vector database for embedding, similarity search, and retrieval of structured data.
*   **RAG Worker:** Retrieval-Augmented Generation (LlamaIndex + Python + ollama model) can work with multiple knowledge bases and use llm model dynamically.
*   **[n8n](https://github.com/n8n-io/n8n):** Workflow automation platform that gives technical teams the flexibility of code with the speed of no-code.
*   **[AnythingLLM](https://github.com/Mintplex-Labs/anything-llm):** The all-in-one AI app you were looking for. Chat with your docs, use AI Agents, hyper-configurable, multi-user, & no frustrating setup required..

### Media Services

This directory contains Docker Compose files for running media-related services.

*   **Plex:** A popular media server for organizing and streaming your personal media collection.
*   **Jellyfin:** Another open-source media server, similar to Plex, offering a free and customizable experience.

### NVIDIA SMI

This directory contains Docker Compose files for running services related to NVIDIA GPU management.
*   **[NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html):** A toolkit that allows you to run GPU-accelerated applications in containers.
*   **[nvidia-docker2](https://github.com/NVIDIA/nvidia-docker):** An alternative to the NVIDIA Container Toolkit, providing similar functionality.

### Productivity Services

This directory contains Docker Compose files for running productivity-related services.

*   **[Nextcloud](https://nextcloud.com):** A self-hosted file synchronization and sharing solution.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Docker:**  [Install Docker](https://docs.docker.com/get-docker/)
*   **Docker Compose:** [Install Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1.  Clone this repository:

    ```
    git clone https://github.com/dmardus/home-services.git
    cd home-services
    ```

2.  Navigate to the directory of the service you want to deploy (e.g., `ai-services`):

    ```
    cd ai-services
    ```

3.  Run `docker-compose up -d --build --force-recreate --remove-orphans`:

    ```
    docker-compose up -d --build --force-recreate --remove-orphans
    ```

    This will download the necessary images and start the service in detached mode.

## Usage

*   **Accessing Services:** After the services are running, you can access them by navigating to the appropriate port in your web browser (e.g., `http://localhost:8080`).  Refer to the specific service's documentation for default ports and configuration options.
*   **Updating Services:** To update a service, navigate to its directory and run:

    ```
    docker-compose pull
    docker-compose up -d
    ```

*   **Update only rag-worker**
    ```
    docker compose up -d --build --no-deps --force-recreate rag-worker
    ```

*   **Optional: Clean up old unused containers/images**
    ```
    docker system prune -f
    ```

*   **How to ingest documents**

    ```
    docker exec -it rag-worker python ingest.py --collection finance_kb --data_path ./data/finance_kb --embed_model nomic-embed-text [optional] --delete_collection true
    ```

*   **Query RAG via curl**


    ```
    curl -X POST http://localhost:8001/query \
      -H "Content-Type: application/json" \
      -d '{"question":"Provide a breakdown for my current investments", "collection":"finance_kb", "model":"phi3"}'

    ```

*   **Integrate RAG into System Prompt of Open WebUI Assistants**

    ```
    You're a highly knowledgeable  personal finance advisor. When users ask finance-related questions, you must call the RAG API first:

    Endpoint: http://host.docker.internal:8001/query
    Collection: finance_kb
    Model: phi3

    If a relevant answer is returned, summarize and include it before giving your own insights.
    ```

## Contributing

Contributions are welcome! If you have improvements, new service configurations, or bug fixes, please submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
