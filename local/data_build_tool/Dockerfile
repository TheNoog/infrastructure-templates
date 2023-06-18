# https://discourse.getdbt.com/t/publishing-dbt-docs-from-a-docker-container/141
FROM python:3.8.7-slim-buster

RUN apt update --fix-missing \
    && apt upgrade -y \
    && apt install -y curl gcc git gnupg2 nano python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev g++ unixodbc-dev \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && ACCEPT_EULA=Y apt-get install -y mssql-tools

# Install DBT & python requirements
RUN python3 -m pip install --upgrade pip
RUN pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org dbt==0.19.0
#dbt-sqlserver
ADD requirements.txt requirements.txt
RUN pip3 install --trusted-host files.pythonhosted.org -r requirements.txt

# Add entrypoint
COPY docker-entrypoint.sh docker-entrypoint.sh
RUN chmod 777 docker-entrypoint.sh

# Initialise dbt & copy repository across
RUN dbt init data_build_tool_models
COPY * /data_build_tool_models/
COPY profiles.yml /root/.dbt/profiles.yml

# Debug and compile the manifest
# RUN cd /data_build_tool_models && dbt debug
# RUN cd /data_build_tool_models && dbt compile

#ENTRYPOINT ["/bin/bash", "docker-entrypoint.sh"]
CMD ["bash"]

# To compile, run:
# 1. docker build -t dbt:latest .
# 2. docker run -it dbt:latest bash
# 2. docker run -v /myProject/data_build_tool_models/:/root/.dbt/ -it dbt:latest bash
# 3. docker tag dbt:latest containerregistry.azurecr.io/dbt:latest
# 4. docker push containerregistry.azurecr.io/dbt:latest
# docker login containerregistry.azurecr.io
#       enter the service principal userid and password (or your credentials)

# cd /data_build_tool_models && dbt --no-write-json run --target prod --models my_first_dbt_model
# cd /data_build_tool_models && dbt debug
# cd /data_build_tool_models && dbt compile
# cd /data_build_tool_models && python3 create-dags-from-manifest.py

# Potential solutions
# https://medium.com/faun/building-docker-images-using-azure-devops-pipelines-with-private-devops-artifactory-pypi-feed-8e1637286474