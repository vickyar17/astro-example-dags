from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG(dag_id="hello_world_dag",
         start_date=datetime(2021,1,1),
         schedule=None,
         catchup=False) as dag:
         task1 = PythonOperator(
            task_id="hello_world",
            python_callable=helloWorld)
task1
