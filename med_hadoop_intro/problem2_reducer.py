#!/usr/bin/python
#!/usr/bin/python

import re
import sys


def production():
    uniqueIndividuals = 0
    (last_siteID, lastBackgroundID, count) = (None, None, None,0)
    for line in sys.stdin:
        (siteID, backgroundID, medication, val) = line.strip().split("\t")
        if last_siteID and lastBackgroundID and (last_siteID!=siteID or lastBackgroundID!=backgroundID) and medication == "lithium":
            reducerOutput(last_siteID,lastBackgroundID,count)
            (last_siteID,lastBackgroundID,count) = (siteID,backgroundID,int(val))
            uniqueIndividuals+=1
        else:
            (last_siteID,lastBackgroundID,count) = (siteID,backgroundID,count+int(val))

    if(last_siteID and lastBackgroundID) and medication == "lithium":
        reducerOutput(last_siteID,lastBackgroundID,count)
        uniqueIndividuals+=1
    print uniqueIndividuals

def reducerOutput(siteID, backgroundID, num):
    print "%s\t%s\t%s" % (siteID,backgroundID,num)

def local():
    uniqueIndividuals = 0
    (last_siteID, lastBackgroundID, count) = (None, None, 0)
    filePath = "output2.txt"
    with open(filePath,"r") as f:
        for line in f:
            (siteID, backgroundID, medication, val) = line.strip().split("\t")
            if last_siteID and lastBackgroundID and (last_siteID!=siteID or lastBackgroundID!=backgroundID) and medication == "lithium":
                reducerOutput(last_siteID,lastBackgroundID,count)
                (last_siteID,lastBackgroundID,count) = (siteID,backgroundID,int(val))
                uniqueIndividuals+=1
            else:
                (last_siteID,lastBackgroundID,count) = (siteID,backgroundID,count+int(val))
        if(last_siteID and lastBackgroundID) and medication == "lithium":
            reducerOutput(last_siteID,lastBackgroundID,count)
            uniqueIndividuals+=1
    print uniqueIndividuals
local()
