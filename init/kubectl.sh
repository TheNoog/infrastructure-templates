#!/usr/bin/env bash


<<COMMENT

  Summary:
    Installs Kubectl for Kubernetes. Version problems can exist with AWS. 
    Show snap list prior to check version compatibility with Kubernetes.

  If already installed, refresh with:

    sudo snap refresh kubectl \
        --channel=1.20/stable \
        --classic

  Reference:
  - https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

COMMENT


sudo snap install kubectl --classic