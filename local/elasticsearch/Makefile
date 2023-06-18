.PHONY: help
help:
	@cat $(MAKEFILE_LIST) \
		| grep -e "^[a-zA-Z0-9_\-]*: *.*## *" \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: ## Clean out all Docker images.
	sudo docker system prune -a --volumes

stop: ## Tear down everything docker-compose
	docker-compose down

elastic_up:  ## Build & run the elasticsearch images.
	sudo sysctl -w vm.max_map_count=262144
	docker-compose up -d --build es01 es02 kibana logstash apm

elastic_down: ## Stop the elastic containers.
	docker stop es01 es02 kibana logstash apm
	#docker system prune -f
