# -*- coding: UTF-8 -*-

import unicodecsv as csv
import sys, os
from selenium import webdriver
sys.path.append('../extraction_data')
from utils import clear_cache

driver = webdriver.Chrome()

filename=sys.argv[1]
f = open(filename)
pos_end_name_field = filename.find('/')

samples = [row for row in csv.reader(f)]
samples[0].append("lat")
samples[0].append("lng")
url_position=1
n = len(samples)
i = 1
bugNumber = 0


while i < n:
    if i > 0:
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

        except Exception as error:
            print 'error en', samples[i][0], ',iteracion',i, ', numero de error', bugNumber
            print error
            print 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
            bugNumber+=1
            if bugNumber > 5:
                bugNumber=0
                samples[i].append('')
                samples[i].append('')
                i+=1
            pass
    else:
        print i
        i+=1

try:
    clear_cache(driver)
except:
    pass
try:
    driver.close()
except:
    pass

#chromedriver dont stop itself
os.system("pkill -f chromedriver")

# name_rute = 'unstructured_data/coordinates_' + filename[pos_end_name_field+1:] + str(j)
# with open(name_rute, 'wb') as csvfile:
#     writer = csv.writer(csvfile, dialect='excel')
#     writer.writerows(samples)

# with open('unstructured_data/coordinates_' + filename[pos_end_name_field+1:], 'wb') as csvfile:
#     writer = csv.writer(csvfile, dialect='excel')
#     writer.writerows(samples)
airbnb_files='coordinates_airbnb_list_homes_Adeje1.csv'
CSVdir="unstructured_data/data_files/"
airbnb_files = os.path.join(CSVdir, airbnb_files)

print airbnb_files
#It writes the comments and posts files
with open(airbnb_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples)