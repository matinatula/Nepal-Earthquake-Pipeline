import ingest
import clean
import load

ingest.ingest_from_api_to_json()
clean.clean_data_into_csv()
load.load_into_database()
