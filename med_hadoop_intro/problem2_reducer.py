#!/usr/bin/python

import re
import sys


def production():
    uniqueIndividuals = 0
    (lastKey, lastMedicine, count) = (None, None, 0)
    for line in sys.stdin:
        splitLine = line.strip().split("\t")
        keyLine = splitLine[0].split(",")
        key = keyLine[0]
        medicine = keyLine[1]
        val = splitLine[1]
        if key!=lastKey and medicine == "Lithium Carbonate":
            #reducerOutput(key,medicine,val)
            (lastKey,lastMedicine,count) = (key,medicine,int(val))
            uniqueIndividuals+=1
    if lastKey and medicine == "Lithium Carbonate":
        #reducerOutput(lastKey,lastMedicine,count)
        uniqueIndividuals+=1
    print uniqueIndividuals

def reducerOutput(lastKey,lastMedicine,count):
    print "%s\t%s\t%s" % (lastKey,lastMedicine,count)

#def local():
#    uniqueIndividuals = 0
#    (lastKey, lastMedicine, count) = (None, None, 0)
#    filePath = "output2.txt"
#    with open(filePath,"r") as f:
#        for line in f:
#            splitLine = line.strip().split("\t")
#            keyLine = splitLine[0].split(",")
#            key = keyLine[0]
#            medicine = keyLine[1]
#            val = splitLine[1]
#            if key!=lastKey and medicine == "Lithium Carbonate":
                #reducerOutput(key,medicine,val)
#                (lastKey,lastMedicine,count) = (key,medicine,int(val))
#                uniqueIndividuals+=1
#        if lastKey and medicine == "Lithium Carbonate":
            #reducerOutput(lastKey,lastMedicine,count)
#            uniqueIndividuals+=1
#    print uniqueIndividuals
production()
