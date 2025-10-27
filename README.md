# Home Services

A collection of Docker Compose files for self-hosting various services at home.

## Table of Contents

- [About](#about)
- [Stacks](#stacks)
  - [Core Stack](#core-stack)
  - [Observability Stack](#observability-stack)
  - [Proxy Stack](#proxy-stack)
  - [Cloud Stack](#cloud-stack)
  - [AI Stack](#ai-stack)
  - [Media Stack](#media-sstack)
  - [Home Assistant Stack](#ha-sstack)
  - [NVIDIA SMI](#nvidia-smi)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About

This repository contains Docker Compose files that allow you to easily deploy and manage various services on your home server or local machine. The goal is to simplify the setup and maintenance of self-hosted applications for personal use.

## Stacks

This repository is organized into several categories of services, each with its own directory containing the relevant `docker-compose.yml` file and any necessary configuration files.

### Core Stack

This directory contains Docker Compose files for running core services.

*   **[Portainer](https://www.portainer.io/):** Enterprise-grade container management, simplified and engineered for everyone.

### Observability Stack

This directory contains Docker Compose files for running observability services.

*   **[Loki](https://github.com/grafana/loki):** Like Prometheus, but for logs.
*   **[Promtail](https://github.com/jhuix/promtail):** The promtail is the agent based on loki promtail with reserve forward server and client, responsible for gathering logs and sending them to Loki.
*   **[Prometheus](https://github.com/prometheus/prometheus):** The Prometheus monitoring system and time series database.
*   **[cAdvisor](https://github.com/google/cadvisor):** Analyzes resource usage and performance characteristics of running containers.
*   **[Node Explorer](https://github.com/corda/node-explorer):** Corda Node Explorer
*   **[Grafana](https://github.com/grafana/grafana):** The open and composable observability and data visualization platform

### Proxy Stack

This directory contains Docker Compose files for running proxy services.

*   **[Traefik](https://github.com/traefik/traefik):** The Cloud Native Application Proxy.

### Cloud Stack

This directory contains Docker Compose files for running cloud services.

*   **[Nextcloud](https://nextcloud.com):** A self-hosted file synchronization and sharing solution.
*   **[Immich](https://github.com/immich-app/immich):** High performance self-hosted photo and video management solution.

### AI Stack

This directory contains Docker Compose files for running AI-related services.

*   **[Ollama](https://github.com/ollama/ollama):** A service for running large language models locally.
*   **[Open WebUI](https://github.com/open-webui/open-webui):** An extensible, feature-rich, and user-friendly self-hosted AI platform designed to operate entirely offline.
*   **[n8n](https://github.com/n8n-io/n8n):** Workflow automation platform that gives technical teams the flexibility of code with the speed of no-code.
*   **[SearXNG](https://github.com/searxng/searxng):** A free internet metasearch engine which aggregates results from various search services and databases.
*   **[PostgreSQL](https://www.postgresql.org/):** PostgreSQL is a powerful, open source object-relational database system with over 35 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.
*   **[Qdrant](https://github.com/qdrant/qdrant):** High-performance, massive-scale Vector Database and Vector Search Engine for the next generation of AI.
*   **[Chroma DB](https://github.com/chroma-core/chroma):** A document vector database for embedding, similarity search, and retrieval of structured data.

### Media Stack

This directory contains Docker Compose files for running media-related services.

*   **Plex:** A popular media server for organizing and streaming your personal media collection.
*   **Jellyfin:** Another open-source media server, similar to Plex, offering a free and customizable experience.

### Home Assistant Stack

This directory contains Docker Compose files for running Wyoming whisper and piper services.

*   **[Whisper](https://github.com/rhasspy/wyoming-faster-whisper):** Wyoming protocol server for faster whisper speech to text system.
*   **[Piper](https://github.com/rhasspy/piper-samples):** Samples for Piper text to speech system.

### NVIDIA SMI

This directory contains Docker Compose files for running services related to NVIDIA GPU management.
*   **[NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html):** A toolkit that allows you to run GPU-accelerated applications in containers.
*   **[nvidia-docker2](https://github.com/NVIDIA/nvidia-docker):** An alternative to the NVIDIA Container Toolkit, providing similar functionality.

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
    docker compose pull
    docker compose up -d
    ```

*   **Optional: Clean up old unused containers/images**
    ```
    docker system prune -f
    ```

## Useful links, channels

* [What is Agentic RAG](https://weaviate.io/blog/what-is-agentic-rag)
* [NetworkChuck](https://www.youtube.com/@NetworkChuck)
* [Futurepedia](https://www.youtube.com/@futurepedia_io)
* [Cole Medin](https://www.youtube.com/@ColeMedin)
* [Nate Herk | AI Automation](https://www.youtube.com/@nateherk)

## Contributing

Contributions are welcome! If you have improvements, new service configurations, or bug fixes, please submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
