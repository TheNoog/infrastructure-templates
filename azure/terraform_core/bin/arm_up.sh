#!/usr/bin/env bash

<< COMMENT

  Summary:
    Deploys the core infrastructure components using ARM templates
    in individual stages.

  Stages:
    1. Deploy the resource group to the subscription.
    2. Deploy the storage solution to the resource group.
    3. Deploy the Key Vault to the resource group.

COMMENT


### 0.1 SETUP: ENVIRONMENT VARIABLES
while read line; do export $line; done < .env


# Some pretty colours to use with outputs
RED_TEXT="\e[31m"
GREEN_TEXT="\e[32m"
BLUE_TEXT="\e[36m"
YELLOW_TEXT="\e[33m"
CLEAR="\e[0m"
BOLD="\e[1m"
NORMAL="\e[24m"

echo -e "\n${BOLD}${YELLOW_TEXT}***${NORMAL}${BLUE_TEXT} Deploying the ARM templates using the parameters${YELLOW_TEXT}${BOLD} ***${CLEAR}\n"


## 1. Deploy the resource group to the subscription
az deployment sub create \
  --name ${RESOURCE_GROUP_ARM_TEMPLATE_NAME} \
  --location australiaeast \
  --template-file ./lib/resource_group/template.json \
  --parameters "@lib/resource_group/parameters.json" \
  --parameters rgName=${RESOURCE_GROUP_NAME}

echo -e "${GREEN_TEXT}Resource group deployed.${CLEAR}"


## 2. Deploy the storage solution to the resource group
az deployment group create \
  --name ${STORAGE_ACCOUNT_ARM_TEMPLATE_NAME} \
  --resource-group ${RESOURCE_GROUP_NAME} \
  --template-file ./lib/storage/template.json \
  --parameters "@lib/storage/parameters.json" \
  --parameters storageAccountName=${STORAGE_ACCOUNT_NAME}

echo -e "${GREEN_TEXT}Storage solution deployed.${CLEAR}"


## 3. Deploy the Key Vault to store Terraform environment variables
az deployment group create \
  --name ${KEY_VAULT_ARM_TEMPLATE_NAME} \
  --resource-group ${RESOURCE_GROUP_NAME} \
  --template-file ./lib/key_vault/template.json \
  --parameters "@lib/key_vault/parameters.json" \
  --parameters name=${KEY_VAULT_NAME}

echo -e "${GREEN_TEXT}Key Vault deployed.${CLEAR}"
