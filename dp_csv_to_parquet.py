from pyspark.sql import SparkSession
import sys

spark = SparkSession.builder.appName('CSV_to_Parquet').getOrCreate()

input_path = sys.argv[1]  # input path
output_path_parquet = sys.argv[2]  # output path

df = spark.read.csv(input_path, header=True, inferSchema=True)
df.write.parquet(output_path_parquet, mode='overwrite')
spark.stop()