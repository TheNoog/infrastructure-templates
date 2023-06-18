.PHONY: help
help:
	@cat $(MAKEFILE_LIST) \
		| grep -e "^[a-zA-Z0-9_\-]*: *.*## *" \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: ## Clean out all Docker images.
	sudo docker system prune -a --volumes

stop: ## Tear down everything docker-compose
	docker-compose down

nifi_build:  ## Build the nifi images.
	docker-compose build nifi zookeeper

nifi_up:  ## Build & run the nifi images.
	docker-compose up -d --build nifi zookeeper

nifi_down: ## Stop the nifi containers.
	docker stop nifi zookeeper