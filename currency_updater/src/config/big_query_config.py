import os
from google.cloud import bigquery

class BigQueryConfig:
    client = bigquery.Client()
    currency_table = os.getenv("CURRENCY_TABLE", "")