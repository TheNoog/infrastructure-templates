.PHONY: help
help:
	@cat $(MAKEFILE_LIST) \
		| grep -e "^[a-zA-Z0-9_\-]*: *.*## *" \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: ## Clean out all Docker images.
	sudo docker system prune -a --volumes

stop: ## Tear down everything docker-compose
	docker-compose down

cassandra_up:  ## Build & run the cassandra images.
	docker-compose up -d --build cassandra cassandra-load-keyspace

cassandra_down: ## Stop the cassandra container.
	docker stop cassandra cassandra-load-keyspace

# To connect user RazorSQL:
# https://s3.dualstack.us-east-1.amazonaws.com/downloads.razorsql.com/downloads/9_3_4/razorsql9_3_4_linux_x64.zip