import os
from generate import FakerEvents
from dotenv import load_dotenv


load_dotenv()

if __name__ == "__main__":
    pg_host = os.getenv("PG_HOST", "localhost")
    pg_user = os.getenv("PG_USER", "postgres")
    pg_password = os.getenv("PG_PASSWORD", "postgres")
    pg_db = os.getenv("PG_DB", "bike_rental")
    
    db_uri = f"postgresql://{pg_user}:{pg_password}@{pg_host}/{pg_db}"
    
    fake_events = FakerEvents(db_uri)

    fake_events.create_stations(100)
    fake_events.create_status(100)
    fake_events.create_trips(100)
