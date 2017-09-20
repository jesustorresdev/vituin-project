import sys
import unicodecsv as csv
import json

from elasticsearch import Elasticsearch
from elasticsearch import helpers

#takes two arguments:
#   the name of the file to index
#   the starting index for the id
#       the ids shouldn't overlap or you will replace existing opinion units
#IMPORTANT: before indexing opinion units you must index the parent reviews

filename =  sys.argv[1]

#cont_id = int(sys.argv[2])



cont_id = int(1)
f = open(filename)
reference = ["review_date",
             "tittle",
             "reviewer_location",
             "score",
             "negative_content",
             "positive_content",
             "review_key"
            ]

es = Elasticsearch(['elasticsearch:9200'])

count = 0
actions = []


for row in csv.reader(f):

    if(chunk_count!=0):
        item = {}

    	for i in range(len(reference)):
        	item[reference[i]] = row[i]

        action = {
        	"_index": "index_hotels",
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

    	cont_id += 1

    count += 1

if count > 0:
	helpers.bulk(es, actions)
	print "leftovers"
	print "indexed %d" %cont_id

