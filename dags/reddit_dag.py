from datetime import datetime
from airflow import DAG
import os
import sys
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pipelines.reddit_pipeline import reddit_pipeline



default_args = {
    "owner":"dp",
    "start_date": datetime(2025,1,1)
}

file_postfix = datetime.now().strftime("%Y%m%d")

# la deuxième manière de declarer un dag selon la bibliothèque
dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['redit','etl','pipeline'])
    

#extraction from reddit: c'est un workflow
extract  =  PythonOperator(
    task_id = "reddit_extraction",
    python_callable = reddit_pipeline,
    op_kwargs={
        "file_name":f'reddit_{file_postfix}', #la sortie
        "subreddit":'dataengineering',
        "time_filter":'day',
        'limit':100
    },
    dag=dag
)










#upload to S3