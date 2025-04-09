from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Finance_Model_Training").getOrCreate()
df = spark.read.csv("Train_data.csv", header=True, inferSchema=True)
df.show()