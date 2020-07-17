import airflow
from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
import os

# Following are defaults which can be overridden later on
# default_args = {
#     'owner': 'lalit.bhatt',
#     'depends_on_past': False,
#     'start_date': datetime.today(),
#     'email': ['lalit.bhatt@gmail.com'],
#     'email_on_failure': False,
#     'email_on_retry': False,
#     #'retries': 1,
#     'schedule_interval': timedelta(minutes=1),
#     'retry_delay': timedelta(minutes=1),
# }

date = datetime.strptime('14 Jan 2019', '%d %b %Y')
date = date.replace(hour=14, minute=05)
# date = datetime.today()
default_args = {
        'owner': 'vituin',
        'email': ['vituin@gmail.com'],
}

# dag = DAG('probando', default_args=default_args,schedule_interval=timedelta(minutes=1))

dag = DAG(
    dag_id='probando',
    default_args=default_args,
    schedule_interval=timedelta(minutes=1),
    start_date= date
)

# def my_python_call_listHotels():
#     os.system('cd /home/sergio/Escritorio/pruebaDocker/hotel-review-analysis-master-MODIFICADO && scrapy crawl tripadvisor_listHotels -o pruebaAIRFLOW.csv')
#
#
# # t1, t2, t3 and t4 are examples of tasks created using operators
#
# t1 = PythonOperator(
#     task_id='list Tripadvisor',
#     python_callable=my_python_call_listHotels,
#     dag=dag)

#t1 = BashOperator(
#    task_id='task_1',
#    bash_command='scrapy crawl /home/sergio/Escritorio/pruebaDocker/hotel-review-analysis-master/booking -o itemsBooking.csv',
#    dag=dag)

templated_command = """
    echo "Empieza"
    python /usr/local/airflow/dags/a.py
    cd /usr/local/airflow/data_analysis/classify_elastic/unstructured_data/data_files
    ls
    scrapy crawl tripadvisor_listHotels -o pruebaAIRFLOW.csv
"""
# t3 = BashOperator(
#     task_id='templated',
#     bash_command=templated_command,
#     dag=dag)
#

t2 = BashOperator(
    task_id='prueba',
    bash_command=templated_command,
    dag=dag)



# templated_command = """
#     echo "Empieza"
#     python /usr/local/airflow/dags/a.py
# """
#
# t4 = BashOperator(
#     task_id='task_4',
#     bash_command='echo "Hello World form Task 4"',
#     dag=dag)
#
#
# #t2.set_upstream(t1)
# #t3.set_upstream(t1)
# t4.set_upstream(t2)
# t4.set_upstream(t3)


