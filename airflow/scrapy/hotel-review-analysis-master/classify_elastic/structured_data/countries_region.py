# -*- coding: utf-8 -*-

regions = ["España",
           "Islas Británicas",
           "Alemania",
           "Francia",
           "Italia",
           "Europa Nórdica",
           "Europa del Este",
           "Centro Europa",
           "Europa del sur",
           "Europa occidental",
           "América",
           "Resto del mundo",
           "Canarias"]
places = {
    "Canarias":regions[0],
    "Spain": regions[0],
    "España": regions[0],
    "TOTAL RESIDENTES EN ESPAÑA":regions[0],
    "Gran Bretaña": regions[1],
    "UK": regions[1],
    "Irlanda": regions[1],
    "Escocia": regions[1],
    "Gales": regions[1],
    "Inglaterra": regions[1],
    "Irlanda del Norte": regions[1],
    "Alemania": regions[2],
    "Francia": regions[3],
    "Italia": regions[4],
    "Dinamarca": regions[5],
    "Finlandia": regions[5],
    "Suecia": regions[5],
    "Noruega": regions[5],
    "Rumania": regions[6],
    "Bulgaria": regions[6],
    "Bielorrusia": regions[6],
    "Ucrania": regions[6],
    "Rusia": regions[6],
    "Polonia": regions[6],
    "Letonia": regions[6],
    "Lituania": regions[6],
    "Estonia": regions[6],
    "Moldavia": regions[6],
    "Austria": regions[7],
    "Suiza": regions[7],
    "República Checa": regions[7],
    "Republica Checa": regions[7],
    "Eslovaquia": regions[7],
    "Hungria": regions[7],
    "Serbia": regions[8],
    "Eslovenia": regions[8],
    "Croacia": regions[8],
    "Montenegro": regions[8],
    "Bosnia": regions[8],
    "Albania": regions[8],
    "Macedonia": regions[8],
    "Grecia": regions[8],
    "Turquia": regions[8],
    "Turquía": regions[8],
    "Chipre": regions[8],
    "Malta": regions[8],
    "Portugal": regions[8],
    "Andorra": regions[8],
    "Bélgica": regions[9],
    "Belgica": regions[9],
    "Países Bajos": regions[9],
    "Paises Bajos": regions[9],
    "Holanda": regions[9],
    "Liechtenstein": regions[9],
    "EEUU": regions[10],
    "Estados Unidos": regions[10],
    "Canada": regions[10],
    "Mexico": regions[10],
    "Mejico": regions[10],
    "Colombia": regions[10],
    "Venezuela": regions[10],
    "Paraguay": regions[10],
    "Uruguay": regions[10],
    "Bolivia": regions[10],
    "Ecuador": regions[10],
    "Guayana": regions[10],
    "Surinam": regions[10],
    "Chile": regions[10],
    "Argentina": regions[10],
    "Brasil": regions[10],
    "Honduras": regions[10],
    "Panamá": regions[10],
    "Panama": regions[10],
    "Puerto Rico": regions[10],
    "Costa Rica": regions[10],
    "El Salvador": regions[10],
    "Guatemala": regions[10],
    "Belice": regions[10],
    "Nicaragua": regions[10],
    "Cuba": regions[10],
    "Jamaica": regions[10],
    "Haití": regions[10],
    "Haiti": regions[10],
    "República Dominicana": regions[10],
    "Republica Dominicana": regions[10],
    "Alicante" : regions[0],
    "Asturias" : regions[0],
    "Barcelona" : regions[0],
    "Bilbao" : regions[0],
    "Girona" : regions[0],
    "Madrid" : regions[0],
    "Madrid/Barajas" : regions[0],
    "Malaga" : regions[0],
    "Santiago de Compostela" : regions[0],
    "Sevilla" : regions[0],
    "Valencia" : regions[0],
    "Zaragoza" : regions[0],
    "Tenerife" : regions[12],
    "Lanzarote" : regions[12],
    "Fuerteventura" : regions[12],
    "Gran Canaria" : regions[12],
    "La Gomera" : regions[12],
    "La Palma" : regions[12],
    "El Hierro" : regions[12]
}

places2 = {
    "España" : regions[8],
    "Italia" : regions[8],
    "Alemania" : regions[9],
    "Francia" : regions[9],
    "Canarias" : regions[0]
}


def get_region(place, **kwords):


    if place[:5].lower() != 'total' or place[-6:].lower() == 'españa'.decode('UTF-8'):

        try:
            region = places[place.encode('UTF-8')].decode('UTF-8')
            # print 'region-------->',region
            try:
                region2=places2[region.encode('UTF-8')].decode('UTF-8')
            except:
                region2=''
        except:
            region = regions[11]
            region2 = ''
    else:
        region = 'total'
        region2 = ''

    field_region = 'region'
    field_region2 = 'region2'


    #If it was passed a name of field, the name of field result is the combination of both
    if 'field'in kwords:
        field_region = kwords['field'] + '_' + field_region
        field_region2 = kwords['field'] + '_' + field_region2


    return {field_region: region, field_region2: region2}

