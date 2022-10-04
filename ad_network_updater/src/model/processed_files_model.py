from src.config import BigQueryConfig, EtlConfig
from src.caller import BigQueryCaller
from loguru import logger

class ProcessedFilesDataModel:
    @staticmethod
    def get_file_names():
        query_path = "src/sql/get_processed_files.sql"
        parameters = {"table_name": BigQueryConfig.processed_file_table, 
                      "date": EtlConfig.min_date}
        return BigQueryCaller.get_data(query_path, parameters)

    @staticmethod
    def insert_file_name(file_name):
        rows = [{"dt": file_name[0], "file_name": file_name[1]}]
        BigQueryCaller.insert_rows(rows, BigQueryConfig.processed_file_table)