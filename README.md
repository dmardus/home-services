# Home Services

A collection of Docker Compose files for self-hosting various services at home.

## Table of Contents

- [About](#about)
- [Stacks](#stacks)
  - [Core Stack](#core-stack)
  - [Observability Stack](#observability-stack)
  - [Proxy Stack](#proxy-stack)
  - [Photo Stack](#photo-stack)
  - [AI Stack](#ai-stack)
  - [Media Stack](#media-stack)
  - [Home Assistant Stack](#home-assistant-stack)
  - [NVIDIA SMI](#nvidia-smi)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Useful links, channels](#useful-links-channels)
- [Contributing](#contributing)
- [License](#license)

## About

This repository contains Docker Compose files that allow you to easily deploy and manage various services on your home server or local machine. The goal is to simplify the setup and maintenance of self-hosted applications for personal use.

Most stacks are defined as Docker Compose files. A few (Core, AI, Media, Home Assistant) also include experimental Podman equivalents (`podman-compose.yaml`, or Kubernetes-style pod manifests for `podman kube play`). This Podman path is a work in progress and isn't fully documented yet — treat the Docker Compose files as the primary way to run each stack.

## Stacks

This repository is organized into several categories of services, each with its own directory containing the relevant `docker-compose.yaml` file and any necessary configuration files.

### Core Stack

This directory contains Docker Compose files for running core services.

*   **[Portainer](https://www.portainer.io/):** Enterprise-grade container management, simplified and engineered for everyone.
*   **[Dockhand](https://github.com/Finsys/dockhand):** A lightweight Docker and Compose stack management UI.
*   **[Cloudflare Tunnel](https://github.com/cloudflare/cloudflared):** Exposes local services to the internet without opening inbound ports.

### Observability Stack

This directory contains Docker Compose files for running observability services.

*   **[Uptime Kuma](https://github.com/louislam/uptime-kuma):** Self-hosted monitoring tool for tracking uptime of services and endpoints.
*   **[Beszel](https://github.com/henrygd/beszel):** Lightweight server monitoring hub and agent for tracking host resource usage.
*   **[Loki](https://github.com/grafana/loki):** Like Prometheus, but for logs.
*   **[Promtail](https://github.com/jhuix/promtail):** The promtail is the agent based on loki promtail with reserve forward server and client, responsible for gathering logs and sending them to Loki.
*   **[Prometheus](https://github.com/prometheus/prometheus):** The Prometheus monitoring system and time series database.
*   **[Node Exporter](https://github.com/prometheus/node_exporter):** Exposes host-level hardware and OS metrics for Prometheus.
*   **[cAdvisor](https://github.com/google/cadvisor):** Analyzes resource usage and performance characteristics of running containers.
*   **[Logporter](https://github.com/Lifailon/logporter):** Lightweight alternative to cAdvisor for exposing container metrics, including metrics derived from logs.
*   **[Grafana](https://github.com/grafana/grafana):** The open and composable observability and data visualization platform.

### Proxy Stack

This directory contains Docker Compose files for running proxy services.

*   **[Traefik](https://github.com/traefik/traefik):** The Cloud Native Application Proxy.
*   **[Watchtower](https://github.com/containrrr/watchtower):** Automatically updates running containers. Configured in `monitor-only` mode in this stack.

> This stack is currently not deployed but is kept in the repository as-is.

### Photo Stack

This directory contains Docker Compose files for running Immich, our self-hosted photo and video management solution. It replaces a previous "Cloud Stack" that also included Nextcloud; Nextcloud has been dropped and only the Immich-based photo stack remains.

*   **[Immich](https://github.com/immich-app/immich):** High performance self-hosted photo and video management solution (server, machine learning, database, and cache components).

### AI Stack

This directory contains Docker Compose files for running AI-related services.

*   **[Ollama](https://github.com/ollama/ollama):** A service for running large language models locally.
*   **[Open WebUI](https://github.com/open-webui/open-webui):** An extensible, feature-rich, and user-friendly self-hosted AI platform designed to operate entirely offline.
*   **[n8n](https://github.com/n8n-io/n8n):** Workflow automation platform that gives technical teams the flexibility of code with the speed of no-code. Sample workflows are included in `n8n_workflows/`.
*   **[SearXNG](https://github.com/searxng/searxng):** A free internet metasearch engine which aggregates results from various search services and databases.
*   **[PostgreSQL](https://www.postgresql.org/)** (with the [pgvector](https://github.com/pgvector/pgvector) extension): Relational database used for long-term memory/embeddings, plus a separate instance backing n8n.
*   **[Qdrant](https://github.com/qdrant/qdrant):** High-performance, massive-scale Vector Database and Vector Search Engine for the next generation of AI.
*   **[Redis](https://redis.io/):** In-memory cache used for short-term memory.

### Media Stack

This directory contains Docker Compose files for running media-related services.

*   **Plex:** A popular media server for organizing and streaming your personal media collection.
*   **Jellyfin:** Another open-source media server, similar to Plex, offering a free and customizable experience.
*   **[Navidrome](https://github.com/navidrome/navidrome):** A self-hosted music streaming server compatible with the Subsonic API.

### Home Assistant Stack

This directory contains Docker Compose files for running Wyoming whisper and piper services.

*   **[Whisper](https://github.com/rhasspy/wyoming-faster-whisper):** Wyoming protocol server for faster whisper speech to text system.
*   **[Piper](https://github.com/rhasspy/piper-samples):** Samples for Piper text to speech system.

### NVIDIA SMI

This directory contains a minimal Docker Compose file used to verify that GPU passthrough is working correctly before deploying GPU-dependent stacks (it just runs `nvidia-smi` inside a container). It requires the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) to be installed on the host.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Docker:**  [Install Docker](https://docs.docker.com/get-docker/)
*   **Docker Compose:** [Install Docker Compose](https://docs.docker.com/compose/install/)
*   **NVIDIA Container Toolkit** (optional): required only for GPU-accelerated services (Ollama, Plex, Jellyfin, Immich ML) — [install guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)

### Installation

1.  Clone this repository:

    ```
    git clone https://github.com/dmardus/home-services.git
    cd home-services
    ```

2.  Navigate to the directory of the stack you want to deploy (e.g., `ai`):

    ```
    cd ai
    ```

3.  Each stack connects to its own external Docker network, so create it before starting the stack for the first time (the network name matches the stack, e.g. `ai-network`):

    ```
    docker network create ai-network
    ```

4.  Copy/edit the `.env` file in that directory with your own values (ports, credentials, paths, etc.), then start the stack:

    ```
    docker compose up -d --force-recreate --remove-orphans --pull always
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

## Contributing

Contributions are welcome! If you have improvements, new service configurations, or bug fixes, please submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
