import requests
import os
import unicodecsv as csv
from pruebaSelFacebook import get_data_Facebook



#Fields where data will be write
posts_files='posts_facebook_all.csv'
comments_files='comments.csv'
CSVdir=''
posts_files = os.path.join(CSVdir, posts_files)
comments_files = os.path.join(CSVdir, comments_files)


#Arrays will be save the dada
samples_posts=[]
samples_posts.append(["url","creation_time","year","month","day","extraction_time"])

index_posts=1

comments = True
posts_comments = {}

posts_comments["index_posts"] = index_posts
posts_comments["samples_posts"] = samples_posts


#Number of days that it will be get
days = 500
dict_result = get_data_Facebook(days, posts_comments)

ex_posts = dict_result["index_posts"]
samples_posts = dict_result["samples_posts"]


print('--------------')
print(samples_posts[0])
print('Write ' + str(index_posts-1) + ' posts')

#It writes the comments and posts files
with open(posts_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples_posts)



