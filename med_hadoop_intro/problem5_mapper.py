#!/usr/bin/python
import re
import sys
LOCAL_TEST_PATH = './test.txt'
#Need Siteid, BackgroundID, Medication
#def local():
#    with open (LOCAL_TEST_PATH, "r") as f, open ("output5.txt","w") as of:
#        for line in f:
#            strippedLine = line.strip()
#            if strippedLine!="":
#                delimList = strippedLine.split(',')
#                siteID = delimList[0]
#                backgroundID = delimList[1]
#                medication = delimList[5]
#                outputMap(siteID,backgroundID,medication)
#                of.write("%s,%s,%s\t1\n" % (siteID, backgroundID, medication))

def outputMap(siteID, backgroundID, medication):
    print "%s,%s,%s\t1" % (siteID, backgroundID, medication)

def production():
    for line in sys.stdin:
        strippedLine = line.strip()
        if strippedLine!="":
            delimList = strippedLine.split(',')
            siteID = delimList[0]
            backgroundID = delimList[1]
            medication = delimList[5]
            if siteID!="siteId":
                outputMap(siteID,backgroundID,medication)

production()
