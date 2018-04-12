#!/usr/bin/python
import re
import sys
import operator

def production():
    (lastSiteID, lastBackgroundID, lastMedication) = (None, None, None)
    medicationToOccurences = {}
    for line in sys.stdin:
        splitLine = line.strip().split("\t")
        keyLine = splitLine[0].split(",")
        val = splitLine[1]
        siteID = keyLine[0]
        backgroundID = keyLine[1]
        medication = keyLine[2]
        #print siteID, backgroundID, medication, val
        #print lastSiteID, lastBackgroundID, lastMedication
        #dict from medication to occurences, addition if unique siteID and backgroundID...
        #on new siteID, find the dictionary key with highest value and output
        if lastSiteID and lastBackgroundID and lastMedication:
            #print lastSiteID, siteID
            if lastSiteID!=siteID:
                #New site
                #find key with highest val
                if len(medicationToOccurences)!=0:
                    highestOccurence = max(medicationToOccurences.iteritems(), key=operator.itemgetter(1))[0]
                    print lastSiteID,": ",highestOccurence, "Occurences: ", medicationToOccurences[highestOccurence]
                #clear dictionary
                medicationToOccurences.clear()
                medicationToOccurences[medication] = 1
            elif lastBackgroundID!=backgroundID or lastMedication!=medication:
                if medication not in medicationToOccurences:
                    #New entry
                    #print "\tnew entry"
                    medicationToOccurences[medication] = 1
                else:
                    #Add to existing entry
                    #print "\texisting entry"
                    occurences = medicationToOccurences[medication]
                    medicationToOccurences[medication] = occurences+1
        else:
            medicationToOccurences[medication] = 1
        (lastSiteID, lastBackgroundID, lastMedication) = (siteID, backgroundID, medication)
    if len(medicationToOccurences)>0:
        highestOccurence = max(medicationToOccurences.iteritems(), key=operator.itemgetter(1))[0]
        print lastSiteID,": ",highestOccurence, "Occurences: ", medicationToOccurences[highestOccurence]
#def local():
#    filePath = "output5.txt"
#    (lastSiteID, lastBackgroundID, lastMedication) = (None, None, None)
#    medicationToOccurences = {}
#    with open(filePath,"r") as f:
#        for line in f:
#            splitLine = line.strip().split("\t")
#            keyLine = splitLine[0].split(",")
#            val = splitLine[1]
#            siteID = keyLine[0]
#            backgroundID = keyLine[1]
#            medication = keyLine[2]
            #print siteID, backgroundID, medication, val
            #print lastSiteID, lastBackgroundID, lastMedication
            #dict from medication to occurences, addition if unique siteID and backgroundID...
            #on new siteID, find the dictionary key with highest value and output
#            if lastSiteID and lastBackgroundID and lastMedication:
                #print "\t",lastSiteID, siteID
#                if lastSiteID!=siteID:
                    #New site
                    #find key with highest val
#                    if len(medicationToOccurences)!=0:
#                        highestOccurence = max(medicationToOccurences.iteritems(), key=operator.itemgetter(1))[0]
#                        print lastSiteID,": ",highestOccurence, "Occurences: ", medicationToOccurences[highestOccurence]
#                        medicationToOccurences.clear()
#                    medicationToOccurences[medication] = 1
#                elif lastBackgroundID!=backgroundID or lastMedication!=medication:
#                    if medication not in medicationToOccurences:
                        #New entry
                        #print "\tnew entry"
#                        medicationToOccurences[medication] = 1
#                    else:
                        #Add to existing entry
                        #print "\texisting entry"
#                        occurences = medicationToOccurences[medication]
#                        medicationToOccurences[medication] = occurences+1
#            else:
#                medicationToOccurences[medication] = 1
#            (lastSiteID, lastBackgroundID, lastMedication) = (siteID, backgroundID, medication)
#        if len(medicationToOccurences)>0:
#            highestOccurence = max(medicationToOccurences.iteritems(), key=operator.itemgetter(1))[0]
#            print lastSiteID,": ",highestOccurence, "Occurences: ", medicationToOccurences[highestOccurence]
production()
