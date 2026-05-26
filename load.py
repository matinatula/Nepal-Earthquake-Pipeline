from sqlalchemy import create_engine, URL, TIMESTAMP
import os
from dotenv import load_dotenv
import pandas as pd


load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB = os.getenv('DB')

url_object = URL.create(
    "postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    database=DB,
)

def load_into_database(url_object=url_object):
    engine = create_engine(url_object)

    df = pd.read_csv('clean_earthquakes.csv')
    df['time'] = pd.to_datetime(df['time'])
    df.to_sql(name='nepal_earthquakes', con=engine,
            index=False, if_exists='replace', dtype={'time': TIMESTAMP})
    print("\nData has been loaded into the database.\n")
