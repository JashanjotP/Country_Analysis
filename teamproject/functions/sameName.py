#!/usr/bin/env python3

#scriptAustralia.py

# Libraries
import csv

def californiaSameName ():

    maleNames = []
    sharedNames = []
    counter = 0
    numOfNames = 0
    temp = 0

    # Appends all male names to a list 
    with open ("sortedFiles/sortedMaleCali.csv") as csvData1:
        csvReader1 = csv.reader(csvData1, delimiter = ',')
        for row in csvReader1:
            if counter == 0:
                counter += 1
            else:
                maleNames.append(row[1])

    # Checks all female names if they appear in the list of male names, appends the name to a shareNames list if the name appears in the male list 
    with open ("sortedFiles/sortedFemaleCali.csv") as csvData2:
        csvReader2 = csv.reader(csvData2, delimiter = ',')
        for row in csvReader2:
            if counter == 0:
                counter += 1
            else:
                temp = maleNames.count(row[1])
                if temp > 1:
                    sharedNames.append(row[1])
                    temp = 0
                    numOfNames += 1

    # Print statements 
    if numOfNames == 0:
        print("\t[OUTPUT]: There are no names that appear in both male and female lists of Califoria names.")
    else:
        print("\t[OUTPUT]: There are " + str(numOfNames) + " names that appear in both male and female lists of Califoria names:")
        for name in sharedNames:
            print("\t", name.capitalize())

def australiaSameName():
    
    maleNames = []
    sharedNames = []
    counter = 0
    numOfNames = 0
    temp = 0
    counter2 = 1

    # Appends all male names to a list 
    with open ("sortedFiles/sortedMaleAus.csv") as csvData1:
        csvReader1 = csv.reader(csvData1, delimiter = ',')
        for row in csvReader1:
            if counter == 0:
                counter += 1
            else:
                maleNames.append(row[1])

    # Checks all female names if they appear in the list of male names, appends the name to a shareNames list if the name appears in the male list 
    with open ("sortedFiles/sortedFemaleAus.csv") as csvData2:
        csvReader2 = csv.reader(csvData2, delimiter = ',')
        for row in csvReader2:
            if counter == 0:
                counter += 1
            else:
                temp = maleNames.count(row[1])
                if temp > 1:
                    if row[1] not in sharedNames:
                        sharedNames.append(row[1])
                        numOfNames += 1
                    temp = 0

    # Print statements 
    if numOfNames == 0:
        print("\t[OUTPUT]: There are no names that appear in both male and female lists of Australia names.")
    else:
        print("\t[OUTPUT]: There are " + str(numOfNames) + " names that appear in both male and female lists of Australia names:")
        for name in sharedNames:
            print("\t", name.capitalize())