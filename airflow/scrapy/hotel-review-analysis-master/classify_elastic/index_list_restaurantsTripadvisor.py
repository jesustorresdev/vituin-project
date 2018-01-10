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

#cont_id = int(sys.argv[2])
place_type = ["PtoCruz", "Tenerife","Canarias"]
place = place_type[int(sys.argv[2])]


cont_id = int(1)
f = open(filename)
'''
reference = ["service",
	     "atmosphere",
             "name",
             "extended_address",
	     "food",
             "has_reviews",
             "locality_address",
	     "url",
         "ratingExcellent",
         "value",
         "phone",
         "ratingVeryGood",
         "score",
         "ratingAverage",
         "ratingTerrible",
         "price",
         "street_address",
         "ratingPoor",
             "key"
            ]
'''
es = Elasticsearch(
   [
     'elastic:vituinproject@elasticsearch:9200/',
   ]
)

count = 0
actions = []


for row in csv.reader(f):

    if(count!=0):
        item={}
        '''
        item = {
         "service":{ "type":"String"},
         "atmosphere":{ "type":float},
         "name":{ "type":"String"},
         "extended_address":{ "type":"String"},
         "food":{ "type":float},
         "has_reviews":{ "type":int},
         "locality_address":{ "type":"String"},
         "url":{ "type":"String"},
         "ratingExcellent":{ "type":int},
         "value":{ "type":float},
         "phone":{ "type":int},
         "ratingVeryGood":{ "type":int},
         "score":{ "type":float},
         "ratingAverage": { "type":"integer"},
         "ratingTerrible":{ "type":int},
         "price":{ "type":"String"},
         "street_address":{ "type":"String"},
         "ratingPoor":{ "type":int},
         "key":{ "type":"String"}

        }
        '''
        item['insert_time']=datetime.datetime.today()
        try:
            item['service']=float(row[0])#service
        except:
            item['service']=float(-1)
        try:
            item['atmosphere']=float(row[1])#atmosphere
        except:
            item['atmosphere']=float(-1)
        item['name']=row[2]#name
        item['extended']=row[3]#extended
        try:
            item['food']=float(row[4])#food
        except:
            item['food']=float(-1)        
        item['has_review']=int(row[5])#has_review
        item['locality']=row[6]#locality
        item['url']=row[7]#url
        item['ratingExcellent']=int(row[8])#ratingExcelent
        try:        
            item['value']=float(row[9])#value
        except:
            item['value']=float(-1)              
        item['phone']=row[10]#phone
        item['ratingVeryGood']=int(row[11])#ratingVeryGood
        item['score']=float(row[12])#score
        item['ratingAverage']=int(row[13])#ratingAverage
        item['ratingTerrible']=int(row[14])#ratingTerrible
        if row[15] == "":
            row[15]="None"
        item['price']=row[15]#price
        item['street_address']=row[16]#street_address
        item['ratingpoor']=int(row[17])#ratingpoor
        item['key']=str(row[18])#key
        item['place'] = 'Canarias'

        '''
        item['insert_time']=datetime.datetime.today()
        item[reference[0]]=row[0]#service
        item[reference[1]]=row[1]#atmosphere
        item[reference[2]]=row[2]#name
        item[reference[3]]=row[3]#extended
        item[reference[4]]=row[4]#food
        item[reference[5]]=row[5]#has_review
        item[reference[6]]=row[6]#locality
        item[reference[7]]=row[7]#url
        item['ratingExcellent']=int(3)#ratingExcelent
        item[reference[9]]=row[9]#value
        item[reference[10]]=row[10]#phone
        item[reference[11]]=int(row[11])#ratingVeryGood
        item[reference[12]]=row[12]#score
        item[reference[13]]=int(row[13])#ratingAverage
        item[reference[14]]=int(row[14])#ratingTerrible
        item[reference[15]]=row[15]#price
        item[reference[16]]=row[16]#street_address
        item[reference[17]]=int(row[17])#ratingpoor
        item[reference[18]]=row[18]#key
        '''

        '''
    	for i in range(len(reference)):
            item[reference[i]] = row[i]
            item['insert_time']=datetime.datetime.today()
            if item[reference[i]] == "":
                item[reference[i]] = -1
            try:
                item[reference[i]] = float(item[reference[i]])
                print(item[reference[i]])
                print(type(item[reference[i]]))
            except:
                pass
        '''        
	action = {
        	"_index": "index_establishments_tripadvisor",
                "_type": "restaurants_list",
            	#"_id": cont_id,
           	"_source": item
            	}

	actions.append(action)
    	cont_id += 1
        
    count += 1

if count > 0:
	helpers.bulk(es, actions)
	print "leftovers"
	print "indexed %d" %cont_id


