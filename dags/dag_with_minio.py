from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor



default_args = {
    'owner': 'vlad',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id="dag_with_minio_vladdybucket_v1a",
    start_date=datetime(2023, 4, 13),
    schedule_interval="@daily",
) as dag:
    task1 = S3KeySensor(
        task_id='sensor_minio_s3',
        bucket_name = 'vladdybucket',
        bucket_key = 'astronauts.csv',
        aws_conn_id = 'vlad_s3',
        mode = 'poke',
        poke_interval = 5,
        timeout = 30
    )
    task1