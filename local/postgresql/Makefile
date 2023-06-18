.PHONY: help
help:
	@cat $(MAKEFILE_LIST) \
		| grep -e "^[a-zA-Z0-9_\-]*: *.*## *" \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: ## Clean out all Docker images.
	sudo docker system prune -a --volumes

stop: ## Tear down everything docker-compose
	docker-compose down

postgres_up:  ## Build & run the postgresql image.
	docker-compose up -d --build postgresql pgadmin

postgres_down: ## Stop the postgresql containers.
	docker-compose down
