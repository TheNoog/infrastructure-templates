#!/bin/bash


<<COMMENT

  Summary:
  The following code will install Docker and Docker-Compose to 
    use for testing docker containers and building dockerfiles.

  For Ubuntu 22.04 LTS+.

  NOTE: Permissions will also be added to the current user to 
    enable them to run docker commands with the docker group.

COMMENT

# Docker
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker.service
sudo systemctl enable docker.service
sudo docker version
sudo usermod -aG docker $USER

# Docker-Compose
sudo apt install -y ca-certificates curl gnupg lsb-release
curl -s https://api.github.com/repos/docker/compose/releases/latest | grep browser_download_url  | grep docker-compose-linux-x86_64 | cut -d '"' -f 4 | wget -qi -
chmod +x docker-compose-linux-x86_64
sudo mv docker-compose-linux-x86_64 /usr/local/bin/docker-compose
rm docker-compose-linux-x86_64.sha256
docker-compose version