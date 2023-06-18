.PHONY: help
help:
	@cat $(MAKEFILE_LIST) \
		| grep -e "^[a-zA-Z0-9_\-]*: *.*## *" \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: ## Clean out all Docker images.
	sudo docker system prune -a --volumes

stop: ## Tear down everything docker-compose
	docker-compose down

cockroachdb_up:  ## Build & run the cockroachdb images.
	docker-compose up -d --build cockroachdb_node_1 cockroachdb_node_2 cockroachdb_node_3

cockroachdb_down: ## Stop the cockroachdb containers.
	docker stop cockroachdb_node_1 cockroachdb_node_2 cockroachdb_node_3