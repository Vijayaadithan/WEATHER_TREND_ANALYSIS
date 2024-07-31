import sqlite3
import pandas as pd

def create_database(db_name):
    # Create a new SQLite database
    conn = sqlite3.connect(db_name)
    conn.close()

def store_data_in_db(db_name, df, table_name):
    # Store the processed data into the database
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()



db_name = 'weather_data.db'
table_name = 'delhi_weather'
processed_data_path = 'processed_delhi_weather_data.csv'
create_database(db_name)
df = pd.read_csv(processed_data_path)
store_data_in_db(db_name, df, table_name)

