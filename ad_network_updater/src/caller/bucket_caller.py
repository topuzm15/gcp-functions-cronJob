from src.config import BucketConfig
from dask import dataframe as dd
from loguru import logger


class BucketCaller:  
    @staticmethod
    def get_file_names():
        blobs_all = list(BucketConfig.bucket.list_blobs(prefix='case_daily/2'))
        return [(blob.name.split('/')[-2], blob.name.split('/')[-1].split('.')[0], blob) for blob in blobs_all]

    @staticmethod
    def get_data(file_name):
        logger.info(f"file goingto read gcs://{BucketConfig.bucket_name}/{file_name.name}")
        df =  dd.read_parquet(f"gcs://{BucketConfig.bucket_name}/{file_name.name}", engine='fastparquet')
        df["dt"] = df.dt.apply(lambda x: x.strftime("%Y-%m-%d"), meta=('dt', 'str'))
        return df