import requests
import os
import unicodecsv as csv
from facebook_posts import getPosts


params = {'access_token': \
'EAACEdEose0cBAGZCoXSQfuKRxaZAbOQNhNZBkMTXfcfm1hQnHuRcjZBQVXSyoKtqj0RJdVbI1Az74rrAnxBRleGHbWcMX1PioZCK4i1lvmHG97FG3AHaxUyd60vfO07b0dPSxDbdLxrY6yVZAnweBw9UpZCcy2PyQQhWp7aPDZA7S1qpy0QdTwAedyWfZBccmrf22Gn7ZC6AB2ZCAZDZD' \
}

page_url = 'https://graph.facebook.com/v2.10/VisitPuertodelaCruz/feed'
#page_url = 'https://graph.facebook.com/v2.10/910220492463934/feed'

result = requests.get(page_url, params = params)
data = result.json()


#Fields where data will be write
posts_files='posts.csv'
comments_files='comments.csv'
CSVdir='/usr/local/airflow/scrapy-hotels/hotel-review-analysis-master/classify_elastic'
posts_files = os.path.join(CSVdir, posts_files)
comments_files = os.path.join(CSVdir, comments_files)


#Arrays will be save the dada
samples_posts=[]
samples_posts.append(["id", "message", "story", "comments", "shares","likes","loves","wows","hahas","sads","angries","thankfuls","prides", "key", "creation_time", "extraction_time"])

samples_comments=[]
samples_comments.append(["id", "message","likes","loves","wows","hahas","sads","angries","thankfuls","prides", "key", "creation_time", "extraction_time" "parent"])

samples_hastags=[]
samples_hastags.append(["hastag", "parent", "social_network", "type_parent", "key", "creation_time", "extraction_time","number_hastag", "number_of_this_hastags_in_message"])

index_posts=1
index_comments=1
index_hastags=1

comments = True
posts_comments = {}

posts_comments["index_posts"] = index_posts
posts_comments["samples_posts"] = samples_posts
posts_comments["index_comments"] = index_comments
posts_comments["samples_comments"] = samples_comments

#Number of days that it will be get
days = 100

#We call to the def in facebook_posts
dic_result = getPosts(data,comments, posts_comments, days)

index_posts = dic_result["index_posts"]
samples_posts = dic_result["samples_posts"]
index_comments = dic_result["index_comments"]
samples_comments = dic_result["samples_comments"]



print('--------------')
print(samples_posts[0])
print('Write ' + str(index_posts-1) + ' posts')

print('--------------')
print(samples_comments[0])
print('Write ' + str(index_comments-1) + ' comments')

#It writes the comments and posts files
with open(posts_files, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(samples_posts)

with open(comments_files, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(samples_comments)


