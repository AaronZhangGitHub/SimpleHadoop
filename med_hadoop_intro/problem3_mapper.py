#!/usr/bin/python
import re
import sys

LOCAL_TEST_PATH = './example_input_meds.txt'

def runProduction():
    for line in sys.stdin:
        #siteID and BackgroundID uniquely id a patient
        strippedLine = line.strip()
        if strippedLine!="":
            delimList = strippedLine.split(',')
            if delimList[0]!="siteId":
                outputMap(delimList[0],delimList[1], delimList[6])

#def runLocal():
#    with open (LOCAL_TEST_PATH, "r") as f, open ("output3.txt","w") as of:
#        for line in f:
#            strippedLine = line.strip()
#            if strippedLine!="":
#                delimList = strippedLine.split(',')
#                if delimList[0] != "siteId":
#                    str = "%s,%s%s\t1\n" % (delimList[6],delimList[0], delimList[1])
#                    of.write(str)

def outputMap(siteID, backgroundID, medicationGenericName):
    print "%s,%s%s\t1" % (medicationGenericName,siteID, backgroundID)

runProduction()
