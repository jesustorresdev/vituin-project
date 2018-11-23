# -*- coding: utf-8 -*-

# Here, it is define the urls where scrapy will go to work


def TripAdvisorHotelsURLs():
    urls = [
        "https://www.tripadvisor.co.uk/Hotel_Review-g1064199-d585324-Reviews-The_Ritz_Carlton_Abama-Guia_de_Isora_Tenerife_Canary_Islands.html",
        "https://www.tripadvisor.co.uk/Hotel_Review-g187482-d1555517-Reviews-IBEROSTAR_Grand_Hotel_Mencey-Santa_Cruz_de_Tenerife_Tenerife_Canary_Islands.html"
    ]
    return urls

def TripAdvisorZoneTenerifeURLs():
    urls = [
        "https://www.tripadvisor.co.uk/Hotels-g187479-Tenerife_Canary_Islands-Hotels.html"
    ]

    return urls

def TripAdvisorZonePuertoDeLaCruzURLs():
    urls = [
        "https://www.tripadvisor.co.uk/Hotels-g187481-Puerto_de_la_Cruz_Tenerife_Canary_Islands-Hotels.html"
    ]

    return urls

def TripAdvisorZoneFuerteventuraURLs():
    urls = [
        "https://www.tripadvisor.co.uk/Hotels-g187467-Fuerteventura_Canary_Islands-Hotels.html"
    ]

    return urls

def BookingHotelsURLs():
    urls = [ ]

    return urls

def BookingZoneURLs(place):
    urls= {
        'Fuerteventura' : [
            "https://www.booking.com/searchresults.es.html?aid=324799&label=fuerteventura-FfB3mofWUmwsYQfzLmt1dgS255698933501%3Apl%3Ata%3Ap1560%3Ap2%3Aac%3Aap1t1%3Aneg%3Afi%3Atikwd-2877377017%3Alp1005465%3Ali%3Adec%3Adm&sid=b9b5230609de880a1134cf7bbe706add&sb=1&src=region&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fregion%2Fes%2Ffuerteventura.es.html%3Faid%3D324799%3Blabel%3Dfuerteventura-FfB3mofWUmwsYQfzLmt1dgS255698933501%253Apl%253Ata%253Ap1560%253Ap2%253Aac%253Aap1t1%253Aneg%253Afi%253Atikwd-2877377017%253Alp1005465%253Ali%253Adec%253Adm%3Bsid%3Db9b5230609de880a1134cf7bbe706add%3Binac%3D0%26%3B&region=752&checkin_monthday=&checkin_month=&checkin_year=&checkout_monthday=&checkout_month=&checkout_year=&no_rooms=1&group_adults=2&group_children=0&from_sf=1"
        ],
        'Puerto de la Cruz' : [
            "https://www.booking.com/searchresults.en-gb.html?aid=356984&label=gog235jc-country-en-gb-gb-unspec-es-com-L%3Aen-O%3Ax11-B%3Achrome-N%3Ayes-S%3Abo-U%3Ac-H%3As&lang=en-gb&sid=b9b5230609de880a1134cf7bbe706add&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.en-gb.html%3Faid%3D356984%3Blabel%3Dgog235jc-country-en-gb-gb-unspec-es-com-L%253Aen-O%253Ax11-B%253Achrome-N%253Ayes-S%253Abo-U%253Ac-H%253As%3Bsid%3Db9b5230609de880a1134cf7bbe706add%3Bclass_interval%3D1%3Bdest_id%3D777%3Bdest_type%3Dregion%3Bdtdisc%3D0%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Boffset%3D0%3Bpostcard%3D0%3Bregion%3D777%3Broom1%3DA%252CA%3Bsb_price_type%3Dtotal%3Bss_all%3D0%3Bssb%3Dempty%3Bsshis%3D0%26%3B&ss=Puerto+de+la+Cruz%2C+Canary+Islands%2C+Spain&ssne=Tenerife&ssne_untouched=Tenerife&checkin_monthday=&checkin_month=&checkin_year=&checkout_monthday=&checkout_month=&checkout_year=&group_adults=2&group_children=0&no_rooms=1&from_sf=1&ss_raw=Puerto+de+la+Cruz&ac_position=0&ac_langcode=en&dest_id=-397851&dest_type=city&place_id_lat=28.4159&place_id_lon=-16.5533&search_pageview_id=d89861ac613f030f&search_selected=true&search_pageview_id=d89861ac613f030f&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0"
        ],
        'Adeje' : [
            "https://www.booking.com/searchresults.en-gb.html?aid=356984&label=gog235jc-country-en-gb-gb-unspec-es-com-L%3Aen-O%3Ax11-B%3Achrome-N%3Ayes-S%3Abo-U%3Ac-H%3As&sid=b9b5230609de880a1134cf7bbe706add&ac_click_type=b&ac_position=1&city=-369166&class_interval=1&dest_id=3490&dest_type=region&from_sf=1&group_adults=2&group_children=0&label_click=undef&no_rooms=1&raw_dest_type=region&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=searchresults&src_elem=sb&srpvid=342a09a8d61600ff&ss=Costa%20Adeje%2C%20Spain&ss_raw=Costa%20adeje&ssb=empty&ssne_untouched=Adeje&rows=15"
        ]
    }
    return urls[place]

def TripadvisorPtoCruzRestaurantsURLs():

    urls = [
        "https://www.tripadvisor.es/Restaurants-g187481-Puerto_de_la_Cruz_Tenerife_Canary_Islands.html"
    ]
    return urls

def TripadvisorHolidaysRentURLs(place):
    urls= {
        'Fuerteventura' : [
            "https://www.tripadvisor.es/VacationRentals-g187467-Reviews-Fuerteventura_Canary_Islands-Vacation_Rentals.html"
        ],
        'Puerto de la Cruz' : [
            "https://www.tripadvisor.es/VacationRentals-g187481-Reviews-Puerto_de_la_Cruz_Tenerife_Canary_Islands-Vacation_Rentals.html"
        ],
        'Adeje' : [
            ""
        ]
    }

    return urls


def AirbnbURLs(place):
    urls= {
        'Fuerteventura' : [
            "https://www.airbnb.es/s/La-Oliva--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=La%20Oliva%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&ne_lat=28.781945916027258&ne_lng=-13.733527842439116&sw_lat=28.374168287219444&sw_lng=-14.080283823884429&zoom=11&search_by_map=true&s_tag=TA-yLyvt",
            "https://www.airbnb.es/s/Corralejo--Las-Palmas--Corralejo--Spanien/all?place_id=ChIJ2daP6eM0RgwRdZXnYcB3rvw&query=Corralejo%2C%20Las%20Palmas%2C%20Corralejo%2C%20Spanien&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&refinement_paths%5B%5D=%2Ffor_you&map_toggle=true",
            "https://www.airbnb.es/s/Puerto-del-Rosario--Las-Palmas/all?place_id=ChIJbQDwZyy4RwwR8BNNvvNAAwQ&query=Puerto%20del%20Rosario%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&refinement_paths%5B%5D=%2Ffor_you&map_toggle=true",
            "https://www.airbnb.es/s/Jand%C3%ADa--Las-Palmas/all?refinement_paths%5B%5D=%2Ffor_you&place_id=ChIJ7dMyziCeRwwRoL7TLC8P2G8&query=Jand%C3%ADa%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true",
            "https://www.airbnb.es/s/El-Cotillo-Beach--La-Oliva--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJn_SzJlizRwwRnlqslkb2yH4&query=El%20Cotillo%20Beach%2C%20La%20Oliva%2C%20Espa%C3%B1a&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=M7KQuUYM",
            "https://www.airbnb.es/s/Betancuria--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJt3cGxDq7RwwRUBNNvvNAAwQ&query=Betancuria%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=lr9wzhYD",
            "https://www.airbnb.es/s/P%C3%A1jara--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJW7aK4CCeRwwR0BNNvvNAAwQ&query=P%C3%A1jara%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=lBg70n0z",
            "https://www.airbnb.es/s/Morro-Jable/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJt2AGAwl5RwwRFdR28SwU6X0&query=Morro%20Jable&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=vpTJa7RO",
            "https://www.airbnb.es/s/Tuineje--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJDWKIAkWWRwwRwBRNvvNAAwQ&query=Tuineje%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=TAXBIYPr",
            "https://www.airbnb.es/s/Antigua--Fuerteventura--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJJbEGZvu7RwwRuUYQC3VGftw&query=Antigua%2C%20Fuerteventura%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=0TOCC4Ck",
            "https://www.airbnb.es/s/Salinas-del-Carmen--Spain/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJmVPd803ARwwRea7KSt0NYiA&query=Salinas%20del%20Carmen%2C%20Spain&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=8WtyKRwY",
            "https://www.airbnb.es/s/COSTA-CALMA--P%C3%A1jara--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJAQAAAPCbRwwR47xhAJraNE0&query=COSTA%20CALMA%2C%20P%C3%A1jara%2C%20Espa%C3%B1a&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=kIWvGUxb",
            "https://www.airbnb.es/s/Fuerteventura--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJgQ_Cr3OkRwwRI3-1tRMcxyo&query=Fuerteventura%2C%20Las%20Palmas&allow_override%5B%5D=&s_tag=0fn5-6DG"
        ],
        'Puerto de la Cruz' : [
            "https://www.airbnb.es/s/Puerto-de-la-Cruz--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJBxuTnlXVQQwRQWOmKGEY6s0&query=Puerto%20de%20la%20Cruz%2C%20Santa%20Cruz%20de%20Tenerife&allow_override%5B%5D=&s_tag=o78DH6Gz"
        ],
        'Adeje' : [
            "https://www.airbnb.es/s/Avenida-Rafael-Puig-Lluvina--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Avenida%20Rafael%20Puig%20Lluvina%2C%20Adeje%2C%20Espa%C3%B1a&place_id=EitBdmVuaWRhIFJhZmFlbCBQdWlnIExsdXZpbmEsIEFkZWplLCBFc3Bhw7FhIi4qLAoUChIJ2_n_92SXagwRoNry88wONDsSFAoSCe0sQ9WbkGoMEQNBP_KTXbsq&allow_override%5B%5D=&s_tag=-MMLU5YD",
            "https://www.airbnb.es/s/Avenida-de-los-Pueblos--Costa-Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Avenida%20de%20los%20Pueblos%2C%20Costa%20Adeje%2C%20Espa%C3%B1a&place_id=EixBdmVuaWRhIGRlIGxvcyBQdWVibG9zLCBDb3N0YSBBZGVqZSwgRXNwYcOxYSIuKiwKFAoSCTcyujxhl2oMEb43GcnxZNX3EhQKEgnLOPMeWpdqDBGfTgTVe4yMug&allow_override%5B%5D=&s_tag=3nBv6zZn",
            "https://www.airbnb.es/s/Calle-Gran-Breta%C3%B1a--Costa-Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Calle%20Gran%20Breta%C3%B1a%2C%20Costa%20Adeje%2C%20Espa%C3%B1a&place_id=EilDYWxsZSBHcmFuIEJyZXRhw7FhLCBDb3N0YSBBZGVqZSwgRXNwYcOxYSIuKiwKFAoSCXnJ2n9el2oMEYaLQS41eqFJEhQKEgnLOPMeWpdqDBGfTgTVe4yMug&allow_override%5B%5D=&s_tag=lLtmkocG",
            "https://www.airbnb.es/s/Avenida-de-Espa%C3%B1a--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Avenida%20de%20Espa%C3%B1a%2C%20Adeje%2C%20Espa%C3%B1a&place_id=EiJBdmVuaWRhIGRlIEVzcGHDsWEsIEFkZWplLCBFc3Bhw7FhIi4qLAoUChIJJcugjVyXagwR1xge9Dwm0hYSFAoSCe0sQ9WbkGoMEQNBP_KTXbsq&allow_override%5B%5D=&s_tag=JITVUhln",
            # "https://www.airbnb.es/s/Playa-de-Troya--Islas-Canarias--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Playa%20de%20Troya%2C%20Islas%20Canarias%2C%20Espa%C3%B1a&place_id=ChIJZ7ou-miXagwRPZd98Sj8Knw&map_toggle=true&allow_override%5B%5D=&s_tag=2UqOQOXc",
            # "https://www.airbnb.es/s/Puerto-Colon--Playa-de-la-Am%C3%A9ricas--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Puerto%20Colon%2C%20Playa%20de%20la%20Am%C3%A9ricas%2C%20Espa%C3%B1a&place_id=ChIJv56cUEOXagwRR4J2T1JFI9Y&map_toggle=true&allow_override%5B%5D=&s_tag=9YeuCGCc",
            # "https://www.airbnb.es/s/Playa-Fa%C3%B1abe--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Playa%20Fa%C3%B1abe%2C%20Adeje%2C%20Espa%C3%B1a&place_id=ChIJmW_f_06XagwRnJ62y5AbUzQ",
            # "https://www.airbnb.es/s/Playa-Fa%C3%B1abe--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Playa%20Fa%C3%B1abe%2C%20Adeje%2C%20Espa%C3%B1a&place_id=ChIJmW_f_06XagwRnJ62y5AbUzQ",
            # "https://www.airbnb.es/s/Playa-del-Duque--Santa-Cruz-de-Tenerife--Spain/homes?refinement_paths%5B%5D=%2Fhomes&query=Playa%20del%20Duque%2C%20Santa%20Cruz%20de%20Tenerife%2C%20Spain&place_id=ChIJ0cRmSUqXagwR6qRnp8xGs4I&map_toggle=true&allow_override%5B%5D=&s_tag=Ru9Zh_yf",
            # "https://www.airbnb.es/s/La-Caleta-de-Adeje--La-Caleta/homes?refinement_paths%5B%5D=%2Fhomes&query=La%20Caleta%20de%20Adeje%2C%20La%20Caleta&place_id=ChIJI5Gz9s6QagwR5e8KupQk354&map_toggle=true&allow_override%5B%5D=&s_tag=O8OCFjjT",
            # "https://www.airbnb.es/s/Golf-Costa-Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Golf%20Costa%20Adeje%2C%20Espa%C3%B1a&place_id=ChIJl1EFE2-aagwRf2htVeWBRxk&map_toggle=true&allow_override%5B%5D=&s_tag=eBC8f0Nd",
            # "https://www.airbnb.es/s/Avenida-Madro%C3%B1al--Costa-Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Avenida%20Madro%C3%B1al%2C%20Costa%20Adeje%2C%20Espa%C3%B1a&place_id=EidBdmVuaWRhIE1hZHJvw7FhbCwgQ29zdGEgQWRlamUsIEVzcGHDsWEiLiosChQKEgmLQHuK_ZlqDBHSxM3Kv0my4hIUChIJyzjzHlqXagwRn04E1XuMjLo&map_toggle=true&allow_override%5B%5D=&s_tag=ya8prbvn",
            # "https://www.airbnb.es/s/Calle-Extremadura--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Calle%20Extremadura%2C%20Adeje%2C%20Espa%C3%B1a&place_id=EiFDYWxsZSBFeHRyZW1hZHVyYSwgQWRlamUsIEVzcGHDsWEiLiosChQKEgmFqDKJ-ZlqDBHPAtLr7x8yQhIUChIJ7SxD1ZuQagwRA0E_8pNduyo&map_toggle=true&allow_override%5B%5D=&s_tag=OIIZPy6K",
            # "https://www.airbnb.es/s/Avenida-Francia--Costa-Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Avenida%20Francia%2C%20Costa%20Adeje%2C%20Espa%C3%B1a&place_id=EiVBdmVuaWRhIEZyYW5jaWEsIENvc3RhIEFkZWplLCBFc3Bhw7FhIi4qLAoUChIJSVq4suOZagwRva1C36s0UqsSFAoSCcs48x5al2oMEZ9OBNV7jIy6&map_toggle=true&allow_override%5B%5D=&s_tag=W5eCnmgU",
            # "https://www.airbnb.es/s/homes?refinement_paths%5B%5D=%2Fhomes&query=Avenida%20europa%2C%20Costa%20Adeje%2C%20Espa%C3%B1a&map_toggle=true&allow_override%5B%5D=&s_tag=9otg5AwJ",
            # "https://www.airbnb.es/s/Callao-Salvaje--Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&query=Callao%20Salvaje%2C%20Tenerife&place_id=ChIJXY2y6QWRagwRwNKxQOqEKYo&map_toggle=true&allow_override%5B%5D=&s_tag=W3rd-CIE",
            # "https://www.airbnb.es/s/Calle-el-Puertito--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Calle%20el%20Puertito%2C%20Adeje%2C%20Espa%C3%B1a&place_id=EiFDYWxsZSBlbCBQdWVydGl0bywgQWRlamUsIEVzcGHDsWEiLiosChQKEgm5kc4a4JBqDBFc76yYNYDOBRIUChIJ7SxD1ZuQagwRA0E_8pNduyo&map_toggle=true&allow_override%5B%5D=&s_tag=LWB0xg1-",
            # "https://www.airbnb.es/s/Marazul--Tenerife--Spanje/homes?refinement_paths%5B%5D=%2Fhomes&query=Marazul%2C%20Tenerife%2C%20Spanje&place_id=ChIJSbJ82LyRagwRlvYCvJUtX58&map_toggle=true&allow_override%5B%5D=&s_tag=MllgsHUt",
            # "https://www.airbnb.es/s/Avenida-San-Borondon--Fa%C3%B1ab%C3%A9--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Avenida%20San%20Borondon%2C%20Fa%C3%B1ab%C3%A9%2C%20Espa%C3%B1a&place_id=EidBdmVuaWRhIFNhbiBCb3JvbmRvbiwgRmHDsWFiw6ksIEVzcGHDsWEiLiosChQKEgmjtW_FqJBqDBEon4YXdkLYahIUChIJ3y_vyqiQagwRUOgQKm7zeAY&map_toggle=true&allow_override%5B%5D=&s_tag=WkC2INvb",
            # "https://www.airbnb.es/s/Calle-Hermano-Pedro--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Calle%20Hermano%20Pedro%2C%20Adeje%2C%20Espa%C3%B1a&place_id=EiNDYWxsZSBIZXJtYW5vIFBlZHJvLCBBZGVqZSwgRXNwYcOxYSIuKiwKFAoSCS9_6JWfkGoMEb4wkDfukQdCEhQKEgntLEPVm5BqDBEDQT_yk127Kg&map_toggle=true&allow_override%5B%5D=&s_tag=818jPPLl",
            # "https://www.airbnb.es/s/Avenida-del-Poniente--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Avenida%20del%20Poniente%2C%20Adeje%2C%20Espa%C3%B1a&place_id=EiRBdmVuaWRhIGRlbCBQb25pZW50ZSwgQWRlamUsIEVzcGHDsWEiLiosChQKEgmzHhh3pJBqDBGyyIqnZMBMpBIUChIJ7SxD1ZuQagwRA0E_8pNduyo&map_toggle=true&allow_override%5B%5D=&s_tag=NJp9ZbKh&section_offset=4&items_offset=54",
            # "https://www.airbnb.es/s/Avenida-de-Ayyo--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Avenida%20de%20Ayyo%2C%20Adeje%2C%20Espa%C3%B1a&place_id=Eh9BdmVuaWRhIGRlIEF5eW8sIEFkZWplLCBFc3Bhw7FhIi4qLAoUChIJRcBJwZaQagwR2rylPPxvws4SFAoSCe0sQ9WbkGoMEQNBP_KTXbsq&map_toggle=true&allow_override%5B%5D=&s_tag=mx4lW3Rb",
            # "https://www.airbnb.es/s/Arme%C3%B1ime--Santa-Cruz-de-Tenerife/homes?refinement_paths%5B%5D=%2Fhomes&query=Arme%C3%B1ime%2C%20Santa%20Cruz%20de%20Tenerife&place_id=ChIJyaWIKO6QagwROO9OnpFk9Ak&map_toggle=true&allow_override%5B%5D=&s_tag=cxcaf8I3",
            # "https://www.airbnb.es/s/Calle-Pedro-Garcia-Cabrera--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Calle%20Pedro%20Garcia%20Cabrera%2C%20Adeje%2C%20Espa%C3%B1a&place_id=EipDYWxsZSBQZWRybyBHYXJjaWEgQ2FicmVyYSwgQWRlamUsIEVzcGHDsWEiLiosChQKEgm9kfYS8ZBqDBHTj2XbgLrsAxIUChIJ7SxD1ZuQagwRA0E_8pNduyo&map_toggle=true&allow_override%5B%5D=&s_tag=sCO-D9Nq",
            # "https://www.airbnb.es/s/Carretera-Taucho--Adeje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Carretera%20Taucho%2C%20Adeje%2C%20Espa%C3%B1a&place_id=EiBDYXJyZXRlcmEgVGF1Y2hvLCBBZGVqZSwgRXNwYcOxYSIuKiwKFAoSCf1D1r95kGoMERFexCCeII08EhQKEgntLEPVm5BqDBEDQT_yk127Kg&allow_override%5B%5D=&map_toggle=true&s_tag=DW7sVNRW",
            # "https://www.airbnb.es/s/Calle-la-Un%C3%AD%C3%B3n--Tijoco-Bajo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&query=Calle%20la%20Un%C3%AD%C3%B3n%2C%20Tijoco%20Bajo%2C%20Espa%C3%B1a&place_id=EiZDYWxsZSBsYSBVbsOtw7NuLCBUaWpvY28gQmFqbywgRXNwYcOxYSIuKiwKFAoSCYv8RmZKkGoMEYYPzBRWvKOcEhQKEgmJNxKJNZBqDBGKVf3re-SNOg&allow_override%5B%5D=&map_toggle=true&s_tag=9w0QyO0x",
        ]
    }
    return urls[place]

def AtraveoURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.atraveo.es/adeje#eyJkYXRhIjp7ImNvdW50cnlJZCI6IkVTIiwicmVnaW9uSWQiOiIxNzUiLCJzdWJSZWdpb25JZCI6Ijg4MyIsImNpdHlJZCI6Ijk4MjcifSwiY29uZmlnIjp7fX0="
        ],
        'Adeje' : [
            "https://www.atraveo.es/adeje#eyJkYXRhIjp7ImNvdW50cnlJZCI6IkVTIiwicmVnaW9uSWQiOiIxNzUiLCJzdWJSZWdpb25JZCI6Ijg5NSIsImNpdHlJZCI6IjczNDM3MiIsImR1cmF0aW9uIjo3fSwiY29uZmlnIjp7InBhZ2UiOiIwIn19",
            "https://www.atraveo.es/costa_adeje_%28costa_oeste_de_tenerife%29#eyJkYXRhIjp7ImNvdW50cnlJZCI6IkVTIiwicmVnaW9uSWQiOjE3NSwiY2l0eUlkIjo1ODQwNzQsImR1cmF0aW9uIjo3fSwiY29uZmlnIjp7fX0="
        ]
    }
    return urls[place]

def HomewayURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.homeaway.es/results/region:1976/@28.33705961045927,-16.61179916612673,28.48894858941568,-16.464631721897604,12z?petIncluded=false&ssr=true&legacyRegionPath=canarias&legacyRegionPath=puerto-de-la-cruz"
        ],
        'Adeje' : [
            "https://www.homeaway.es/search/keywords:Adeje,%20Canarias,%20Espa%C3%B1a"
        ]
    }
    return urls[place]

def HometogoURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.hometogo.es/search/5460aedcd4609?bedrooms=1&bounds=28.42563%2C-16.56022%3B28.39316%2C-16.53416&lastZoom=15&mapZoom=15&persons=2&pricetype=perNight"
        ],
        'Adeje' : [
            ""
        ]
    }
    return urls[place]

def NiumbaURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.niumba.com/islas-canarias/santa-cruz-de-tenerife/puerto-de-la-cruz/hom_sleeps_max."
        ],
        'Adeje' : [
            ""
        ]
    }
    return urls[place]

def OnlyApartmentsURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.only-apartments.es/apartamentos-en-puerto-de-la-cruz.html"
        ],
        'Adeje' : [
            "https://www.only-apartments.es/apartamentos-en-costa-adeje.html",
            "https://www.only-apartments.es/apartamentos-en-adeje.html",
            "https://www.only-apartments.es/apartamentos-en-callao-salvaje.html"
        ]
    }
    return urls[place]

def Flats9URLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://www.9flats.com/es/searches?utf8=%E2%9C%93&mode=list&search%5Bplace_type%5D=&search%5Bprice_min%5D=&search%5Bprice_max%5D=&search%5Bcurrency%5D=EUR&search%5Bsort_by%5D=top_ranking&search%5Bview_index%5D=0&search%5Bnumber_of_bathrooms%5D=0&search%5Bnumber_of_bedrooms%5D=0&search%5Bradius%5D=25&search%5Bamenities%5D=&search%5Bwoeid%5D=770966&search%5Bbb_sw%5D=&search%5Bbb_ne%5D=&search%5Blat%5D=28.4142&search%5Blng%5D=-16.5474&search%5Biso%5D=&search%5Bis_country%5D=&search%5Bcategory%5D=&search%5Bgeo_search%5D=&search%5Bgeo_region%5D=false&search%5Bpoint_of_interest%5D=false&search%5Bprice_range%5D=&search%5Bancestries%5D=&search%5Bcontinuous_update%5D=&search%5Bbooking_type%5D=&search%5Bpayment_type%5D=&search%5Bstart_date_alt%5D=&search%5Bend_date_alt%5D=&search%5Bquery%5D=Puerto+de+la+Cruz%2C+Pto+de+la+Cruz"
        ],
        'Adeje' : [
            "https://www.9flats.com/es/searches?utf8=%E2%9C%93&mode=list&search%5Bcurrency%5D=EUR&search%5Bsort_by%5D=top_ranking&search%5Bradius%5D=25&search%5Bwoeid%5D=751413&search%5Blat%5D=28.4142&search%5Blng%5D=-16.5474&search%5Bgeo_region%5D=false&search%5Bpoint_of_interest%5D=false&search%5Bquery%5D=Adeje%2C+Adeje+Municipio%2C+Tenerife%2C+Islas+Canarias%2C+Espa%C3%B1a&search%5Bstart_date%5D=&search%5Bend_date%5D=&search%5Bnumber_of_beds%5D=2&number_of_adults=2&search%5Bnumber_of_children%5D=0&number_of_bedrooms=&number_of_bathrooms="
        ]
    }
    return urls[place]

def RentaliaURLs(place):
    urls= {
        'Puerto de la Cruz' : [
            "https://es.rentalia.com/alquiler-vacaciones-puerto-de-la-cruz/"
        ],
        'Adeje' : [
            "https://es.rentalia.com/alquiler-vacaciones-adeje/"
        ]
    }
    return urls[place]