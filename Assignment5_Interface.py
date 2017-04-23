#!/usr/bin/python2.7
#
# Assignment3 Interface
# Name: Chandan G Somasekhar
#

from pymongo import MongoClient
import os
import sys
import json

def FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection):
    print collection
    col=collection.find_one()
    print "Collection:"
    #print col.count()
    for rec in col:
        print rec
    #col=collection.find([{"city": cityToSearch}])
    print "done city search"
    pass

def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection):
    pass

