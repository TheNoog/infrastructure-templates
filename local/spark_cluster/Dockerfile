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
    scala \
    wget \
    libodbc1 unixodbc unixodbc-dev

# Spark
ENV SPARK_VERSION=3.3.1
ENV HADOOP_VERSION=3
ENV SCALA_VERSION=2.13

RUN wget https://downloads.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}-scala${SCALA_VERSION}.tgz 
RUN tar xvf spark-*
RUN mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}-scala${SCALA_VERSION} /opt/spark
RUN rm -rf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}-scala${SCALA_VERSION}.tgz
#RUN chmod +x /opt/spark/spark-${SPARK_VERSION}-bin-hadoop3.2/sbin/start-master.sh
RUN echo "export SPARK_HOME=/opt/spark" >> ~/.profile
RUN echo "export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin" >> ~/.profile
RUN echo "export PYSPARK_PYTHON=/usr/bin/python3" >> ~/.profile
# 	export SPARK_EXAMPLES_JAR=/usr/local/spark/examples/jars/spark-examples_2.12-3.0.0.jar


# Create a log4j.properties file for Hadoop.
# https://stackoverflow.com/questions/33897307/hadoop-log4j-not-working-as-no-appenders-could-be-found-for-logger-org-apache-h
# src/main/resources/log4j.properties

ENV LOG4J_LOCATION=/src/main/resources/log4j.properties

RUN mkdir /src
RUN mkdir /src/main
RUN mkdir /src/main/resources
RUN touch ${LOG4J_LOCATION}
RUN echo "hadoop.root.logger=DEBUG, console" >> ${LOG4J_LOCATION}
RUN echo "log4j.rootLogger = DEBUG, console" >> ${LOG4J_LOCATION}
RUN echo "log4j.appender.console=org.apache.log4j.ConsoleAppender" >> ${LOG4J_LOCATION}
RUN echo "log4j.appender.console.target=System.out" >> ${LOG4J_LOCATION}
RUN echo "log4j.appender.console.layout=org.apache.log4j.PatternLayout" >> ${LOG4J_LOCATION}
RUN echo "log4j.appender.console.layout.ConversionPattern=%d{yy/MM/dd HH:mm:ss} %p %c{2}: %m%n" >> ${LOG4J_LOCATION}


# Jupyter Notebook
# RUN export PYSPARK_DRIVER_PYTHON="jupyter"
# RUN export PYSPARK_DRIVER_PYTHON=OPTS="notebook"
# RUN export PYSPARK_PYTHON=python3

RUN echo SPARK_NO_DAEMONIZE=true > /opt/spark/conf/spark-env.sh

# Add PySpark and common dependencies (e.g. cloud storage)
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# SBT for Scala -> jar
# https://www.scala-sbt.org/download.html
# RUN echo "deb https://repo.scala-sbt.org/scalasbt/debian all main" | tee /etc/apt/sources.list.d/sbt.list
# RUN echo "deb https://repo.scala-sbt.org/scalasbt/debian /" | tee /etc/apt/sources.list.d/sbt_old.list
# RUN curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | apt-key add
# RUN apt-get update
# RUN apt-get install sbt

# ENTRYPOINT ["tail"]
# CMD ["-f", "/dev/null"]