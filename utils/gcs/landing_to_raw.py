import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import psycopg2
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from google.cloud import storage
from io import BytesIO
from sqlalchemy import create_engine
from dotenv import load_dotenv


load_dotenv()


pg_host = os.getenv("PG_HOST")
pg_user = os.getenv("PG_USER")
pg_password = os.getenv("PG_PASSWORD")
pg_db = os.getenv("PG_DB")

gcs_bucket_name = os.getenv("GCS_BUCKET_NAME")


def process_etl():
    tables = ["stations", "status", "trips"]

    storage_client = storage.Client()
    bucket = storage_client.bucket(gcs_bucket_name)
    
    raw_blob = bucket.blob("raw/")
    if not raw_blob.exists():
        raw_blob.upload_from_string("")

    connection = psycopg2.connect(
        host=pg_host, user=pg_user, password=pg_password, dbname=pg_db
    )
    engine = create_engine(
        f"postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{pg_db}"
    )

    for table in tables:
        sql_query = f"SELECT * FROM {table}"
        df = pd.read_sql_query(sql_query, engine)
        
        parquet_buffer = BytesIO()
        pq.write_table(pa.Table.from_pandas(df), parquet_buffer)
        parquet_buffer.seek(0)
        
        blob_name = f"raw/{table}.parquet"
        blob = bucket.blob(blob_name)
        blob.upload_from_file(parquet_buffer, content_type="application/octet-stream")
        print(f"Uploaded {table}.parquet to gs://{gcs_bucket_name}/{blob_name}")

    connection.close()
    print("Done!")


if __name__ == "__main__":
    process_etl() 