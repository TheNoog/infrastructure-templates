.PHONY: help
help:
	@cat $(MAKEFILE_LIST) \
		| grep -e "^[a-zA-Z0-9_\-]*: *.*## *" \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

aws: ## Install AWS Cli.
	sudo init/aws.sh

azure: ## Install Azure Cli (az).
	init/azure.sh

docker: ## Install Docker and Docker-Compose
	init/docker.sh

gcp: ## Install GCP CLi (gcloud).
	init/gcp.sh

helm: ## Install Helm.
	init/helm.sh

kubectl: ## Install kubectl for Kubernetes.
	init/kubectl.sh

terraform: ## Install Terraform.
	init/terraform.sh