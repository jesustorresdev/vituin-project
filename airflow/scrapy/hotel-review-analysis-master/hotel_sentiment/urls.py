# -*- coding: utf-8 -*-

# Here, it is define the urls where scrapy will go to work


def TripAdvisorHotelsURLs():
    urls = [
        "https://www.tripadvisor.co.uk/Hotel_Review-g1064199-d585324-Reviews-The_Ritz_Carlton_Abama-Guia_de_Isora_Tenerife_Canary_Islands.html",
        "https://www.tripadvisor.co.uk/Hotel_Review-g187482-d1555517-Reviews-IBEROSTAR_Grand_Hotel_Mencey-Santa_Cruz_de_Tenerife_Tenerife_Canary_Islands.html"
    ]
    return urls

def TripAdvisorZoneURLs():
    urls = [
        "https://www.tripadvisor.co.uk/Hotels-g187479-Tenerife_Canary_Islands-Hotels.html"
    ]

    return urls

def BookingHotelsURLs():
    urls = [ ]

    return urls

def BookingZoneURLs():
    urls = [
	"https://www.booking.com/searchresults.en-gb.html?aid=356984;label=gog235jc-country-en-gb-gb-unspec-es-com-L%3Aen-O%3Ax11-B%3Achrome-N%3Ayes-S%3Abo-U%3Ac-H%3As;sid=3d9a779adf10f3e6b7e0a80e5c9500df;region=777"
    ]
    return urls

def TripadvisorPtoCruzRestaurantsURLs():

    urls = [
        "https://www.tripadvisor.es/Restaurants-g187481-Puerto_de_la_Cruz_Tenerife_Canary_Islands.html"
    ]
    return urls
