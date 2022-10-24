import pytest
from chispa.dataframe_comparer import assert_df_equality
from pyspark.sql import Row
from pyspark.sql.types import IntegerType, StructField, StructType

from pyspark_ci.add_number import add_1


def test_add_1(spark):

    # arrange
    data = [{"num": 1}]

    expected_data = [{"num": 1, "num_plus_one": 2}]

    schema = StructType([StructField("num", IntegerType())])

    expected_schema = StructType([StructField("num", IntegerType()), StructField("num_plus_one", IntegerType())])

    data_df = spark.createDataFrame([Row(**x) for x in data], schema)

    expected_df = spark.createDataFrame([Row(**x) for x in expected_data], expected_schema)

    # act
    result_df = add_1(data_df, "num")

    # assert
    assert_df_equality(result_df, expected_df)
