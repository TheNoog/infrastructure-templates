PROJECT_ID := apache_atlas

DOCKER_COMPOSE_VERSION := 1.24.1
DOCKER_COMPOSE_URL := "https://github.com/docker/compose/releases/download/$(DOCKER_COMPOSE_VERSION)/docker-compose-$(shell uname -s)-$(shell uname -m)"

# to pull these through nodejs needs to be installed (apt install nodejs)
ATLAS_USR := $(shell node -p "require('./credentials/atlas.json').user")
ATLAS_PWD := $(shell node -p "require('./credentials/atlas.json').password")
ATLAS_SHA := $(shell node -p "require('./credentials/atlas.json').sha256")

.PHONY: help
help:
	@cat $(MAKEFILE_LIST) \
		| grep -e "^[a-zA-Z0-9_\-]*: *.*## *" \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

down: ## Tear down local Docker cluster based on project_id
	PROJECT_ID=$(PROJECT_ID) \
	    docker-compose -p $(PROJECT_ID) down
	    docker system prune -f

init: ## For Ubuntu 20.04; assumes a clean install with just "apt install git make" and then this repo cloned.
	sudo apt -y install apt-transport-https ca-certificates curl software-properties-common
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg --insecure | sudo apt-key add -
	sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
	sudo apt-get update
	sudo apt-get -y install docker-ce docker-ce-cli containerd.io
	sudo curl -L $(DOCKER_COMPOSE_URL) --insecure -o /usr/local/bin/docker-compose
	sudo chmod +x /usr/local/bin/docker-compose

up: ## Deploy Atlas container
	PROJECT_ID=$(PROJECT_ID) ATLAS_USR=$(ATLAS_USR) ATLAS_PWD=$(ATLAS_PWD) ATLAS_SHA=$(ATLAS_SHA) \
		docker-compose -p $(PROJECT_ID) up --build -d
	# add credentials to Atlas.
	ATLAS_USR=$(ATLAS_USR) ATLAS_SHA=$(ATLAS_SHA) | sed "s/ATLAS_USR/$(ATLAS_USR)/g; s/ATLAS_SHA/$(ATLAS_SHA)/g" ./docker/atlas/users-credentials.template > ./docker/atlas/users-credentials.properties
	ATLAS_USR=$(ATLAS_USR) | sed "s/ATLAS_USR/$(ATLAS_USR)/g" ./docker/atlas/atlas-simple-authz-policy-template.json > ./docker/atlas/atlas-simple-authz-policy.json