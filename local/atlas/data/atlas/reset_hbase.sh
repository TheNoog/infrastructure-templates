#!/bin/sh

# this method won't work easily due to data encapsulation.
# It is better to keep Atlas running and then delete the entities through the API.

# Stop Atlas
#sudo docker exec -ti dg_atlas <- inside this container
python /opt/apache-atlas-2.1.0/bin/atlas_stop.py

# In HBase terminal
#disable 'atlas_titan'
#drop 'atlas_titan'

# Restart Atlas
