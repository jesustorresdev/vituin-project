# -*- coding: utf-8 -*-
def change_field_name_json(field, fs_change):
    return fs_change[field].decode('UTF-8')

def getAttribute_Fixed(item, attr_fix):

    for k,v in attr_fix.items():
        item[k]=v

    return item

def getAttributes_Split(item, name_items, attr_spl):

    for k,v in name_items.items():
        if v[:-2]=="attribute_to_split":                                #if is a attr_split type
            for i in range (0,len(attr_spl)):                           #See how many attr_spl there are. For each one, we'll save new item
                attribute = attr_spl[i]
                value_item = item["attribute_to_split_"+str(i)].split() #It's a array with all words for the name of the first item (without split)

                for j in range(0,len(attribute["attributes"])):         #Number of new items than we are going to create
                    key_item = attribute["attributes"][j]
                    item[key_item] = ''

                    for number in attribute["attr"+str(j)]:
                        item[key_item] += value_item[number]            #Set new items
                        item[key_item] += ' '
                item[key_item] = item[key_item][:-1]                    #Eliminate last space
                del item["attribute_to_split_"+str(i)]                  #Delete to the old item
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
