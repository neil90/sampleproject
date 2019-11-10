from pyspark.sql import SparkSession


def main():
    """Entry point for the application script"""
    print("Call your main application code here")


def spark_counter(num):
    spark = SparkSession.builder.getOrCreate()

    return spark.range(num).count()
