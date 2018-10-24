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
place_type = ["Puerto de la Cruz", "Tenerife","Canarias", "Fuerteventura"]
place = place_type[int(sys.argv[2])]

f = open(filename)
reference = ["value_for_money_rating",
             "facilities_rating",
             "comfort_rating",
             "lat",
             "review_count",
             "staff_rating",
             "price_min",
             "type_establishment",
             "score",
             "id_booking",
             "stars",
             "postalCode",
             "cleanliness_rating",
             "location_rating",
             "description",
             "phone",
             "wifi_rating",
             "address",
             "lng",
             "name",
             "url",
             "region"
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
res = []
try:
    res = es.search(index='index_list_homes_booking', body=doc, size=0)
    #The next element indexed going to be the next id doesn't used
    cont_id = int(res['hits']['total'])

except:
    #If it's the first gruop of elements indexed
    print("First indexed")
    cont_id = 0


for row in csv.reader(f):

    if(count!=0):
        item = {}

        for i in range(len(reference)):
            item[reference[i]] = row[i]


        item['upload_date']=datetime.datetime.today()
        item['place']=place

        if not res or res['hits']['hits'] == []: #If there isn't result

            action = {
                "_index": "index_list_homes_booking",
                "_type": "unstructured",
                "_id": cont_id,
                "_source": item
            }

            actions.append(action)

            cont_id += 1
        else:
            print 'repeat ', count
            same = False
            for element in res['hits']['hits']['_source']:
                if item[element] == res['hits']['hits']['_source'][element]:
                    same = True

            if same is False:

                action = {
                    "_index": "index_list_homes_booking",
                    "_type": "unstructured",
                    "_id": cont_id,
                    "_source": item
                }

                actions.append(action)

                cont_id += 1




    count += 1

if count > 0:
    helpers.bulk(es, actions)
    print "leftovers"
    print "indexed %d" %cont_id

