
import sqlite3
import pandas as pd

def retrieve_weather_details(db_name='weather_data.db', table_name='delhi_weather', year=None, month=None):
    conn = sqlite3.connect(db_name)
    query = f"SELECT _conds, _tempm, _hum, _pressurem FROM {table_name} WHERE year={year} AND month={month}"
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data

def get_temperature_stats(db_name='weather_data.db', table_name='delhi_weather', year=None):
    conn = sqlite3.connect(db_name)
    query = f"SELECT month, MAX(_tempm) as max_temp, AVG(_tempm) as avg_temp, MIN(_tempm) as min_temp FROM {table_name} WHERE year={year} GROUP BY month"
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data
def get_direction(db_name='weather_data.db', table_name='delhi_weather'):
    conn=sqlite3.connect(db_name)
    query=f"select _wdire from {table_name} group by _wdire order by count(*) desc limit 1"
    data=pd.read_sql_query(query,conn)
    conn.close()
    return data




