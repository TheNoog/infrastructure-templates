.PHONY: help
help:
	@cat $(MAKEFILE_LIST) \
		| grep -e "^[a-zA-Z0-9_\-]*: *.*## *" \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: ## Clean out all Docker images.
	sudo docker system prune -a --volumes

stop: ## Tear down everything docker-compose
	docker-compose down

# connect with Robot 3T
build:  ## Build the mongodb images.
	docker-compose build mongodb

up:  ## Build & run the mongodb images.
	docker-compose up -d --build mongodb

down: ## Stop the mongodb container.
	docker-compose down
	# docker stop mongodb
	#docker system prune -f

# To connect and view install: https://robomongo.org/download