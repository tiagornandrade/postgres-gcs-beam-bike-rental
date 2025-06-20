import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import pandas as pd
from google.cloud import storage
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

gcs_bucket_name = os.getenv("GCS_BUCKET_NAME")


def download_data_from_gcs(table):
    storage_client = storage.Client()
    bucket = storage_client.bucket(gcs_bucket_name)

    blob_name = f"trusted/{table}.csv"
    blob = bucket.blob(blob_name)

    if not blob.exists():
        raise FileNotFoundError(f"File {blob_name} not found in bucket {gcs_bucket_name}")

    content = blob.download_as_bytes()
    return pd.read_csv(BytesIO(content))


def promotion_to_refined():
    tables = ["stations", "status", "trips"]

    storage_client = storage.Client()
    bucket = storage_client.bucket(gcs_bucket_name)
    
    refined_blob = bucket.blob("refined/")
    if not refined_blob.exists():
        refined_blob.upload_from_string("")

    for table in tables:
        df = download_data_from_gcs(table)

        csv_buffer = BytesIO()
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)

        blob_name = f"refined/{table}.csv"
        blob = bucket.blob(blob_name)
        blob.upload_from_file(csv_buffer, content_type="text/csv")
        
        print(f"Promoting trusted.{table} to refined.{table}")

    print("Done!")


if __name__ == "__main__":
    promotion_to_refined() 