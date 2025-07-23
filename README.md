# DeCodeX Backend

This is the **backend** for [DeCodeX](https://decodex.isaiahozadhe.tech/), an **AI-powered code analysis tool** that helps developers understand, debug, and optimize their code.  
The backend is built with **Python (FastAPI)** and uses **Docker, Redis, WebSockets, and OpenRouter API** for scalable, real-time processing.

The **frontend repository** for this project can be found here:  
➡️ [DeCodeX Frontend Repository](https://github.com/Tekkieware/decodex)

---

## Technologies Used

- [Python](https://www.python.org/) – Core backend language.
- [FastAPI](https://fastapi.tiangolo.com/) – High-performance framework for building APIs.
- [Redis](https://redis.io/) – In-memory data store for queues and caching.
- [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) – Enables real-time communication with the frontend.
- [Docker](https://docs.docker.com/) – Containerization for easy deployment.
- [Docker Compose](https://docs.docker.com/compose/) – Orchestrates multiple services.
- [OpenRouter API](https://openrouter.ai/docs) – AI integration for code analysis.

---

## Features

- REST API for handling AI-driven code analysis.
- Real-time updates via WebSockets.
- Redis-based task queue for managing background processing.
- Containerized with Docker for consistent development and deployment.

---

## Prerequisites

Before running the backend, ensure you have the following installed:

### 1. Docker

Follow the official installation guide:

- [Docker for Windows](https://docs.docker.com/desktop/install/windows/)
- [Docker for macOS](https://docs.docker.com/desktop/install/mac/)
- [Docker for Linux](https://docs.docker.com/engine/install/)

Verify Docker is installed:

```bash
docker --version
```

### 2. Docker Compose

Docker Desktop comes with Compose pre-installed.  
For Linux or standalone installs, follow:

- [Install Docker Compose](https://docs.docker.com/compose/install/)

Verify Docker Compose is installed:

```bash
docker compose version
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Tekkieware/decodex-backend.git
cd decodex-backend
```

### 2. Environment Variable

Before starting, create a `.env` file in the root directory and configure your OpenRouter API URL:

```bash
OPEN_ROUTER_API_URL=<your-openrouter-api-url>
```


## Running the Backend

Start all backend services (API, Redis, WebSocket, workers) using Docker Compose:

```bash
docker compose up --build
```

This will:

- Build all service containers.
- Start FastAPI, Redis, WebSocket services, and background workers.
- Expose the API on the configured port (default: `8000`).

Access the API at:  
[http://localhost:8000](http://localhost:8000)

Stop the containers:

```bash
docker compose down
```

---


---

## Notes

- Ensure the `OPEN_ROUTER_API_URL` environment variable is set, or the AI-powered analysis features will not work.
- The backend automatically integrates with the [DeCodeX Frontend](https://github.com/Tekkieware/decodex) when both are running.

---


---

## Links

- **Backend Repository:** [DeCodeX Backend](https://github.com/Tekkieware/decodex-backend)  
- **Frontend Repository:** [DeCodeX Frontend](https://github.com/Tekkieware/decodex)  
- **Live Demo:** [DeCodeX Live](https://decodex.isaiahozadhe.tech/)
