.PHONY: help
help:
	@cat $(MAKEFILE_LIST) \
		| grep -e "^[a-zA-Z0-9_\-]*: *.*## *" \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: ## Clean out all Docker images.
	sudo docker system prune -a --volumes

stop: ## Tear down everything docker-compose
	docker-compose down

metabase_build:  ## Build the metabase image.
	docker-compose build metabase

metabase_up: ## Run metabase docker-compose
	docker-compose up -d --build metabase

metabase_down:  ## Stop metabase
	docker stop metabase
