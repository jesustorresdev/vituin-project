import sys
import unicodecsv as csv
from elasticsearch import Elasticsearch
from elasticsearch import helpers

#takes two arguments:
#   the name of the file to index
#   the starting index for the id
#       the ids shouldn't overlap or you will replace existing opinion units
#IMPORTANT: before indexing opinion units you must index the parent reviews

filename =  sys.argv[1]
#It return all hashtags of one message and its number in the message
def hashtags_of_message(res, id):

    hashtag=[]
    number_hashtag = []
    parent=[]
    for hit in res['hits']['hits']:
        element = hit
        if element["_source"]["parent"] == id:
            hashtag.append(element["_source"]["hashtag"])
            number_hashtag.append(element["_source"]["number_hashtag"])
            parent.append(element["_source"]["parent"])

    result = [{"parent" : parent, "hashtag":hashtag, "number_hashtag" : number_hashtag}]

    return  result

def delete_in_messages_visited(item, messages_visited):
    message_result = messages_visited

    for j in range(0,len(messages_visited)-1):
        for i in range(0,len(message)-1):
            if messages_visited[j]['parent'][i] == item['parent'] \
                and messages_visited[j]['hashtag'] == item['hashtag'] \
                and messages_visited[j]['number_hashtag'] == item['number_hashtag']:

                del message_result[j]



f = open(filename)
reference = ["hashtag",
             "parent",
             "social_network",
             "type_parent",
             "key",
             "creation_time",
             "extraction_time",
             "number_hashtag",
             "number_total_this_hashtag_in_message"
             ]

es = Elasticsearch(
    [
        'elasticsearch:9200/'
    ]
)

#Search the last indexed id
doc = {
    'size' : 10000,
    'query': {
        'match_all' : {}
    }
}
try:
    res = es.search(index='index_hashtags', body=doc, size=0)
    #The next element indexed going to be the next id doesn't used
    cont_id = int(res['hits']['total'])

except:
    #If it's the first gruop of elements indexed
    print("First indexed")
    cont_id = 0


count = 0
actions = []

messages_visited = []

for row in csv.reader(f):

    if(count!=0):
        item = {}

        for i in range(len(reference)):
            item[reference[i]] = row[i]

        if item['social_network'] == 'twitter':
            index = 'index_tweets'
        elif item['social_network'] == 'facebook':
            if item['type_parent'] == ['post']:
                index = 'index_facebook_post'
            elif item['type_parent'] == ['comment']:
                index = 'index_facebook_comment'
        elif item['social_network'] == 'instagram':
            if item['type_parent'] == 'photo':
                index = 'index_instagram_photo'
            elif item['type_parent'] == 'comment':
                index = 'index_instagram_comment'

        #ID parent in facebook
        parent = item['parent']
        res = es.search(index=index, body={
            "query": {
                "match_phrase": {
                    "parent": parent
                }
            }
        })

        #If exist in elastic this parent
        if res:
            #If it's the first hashtag for this message in the document
            if not parent in messages_visited:
                messages_visited.update(hashtags_of_message(res, parent))

        exist = False
        element = {}


        #ID parent in facebook
        key = item['key']
        res = es.search(index="index__hashtags", body={
            "query": {
                "match_phrase": {
                    "id_parent": key
                }
            }
        })

        #Exist hashtag with this key. It's not modified.
        for hit in res['hits']['hits']:
            exist = True
            element = hit

            #How hashtag exist, we going to delete this in the list
            delete_in_messages_visited(item,messages_visited)

        #If not exists in de index this element
        if not exist:

            action = {
                "_index": "index_hashtags",
                "_type": "posts",
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

    #Delete all hashtags in elastic that now it isn't exist because message was modified
    for message in messages_visited:
        for i in range(0, len(message['hashtag'])):
            es.delete_by_query(index='index_hashtags',doc_type='unstructured', q={'parent': message['parent'][i], 'hashtag':message['hashtag'][i], 'number_hashtag':message['number_hashtag'][i]})





