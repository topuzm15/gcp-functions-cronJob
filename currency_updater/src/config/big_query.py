from google.cloud import bigquery

class BigQueryConfig:
    client = bigquery.Client()
    currency_table = "dreamcaseemin.case_study.daily_currency_rate_dev"