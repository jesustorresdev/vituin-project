# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HotelSentimentItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    stars = scrapy.Field()

class ListPriceHotelsItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    time_borrow = scrapy.Field()
    company = scrapy.Field()
    price = scrapy.Field()

class ListHotelsTripadvisorItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    has_reviews = scrapy.Field()
    phone = scrapy.Field()
    street_address = scrapy.Field()
    extended_address = scrapy.Field()
    locality_address = scrapy.Field()
    postal_code = scrapy.Field()
    score = scrapy.Field()
    island = scrapy.Field()
    excelent = scrapy.Field()
    very_good = scrapy.Field()
    average = scrapy.Field()
    poor = scrapy.Field()
    terrible = scrapy.Field()

class ListHomesTripadvisorItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    has_reviews = scrapy.Field()
    lo = scrapy.Field()
    lat = scrapy.Field()
    price = scrapy.Field()
    rooms = scrapy.Field()
    bathrooms = scrapy.Field()
    n_people = scrapy.Field()
    type = scrapy.Field()
    score = scrapy.Field()
    locality = scrapy.Field()

class ListRestaurantsTripadvisorItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    has_reviews = scrapy.Field()
    phone = scrapy.Field()
    street_address = scrapy.Field()
    extended_address = scrapy.Field()
    locality_address = scrapy.Field()
    score = scrapy.Field()
    price = scrapy.Field()
    ratingExcellent = scrapy.Field()
    ratingVeryGood = scrapy.Field()
    ratingAverage = scrapy.Field()
    ratingPoor = scrapy.Field()
    ratingTerrible = scrapy.Field()
    service = scrapy.Field()
    food = scrapy.Field()
    value = scrapy.Field()
    atmosphere = scrapy.Field()

class ListHotelsBookingItem(scrapy.Item):
    id_booking = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    # has_reviews = scrapy.Field()
    phone = scrapy.Field()
    address = scrapy.Field()
    region = scrapy.Field()
    postalCode = scrapy.Field()
    score = scrapy.Field()
    stars = scrapy.Field()
    cleanliness_rating = scrapy.Field()
    comfort_rating = scrapy.Field()
    facilities_rating = scrapy.Field()
    staff_rating = scrapy.Field()
    value_for_money_rating = scrapy.Field()
    wifi_rating = scrapy.Field()
    location_rating = scrapy.Field()
    review_count = scrapy.Field()
    type_establishment = scrapy.Field()
    price_min = scrapy.Field()
    lat = scrapy.Field()
    lng = scrapy.Field()

class TripAdvisorReviewItem(scrapy.Item):
    # comento los campos que no se usan para que no salgan en el CSV
    # los que si se usan se describen después como se extraen en el
    # tripadvisor_spyder.py
    hotel_name = scrapy.Field()
    hotel_street_address = scrapy.Field()
    hotel_extended_address = scrapy.Field()
    hotel_locality_address = scrapy.Field()
    hotel_score = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    review_stars = scrapy.Field()
    review_date = scrapy.Field() #se anade para poder sacar la fecha del review
    #review_date2 = scrapy.Field() #se anade para poder sacar la fecha del review
    #reviewer_id = scrapy.Field()
    #reviewer_name = scrapy.Field()
    #reviewer_level = scrapy.Field()
    reviewer_location = scrapy.Field()

    
    #city = scrapy.Field()


    #hotel_name = scrapy.Field()
    #hotel_url = scrapy.Field()
    #hotel_classs = scrapy.Field()
    #hotel_address = scrapy.Field()
    #hotel_locality = scrapy.Field()
    #hotel_review_stars = scrapy.Field()
    #hotel_review_qty = scrapy.Field()


class BookingReviewItem(scrapy.Item):
    title = scrapy.Field()
    score = scrapy.Field()
    positive_content = scrapy.Field()
    negative_content = scrapy.Field()
    #comento las tags no la usamos en el proyecto
    #tags = scrapy.Field()
    review_date =scrapy.Field() # anadido para sacar la fecha del review
    reviewer_location = scrapy.Field() # anadido para sar la localizacion
    hotel_name = scrapy.Field()
    hotel_address = scrapy.Field()
    hotel_score = scrapy.Field()
    
class AirbnbReviewItem(scrapy.Item):
    content = scrapy.Field()
    review_date =scrapy.Field() # anadido para sacar la fecha del review
    

