# -*- coding: utf-8 -*-
from googlemaps import Client as GoogleMaps

def change_field_name_json(field, fs_change):
    return fs_change[field].decode('UTF-8')

def getAttribute_Fixed(item, attr_fix):

    for k,v in attr_fix.items():
        item[k]=v

    return item

def getAttributes_Split(item, name_items, attr_spl):
    for k,v in name_items.items():
        if v[:-2]=="attribute_to_split":                                #if is a attr_split type
            for i in range(0,len(attr_spl)):                           #See how many attr_spl there are. For each one, we'll save new item
                attribute = attr_spl[i]
                value_item = item["attribute_to_split_"+str(i)].split() #It's a array with all words for the name of the first item (without split)

                #If not an exception. It can be a field without second value
                if len(value_item) != 1:
                    for j in range(0,len(attribute["attributes"])):         #Number of new items than we are going to create
                        key_item = attribute["attributes"][j]
                        item[key_item] = ''

                        for number in attribute["attr"+str(j)]:
                            item[key_item] += value_item[number]            #Set new items
                            item[key_item] += ' '
                    item[key_item] = item[key_item][:-1]                    #Eliminate last space
                    del item["attribute_to_split_"+str(i)]                  #Delete to the old item
                else:
                    key_item = attribute["exception"]
                    item[key_item] = value_item[0]
                    del item["attribute_to_split_"+str(i)]                  #Delete to the old item

                    temp_attr = attribute["attributes"][:]                  #copy the list
                    temp_attr.remove(attribute["exception"])
                    #For each exclude add value
                    for j in range(0,len(temp_attr)):
                        key_item = temp_attr[j]
                        item[key_item] = attribute["exclude"][j]


    return item

def getAttributes_Split_Remove(item, name_items, attr_spl_r):

    for element in attr_spl_r:
        for i in range(0,len(element["attributes"])):                                  #All elements to split
            for k,v in name_items.items():
                if v == element["attributes"][i]:                                      #if is the element
                    split_item = item[v].split()
                    condition = False
                    #There are condition in this split. It means that exits value that should change but others not should change
                    if "condition" in element:
                        condition = True
                        for j in range(0,len(element["condition"])):
                            try:
                                if element["condition"][j].decode('UTF-8') != split_item[element["condition_pos"][j]]:
                                    condition = False
                                    break
                            except:
                                condition =  False
                    else:
                        condition = True

                    if condition == True:
                        item[v] = ''
                        for attribute in element["attr"+str(i)]:
                            item[v] += split_item[attribute] + ' '
                        item[v] = item[v][:-1]                                              #Eliminate last space
    return item


def change_field_name(item, fs_change):

    for element in item:
        #if the name of item is a field that should to change
        if item[element] in fs_change:
            item[element] = fs_change[item[element]].decode('UTF-8')

    return item

def getValue_with_type(type_value, value):
    if type_value == int:
        try:
            value_type = int(value.replace(".",""))
        except:
            value_type = int(value)

    elif type_value == float:
        try:
            value_type = float(value.replace(",","."))
        except:
            try:
                value_type = value.replace(".","")
                value_type = float(value_type.replace(",","."))
            except:
                value_type = float(value)
    else:
        value_type = value

    return value_type

def getCoordinates(coordinates,item):

    result_coordinates = {'lat':'','lng':''}

    place = ''
    for field in coordinates:
        if field in item:
            place += str(item[field].encode('UTF-8'))                   #The place searched is the composed to the fields to get the coordinates
            place += ' '
    api_key = 'AIzaSyD2owaTzJTWi9m1f2QqAlJ1S0hfFT3nT0w'
    gmaps = GoogleMaps(api_key)
    location = gmaps.geocode(place)
    try:
        if 'location' in location[0]['geometry']:
            lat=location[0]['geometry']['location']['lat']
            lng=location[0]['geometry']['location']['lng']
        else:  #if it's a aproximation
            lat = location[0]['geometry']['bounds']['northeast']['lat'] + location[0]['geometry']['bounds']['southwest']['lat']
            lng = location[0]['geometry']['bounds']['northeast']['lng'] + location[0]['geometry']['bounds']['southwest']['lng']
    except:
        print 'algo va mal'
        pass

    result_coordinates['lat']=lat
    result_coordinates['lng']=lng
    return result_coordinates
