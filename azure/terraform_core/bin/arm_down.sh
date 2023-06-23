#!/usr/bin/env bash

<< COMMENT

  Summary:
    Deploys the core infrastructure components using ARM templates
    in individual stages.

  Stages:
    1. Destroy the resource group to the subscription
    2. Destroy the deployment (if still exists)

COMMENT


RED_TEXT="\e[31m"
GREEN_TEXT="\e[32m"
BLUE_TEXT="\e[36m"
YELLOW_TEXT="\e[33m"
CLEAR="\e[0m"
BOLD="\e[1m"
NORMAL="\e[24m"

### 0.1 SETUP: ENVIRONMENT VARIABLES
while read line; do export $line; done < .env

echo -e "\n${BOLD}${RED_TEXT}***${NORMAL}${RED_TEXT} Destroy the ARM template and ${RESOURCE_GROUP_NAME} resource group.${BOLD} ***${CLEAR}\n"

# 1. Delete the resource group
az group delete -n ${RESOURCE_GROUP_NAME}

# 2. Delete the resource group deployment in the subscription
az deployment sub delete --name ${RESOURCE_GROUP_ARM_TEMPLATE_NAME}
