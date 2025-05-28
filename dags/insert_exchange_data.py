import json
import os
import psycopg2
from datetime import datetime

def insert_exchange_data():
    today = datetime.today().strftime('%Y-%m-%d')
    filename = f"/opt/airflow/data_{today}.json"
    print("Looking for file:", filename)
    print("File exists?", os.path.exists(filename))
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        return
    with open(filename, "r") as f:
        data = json.load(f)
    print("Loaded data keys:", data.keys())
    conn = psycopg2.connect(
        host='postgres',
        database='airflow',
        user='airflow',
        password='airflow'
    )
    cur = conn.cursor()
    base = data['base']
    date = data['date']
    rates = data['rates']
    for currency, rate in rates.items():
        cur.execute("""
            INSERT INTO exchange_rates (base, date, currency, rate)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (base, date, currency)
            DO UPDATE SET rate = EXCLUDED.rate;
        """, (base, date, currency, rate))
    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted successfully.")




