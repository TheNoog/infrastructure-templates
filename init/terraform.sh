#!/bin/bash

<<COMMENT

  Summary:
  The following code will install Terraform.

  Note: Extra plugins can be added at the end of the code,
    e.g. Snowflake plugin.

  You may need to install zip if not already on your machine.
    sudo yum install zip -y

  # Snowflake Plugin
  curl https://raw.githubusercontent.com/chanzuckerberg/terraform-provider-snowflake/main/download.sh | sudo bash -s -- -b $HOME/.terraform.d/plugins

COMMENT


TF_VERSION=1.5.0
wget https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip
unzip terraform_${TF_VERSION}_linux_amd64.zip
sudo mv terraform /usr/local/bin/
rm terraform_${TF_VERSION}_linux_amd64.zip
terraform version