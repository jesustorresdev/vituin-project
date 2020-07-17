from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
import os

# Following are defaults which can be overridden later on
default_args = {
    'owner': 'lalit.bhatt',
    'depends_on_past': False,
    'start_date': datetime.today(),
    'email': ['lalit.bhatt@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    #'retries': 1,
    #'retry_delay': timedelta(minutes=1),
}

start_date = datetime.combine(datetime.today(),datetime.min.time())
date= datetime.today()
papa="gfjyktkiyiot"

dag = DAG('tutorial2', default_args=default_args,schedule_interval=timedelta(minutes=1))
'''
def my_python_call_booking():
    os.system('cd /home/sergio/Escritorio/pruebaDocker/hotel-review-analysis-master-MODIFICADO && scrapy crawl booking -o itemsBooking3.csv')


# t1, t2, t3 and t4 are examples of tasks created using operators

t1 = PythonOperator(
    task_id='Booking',
    python_callable=my_python_call_booking,
    dag=dag)
'''
#t1 = BashOperator(
#    task_id='task_1',
#    bash_command='scrapy crawl /home/sergio/Escritorio/pruebaDocker/hotel-review-analysis-master/booking -o itemsBooking.csv',
#    dag=dag)

t2 = BashOperator(
    task_id='prueba',
    bash_command='echo ' + str(date),
    dag=dag)

t3 = BashOperator(
    task_id='task_3',
    bash_command='echo "Hello World from Task 3"',
    dag=dag)

t4 = BashOperator(
    task_id='task_4',
    bash_command='echo "Hello World form Task 4"',
    dag=dag)



#t2.set_upstream(t1)
#t3.set_upstream(t1)
t4.set_upstream(t2)
t4.set_upstream(t3)


