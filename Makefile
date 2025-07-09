DOCKER_COMPOSE := docker compose

.PHONY: backend frontend unit individual_test

backend:
	@$(DOCKER_COMPOSE) up --build backend; $(DOCKER_COMPOSE) down

frontend:
	@$(DOCKER_COMPOSE) -f docker-compose.yml up --build frontend

unit:
	$(DOCKER_COMPOSE) run --rm backend pytest tests/unit

# Example: make individual_test test=tests/unit/domain/services/test_starwars_entity_service.py::test_starwars_entity_service_get_all_elements
individual_test:
	$(DOCKER_COMPOSE) run --rm backend pytest $(test)

# Code Formatting
format_backend:
	@flake8 backend/