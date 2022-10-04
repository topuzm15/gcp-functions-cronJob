import os
from google.cloud import bigquery
from sqlalchemy import create_engine

class BigQueryConfig:
    client = bigquery.Client()
    ad_network_table = os.getenv("AD_NETWORK_TABLE", "")
    processed_file_table = os.getenv("PROCESSED_FILE_TABLE", "")
    bigquery_engine = create_engine('bigquery://', credentials_path=os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))