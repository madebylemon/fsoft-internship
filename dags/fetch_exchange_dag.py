from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from fetch_exchange_rate import fetch_exchange_rate
from create_table import create_exchange_rate_table
from insert_exchange_data import insert_exchange_data

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}
with DAG(
    dag_id='exchange_rate_fetch_dag',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['exchange', 'api']
) as dag:
    task1 = PythonOperator(
        task_id='fetch_exchange_data',
        python_callable=fetch_exchange_rate
    )
    task2 = PythonOperator(
        task_id='create_exchange_rate_table',
        python_callable=create_exchange_rate_table
    )
    task3 = PythonOperator(
        task_id='insert_exchange_data',
        python_callable=insert_exchange_data
    )
    task1 >> task2 >> task3 


