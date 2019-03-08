import requests
import os
import unicodecsv as csv
from functions_intsagram_photos import getPhotos


params = {'access_token': \
              'EAACEdEose0cBAGZCoXSQfuKRxaZAbOQNhNZBkMTXfcfm1hQnHuRcjZBQVXSyoKtqj0RJdVbI1Az74rrAnxBRleGHbWcMX1PioZCK4i1lvmHG97FG3AHaxUyd60vfO07b0dPSxDbdLxrY6yVZAnweBw9UpZCcy2PyQQhWp7aPDZA7S1qpy0QdTwAedyWfZBccmrf22Gn7ZC6AB2ZCAZDZD' \
          }

page_url = 'https://graph.facebook.com/v2.10/VisitPuertodelaCruz/feed'
#page_url = 'https://graph.facebook.com/v2.10/910220492463934/feed'

result = requests.get(page_url, params = params)
data = result.json()


#Fields where data will be write
photos_files='photosInstagram.csv'
comments_files='comments.csv'
hashtags_files='hashtagsInstagram.csv'
CSVdir='/usr/local/airflow/data_analysis/classify_elastic/unstructured_data/data_files'
photos_files = os.path.join(CSVdir, photos_files)
comments_files = os.path.join(CSVdir, comments_files)
hashtags_files = os.path.join(CSVdir, hashtags_files)


#Arrays will be save the dada
samples_photos=[]
samples_photos.append(["id", "message", "story", "comments", "shares","likes", "key", "creation_time", "extraction_time", "exist_now"])

samples_comments=[]
samples_comments.append(["id", "message","likes", "key", "creation_time", "extraction_time", "parent", "exist_now"])

samples_hashtags=[]
samples_hashtags.append(["hashtag", "parent", "social_network", "type_parent", "key", "creation_time", "extraction_time","number_hashtag", "number_total_this_hashtag_in_message"])

index_photos=1
index_comments=1
index_hashtags=1

comments = True
photos_comments = {}

photos_comments["index_posts"] = index_photos
photos_comments["samples_posts"] = samples_photos
photos_comments["index_comments"] = index_comments
photos_comments["samples_comments"] = samples_comments
photos_comments["index_hashtags"] = index_hashtags
photos_comments["samples_hashtags"] = samples_hashtags

#Number of days that it will be get
days = 100

#We call to the def in facebook_posts
dic_result = getPhotos(data,comments, photos_comments, days)

index_photos = dic_result["index_posts"]
samples_photos = dic_result["samples_posts"]
index_comments = dic_result["index_comments"]
samples_comments = dic_result["samples_comments"]
index_hashtags = dic_result["index_hashtags"]
samples_hashtags = dic_result["samples_hashtags"]


print('--------------')
print(samples_photos[0])
print('Write ' + str(index_photos-1) + ' posts')

print('--------------')
print(samples_comments[0])
print('Write ' + str(index_comments-1) + ' comments')

print('--------------')
print(samples_hashtags[0])
print('Write ' + str(index_hashtags-1) + ' hashtags')

#It writes the comments, photos and hashtags files
with open(photos_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples_photos)

with open(comments_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples_comments)


with open(hashtags_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples_hashtags)


