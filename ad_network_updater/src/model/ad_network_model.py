from src.config import BigQueryConfig, EtlConfig
from src.caller import BigQueryCaller
from loguru import logger

class AdNetworkDataModel:
    @staticmethod
    def delete_old_data(file_names):
        logger.info("Deleting old data")
        query_path = 'src/sql/delete_old_data.sql'
        parameters = {"target_table_name": BigQueryConfig.ad_network_table, 
                      "processed_table_name": BigQueryConfig.processed_file_table,
                      "file_names": "'" + "','".join([i[1] for i in file_names]) + "'", 
                      "date": EtlConfig.min_date}
        BigQueryCaller.exacute_query(query_path, parameters)

    @staticmethod
    def get_target_data(dt_range, network_range, currency_range, platform_range):
        logger.info("Getting target data")
        query_path = 'src/sql/get_target_data.sql'
        parameters = {"table_name": BigQueryConfig.ad_network_table, 
                      "dates": "'" + "','".join(dt_range) + "'", 
                      "networks": "'" + "','".join(network_range) + "'", 
                      "currencies": "'" + "','".join(currency_range) + "'", 
                      "platforms": "'" + "','".join(platform_range) + "'"}
        return BigQueryCaller.get_data(query_path, parameters)

    @staticmethod
    def delete_target_data(dt_range, network_range, currency_range, platform_range):
        logger.info("Deleting target data")
        query_path = 'src/sql/delete_target_data.sql'
        parameters = {"table_name": BigQueryConfig.ad_network_table, 
                      "dates": "'" + "','".join(dt_range) + "'", 
                      "networks": "'" + "','".join(network_range) + "'", 
                      "currencies": "'" + "','".join(currency_range) + "'", 
                      "platforms": "'" + "','".join(platform_range) + "'"}
        BigQueryCaller.exacute_query(query_path, parameters)

    @staticmethod
    def inssert_data_frame(df):
        logger.info("Uploading data to bigquery")
        BigQueryCaller.insert_data_frame(df, BigQueryConfig.ad_network_table)