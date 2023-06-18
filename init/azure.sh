#!/usr/bin/env bash


<<COMMENT

  Summary:
  The following code will install the Azure command line interface.
  This code is for Ubuntu 22.04 LTS+.

  Note: Pass through the current subscription when running the 
    command.

  To configure:
    az account set --subscription $(SUBSCRIPTION)
    az login --allow-no-subscriptions

COMMENT


sudo apt install -y python3-pip
sudo pip3 install azure-cli

az login --use-device-code