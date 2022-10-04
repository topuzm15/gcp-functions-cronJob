from loguru import logger
from src.caller import BucketCaller, CurrencyCaller
from src.model import AdNetworkDataModel, ProcessedFilesDataModel


class AdNetworkUpdater:
    def filter_processed_files(file_names):
        df = ProcessedFilesDataModel.get_file_names()
        processed_file_names = set(df.file_name.unique().compute().to_list())
        return [i for i in file_names if i[1] not in processed_file_names]

    def get_unique_values(df):
        dt_range = df["dt"].unique().compute().to_list()
        currency_range = df["currency"].unique().compute().to_list()
        network_range = df["network"].unique().compute().to_list()
        platform_range = df["platform"].unique().compute().to_list()

        return dt_range, currency_range, network_range, platform_range
    
    def convert_currency(df, currency_range):
        logger.info("Converting currency")
        currency_dict = CurrencyCaller.get_currency_dict(currency_range)
        df["cost_usd"] = df["cost"] * df["currency"].map(currency_dict)
        return df

    def filter_low_cost(df):
        logger.info("Filtering low cost data")
        return df.groupby(["dt", "network", "currency", "platform"]).agg({"cost": "max"}).reset_index()

    def check_target_table(df, target_df):
        df_join = df.merge(target_df, on=["dt", "network", "currency", "platform"], how="left")
        df_join = df_join[(df_join["cost_target"] < df_join["cost_usd"]) | (df_join["cost_target"].isnull())].drop(columns=["cost_target"])
        df_join = AdNetworkUpdater.filter_low_cost(df_join)
        dt_range, network_range, currency_range, platform_range = AdNetworkUpdater.get_unique_values(df_join)
        AdNetworkDataModel.delete_target_data(dt_range, network_range, currency_range, platform_range)
        return df_join


    def insert_data_partition(file_info):
        df = BucketCaller.get_data(file_info[2])
        df = AdNetworkUpdater.filter_low_cost(df)
        dt_range, currency_range, network_range, platform_range = AdNetworkUpdater.get_unique_values(df)
        df = AdNetworkUpdater.convert_currency(df, currency_range)
        target_df = AdNetworkDataModel.get_target_data(dt_range, network_range, currency_range, platform_range)
        df = AdNetworkUpdater.check_target_table(df, target_df)
        df["file_name"] = file_info[1]
        AdNetworkDataModel.inssert_data_frame(df)
        ProcessedFilesDataModel.insert_file_name(file_info)

    @staticmethod
    def insert_data():
        file_names = BucketCaller.get_file_names()
        AdNetworkDataModel.delete_old_data(file_names)
        file_names = AdNetworkUpdater.filter_processed_files(file_names)
        logger.info(f"Number of files to be processed: {len(file_names)}")
        for i, file_name in enumerate(file_names):
            logger.info(f"Processed file info: {i}")
            AdNetworkUpdater.insert_data_partition(file_name)

        return f'Operation completed successfully'

