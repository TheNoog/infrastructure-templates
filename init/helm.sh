#!/bin/bash

<<COMMENT

  Summary:
  The following code will install Helm to enable the use of Helm
    charts with Kubernetes.

  Note: This method assumes snap is already installed.

COMMENT


snap install helm --classic
helm repo add stable https://charts.helm.sh/stable

helm repo add apache-airflow https://airflow.apache.org
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add nginx-stable https://helm.nginx.com/stable

helm repo update