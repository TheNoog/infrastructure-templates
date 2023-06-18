from pyspark.shell import spark
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import col
import pyspark.sql.functions as f

 
a = [1002, 3001, 4002, 2003, 2002, 3004, 1003, 4006]
b = spark.createDataFrame(a, IntegerType()).withColumn("x", col("value") % 1000)

b.show()

c = b.groupBy(col("x"))\
    .agg(f.count("x"), f.sum("value"))\
    .drop("x")\
    .toDF("count", "total")\
    .orderBy(col("count").desc(), col("total"))\
    .limit(1)\
    .show()


# Run a Python application on a Spark standalone cluster
# Run the following line inside the master node of the cluster. Note that this file must be mounted in /data for this to work.
# docker exec spark-master bash ./opt/spark/bin/spark-submit --master spark://master:7077 data_py/spark/pyspark-example.py 1000