import requests
import os
import unicodecsv as csv
from requests_oauthlib import OAuth1
from functions_twitter import get_tweets_items, extract_tweets_from_dict


###parameters according to Twitter API
consumer_key = 'KUFD92Au2nr2MdoqTjJZIlC6A'
consumer_secret = 'VzDQh4NpzyME30t5diuMIuWnPXTZgZnx2CVj2PDqotc4sDub82'
access_token = '448386715-4wJO6W9Y5miuSIhDxZaNp2WSx4fw2z1y3r3Dwltf'
access_token_secret = 'ZWRu9aCDM2C3RZUyCZ5AAE26F2SNi7R84FM0PhN1EIDsB'

auth = OAuth1(consumer_key, consumer_secret, access_token,
              access_token_secret)

user = 'SerDiaz_'

#Fields where data will be write
# tweets_files='tweets_'+user+'.csv'
# CSVdir='/usr/local/airflow/scrapy-hotels/hotel-review-analysis-master/classify_elastic'
# tweets_files = os.path.join(CSVdir, tweets_files)
#
# hashtags_files='hashtags_'+user+'.csv'
# CSVdir='/usr/local/airflow/scrapy-hotels/hotel-review-analysis-master/classify_elastic'
# hashtags_files = os.path.join(CSVdir, hashtags_files)

#Arrays will be save the dada
sample_tweets=[]
sample_tweets.extend([["id", "text", "user_searched", "replies", "retweets","favorites","parent", "creation_time", "extraction_time"]])


sample_hashtags=[]
sample_hashtags.extend(["hashtag", "parent", "social_network", "type_parent", "key", "creation_time", "extraction_time","number_hashtag", "number_total_this_hashtag_in_message"])

index_tweets=1
index_hashtags=1

comments = True
tweets = {}
words = ['Puerto de la Cruz', 'Pto de la Cruz', 'Pto Cruz', 'Puerto Cruz','Jardín Botanico', 'Mueca', 'Tenerife']

tweets["index_tweets"] = index_tweets
tweets["sample_tweets"] = sample_tweets
tweets["index_hashtags"] = index_hashtags
tweets["sample_hashtags"] = sample_hashtags

#Number of days that it will be get
days = 100

#We call to the def in facebook_posts
dic_result = extract_tweets_from_dict(tweets, words, auth, days)
import sys

index_tweets = dic_result["index_tweets"]
sample_tweets = dic_result["sample_tweets"]
index_hashtags = dic_result["index_tweets"]
sample_hashtags = dic_result["sample_tweets"]

print('--------------')
print(sample_tweets[0])
print('Write ' + str(index_tweets-1) + ' tweets')

print('--------------')
print(sample_hashtags[0])
print('Write ' + str(index_hashtags-1) + ' hashtags')

#It writes the comments and posts files
# with open(tweets_files, 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(samples_posts)
#
# with open(hashtags_files, 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(samples_hashtags)



