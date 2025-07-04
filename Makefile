.PHONY: frontend

frontend:
	@$(DOCKER_COMPOSE) -f docker-compose.yml up --build frontend
