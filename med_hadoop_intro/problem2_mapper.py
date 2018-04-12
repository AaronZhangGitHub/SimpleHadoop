#!/usr/bin/python
import re
import sys

LOCAL_TEST_PATH = './example_input_meds.txt'
LOCAL_TEST_PATH1 = './test.txt'
def runProduction():
    for line in sys.stdin:
        #siteID and BackgroundID uniquely id a patient
        strippedLine = line.strip()
        if strippedLine!="":
            delimList = strippedLine.split(',')
            if delimList[0]!="siteId":
                outputMap(delimList[0],delimList[1], delimList[5])

#def runLocal():
#    with open (LOCAL_TEST_PATH1, "r") as f, open ("output2.txt","w") as of:
#        for line in f:
#            strippedLine = line.strip()
#            if strippedLine!="":
#                delimList = strippedLine.split(',')
#                if delimList[0] != "siteId":
#                    str = "%s%s,%s\t1\n" % (delimList[0], delimList[1], delimList[5])
#                    print str
#                    of.write(str)

def outputMap(siteID, backgroundID, medication):
    print "%s%s,%s\t1" % (siteID, backgroundID, medication)

runProduction()
