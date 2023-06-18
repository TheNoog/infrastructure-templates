.PHONY: help
help:
	@cat $(MAKEFILE_LIST) \
		| grep -e "^[a-zA-Z0-9_\-]*: *.*## *" \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


build:  ## Build the spark images.
	docker-compose build spark

# https://github.com/apache/spark/blob/master/resource-managers/kubernetes/docker/src/main/dockerfiles/spark/Dockerfile
up:  ## Build & run the spark images.
	docker-compose up -d --build spark
# docker exec spark-master jupyter notebook --allow-root
# docker exec spark-master curl -v 127.0.0.1:8888

down:  ## Stop the Spark images
	docker stop spark

docker: ## Create and upload the docker container to kubernetes
	docker-compose up -d --build
	docker tag streaming-project_spark-master:latest localhost:32000/streaming-project_spark-master:3.1.2
	docker push localhost:32000/streaming-project_spark-master:3.1.2
	docker tag streaming-project_spark-worker-1:latest localhost:32000/streaming-project_spark-worker-1:3.1.2
	docker push localhost:32000/streaming-project_spark-worker-1:3.1.2

test:  ## Send a test packet to the spark cluster
	curl -X POST http://localhost:7077/v1/submissions/create --header "Content-Type:application/json;charset=UTF-8" --data ./code-examples/scala/pi.scala

local: ## install locally
	echo "Use the spark dockerfile for ubuntu!"
# TO RUN: spark-shell
# TO STOP: sys.exit