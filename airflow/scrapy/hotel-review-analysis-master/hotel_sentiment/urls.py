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

def BookingZoneURLs():
    urls = [
    #Tenerofe
	# "https://www.booking.com/searchresults.en-gb.html?aid=356984;label=gog235jc-country-en-gb-gb-unspec-es-com-L%3Aen-O%3Ax11-B%3Achrome-N%3Ayes-S%3Abo-U%3Ac-H%3As;sid=3d9a779adf10f3e6b7e0a80e5c9500df;region=777"

    # #Puerto de la Cruz
    # "https://www.booking.com/searchresults.en-gb.html?aid=356984&label=gog235jc-country-en-gb-gb-unspec-es-com-L%3Aen-O%3Ax11-B%3Achrome-N%3Ayes-S%3Abo-U%3Ac-H%3As&lang=en-gb&sid=b9b5230609de880a1134cf7bbe706add&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.en-gb.html%3Faid%3D356984%3Blabel%3Dgog235jc-country-en-gb-gb-unspec-es-com-L%253Aen-O%253Ax11-B%253Achrome-N%253Ayes-S%253Abo-U%253Ac-H%253As%3Bsid%3Db9b5230609de880a1134cf7bbe706add%3Bclass_interval%3D1%3Bdest_id%3D777%3Bdest_type%3Dregion%3Bdtdisc%3D0%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Boffset%3D0%3Bpostcard%3D0%3Bregion%3D777%3Broom1%3DA%252CA%3Bsb_price_type%3Dtotal%3Bss_all%3D0%3Bssb%3Dempty%3Bsshis%3D0%26%3B&ss=Puerto+de+la+Cruz%2C+Canary+Islands%2C+Spain&ssne=Tenerife&ssne_untouched=Tenerife&checkin_monthday=&checkin_month=&checkin_year=&checkout_monthday=&checkout_month=&checkout_year=&group_adults=2&group_children=0&no_rooms=1&from_sf=1&ss_raw=Puerto+de+la+Cruz&ac_position=0&ac_langcode=en&dest_id=-397851&dest_type=city&place_id_lat=28.4159&place_id_lon=-16.5533&search_pageview_id=d89861ac613f030f&search_selected=true&search_pageview_id=d89861ac613f030f&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0"
    #
    #Furteventura
    "https://www.booking.com/searchresults.es.html?aid=324799&label=fuerteventura-FfB3mofWUmwsYQfzLmt1dgS255698933501%3Apl%3Ata%3Ap1560%3Ap2%3Aac%3Aap1t1%3Aneg%3Afi%3Atikwd-2877377017%3Alp1005465%3Ali%3Adec%3Adm&sid=b9b5230609de880a1134cf7bbe706add&sb=1&src=region&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fregion%2Fes%2Ffuerteventura.es.html%3Faid%3D324799%3Blabel%3Dfuerteventura-FfB3mofWUmwsYQfzLmt1dgS255698933501%253Apl%253Ata%253Ap1560%253Ap2%253Aac%253Aap1t1%253Aneg%253Afi%253Atikwd-2877377017%253Alp1005465%253Ali%253Adec%253Adm%3Bsid%3Db9b5230609de880a1134cf7bbe706add%3Binac%3D0%26%3B&region=752&checkin_monthday=&checkin_month=&checkin_year=&checkout_monthday=&checkout_month=&checkout_year=&no_rooms=1&group_adults=2&group_children=0&from_sf=1"
    ]
    return urls

def TripadvisorPtoCruzRestaurantsURLs():

    urls = [
        "https://www.tripadvisor.es/Restaurants-g187481-Puerto_de_la_Cruz_Tenerife_Canary_Islands.html"
    ]
    return urls

def TripadvisorPtoCruzHolidaysRentUrls():

    urls = [
        "https://www.tripadvisor.es/VacationRentals-g187481-Reviews-Puerto_de_la_Cruz_Tenerife_Canary_Islands-Vacation_Rentals.html"
    ]
    return urls

def TripadvisorFuerteventuraHolidaysRentUrls():

    urls = [
        "https://www.tripadvisor.es/VacationRentals-g187467-Reviews-Fuerteventura_Canary_Islands-Vacation_Rentals.html"
    ]
    return urls

def AirbnbFuerteventuraURLs():
    urls = [
        # "https://www.airbnb.es/s/La-Oliva--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&query=La%20Oliva%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&ne_lat=28.781945916027258&ne_lng=-13.733527842439116&sw_lat=28.374168287219444&sw_lng=-14.080283823884429&zoom=11&search_by_map=true&s_tag=TA-yLyvt",
        # "https://www.airbnb.es/s/Corralejo--Las-Palmas--Corralejo--Spanien/all?place_id=ChIJ2daP6eM0RgwRdZXnYcB3rvw&query=Corralejo%2C%20Las%20Palmas%2C%20Corralejo%2C%20Spanien&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&refinement_paths%5B%5D=%2Ffor_you&map_toggle=true",
        # "https://www.airbnb.es/s/Puerto-del-Rosario--Las-Palmas/all?place_id=ChIJbQDwZyy4RwwR8BNNvvNAAwQ&query=Puerto%20del%20Rosario%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&refinement_paths%5B%5D=%2Ffor_you&map_toggle=true",
        # "https://www.airbnb.es/s/Jand%C3%ADa--Las-Palmas/all?refinement_paths%5B%5D=%2Ffor_you&place_id=ChIJ7dMyziCeRwwRoL7TLC8P2G8&query=Jand%C3%ADa%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true",
        # "https://www.airbnb.es/s/El-Cotillo-Beach--La-Oliva--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJn_SzJlizRwwRnlqslkb2yH4&query=El%20Cotillo%20Beach%2C%20La%20Oliva%2C%20Espa%C3%B1a&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=M7KQuUYM",
        # "https://www.airbnb.es/s/Betancuria--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJt3cGxDq7RwwRUBNNvvNAAwQ&query=Betancuria%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=lr9wzhYD",
        # "https://www.airbnb.es/s/P%C3%A1jara--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJW7aK4CCeRwwR0BNNvvNAAwQ&query=P%C3%A1jara%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=lBg70n0z",
        # "https://www.airbnb.es/s/Morro-Jable/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJt2AGAwl5RwwRFdR28SwU6X0&query=Morro%20Jable&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=vpTJa7RO",
        # "https://www.airbnb.es/s/Tuineje--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJDWKIAkWWRwwRwBRNvvNAAwQ&query=Tuineje%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=TAXBIYPr",
        # "https://www.airbnb.es/s/Antigua--Fuerteventura--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJJbEGZvu7RwwRuUYQC3VGftw&query=Antigua%2C%20Fuerteventura%2C%20Las%20Palmas&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=0TOCC4Ck",
        # "https://www.airbnb.es/s/Salinas-del-Carmen--Spain/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJmVPd803ARwwRea7KSt0NYiA&query=Salinas%20del%20Carmen%2C%20Spain&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=8WtyKRwY",
        # "https://www.airbnb.es/s/COSTA-CALMA--P%C3%A1jara--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJAQAAAPCbRwwR47xhAJraNE0&query=COSTA%20CALMA%2C%20P%C3%A1jara%2C%20Espa%C3%B1a&click_referer=t%3ASEE_ALL%7Csid%3Ad96206c4-a8e2-4998-a77c-5e98cf68f96d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&allow_override%5B%5D=&s_tag=kIWvGUxb",
        # "https://www.airbnb.es/s/Fuerteventura--Las-Palmas/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJgQ_Cr3OkRwwRI3-1tRMcxyo&query=Fuerteventura%2C%20Las%20Palmas&allow_override%5B%5D=&s_tag=0fn5-6DG"
       "https://www.airbnb.es/s/Parque-Holand%C3%A9s--La-Oliva--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&place_id=EiNQYXJxdWUgSG9sYW5kw6lzLCBMYSBPbGl2YSwgRXNwYcOxYQ&query=Parque%20Holand%C3%A9s%2C%20La%20Oliva%2C%20Espa%C3%B1a&allow_override%5B%5D=&s_tag=x_5PQnvx",
        "https://www.airbnb.es/s/Calle-Tajora--La-Oliva--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&place_id=Eh9DYWxsZSBUYWpvcmEsIExhIE9saXZhLCBFc3Bhw7Fh&query=Calle%20Tajora%2C%20La%20Oliva%2C%20Espa%C3%B1a&allow_override%5B%5D=&s_tag=cY9ABEox",
        "https://www.airbnb.es/s/Calle-Majanicho--Majanicho--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&place_id=EiNDYWxsZSBNYWphbmljaG8sIE1hamFuaWNobywgRXNwYcOxYQ&query=Calle%20Majanicho%2C%20Majanicho%2C%20Espa%C3%B1a&allow_override%5B%5D=&s_tag=GZmP-pXM",
        "https://www.airbnb.es/s/Gran-Tarajal--Tuineje--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&place_id=Eh5HcmFuIFRhcmFqYWwsIFR1aW5lamUsIEVzcGHDsWE&query=Gran%20Tarajal%2C%20Tuineje%2C%20Espa%C3%B1a&allow_override%5B%5D=&s_tag=8-UQxMws",
        "https://www.airbnb.es/s/Avenida-Corralejo-Grandes-Playas--Corralejo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&place_id=EjRBdmVuaWRhIENvcnJhbGVqbyBHcmFuZGVzIFBsYXlhcywgQ29ycmFsZWpvLCBFc3Bhw7Fh&query=Avenida%20Corralejo%20Grandes%20Playas%2C%20Corralejo%2C%20Espa%C3%B1a&click_referer=t%3ASEE_ALL%7Csid%3Ad9dcced4-7db3-4772-9c0a-b28e5debd9d7%7Cst%3AMAGAZINE_HOMES&title_type=MAGAZINE_HOMES&allow_override%5B%5D=&s_tag=feNLsiWd",
        "https://www.airbnb.es/s/Calle-Galicia--Corralejo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&place_id=EiFDYWxsZSBHYWxpY2lhLCBDb3JyYWxlam8sIEVzcGHDsWE&query=Calle%20Galicia%2C%20Corralejo%2C%20Espa%C3%B1a&click_referer=t%3ASEE_ALL%7Csid%3A5e8977ec-bef7-43d8-bb29-e79b1cad3c54%7Cst%3AMAGAZINE_HOMES&map_toggle=true&title_type=MAGAZINE_HOMES&allow_override%5B%5D=&s_tag=8zRLWiwD",
        "https://www.airbnb.es/s/Avenida-Nuestra-Se%C3%B1ora-del-Carmen--Corralejo--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&place_id=EjZBdmVuaWRhIE51ZXN0cmEgU2XDsW9yYSBkZWwgQ2FybWVuLCBDb3JyYWxlam8sIEVzcGHDsWE&query=Avenida%20Nuestra%20Se%C3%B1ora%20del%20Carmen%2C%20Corralejo%2C%20Espa%C3%B1a&click_referer=t%3ASEE_ALL%7Csid%3A96725256-1bd7-419e-ae65-6dbbefc0c45d%7Cst%3AMAGAZINE_HOMES&map_toggle=true&title_type=MAGAZINE_HOMES&allow_override%5B%5D=&s_tag=EwhTZ2wp",
        "https://www.airbnb.es/s/Calle-Pardelas--La-Oliva--Espa%C3%B1a/homes?refinement_paths%5B%5D=%2Fhomes&place_id=EiFDYWxsZSBQYXJkZWxhcywgTGEgT2xpdmEsIEVzcGHDsWE&query=Calle%20Pardelas%2C%20La%20Oliva%2C%20Espa%C3%B1a&click_referer=t%3ASEE_ALL%7Csid%3Ada8f4516-731a-4fa1-9aba-d178213f0fae%7Cst%3AMAGAZINE_HOMES&map_toggle=true&title_type=MAGAZINE_HOMES&allow_override%5B%5D=&s_tag=X3pwsWzx"
    ]
    return urls