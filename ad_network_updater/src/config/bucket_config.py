import os
from google.cloud import storage

class BucketConfig:
    bucket_name = os.environ.get('BUCKET_NAME')
    gcs = storage.Client()
    bucket = gcs.get_bucket(bucket_name)
