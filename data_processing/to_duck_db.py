from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, LongType

# Create Spark Session 
spark = SparkSession.builder \
        .appName("testing") \
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.13:3.4.1") \
        .getOrCreate()

#
after_schema = StructType([
    StructField("id", IntegerType()),
    StructField("orders_id", IntegerType()),
    StructField("status", StringType()),
    StructField("destination_id", IntegerType()),
    StructField("location", StringType()),
    StructField("updated_at", LongType())
])

envelope_schema = StructType([
    StructField("payload", StructType([
        StructField("after", after_schema),
        StructField("op", StringType())
    ]))
])

df_raw = spark.readStream.format("kafka")\
        .option("kafka.bootstrap.servers", "localhost:9092")\
        .option("subscribe", "orders_history.public.orders_history")\
        .load()

df_parsed = df_raw.selectExpr("CAST(value AS STRING) as json_str") \
        .select(from_json(col("json_str"), envelope_schema).alias("data")) \
        .filter(col("data.payload.op").isin("c", "u"))\
        .select("data.payload.after.*")


query = df_parsed.writeStream\
        .format("console")\
        .option("truncate", False)\
        .start()

query.awaitTermination()
