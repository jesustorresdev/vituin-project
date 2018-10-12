import unicodecsv as csv
import hashlib
import sys
from opinionTokenizer import tokenize_into_opinion_units
#import nltk
#nltk.download('punkt')

filename=sys.argv[1]
f = open(filename)
samples = [row for row in csv.reader(f)]
samples[0].append("key")
review_date_position=0
key_position=len(samples[0])-1

i=0
for field in samples[0]:
  if field=='review_date':
    review_date=i
  i=i+1

for i in range(1,len(samples)):
    key =  hashlib.md5(samples[i][review_date_position].encode('utf-8')).hexdigest()
    samples[i].append(key)


if (filename[:17]) == "unstructured_data": #If its a unstructured data
    filename=filename[18:]
    type='unstructured_data/'
else:
    filename=filename[16:]                 #If its a structured data
    type='structured_data/'
#write the reviews with the keys, this file will be used for indexing

with open(type + 'keys_' + filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerows(samples)

