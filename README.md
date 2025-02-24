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
*   **[SearXNG](https://github.com/searxng/searxng):** A free internet metasearch engine which aggregates results from various search services and databases

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
    docker-compose up -d --build --force-recreate --remove-orphans
    ```

## Contributing

Contributions are welcome! If you have improvements, new service configurations, or bug fixes, please submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
