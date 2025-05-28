import psycopg2
import csv
def export_to_csv():
    conn = psycopg2.connect(
        host="localhost", 
        port="5432",
        database="airflow",
        user="airflow",
        password="airflow"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM exchange_rates")

    rows = cur.fetchall()
    with open("exchange_rates_export.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["base", "date", "currency", "rate"])  
        writer.writerows(rows)
    cur.close()
    conn.close()
    print("CSV exported: exchange_rates_export.csv")
export_to_csv()
