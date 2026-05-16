.PHONY: up down build logs test pull-model shell status

up:
	docker compose up -d

down:
	docker compose down

build:
	docker compose build --no-cache

logs:
	docker compose logs -f

test:
	pytest app/tests/ -v

pull-model:
	docker exec ollama ollama pull $(model)
# Usage: make pull-model model=mistral

shell:
	docker exec -it ai-chat-api bash

status:
	docker compose ps
