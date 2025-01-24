from airflow import DAG # type: ignore
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator


default_args = {
    'owner' : 'ikrar',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=2) 
}

with DAG(
    dag_id ='testing_first_dag',
    default_args = default_args,
    description='This is first DAG testing',
    start_date=datetime(2025,1,19,13),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='testing_first_task',
        bash_command='Testing first task'
    )
    task1