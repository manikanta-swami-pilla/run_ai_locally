# 🤖 GitOps Local AI — FastAPI + Ollama + Docker

A production-ready GitOps project that runs a local AI chat API using **FastAPI**, **Ollama**, and **Docker**. Every `git push` to `main` automatically tests, builds, and deploys your AI app.

---

## 📁 Project Structure

```
gitops-local-ai/
├── .github/
│   └── workflows/
│       ├── ci.yml              # Test on every PR
│       └── deploy.yml          # Deploy on merge to main
├── app/
│   ├── main.py                 # FastAPI app
│   ├── config.py               # Settings
│   ├── requirements.txt
│   ├── Dockerfile
│   └── tests/
│       └── test_main.py
├── docker-compose.yml          # Local dev orchestration
├── docker-compose.prod.yml     # Production overrides
├── Makefile                    # Dev shortcuts
├── .env.example
└── README.md
```

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/your-username/gitops-local-ai
cd gitops-local-ai

# 2. Copy env file
cp .env.example .env

# 3. Start everything (Ollama auto-downloads llama3.2 ~2GB)
make up

# 4. Test the API
curl http://localhost:8000/health

curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is GitOps?"}'

# 5. Swap model anytime
make pull-model model=mistral
```

---

## 🔗 API Endpoints

| Method | Endpoint   | Description              |
|--------|------------|--------------------------|
| GET    | /health    | Health check             |
| GET    | /models    | List available models    |
| POST   | /chat      | Send a message to AI     |
| GET    | /docs      | Swagger UI (auto-generated) |

---

## 🔄 GitOps Flow

```
Developer
   │
   ▼
 git push (feature branch)
   │
   ▼
GitHub PR ──► CI runs (test + lint + docker build)
   │
   ▼ (merge to main)
GitHub Actions ──► Build image ──► Push to GHCR
   │
   ▼
SSH into server ──► git pull + docker compose up
   │
   ▼
  Live! 🚀
```

---

## 🔐 GitHub Secrets Required

Go to **Settings → Secrets → Actions** and add:

| Secret           | Value                   |
|------------------|-------------------------|
| `SERVER_HOST`    | Your server IP address  |
| `SERVER_USER`    | `ubuntu` or `root`      |
| `SERVER_SSH_KEY` | Your private SSH key    |

---

## 🛠️ Makefile Commands

```bash
make up            # Start all containers
make down          # Stop all containers
make build         # Rebuild images
make logs          # Follow logs
make test          # Run pytest
make status        # Show container status
make shell         # Shell into app container
make pull-model model=mistral  # Pull a new Ollama model
```

---

## 💡 Hardware Requirements

| RAM     | Recommended Model |
|---------|-------------------|
| 4–8 GB  | gemma:2b, phi3    |
| 8–16 GB | llama3.2, mistral |
| 16 GB+  | llama3.3, mixtral |

---

## 📝 License

MIT — free to use, modify, and distribute.
