import sys
import unicodecsv as csv
import json
import datetime

from elasticsearch import Elasticsearch
from elasticsearch import helpers

#filename = "classified_opinion_units_keys_tripadvisor_bangkok.csv"
#takes two arguments:
#   the name of the file to index
#   the starting index for the id
#       the ids shouldn't overlap or you will replace existing opinion units
#IMPORTANT: before indexing opinion units you must index the parent reviews

#filename =  sys.argv[1]
filename = "keys_itemsBooking.csv"

#cont_id = int(sys.argv[2])



cont_id = int(1)
f = open(filename)
reference = ["review_key",
             "content",
             "sentiment",
             "sent_probability",
             "topic"
            ]

es = Elasticsearch(['http://localhost:9200'])
#index by chunk of 10000 items
chunk_count = 0
actions = []
now = datetime.datetime.combine(datetime.datetime.today(), datetime.time(0, 0))
#es = Elasticsearch()

for row in csv.reader(f):
    item = {}
    
    for i in range(len(reference)):
        item[reference[i]] = row[i]
    action = {
            "_index": "index_hotels_4",
            "_type": "opinion_unit",
            "_id": cont_id,
            "_source": item
            }
    '''
    if item['review_date'] ==  now - 7:
      key = item['key'] 
      res = es.search(index="index_hotels_4", q="review_key:"+key)
      if !res
        actions.append(action)
    else:
      actions.append(action)
    '''  

    actions.append(action)

    chunk_count += 1

    cont_id += 1

#if chunk_count > 0:
helpers.bulk(es, actions)

print "leftovers"
print "indexed %d" %cont_id
'''

es = Elasticsearch(['http://localhost:9200'])

actions = [
  {
    "_index": "tickets-index2",
    "_type": "tickets",
    "_id": j,
    "_source": {
        "any":"data" + str(j),
        "timestamp": "datetime.now()"}
  }
  for j in range(0, 10)
]

helpers.bulk(es, actions)
'''
