def save_df_to_databricks(df, table_name, schema_name = 'lisapritchett'):
  '''save a pandas dataframe to databricks as schema_name.table_name'''
  spark.createDataFrame(df).write.mode("overwrite").saveAsTable("{}.{}".format(schema_name, table_name))


def get_df_from_databricks(table_name, schema_name = 'lisapritchett'):
  '''return a pandas dataframe saved in databricks schema_name.table_name'''
  return spark.sql("SELECT * FROM {schema}.{table}".format(schema=schema_name, table=table_name)).toPandas()

