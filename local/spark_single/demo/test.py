from pyspark.shell import spark
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import col
import pyspark.sql.functions as f


# Pull in a csv as a dataframe
file_path = '/insights.csv'
df = spark.read.csv(file_path, sep =',', header = True)

df.show()

# Count the rows
# extracting number of rows from the Dataframe
row = df.count()

# extracting number of columns from the Dataframe
col = len(df.columns)

# printing
print(f'********************************Dimension of the Dataframe is: {(row,col)}')

file_path = '/insights.csv'
df2 = spark.read.csv(file_path, sep =',', header = True)

df2.show()
row = df2.count()
col = len(df2.columns)
print(f'********************************Dimension of the Dataframe 2 is: {(row,col)}')



# Create Spark tables in RAM
df.createOrReplaceTempView(f'right_table')
df2.createOrReplaceTempView(f'left_table')



# Create an explosion, left join on date (big onto little table - worst practice, but let's see how fast it goes)
output_dataframe = spark.sql("""SELECT * FROM left_table LEFT JOIN right_table ON left_table.date == right_table.date""")

output_dataframe.show()
row = output_dataframe.count()
col = len(output_dataframe.columns)
print(f'********************************Dimension of the Dataframe 2 is: {(row,col)}')


# Write to disk
output_dataframe.write.option("sep","~").option("header","true").csv("/mnt/datalake/weblead_spark_transform.csv")

print("**********************************Written to disk!")

# 22/09/10 22:24:21 INFO DAGScheduler: Job 14 finished: count at NativeMethodAccessorImpl.java:0, took 0.058225 s
# ********************************Dimension of the Dataframe 2 is: (77877092, 30)

# PWD=$(pwd)

# docker run -v ${PWD}/demo:/demo -v /insights:/insights --name spark3 spark_single_spark:latest /usr/local/bin/spark-submit /demo/test.py

# docker rm spark3
