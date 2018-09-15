import unicodecsv as csv
import sys
from opinionTokenizer import tokenize_into_opinion_units
#import nltk
#nltk.download('punkt')

filename=sys.argv[1]
f = open(filename)
samples = [row for row in csv.reader(f)]
samples[0].extend(["n_people", "rooms", "beds", "bathrooms"])
details_position=0

i=0
for field in samples[0]:
  if field=='details_str':
      details_position=i
  i=i+1

samples[0].remove('details_str')

for i in range(1,len(samples)):
    details =  samples[i][details_position]

    elements=details.split(',')
    n_people=elements[0].strip()
    rooms=elements[1].strip()
    beds=elements[2].strip()
    bathrooms=elements[3].strip()

    samples[i].extend([n_people, rooms, beds, bathrooms])
    samples[i].remove(details)

if (filename[:17]) == "unstructured_data": #If its a unstructured data
    filename=filename[18:]
    type='unstructured_data/'
else:
    filename=filename[16:]                 #If its a structured data
    type='structured_data/'
#write the reviews with the keys, this file will be used for indexing

with open(type + 'separate_' + filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerows(samples)

