import unicodecsv as csv
import sys
from googlemaps import Client as GoogleMaps

from opinionTokenizer import tokenize_into_opinion_units
#import nltk

filename=sys.argv[1]
f = open(filename)
samples = [row for row in csv.reader(f)]
samples[0].append("lat")
samples[0].append("lng")
review_date_position=0
# key_position=len(samples[0])-1

coordinates_fields = sys.argv[2]
for i in range(1,len(samples)):

    coordinates={'name':[],'lat':[],'lng':[]}

    place = ''
    for j in range(0,len(samples[0])):
        if samples[0][j] in coordinates_fields:
            place += str(samples[i][j].encode('UTF-8'))                   #The place searched is the composed to the fields to get the coordinates
            place += ' '

    api_key = 'AIzaSyD2owaTzJTWi9m1f2QqAlJ1S0hfFT3nT0w'
    gmaps = GoogleMaps(api_key)
    # print 'gmaps'
    location = gmaps.geocode(place)
    # print 'location'
    print 'i-->', i
    try:
        if 'location' in location[0]['geometry']:
            lat=location[0]['geometry']['location']['lat']
            lng=location[0]['geometry']['location']['lng']
            # print 'Exacto', lat, lng
        else:  #if it's a aproximation
            lat = location[0]['geometry']['bounds']['northeast']['lat'] + location[0]['geometry']['bounds']['southwest']['lat']
            lng = location[0]['geometry']['bounds']['northeast']['lng'] + location[0]['geometry']['bounds']['southwest']['lng']
            # print 'Aproximado', lat, lng
    except:
        print 'algo mal'
        pass


    samples[i].extend([lat,lng])

if (filename[:17]) == "unstructured_data": #If its a unstructured data
    filename=filename[18:]
    type='unstructured_data/'
else:
    filename=filename[16:]                 #If its a structured data
    type='structured_data/'
#write the reviews with the keys, this file will be used for indexing
with open(type + 'coordinates_' + filename, 'wb') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerows(samples)

