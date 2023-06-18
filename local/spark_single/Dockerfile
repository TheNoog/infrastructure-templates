# https://phoenixnap.com/kb/install-spark-on-ubuntu
FROM ubuntu:22.04

# Add repositories
RUN apt-get update -y
RUN apt-get install -y software-properties-common

# Install the requirements
RUN apt-get install -y --fix-missing \
    curl \
    default-jdk \
    git \
    maven \
    mlocate \
    nano \
    python3-pip \
    wget \
    libodbc1 unixodbc unixodbc-dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


# PWD=$(pwd)
# docker run -v ${PWD}/demo:/demo --name spark3 spark_single_spark:latest /usr/local/bin/spark-submit /demo/pyspark-example.py
# docker rm spark3