import sys
import unicodecsv as csv
import json
import datetime

from elasticsearch import Elasticsearch
from elasticsearch import helpers

#takes two arguments:
#   the name of the file to index
#   the starting index for the id
#       the ids shouldn't overlap or you will replace existing opinion units
#IMPORTANT: before indexing opinion units you must index the parent reviews

filename =  sys.argv[1]

f = open(filename)
reference = ["review_date",
             "tittle",
             "reviewer_location",
	     "hotel_address",
             "score",
             "negative_content",
             "hotel_score",
             "positive_content",
	     "hotel_name",
             "review_key"
            ]

es = Elasticsearch(
   [
     'elasticsearch:9200/'
   ]
)

count = 0
actions = []

#Search the last indexed id
doc = {
        'size' : 10000,
        'query': {
             'match_all' : {}
         }
       }
try:
    res = es.search(index='index_booking_hotels_reviews', body=doc, size=0)
    #The next element indexed going to be the next id doesn't used
    cont_id = int(res['hits']['total'])

except:
    #If it's the first gruop of elements indexed
    print("First indexed")
    cont_id = 0


now = datetime.datetime.today()

for row in csv.reader(f):

    if(count!=0):
        item = {}

    	for i in range(len(reference)):
        	item[reference[i]] = row[i]
		#transformar el string de la fecha a formato datetime
                if reference[i] == "review_date":
                        item[reference[i]]=datetime.datetime.strptime(row[i], "%Y-%m-%d %H:%M:%S")
        action = {
        	"_index": "index_booking_hotels_reviews",
                "_type": "reviews",
            	"_id": cont_id,
           	"_source": item
            	}


        if item['review_date'] ==  now.day - 7:
                key = item['key']
                #busqueda de una entrada igual
                res = es.search(index="index_booking_hotels_reviews", body={
                        "query": {
                                "match_phrase": {
                                        "review_key": key
                                        }
                                }
                        })
                exist = '0'
                for hit in res['hits']['hits']:
                        exist = hit["_source"]

                if exist == '0':

                        actions.append(action)
        else:
	        actions.append(action)

    	cont_id += 1

    count += 1

if count > 0:
	helpers.bulk(es, actions)
	print "leftovers"
	print "indexed %d" %cont_id

