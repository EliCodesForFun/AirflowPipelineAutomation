from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args ={
    'owner': 'vlad',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id="our_first_dag_V3",
    default_args = default_args,
    description="This is our first dag that we write",
    start_date=datetime(2023, 4, 14),
    schedule_interval="@daily",
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo "Hello World, this is the first task"'
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo "I am the second task! Hello World, this is the second task"'
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo "I am the task 3. I\'ll be running at the same time as task 2"'
    )

    task1.set_downstream(task2)
    task1.set_downstream(task3)
