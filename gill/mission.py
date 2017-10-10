import pyspark.sql.functions as F

def with_life_goal(df):
    return df.withColumn("life_goal", F.lit("escape!"))

