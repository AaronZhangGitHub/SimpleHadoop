#!/usr/bin/python
import re
import sys

def production():
    (last_genericMedName,last_siteID, lastBackgroundID, count) = (None, None, None, 0)
    personToMedication = {}
    medicationHighestUniquePatients = ""
    medicationHighestUniquePatientsCount = 0
    for line in sys.stdin:
        (genericMedName, siteID, backgroundID, val) = line.strip().split("\t")
        if last_genericMedName and (last_genericMedName!=genericMedName):
            #check if the last count is greater than the current highest count
            if len(personToMedication)>medicationHighestUniquePatientsCount:
                medicationHighestUniquePatients = genericMedName
                medicationHighestUniquePatientsCount = len(personToMedication)
                (last_genericMedName,last_siteID, lastBackgroundID, count) = (genericMedName,siteID,backgroundID,count+int(val))
                personToMedication.clear()
        else:
            personToMedication[(siteID,backgroundID)] = 1
        reducerOutput(last_siteID,lastBackgroundID,count)
    print "count: ", medicationHighestUniquePatients, medicationHighestUniquePatientsCount

def reducerOutput(siteID, backgroundID, num):
    print "%s\t%s\t%s" % (siteID,backgroundID,num)


def local():
    (last_genericMedName,last_siteID, lastBackgroundID, count) = (None, None, None, 0)
    personToMedication = {}
    medicationHighestUniquePatients = ""
    medicationHighestUniquePatientsCount = 0
    filePath = "output3.txt"
    with open(filePath,"r") as f:
        for line in f:
            (genericMedName, siteID, backgroundID, val) = line.strip().split("\t")
            if last_genericMedName and (last_genericMedName!=genericMedName):
                print "j",medicationHighestUniquePatientsCount, medicationHighestUniquePatients, len(personToMedication)
                #check if the last count is greater than the current highest count
                if len(personToMedication)>medicationHighestUniquePatientsCount:
                    print personToMedication
                    print '\t',last_genericMedName, genericMedName, len(personToMedication), medicationHighestUniquePatients, medicationHighestUniquePatientsCount
                    medicationHighestUniquePatients = last_genericMedName
                    medicationHighestUniquePatientsCount = len(personToMedication)
                    (last_genericMedName,last_siteID, lastBackgroundID, count) = (genericMedName,siteID,backgroundID,int(val))
                    personToMedication.clear()
                    print len(personToMedication)
                else:
                    personToMedication.clear()
                    (last_genericMedName,last_siteID, lastBackgroundID, count) = (genericMedName,siteID,backgroundID,int(val))
                    personToMedication[(siteID,backgroundID)] = 1
            else:
                personToMedication[(siteID,backgroundID)] = 1
                (last_genericMedName,last_siteID, lastBackgroundID, count) = (genericMedName,siteID,backgroundID,int(val))
            #reducerOutput(last_siteID,lastBackgroundID,count)
        print "count: ", medicationHighestUniquePatients, medicationHighestUniquePatientsCount
local()
