from instagram.client import InstagramAPI
import requests

APP_ACCESS_TOKEN = '204978804.e02fa55.a655274324e943b9878a789779dbf22e'
BASE_URL = 'https://api.instagram.com/v1/'
access_token = '204978804.e02fa55.a655274324e943b9878a789779dbf22e'

api = InstagramAPI(client_secret='e02fa55f30c741238a06d04a5fd2a16d', access_token = access_token)
#usr = api.user_search('sergiodiaz93')

#print usr

request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
print 'GET request url : %s' % (request_url)
user_info = requests.get(request_url).json()

print user_info
# https://api.instagram.com/v1/tags/nofilter/media/recent?access_token=204978804.e02fa55.a655274324e943b9878a789779dbf22e


# https://api.instagram.com/v1/media/search?lat=48.858844&lng=2.294351&access_token=204978804.e02fa55.a655274324e943b9878a789779dbf22e

# https://notes.acadview.com/?program=backend&class=insta-1#/44

# https://api.instagram.com/v1/media/search?lat=48.858844&lng=2.294351&access_token=ACCESS-TOKEN
