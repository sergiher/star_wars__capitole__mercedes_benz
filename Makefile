DOCKER_COMPOSE := docker compose

.PHONY: backend frontend

backend:
	@$(DOCKER_COMPOSE) up --build backend; $(DOCKER_COMPOSE) down

frontend:
	@$(DOCKER_COMPOSE) -f docker-compose.yml up --build frontend

# Code Formatting
format_backend:
	@flake8 backend/