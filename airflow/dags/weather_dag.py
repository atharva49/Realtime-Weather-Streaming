from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'weather_data_pipeline',
    default_args=default_args,
    description='A simple weather data pipeline',
    schedule_interval=timedelta(hours=1),
)

t1 = BashOperator(
    task_id='start_zookeeper',
    bash_command='~/kafka/bin/zookeeper-server-start.sh -daemon ~/kafka/config/zookeeper.properties',
    dag=dag,
)

t2 = BashOperator(
    task_id='start_kafka',
    bash_command='~/kafka/bin/kafka-server-start.sh -daemon ~/kafka/config/server.properties',
    dag=dag,
)

t3 = BashOperator(
    task_id='create_kafka_topics',
    bash_command='python ~/weather_data_pipeline/scripts/create_kafka_topics.py',
    dag=dag,
)

t4 = BashOperator(
    task_id='start_producer',
    bash_command='python ~/weather_data_pipeline/scripts/weather_producer.py',
    dag=dag,
)

t5 = BashOperator(
    task_id='start_consumer',
    bash_command='python ~/weather_data_pipeline/scripts/weather_consumer.py',
    dag=dag,
)

t1 >> t2 >> t3 >> t4 >> t5
