# -*- coding: UTF-8 -*-

"""Campos obligatorios y opcionales
"""

__authors__ = 'Sergio Díaz, Jesús Torres'
__organization__ = 'Universidad de La Laguna'
__licensed__ = 'UNLICENSED'
__contact__ = "jmtorres@ull.edu.es, sdiazgon@ull.edu.es"
# __copyright__ = f"Copyright 2017-2018 {__organization__}"




def ListTripadvisorHotelsRequiredFields():
    return {
        'id': 'required',
        'title': 'required',
        'url': 'required',
        'review_count': 'optional',
        'street_address': 'optional',
        'extended_address': 'optional',
        'locality_address': 'required',
        'postal_code': 'optional',
        'stars': 'optional',
        'score': 'optional',
        'cleanliness': 'optional',
        'location': 'optional',
        'service': 'optional',
        'value': 'optional',
        'excelent': 'optional',
        'very_good': 'optional',
        'average': 'optional',
        'poor': 'optional',
        'terrible': 'optional',
        'price_range': 'optional',
        'lng': 'required',
        'lat': 'required'
    }

def ListTripadvisorHomesRequiredFields():
    return {
        'id': 'required',
        'title': 'required',
        'description': 'optional',
        'url': 'required',
        'lng': 'required',
        'lat': 'required',
        'price': 'required',
        'rooms': 'required',
        'bathrooms': 'required',
        'n_people': 'required',
        'min_stay': 'required',
        'type_residence': 'required',
        'review_count': 'optional',
        'score': 'optional',
        'place': 'required',
        'place_searched': 'required'
    }


def ListRestaurantsTripadvisorRequiredFields():
    return {
        'name': 'required',
        'url': 'required',
        'has_reviews': 'required',
        'phone': 'required',
        'street_address': 'required',
        'extended_address': 'required',
        'locality_address': 'required',
        'score': 'required',
        'price': 'required',
        'ratingExcellent': 'required',
        'ratingVeryGood': 'required',
        'ratingAverage': 'required',
        'ratingPoor': 'required',
        'ratingTerrible': 'required',
        'service': 'required',
        'food': 'required',
        'value': 'required',
        'atmosphere': 'required'
    }

def ListBookingHomeRequiredFields():
    return {
        'id': 'required',
        'title': 'required',
        'description': 'required',
        'url': 'required',
        'address': 'required',
        'region': 'required',
        'postal_code': 'postal_code.',
        'score': 'optional',
        'stars': 'optional',
        'cleanliness_rating': 'optional',
        'comfort_rating': 'optional',
        'facilities_rating': 'optional',
        'staff_rating': 'optional',
        'value_for_money_rating': 'optional',
        'wifi_rating': 'optional',
        'location_rating': 'optional',
        'review_count': 'optional',
        'type_residence': 'required',
        'price_min': 'optional',
        'lat': 'required',
        'lng': 'required',
        'place_searched': 'required'
    }



def TripAdvisorReviewRequiredFields():
    return {
        # comento los campos que no se usan para que no salgan en el CSV
        # los que si se usan se describen después como se extraen en el
        # tripadvisor_spyder.py
        'hotel_name': 'required',
        'hotel_street_address': 'required',
        'hotel_extended_address': 'required',
        'hotel_locality_address': 'required',
        'hotel_score': 'required',
        'title': 'required',
        'content': 'required',
        'review_stars': 'required',
        'review_date': 'required', #se anade para poder sacar la fecha del review
        #'review_date2': 'required', #se anade para poder sacar la fecha del review
        #'reviewer_id': 'required',
        #'reviewer_name': 'required',
        #'reviewer_level': 'required',
        'reviewer_location': 'required'
    }



def BookingReviewRequiredFields():
    return {
        'title': 'required',
        'score': 'required',
        'positive_content': 'required',
        'negative_content': 'required',
        #comento las tags no la usamos en el proyecto
        #'tags': 'required',
        'review_date':'required', # anadido para sacar la fecha del review
        'reviewer_location': 'required', # anadido para sar la localizacion
        'hotel_name': 'required',
        'hotel_address': 'required',
        'hotel_score': 'required'
    }
def AirbnbReviewRequiredFields():
    return {
        'content': 'required',
        'review_date':'required' # anadido para sacar la fecha del review
    }



#Holiday Rent
def List9FlatHomeRequiredFields():
    return {
        'id': 'required',
        'url': 'required',
        'title': 'required',
        'price': 'required',
        'type_residence': 'required',
        'numberReviews': 'required',
        'stars': 'required',
        'web': 'required',
        'lat': 'required',
        'lng': 'required'
    }

def ListAirbnbHomeRequiredFields():
    return {
        'name': 'optional',
        'url': 'required',
        'id': 'required',
        'lng': 'required',
        'lat': 'required',
        'description': 'optional',
        'capacity': 'optional',
        'bathrooms': 'optional',
        'beds': 'optional',
        'rooms': 'optional',
        'type_residence': 'required',
        # 'min_stay': 'required',
        # 'price': 'required',
        'place': 'required',
        'place_searched': 'required'
    }

def ListAtraveoHomeRequiredFields():
    return {
        'id': 'required',
        'url': 'required',
        'title': 'required',
        'price': 'optional',
        'rooms': 'optional',
        'bathrooms': 'optional',
        'capacity': 'required',
        'place': 'required',
        'type_residence': 'required',
        'number_reviews': 'optional',
        'main_bubbles': 'optional',
        'lat': 'required',
        'lng': 'required',
        # 'min_stay': 'required',
        'm2': 'required',
        'description': 'required',
        'place_searched': 'required'
    }

def ListHometogoHomeRequiredFields():
    return {
        'id': 'required',
        'url_web': 'required',
        'url_details': 'required',
        'price': 'required',
        'web': 'required',
        'type_residence': 'required',
        'number_reviews': 'required',
        'main_bubbles': 'required',
        'lat': 'required',
        'lng': 'required'
    }
def ListHomewayHomeRequiredFields():
    return {
        'id':'required',
        'url':'required',
        'title': 'required',
        'description': 'optional',
        'price': 'optional',
        'rooms': 'optional',
        'bathrooms': 'optional',
        'toilets': 'optional',
        'capacity': 'optional',
        'type_residence': 'optional',
        'number_reviews': 'optional',
        'main_bubbles': 'optional',
        'min_stay': 'optional',
        'lat': 'required',
        'lng': 'required',
        'm2': 'optional',
        'tourist_license': 'optional',
        'place_searched': 'optional'
    }

def ListNiumbaHomeRequiredFields():
    return {
        'id': 'required',
        'title': 'required',
        'description': 'required',
        'url': 'required',
        'price': 'required',
        'capacity': 'required',
        'bathrooms': 'optional',
        'type_residence': 'required',
        'rooms': 'optional',
        'min_stay': 'required',
        'lat': 'optional',
        'lng': 'optional',
        'number_reviews_tripadvisor': 'optional',
        'main_bubbles_tripadvisor': 'optional',
        'tourist_license': 'optional',
        'response_rate': 'optional',
        'years_advertising': 'optional',
        'last_update': 'required',
        'average_response_time': 'optional',
        'place': 'required',
        'place_searched': 'required'
    }

def ListFlipkeyHomeRequiredFields():
    return {
        'id': 'required',
        'title': 'required',
        'description': 'required',
        'url': 'required',
        'price': 'required',
        'capacity': 'required',
        # 'bathrooms': 'optional',
        'type_residence': 'required',
        'rooms': 'optional',
        'min_stay': 'required',
        'lat': 'optional',
        'lng': 'optional',
        'number_reviews_tripadvisor': 'optional',
        'main_bubbles_tripadvisor': 'optional',
        'tourist_license': 'optional',
        'response_rate': 'optional',
        'years_advertising': 'optional',
        'last_update': 'required',
        'average_response_time': 'optional',
        'place': 'required',
        'place_searched': 'required'
    }

def ListHousetripHomeRequiredFields():
    return {
        'id': 'required',
        'title': 'required',
        'description': 'required',
        'url': 'required',
        'price': 'required',
        'capacity': 'required',
        'bathrooms': 'optional',
        'type_residence': 'required',
        'rooms': 'optional',
        'min_stay': 'required',
        'lat': 'optional',
        'lng': 'optional',
        'number_reviews_tripadvisor': 'optional',
        'main_bubbles_tripadvisor': 'optional',
        'tourist_license': 'optional',
        'response_rate': 'optional',
        'years_advertising': 'optional',
        'last_update': 'required',
        'average_response_time': 'optional',
        'place': 'required',
        'place_searched': 'required'
    }

def ListHolidaylettingsHomeRequiredFields():
    return {
        'id': 'required',
        'title': 'required',
        'description': 'required',
        'url': 'required',
        'price': 'required',
        'capacity': 'required',
        'bathrooms': 'optional',
        'type_residence': 'required',
        'rooms': 'optional',
        'min_stay': 'required',
        'lat': 'optional',
        'lng': 'optional',
        'number_reviews_tripadvisor': 'optional',
        'main_bubbles_tripadvisor': 'optional',
        'tourist_license': 'optional',
        'response_rate': 'optional',
        'years_advertising': 'optional',
        'last_update': 'required',
        'average_response_time': 'optional',
        'place': 'required',
        'place_searched': 'required'
    }

def ListOnlyApartmentsHomeRequiredFields():
    return {
        'id': 'required',
        'title': 'required',
        'description': 'required',
        'url': 'required',
        # 'price': 'required',
        'lng': 'required',
        'lat': 'required',
        'type_residence': 'required',
        'street': 'required',
        'place': 'required',
        # 'min_stay': 'required',
        'number_reviews': 'optional',
        'main_bubbles': 'optional',
        'number_reviews_tripadvisor': 'optional',
        'main_bubbles_tripadvisor': 'optional',
        'place_searched': 'required'
    }

def ListRentaliaHomeRequiredFields():
    return {
        'id': 'required',
        'url': 'required',
        'title': 'optional',
        'price': 'required',
        'rooms': 'optional',
        'bathrooms': 'optional',
        'beds': 'optional',
        'capacity': 'optional',
        'place': 'required',
        'type_residence': 'required',
        'number_reviews': 'required',
        'main_bubbles': 'required',
        'min_stay': 'required',
        'lat': 'required',
        'lng': 'required',
        'place_searched': 'required'
    }

def ListCasamundoHomeRequiredFields():
    return {
        'id': 'required',
        'url': 'required',
        'title': 'required',
        'price': 'required',
        'bathrooms': 'optional',
        'beds': 'optional',
        'capacity': 'required',
        'm2': 'required',
        'type_residence': 'required',
        'number_reviews': 'optional',
        'main_bubbles': 'optional',
        'equipment_rating': 'optional',
        'value_rating': 'optional',
        'location_rating': 'optional',
        'general_impression_rating': 'optional',
        'cleanliness_rating': 'optional',
        'kindness_services_rating': 'optional',
        'lat': 'required',
        'lng': 'required',
        'place': 'required',
        'place_searched': 'required'
    }
