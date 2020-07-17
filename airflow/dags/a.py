from datetime import datetime
import unicodecsv as csv
import os

date = datetime.today()
print '---'
print 'Se ha ejecutado esto el', str(date.day), 'del', str(date.month), 'de', str(date.year), 'a las', str(date.hour)+':'+str(date.minute)+':'+str(date.second)
print '---'

#Fields where data will be write
airbnb_files='hora.csv'
CSVdir='/usr/local/airflow/dags'
airbnb_files = os.path.join(CSVdir, airbnb_files)
#It writes the comments and posts files
message = [['Se ha ejecutado esto el '+ str(date.day)+ ' del '+ str(date.month)+ ' de '+ str(date.year)+ ' a las '+ str(date.hour)+':'+str(date.minute)+':'+str(date.second)]]
print message
with open(airbnb_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(message)