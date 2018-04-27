from elasticsearch import Elasticsearch
from elasticsearch import helpers
import datetime
import hashlib


def hastag(message, id_parent, social_network, type_parent, creation_time):
    samples_hastags=[]
    words = []
    message = message.lower()                          #we transform to lower letters

    #Get all hastags words
    for word in message.split(' '):
        if word[:1] == "#":
            words.append(word[1:])

    number_hastag = {}                                 #If there are a hastag duplicated in the message we put the number (by order of founded)
    repeat_hastags = repeatHastagInMessage(words)      #Search hastags repeat in the message

    #For to all hastags words
    for i in range(0,words):
        extraction_time = datetime.datetime.today()
        number_of_this_hastags_in_message = 1          #If there are a hastag duplicated in the message we put the number in total


        if word in repeat_hastags:                     #if this word is repeat we change the number of this hastags in the message
            number_of_this_hastags_in_message = len(repeat_hastags[word])

        if not word in number_hastag:                 #If it's the first time to this hastag is in the words create the key in number_hastag
            number_hastag.update({word : 0})
        else:
            number_hastag[word] += 1


        str_key = str(id_parent) + str(creation_time) + word + number_hastag[word]
        key = hashlib.md5(str_key.encode('utf-8')).hexdigest()

        samples_hastags.append([word[1:], id_parent, social_network, type_parent, key, creation_time, extraction_time, number_hastag[word], number_of_this_hastags_in_message])

    return samples_hastags

def repeatHastagInMessage(words):
    repeat_hastags = {}
    for i in range(0,len(words)):
        for j in range(i+1,len(words)):
            if words[i] == words[j]:
                if words[i] in repeat_hastags:
                    repeat_hastags[words[i]].append(j)
                    print words[i]                                      #second or more than this world have been matched
                    break                                               #break this iteration

                else:
                    repeat_hastags.update({words[i]:[]})
                    repeat_hastags[words[i]]= [i,j]
                    print words[i]                                      #first than this world have been matched
                    break                                               #break this iteration

    return repeat_hastags
#
# def deleteHastags(id_parent, name_index):
#     es = Elasticsearch(
#         [
#             'elasticsearch:9200/'
#         ]
#     )
#
#     res = es.search(index=name_index, body={
#         "query": {
#             "match_phrase": {
#                 "id": id
#             }
#         }
#     })
#
#     for hit in res['hits']['hits']:
#         hit["_source"]["id"]