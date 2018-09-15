# -*- coding: UTF-8 -*-

import unicodecsv as csv
import sys, os
from selenium import webdriver
driver = webdriver.Chrome()

filename=sys.argv[1]
f = open(filename)
pos_end_name_field = filename.find('/')

samples = [row for row in csv.reader(f)]
samples[0].append("lat")
samples[0].append("lng")
url_position=2
i = 2133
bugNumber = 0
j = 0
while i < 2176:

    j = 2178
    driver = webdriver.Chrome()

    while i < 2178:

        url=samples[i][url_position]

        try:
            driver.get(url)
            coordenates = driver.find_element_by_xpath("//div[@class='_59m2yxn']/img").get_attribute('src')
            str_coor = str(coordenates)
            pos1 = str_coor.find("center")+7
            pos2 = str_coor.find("scale")-1
            coor = str_coor[pos1:pos2]
            coor = coor.split(',')
            lat = coor[0]
            lo=coor[1]
            print i, '--->',lat, lo
            bugNumber=0
            samples[i].append(lo)
            samples[i].append(lat)
            i+=1

        except:
            print 'error en', samples[i][0], ',iteracion',i, ', numero de error', bugNumber
            bugNumber+=1
            if bugNumber > 5:
                i+=1
                bugNumber=0
                samples[i].append('')
                samples[i].append('')
            pass

    driver.close()
    #chromedriver dont stop itself
    os.system("pkill -f chromedriver")

    name_rute = 'unstructured_data/coordinates_' + filename[pos_end_name_field+1:] + str(j)
    with open(name_rute, 'wb') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerows(samples)
        print 'escrito'
        print 'escrito'

with open('unstructured_data/coordinates_' + filename[pos_end_name_field+1:], 'wb') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerows(samples)

