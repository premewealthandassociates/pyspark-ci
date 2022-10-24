import pyspark.sql.functions as F
from pyspark.sql import DataFrame

def add_1(df: DataFrame, col_to_add: str):
    "Add 1 to a column."
    return df.withColumn(f"{col_to_add}_plus_one", F.col(col_to_add) + F.lit(1))
