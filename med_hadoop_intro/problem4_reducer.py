#!/usr/bin/python
import re
import sys

def local():
    filePath = "output4.txt"
    with open(filePath,"r") as f:
        patientsOnBothMedications = []
        patientOnLithCar = {}
        patientOnRisperal = {}
        for line in f:
            splitLine = line.strip().split("\t")
            print splitLine
            keyLine = splitLine[0]
            key = keyLine.split(",")[0]
            medicine = keyLine.split(",")[1]
            val = splitLine[1]
            if medicine.lower() == "lithium carbonate":
                #add to LC dict
                patientOnLithCar[key] = 1
            elif medicine.lower() == "risperal":
                #add to LC dict
                patientOnRisperal[key] = 1
        for patient in patientOnLithCar:
            if patient in patientOnRisperal.keys():
                patientsOnBothMedications.append(patient)
        print patientsOnBothMedications

def production():
    patientsOnBothMedications = []
    patientOnLithCar = {}
    patientOnRisperal = {}
    for line in sys.stdin:
        splitLine = line.strip().split("\t")
        key = splitLine[0]
        medicine = splitLine[1]
        if medicine.lower() == "lithium carbonate":
            #add to LC dict
            patientOnLithCar[key] = 1
        elif medicine.lower() == "risperal":
            #add to LC dict
            patientOnRisperal[key] = 1
    for patient in patientOnLithCar:
        if patient in patientOnRisperal.keys():
            patientsOnBothMedications.append(patient)
    print patientsOnBothMedications

local()
