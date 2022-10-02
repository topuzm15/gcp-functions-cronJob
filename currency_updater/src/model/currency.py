from src.config import BigQueryConfig


class CurrencyDataModel:
    def __init__(self) -> None:
        self.client = BigQueryConfig.client

    def delete_data(self, start_date, end_date):
        with open('src/sql/delete_rows.sql', 'r') as file:
            query = file.read().format(**{"table_name": BigQueryConfig.currency_table,
                                          "start_date": start_date,
                                          "end_date": end_date})

        query_job = self.client.query(query)
        return query_job.result()

    def insert_currency_data(self, data):
        self.client.insert_rows_json(BigQueryConfig.currency_table, data)