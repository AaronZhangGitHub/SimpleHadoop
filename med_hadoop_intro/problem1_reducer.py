#!/usr/bin/python

import re
import sys


def production():
    uniqueIndividuals = 0
    (last_key, count) = (None, 0)
    for line in sys.stdin:
        (key, val) = line.strip().split("\t")
        if last_key and last_key!=key:
            uniqueIndividuals+=1
            reducerOutput(last_key,count)
            (last_key,count) = (key,int(val))
        else:
            (last_key,count) = (key,count+int(val))

    if(last_key):
        uniqueIndividuals+=1
        reducerOutput(last_key,count)
    print "count: ",uniqueIndividuals

def reducerOutput(key, num):
    print key, "\t", num

#def local():
#    uniqueIndividuals = 0
#    (last_key, count) = (None, 0)
#    filePath = "output1.txt"
#    with open(filePath,"r") as f:
#        for line in f:
#            (key, val) = line.strip().split("\t")
#            if last_key and last_key!=key:
#                uniqueIndividuals+=1
#                reducerOutput(last_key,count)
#                (last_key,count) = (key,int(val))
#            else:
#                (last_key,count) = (key,count+int(val))
#        if(last_key):
#            uniqueIndividuals+=1
#            reducerOutput(last_key,count)
#    print "count: ", uniqueIndividuals
production()
