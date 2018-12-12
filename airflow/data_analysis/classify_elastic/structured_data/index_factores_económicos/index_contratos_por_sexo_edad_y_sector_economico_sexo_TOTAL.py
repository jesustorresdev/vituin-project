# -*- coding: utf-8 -*-
import datetime

from elasticsearch import Elasticsearch
from elasticsearch import helpers
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import utils

ES = Elasticsearch(
    [
        'elasticsearch:9200/'
    ]
)

FILE_COUNT = 0
ACTIONS = []

ELASTICSEARCH_INDEX='index_contratos_sexo_edad_sector'
ELASTICSEARCH_DOC_TYPE='structured'


#Search the last indexed id
doc = {
    'query': {
        'match_all' : {}
    }
}

i = 0
try:
    res = ES.search(index=ELASTICSEARCH_INDEX, body=doc, size=0)
    #The next element indexed going to be the next id doesn't used
    cont_id = int(res['hits']['total'])


    genders = {'Mujeres':'Hombres', 'Hombres':'Mujeres'}
    for gen in genders:

        must = {
            "must":[
                {"term":{"gender": gen}},
            ]
        }
        res = utils.search_elastic(ELASTICSEARCH_INDEX,ELASTICSEARCH_DOC_TYPE, must = must)

        for item in res:
            print(i)
            i+=1
            item = item['_source']
            #It is going to return one only item
            res_other = ES.search(index=ELASTICSEARCH_INDEX, body={
                "query": {
                    "bool": {
                        "must":[
                            {"term":{"month": item['month']}},
                            {"term":{"age": item['age']}},
                            {"term":{"place": item['place']}},
                            {"term":{"type": item['type']}},
                            {"term":{"sector": item['sector']}},
                            {"term":{"year": item['year']}},
                            {"term":{"gender": genders[gen]}},
                        ]
                    }
                }
            })
            new_item = item.copy()
            new_item['gender'] = 'TOTAL'
            try:
                new_item['value'] += res_other['hits']['hits'][0]['_source']['value']
            except:
                pass
            new_item['insert_time']=datetime.datetime.today()
            new_item['item_creation']='Añadido'.decode('UTF-8')
            res_total ={}
            try:
                #It is going to return one only item if it exists
                res_total = ES.search(index=ELASTICSEARCH_INDEX, body={
                    "query": {
                        "bool": {
                            "must":[
                                {"term":{"month": new_item['month']}},
                                {"term":{"age": new_item['age']}},
                                {"term":{"place": new_item['place']}},
                                {"term":{"type": new_item['type']}},
                                {"term":{"sector": new_item['sector']}},
                                {"term":{"year": new_item['year']}},
                                {"term":{"gender": new_item['gender']}},
                            ]
                        }
                    }
                })
            except:
                pass

            if not res_total or res_total['hits']['hits'] == []: #If there isn't result
                action = {
                    "_index": ELASTICSEARCH_INDEX,
                    "_type": ELASTICSEARCH_DOC_TYPE,
                    "_id": cont_id,
                    "_source": new_item
                }
                ACTIONS.append(action)
                FILE_COUNT +=1
                cont_id +=1
except Exception as error:
    print 'Error', error, ', en', FILE_COUNT
    print 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
    print '------'
    #If it's the first gruop of elements indexed
    print("No exist index")

if FILE_COUNT > 0:
    helpers.bulk(ES, ACTIONS)
    print "leftovers"
    print "indexed", str(cont_id), ",", ELASTICSEARCH_INDEX
else:
    print 'Not indexed'

