import psycopg2

def create_exchange_rate_table():
    conn = psycopg2.connect(
        host='postgres',
        database='airflow',
        user='airflow',
        password='airflow'
    )
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS exchange_rates (
            base TEXT,
            date DATE,
            currency TEXT,
            rate NUMERIC
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Table check completed.")


