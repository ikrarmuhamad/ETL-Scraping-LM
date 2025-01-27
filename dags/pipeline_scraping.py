from airflow import DAG # type: ignore
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from scraping_lm import scraping_etl


default_args = {
    'owner' : 'ikrar',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=2) 
}

with DAG(
    dag_id ='testing_scraping_etl',
    default_args = default_args,
    description='First ETL Scraping',
    start_date=datetime(2025,1,25,21),
    schedule_interval='@daily'
) as dag:
    task_1 = PythonOperator(
        task_id='testing_scraping',
        python_callable=scraping_etl
    )
    task_1