import pandas as pd
from dask import dataframe as dd
from src.config import BigQueryConfig


class BigQueryCaller:
    @staticmethod
    def exacute_query(query_path, parameters):
        with open(query_path, 'r') as f:
            query = f.read().format(**parameters)
        return BigQueryConfig.bigquery_engine.execute(query)

    @staticmethod
    def get_data(query_path, parameters):
        with open(query_path, 'r') as f:
            query = f.read().format(**parameters)

        with BigQueryConfig.bigquery_engine.begin() as conn:
            query_results = dd.from_pandas(
                pd.read_sql(query, conn), npartitions=1)
            query_results["dt"] = query_results["dt"].astype(str)
        return query_results

    @staticmethod
    def insert_data_frame(df, table_name):
        BigQueryConfig.client.insert_rows_from_dataframe(table=table_name,
                                                         selected_fields=BigQueryConfig.client.get_table(
                                                             table_name).schema,
                                                         dataframe=df)

    @staticmethod
    def insert_rows(rows, table_name):
        BigQueryConfig.client.insert_rows_json(table_name, rows,
                                               row_ids=[None] * len(rows))
