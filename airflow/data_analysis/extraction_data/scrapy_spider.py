# -*- coding: UTF-8 -*-

"""Extracción de viviendas en Niumba
"""

__authors__ = 'Sergio Díaz, Jesús Torres'
__organization__ = 'Universidad de La Laguna'
__licensed__ = 'UNLICENSED'
__contact__ = "jmtorres@ull.edu.es, sdiazgon@ull.edu.es"
# __copyright__ = f"Copyright 2017-2018 {__organization__}"

from scrapy.mail import MailSender
from scrapy.exceptions import CloseSpider
import scrapy, re, json
from googlemaps import Client as GoogleMaps
from default_settings import DevelopmentConfig
from extraction_data import db
import datetime


def set_properties(name_items, name_index, type_index):

    es_new = db._ELASTICSEARCH(
        [
            'elasticsearch:9200/'
        ]
    )
    indexSettings = {
        "mappings": {
            type_index: {
                "properties":
                    {value:{"type": "keyword"} for value in name_items}
            }
        }
    }
    es_new.indices.create(index=name_index, body=indexSettings)
    return es_new


#TODO use loaders
class ScrapySpider(scrapy.Spider, DevelopmentConfig):

    def xpath(self, response, xpath, type='text', attribute=False, pos_array=None, pos_extract=0, stop_if_error=False,
              extract_json=False):
        try:
            element = response.xpath(xpath+'/text()') if type == 'text' else \
                response.xpath(xpath+'/@'+attribute) if type == 'attribute' else \
                response.xpath(xpath) if xpath != './' else response

            if pos_array != None:
                element = element[pos_array]

            element = element if type == 'object' else \
                element.extract() if pos_extract is None else element.extract()[pos_extract]

            if extract_json:
                element = json.loads(element)

            return element

        except Exception as error:
            if stop_if_error:
                message = 'STOP obligatorio en caso de error scrapy. Hay error en "'+str(response.url)+'", '+xpath+': ', str(error)
                self.send_email(message)
                raise CloseSpider(message)
            else:
                return ''

    def try_json(self, data, element, element2 = None):
        try:
            if not element2:
                return data[element]
            else:
                return data[element][element2]
        except:
            return ''

    def get_attribute_description(self, element):
        type = ['capacity','rooms','bathrooms','beds', 'min_stay', 'toilets']
        attribute = {
            'capacidad':type[0],
            'huesped':type[0],
            'huéspedes'.decode('UTF-8'):type[0],
            'sleep'.decode('UTF-8'):type[0],
            'sleeps'.decode('UTF-8'):type[0],
            'dormitorio':type[1],
            'dormitorios':type[1],
            'habitaciones':type[1],
            'bedroom':type[1],
            'bedrooms':type[1],
            'baño'.decode('UTF-8'):type[2],
            'baños'.decode('UTF-8'):type[2],
            'bathroom'.decode('UTF-8'):type[2],
            'bathrooms'.decode('UTF-8'):type[2],
            'cama':type[3],
            'camas':type[3],
            'estancia mín.'.decode('UTF-8'):type[4],
            'aseos':type[5]
        }
        try:
            return attribute[element.lower()]
        except:
            ''

    def check_item(self, item, required_fields):

        try:
            errors_check = [field for field in required_fields if item[field] == '' and required_fields[field] == 'required']
        except Exception as error:
            message = 'Hay un error a la hora de checkear el item:'+str(error)
            raise CloseSpider(message)

        if errors_check:
            message = 'Hay un error, no existen los siguientes campos obligatorios en "'+ item['url'] +'": '
            for error in errors_check:
                message = message + error + ', '
            message = re.sub(', $', '.' , message)

            # self.send_mail(message, name_spider)
            raise CloseSpider(message)

    def send_email(self, message):
        mailfrom="erroresSpider@gmail.com"
        smtphost="smtp.gmail.com"
        smtpport=587
        smtpuser="erroresSpider@gmail.com"
        smtppass="errores1234"


        #Send a email saying if some bug have ocurred
        mailer = MailSender(mailfrom=mailfrom,smtphost=smtphost,smtpport=smtpport,smtpuser=smtpuser,smtppass=smtppass)
        mailer.send(to=["erroresSpider@gmail.com"], subject='Errores en el Spider '+self.name, body=message)

    def get_attributes_array_tripadvisor_rentals(self, elements):
        return [element.strip(":") for element in elements]

    #
    def get_attribute_tripadvisor_rentals(self, name, value):

        type = ['average_response_time','response_rate','last_update','years_advertising']
        attributes = {
            'Tiempo medio de respuesta':type[0],
            'Índice de respuesta'.decode('UTF-8'):type[1],
            'Última actualización del calendario'.decode('UTF-8'):type[2],
            'años anunciado'.decode('UTF-8'):type[3],
            'Average reply time':type[0],
            'Response rate':type[1],
            'Calendar updated':type[2],
            'Calendar last updated':type[2],
            'Years listed':type[3],
        }

        # return {attributes[name[i]]:value[i]  for i in range(0,len(name))}

        array = {}
        for i in range(0,len(name)):
            try:
                array.update({attributes[name[i]]:value[i]})
            except:
                pass

        return array


    def api_coordinates(self,place):
        api_key = DevelopmentConfig.GOOGLEMAP_ACCESS_TOKEN ##SACAR ESTO DE AQUI
        gmaps = GoogleMaps(api_key)
        location = gmaps.geocode(place)
        lat=''
        lng=''
        try:
            if 'location' in location[0]['geometry']:
                lat=location[0]['geometry']['location']['lat']
                lng=location[0]['geometry']['location']['lng']
            else:  #if it's a aproximation
                lat = location[0]['geometry']['bounds']['northeast']['lat'] + location[0]['geometry']['bounds']['southwest']['lat']
                lng = location[0]['geometry']['bounds']['northeast']['lng'] + location[0]['geometry']['bounds']['southwest']['lng']
        except:
            pass

        return lat, lng

    def get_if_first_searched(self,index_name, index_type):
            doc = {
                'query': {
                    'match_all' : {}
                }
            }

            try:
                res = db._ES.search(index=index_name, body=doc, size=0)
                #The next element indexed going to be the next id doesn't used
                cont_id = int(res['hits']['total'])
                return False
            except:
                #If it's the first gruop of elements indexed
                print("First indexed")
                return True

    def exist_item(self, index_name, url):
        #Search if there is same data in the index
        res = db._ES.search(index=index_name, body={
            "query": {
                "match_phrase": {
                    "url": url
                }
            }
        })
        if res['hits']['hits'] == []: #If there isn't result
            return False
        else:
            print('No index: '+str(url))
            return True

    def update_database(self,item_object, name_index, type_index, first_index):

        item = {}
        for element in item_object:
            item[element] = item_object[element]

        if first_index:
            elasticsearch = set_properties(item, name_index, type_index)
        else:
            elasticsearch = db._ES

        item['insert_time']=datetime.datetime.today()

        action = {
            "_index": name_index,
            "_type": type_index,
            "_source": item
        }

        actions=[action]
        try:
            db._HELPERS.bulk(elasticsearch, actions)
            print "indexed: "+str(item['url'])
        except Exception as error:
            message = 'Hay un error, no se pudo realizar subida en "'+ str(item['url']) +'" por error: '+str(error)
            raise CloseSpider(message)

