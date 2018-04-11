#!/usr/bin/python

import re
import sys


def production():
    uniqueIndividuals = 0
    (last_siteID, lastBackgroundID, count) = (None, None, 0)
    for line in sys.stdin:
        (siteID, backgroundID, val) = line.strip().split("\t")
        if last_siteID and lastBackgroundID and (last_siteID!=siteID or lastBackgroundID!=backgroundID):
            uniqueIndividuals+=1
            reducerOutput(last_siteID,lastBackgroundID,count)
            (last_siteID,lastBackgroundID,count) = (siteID,backgroundID,int(val))
        else:
            (last_siteID,lastBackgroundID,count) = (siteID,backgroundID,count+int(val))

    if(last_siteID and lastBackgroundID):
        uniqueIndividuals+=1
        reducerOutput(last_siteID,lastBackgroundID,count)
    print "count: ",uniqueIndividuals

def reducerOutput(siteID, backgroundID, num):
    print "%s\t%s\t%s" % (siteID,backgroundID,num)

def local():
    uniqueIndividuals = 0
    (last_siteID, lastBackgroundID, count) = (None, None, 0)
    filePath = "output1.txt"
    with open(filePath,"r") as f:
        for line in f:
            (siteID, backgroundID, val) = line.strip().split("\t")
            if last_siteID and lastBackgroundID and (last_siteID!=siteID or lastBackgroundID!=backgroundID):
                uniqueIndividuals+=1
                reducerOutput(last_siteID,lastBackgroundID,count)
                (last_siteID,lastBackgroundID,count) = (siteID,backgroundID,int(val))
            else:
                (last_siteID,lastBackgroundID,count) = (siteID,backgroundID,count+int(val))
        if(last_siteID and lastBackgroundID):
            uniqueIndividuals+=1
            reducerOutput(last_siteID,lastBackgroundID,count)
    print "count: ", uniqueIndividuals
production()
