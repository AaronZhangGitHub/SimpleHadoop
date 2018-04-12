#!/usr/bin/python
import re
import sys

def production():
    #this code is trash and needs refactoring 
    (last_genericMedName, last_key, count) = (None, None, 0)
    personToMedication = {}
    medicationHighestUniquePatients = ""
    medicationHighestUniquePatientsCount = 0
    for line in sys.stdin:
        splitLine = line.strip().split("\t")
        keyLine = splitLine[0]
        val = splitLine[1]
        genericMedName = keyLine.split(",")[0]
        key = keyLine.split(",")[1]
        if last_genericMedName and (last_genericMedName!=genericMedName):
            #check if the last count is greater than the current highest count
            if len(personToMedication)>medicationHighestUniquePatientsCount:
                medicationHighestUniquePatients = last_genericMedName
                medicationHighestUniquePatientsCount = len(personToMedication)
                (last_genericMedName,last_key, count) = (genericMedName,key,int(val))
                personToMedication.clear()
                personToMedication[key] = 1
            else:
                (last_genericMedName,last_key, count) = (genericMedName,key,int(val))
                personToMedication[key] = 1
        else:
            personToMedication[key] = 1
            (last_genericMedName, last_key, count) = (genericMedName, key,int(val))
        #reducerOutput(last_siteID,lastBackgroundID,count)
    if len(personToMedication)>medicationHighestUniquePatientsCount:
        medicationHighestUniquePatients = last_genericMedName
        medicationHighestUniquePatientsCount = len(personToMedication)
    print "Medication prescribed to highest # of unique patients: ", medicationHighestUniquePatients, medicationHighestUniquePatientsCount

def reducerOutput(siteID, backgroundID, num):
    print "%s\t%s\t%s" % (siteID,backgroundID,num)


#def local():
#    (last_genericMedName, last_key, count) = (None, None, 0)
#    personToMedication = {}
#    medicationHighestUniquePatients = ""
#    medicationHighestUniquePatientsCount = 0
#    filePath = "output3.txt"
#    with open(filePath,"r") as f:
#        for line in f:
#            splitLine = line.strip().split("\t")
#            keyLine = splitLine[0]
#            val = splitLine[1]
#            genericMedName = keyLine.split(",")[0]
#            key = keyLine.split(",")[1]
#            if last_genericMedName and (last_genericMedName!=genericMedName):
                #check if the last count is greater than the current highest count
#                if len(personToMedication)>medicationHighestUniquePatientsCount:
#                    medicationHighestUniquePatients = last_genericMedName
#                    medicationHighestUniquePatientsCount = len(personToMedication)
#                    (last_genericMedName,last_key, count) = (genericMedName,key,int(val))
#                    personToMedication.clear()
#                    personToMedication[key] = 1
#                else:
#                    (last_genericMedName,last_key, count) = (genericMedName,key,int(val))
#                    personToMedication[key] = 1
#            else:
#                personToMedication[key] = 1
#                (last_genericMedName, last_key, count) = (genericMedName, key,int(val))
            #reducerOutput(last_siteID,lastBackgroundID,count)
#        if len(personToMedication)>medicationHighestUniquePatientsCount:
#            medicationHighestUniquePatients = last_genericMedName
#            medicationHighestUniquePatientsCount = len(personToMedication)
#        print "Medication prescribed to highest # of unique patients: ", medicationHighestUniquePatients, medicationHighestUniquePatientsCount
production()
