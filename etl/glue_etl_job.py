from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from app.utils.fetch_data import fetch_apod_data, fetch_neo_data, fetch_mars_photos  # Import the fetching functions
from datetime import datetime, timedelta
import json

glueContext = GlueContext(SparkContext.getOrCreate())
spark = SparkSession.builder.appName("NASA_ETL_Job").getOrCreate()

def transform_data(df):
    # Transformation logic (e.g., date normalization, cleaning)
    df = df.withColumn("date", F.to_date(F.col("date"), "yyyy-MM-dd"))
    df = df.dropDuplicates()
    return df

def main():
    # Get the current date
    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")  # Example: last 7 days

    # Fetching data from NASA APIs
    apod_data = fetch_apod_data(start_date, end_date)
    neo_data = fetch_neo_data(start_date, end_date)
    mars_photos = fetch_mars_photos(end_date)  # Use the end_date for Mars photos

    # Convert the fetched JSON data to Spark DataFrames
    apod_df = spark.createDataFrame(apod_data)
    neo_df = spark.createDataFrame(neo_data.get('near_earth_objects', []))  # Extracting relevant field
    mars_df = spark.createDataFrame(mars_photos.get('photos', []))          # Extracting relevant field

    # Transforming the data
    transformed_apod_df = transform_data(apod_df)
    transformed_neo_df = transform_data(neo_df)
    transformed_mars_df = transform_data(mars_df)

    # Writing the transformed data to S3
    transformed_apod_df.write.mode("overwrite").format("parquet").save("s3://nasa-etl-bucket/processed_apod_data/")
    transformed_neo_df.write.mode("overwrite").format("parquet").save("s3://nasa-etl-bucket/processed_neo_data/")
    transformed_mars_df.write.mode("overwrite").format("parquet").save("s3://nasa-etl-bucket/processed_mars_data/")

if __name__ == "__main__":
    main()