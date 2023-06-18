# This DAG is to pull data from an API and push it into Azure Postgresql


# REPLACE THIS WITH API CALL
#----------------------------------------------------------------------
# !pip install Office365-REST-Python-Client
import pandas as pd
from office365.sharepoint.files.file import File
from office365.runtime.auth.user_credential import UserCredential

# username and password that has access to the file on sharepoint
USERNAME = ""
PASSWORD = ""

local_path = "/owid_test.csv"
URL = "https://owid-covid-data.csv"

with open(local_path, 'wb') as local_file:
    File.from_url(URL).with_credentials(UserCredential(USERNAME, PASSWORD)).download(local_file).execute_query()

data = pd.read_csv(local_path)
data = data.fillna(0)
#-------------------------------------------------------------------------

create_table = "CREATE TABLE covid(index FLOAT,"

for i in range(0, len(list(data.columns))):
    
    attr = list(data.columns)[i]
    d_type = list(data.dtypes)[i]
    #print(str(d_type))
    if str(d_type) == "object":
        #print(f"{attr} VARCHAR(MAX),")
        create_table = create_table + f" {attr} VARCHAR(255)"
    else: 
        #print(f"{attr} FLOAT,")
        create_table = create_table + f" {attr} FLOAT"

    if (i+1) == len(list(data.columns)):
        create_table = create_table + f");"
    else:
        create_table = create_table + f","

#print(create_table)


# PASS THESE THROUGH ANOTHER WAY
PG_SERVER_NAME = ""
PG_USERNAME = ""
PG_PASSWORD = ""

import psycopg2

# Update connection string information
host = PG_SERVER_NAME
dbname = "test"
user = PG_USERNAME
password = PG_PASSWORD

conn = psycopg2.connect(host=host, user=user, password=password, dbname=dbname)
print("Connection established")
cursor = conn.cursor()

# drop table if exists
cursor.execute("DROP TABLE IF EXISTS covid;")

# Create a table
cursor.execute(create_table)
print("Finished creating table")

# Clean up
conn.commit()
cursor.close()
conn.close()



# UPLOAD THE DATA
# https://naysan.ca/2020/05/09/pandas-to-postgresql-using-psycopg2-bulk-insert-performance-benchmark/
# fastest method to upload.

from io import StringIO

def copy_from_stringio(conn, df, table):
    """
    Here we are going save the dataframe in memory 
    and use copy_from() to copy it to the table
    """
    # save dataframe to an in memory buffer
    buffer = StringIO()
    df.to_csv(buffer, index_label='id', header=False)
    buffer.seek(0)
    
    cursor = conn.cursor()
    try:
        cursor.copy_from(buffer, table, sep=",")
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("copy_from_stringio() done")
    cursor.close()

conn = psycopg2.connect(host=host, user=user, password=password, dbname=dbname)

copy_from_stringio(conn, data, 'covid')