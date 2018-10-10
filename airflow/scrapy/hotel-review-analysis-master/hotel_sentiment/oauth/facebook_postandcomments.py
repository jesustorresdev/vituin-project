import requests
import os
import unicodecsv as csv
from functions_facebook_posts import getPosts


params = {'access_token': \
'EAAaAhTnkdXgBAC40WERZA8cXeGj0fLVpsiTDiwNUVN79VHlTXN2bL8phFgEHrL0BuqLVGMjBsRBlZAc9ORphkvlBccIXtMZAP8F0pkPgciSSRAS0AsNJKGpNMolss4i5Q2bsZALZALihanQ7eNAeffAvh0FXwcUAacVifvqohboAZAVXKxNpPOLtwG8hXDeqKiDOs1UPunXAZDZD'
}

page_url = 'https://graph.facebook.com/v2.10/VisitPuertodelaCruz/feed'
#page_url = 'https://graph.facebook.com/v2.10/910220492463934/feed'

result = requests.get(page_url, params = params)
data = result.json()
print 'data-->',data

#Fields where data will be write
posts_files='posts19_09.csv'
comments_files='comments19_09.csv'
hashtags_files='hashtags19_09.csv'
CSVdir='/usr/local/airflow/scrapy-hotels/hotel-review-analysis-master/classify_elastic'
posts_files = os.path.join(CSVdir, posts_files)
comments_files = os.path.join(CSVdir, comments_files)
hashtags_files = os.path.join(CSVdir, hashtags_files)


#Arrays will be save the dada
samples_posts=[]
samples_posts.append(["id", "message", "story", "comments", "shares","likes","loves","wows","hahas","sads","angries","thankfuls","prides", "key", "creation_time", "extraction_time", "exist_now"])

samples_comments=[]
samples_comments.append(["id", "message","likes","loves","wows","hahas","sads","angries","thankfuls","prides", "key", "creation_time", "extraction_time", "parent", "exist_now"])

samples_hashtags=[]
samples_hashtags.append(["hashtag", "parent", "social_network", "type_parent", "key", "creation_time", "extraction_time","number_hashtag", "number_total_this_hashtag_in_message"])

index_posts=1
index_comments=1
index_hashtags=1

comments = True
posts_comments = {}

posts_comments["index_posts"] = index_posts
posts_comments["samples_posts"] = samples_posts
posts_comments["index_comments"] = index_comments
posts_comments["samples_comments"] = samples_comments
posts_comments["index_hashtags"] = index_hashtags
posts_comments["samples_hashtags"] = samples_hashtags

#Number of days that it will be get
days = 100

#We call to the def in facebook_posts
dic_result = getPosts(data,comments, posts_comments, days)

index_posts = dic_result["index_posts"]
samples_posts = dic_result["samples_posts"]
index_comments = dic_result["index_comments"]
samples_comments = dic_result["samples_comments"]
index_hashtags = dic_result["index_hashtags"]
samples_hashtags = dic_result["samples_hashtags"]


print('--------------')
print(samples_posts[0])
print('Write ' + str(index_posts-1) + ' posts')

print('--------------')
print(samples_comments[0])
print('Write ' + str(index_comments-1) + ' comments')

print('--------------')
print(samples_hashtags[0])
print('Write ' + str(index_hashtags-1) + ' hashtags')

#It writes the comments and posts files
with open(posts_files, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(samples_posts)

with open(comments_files, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(samples_comments)

with open(hashtags_files, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(samples_hashtags)


