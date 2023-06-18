FROM ubuntu:22.10

# https://sparkbyexamples.com/hadoop/apache-hadoop-installation/

RUN sudo apt-get update
RUN sudo apt-get -y install ssh openjdk-8-jdk-headless

# The name node will use an ssh-connection to connect to other nodes
#  in a cluster with key-pair authentication, to manage the cluster. 
#  hence let’s generate key-pair using ssh-keygen

# if hostname = "namenode"
# else if hostname like "datanode"  -> datanode1

RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa

RUN cat .ssh/id_rsa.pub >> ~/.ssh/authorized_keys

# Now copy authorized_keys to all data nodes in a cluster. This enables 
#  name node to connect to data nodes password less (without prompting 
#  for password)
RUN scp .ssh/authorized_keys datanode1:/home/ubuntu/.ssh/authorized_keys
RUN scp .ssh/authorized_keys datanode2:/home/ubuntu/.ssh/authorized_keys
RUN scp .ssh/authorized_keys datanode3:/home/ubuntu/.ssh/authorized_keys

# Add nodes to /etc/hosts
# sudo vi /etc/hosts
# 192.168.1.100 namenode.socal.rr.com
# 192.168.1.141 datanode1.socal.rr.com
# 192.168.1.113 datanode2.socal.rr.com
# 192.168.1.118 datanode3.socal.rr.com

