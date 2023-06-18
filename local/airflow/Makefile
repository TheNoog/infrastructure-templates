CURRENT_DIR := $(shell pwd)
DAGS_DIR := /usr/local/airflow
DATA_DIR := /data

.PHONY: help
help:
	@cat $(MAKEFILE_LIST) \
		| grep -e "^[a-zA-Z0-9_\-]*: *.*## *" \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: ## Clean out all Docker images.
	sudo docker system prune -a --volumes

up: ## Run airflow docker-compose
	./airflow_up.sh

down: ## Stop the airflow containers.
	./airflow_down.sh
