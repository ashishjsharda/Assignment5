#!/usr/bin/python2.7
#
# Assignment3 Interface
# Name: Chandan G Somasekhar
#

from pymongo import MongoClient
import os
import sys
import json
import codecs
from math import sqrt, radians, sin, asin, cos, atan, atan2, pow

def FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection):

    curs = collection.find({ "city" : {'$regex' : cityToSearch, '$options' : 'i' } })
    city_output = codecs.open(saveLocation1, 'w', encoding='utf-8')

    for row in curs:
        business_name = row.get("name")
        business_address = row.get("full_address").replace("\n", " ,")
        business_city = row.get("city")
        business_state = row.get("state")
        #output_line = "%s$%s$%s$%s\n" % (business_name, business_address, business_city, business_state)
        output_line = business_name+"$"+business_address+"$"+business_city+"$"+business_state+"\n"
        city_output.write(output_line)
    city_output.close()

def calc_distance(lat1, lon1, lat2, lon2 ):
    R = 3959
    print ("in dist:")
    rad_lat1 = radians(lat1)
    rad_lat2 = radians(lat2)
    diff_lat = radians(lat2-lat1)
    diff_long = radians(lon2-lon1)
    a = pow(sin(diff_lat/2), 2) + cos(rad_lat1)*cos(rad_lat2)*pow(sin(diff_long/2), 2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R*c
    print ("distance: "+str(distance))
    return distance


def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection):
    curs = collection.find({ "categories" :{"$in" : categoriesToSearch }},{"categories" : 1,"name" : 1, "longitude" : 1, "latitude" :1 })
    loc_output = codecs.open(saveLocation2, 'w', encoding='utf-8')

    for row in curs:
        print("before break:")
        print(" lat: "+myLocation[0])
        print (type(myLocation[0]))
        latitude1 = (float(myLocation[0]))
        print("after break:")
        longitude1 = (float(myLocation[1]))
        latitude = row.get("latitude")
        longitude = row.get("longitude")
        latitude2 = float(latitude)
        longitude2 = float(longitude)
        distance = calc_distance(latitude1, longitude1, latitude2, longitude2)
        business_name = row.get("name")
        if distance < maxDistance:
            output_line = business_name+"\n"
            print (output_line)
            loc_output.write(output_line)
    loc_output.close()
    collection.drop()
