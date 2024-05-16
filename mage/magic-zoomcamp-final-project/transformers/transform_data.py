import pandas as pd
# import pyspark
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import year, month

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    # # Initialize Spark session
    # spark = SparkSession.builder \
    #     .appName("Test") \
    #     .getOrCreate()
    
    # # data to Spark dataframe
    # df = spark_session.createDataFrame(data)

    # df = df \
    #     .withColumn("year", year("Date")) \
    #     .withColumn("month", month("Date")) \
    #     .withColumn("quarter", quarter("Date")) \
    #     .withColumnRenamed("Year", "Period")

    df = data

    # Rename the column
    df.rename(columns={'Year': 'Period'}, inplace=True)

    # Convert the date column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Add a year and month column by extracting the year from the date column
    df['year'] = df['Date'].dt.year
    df['month'] = df['Date'].dt.month

    # Add quarter column Q + qtr
    prefix = 'Q'
    # Add the prefix to the 'id' column values
    df['quarter'] = df['Date'].dt.quarter.apply(lambda x: f"{prefix}{x}")

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
