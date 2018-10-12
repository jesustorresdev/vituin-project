from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
import os

# Following are defaults which can be overridden later on
default_args = {
    'owner': 'lalit.bhatt',
    'depends_on_past': False,
    'start_date': datetime(2017, 8, 5),
    'email': ['lalit.bhatt@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    #'retries': 1,
    #'retry_delay': timedelta(minutes=1),
}

start_date = datetime.combine(datetime.today(),datetime.min.time())
date= datetime.today()

dag = DAG('scrapy', default_args=default_args,schedule_interval="@weekly")

def call_booking():
    os.system('cd /usr/local/data_analysis/classify_elastic &&  scrapy crawl booking -o itemsBooking.csv')

def call_tripadvisor():
    os.system('cd /usr/local/data_analysis/classify_elastic && scrapy crawl tripadvisor -o itemsTripadvisor.csv -s CLOSESPIDER_ITEMCOUNT=1500')

def send_booking():
    os.system('cd /usr/local/data_analysis/classify_elastic && python generate_files_for_indexing.py && python index_opinion_units.py')

def send_tripadvisor():
    os.system('cd /usr/local/data_analysis/classify_elastic && python generate_files_for_indexing.py && python index_opinion_units.py')



t1 = PythonOperator(
    task_id='Booking',
    python_callable=call_booking,
    dag=dag)

t2 = PythonOperator(
    task_id='Tripadvisor',
    python_callable=call_tripadvisor,
    dag=dag)

t3 = PythonOperator(
    task_id='sendBooking',
    python_callable=send_booking,
    dag=dag)

t4 = PythonOperator(
    task_id='sendTripadvisor',
    python_callable=send_tripadvisor,
    dag=dag)



t3.set_upstream(t1)
t4.set_upstream(t2)
