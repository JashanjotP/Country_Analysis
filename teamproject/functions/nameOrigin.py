#!/usr/bin/env python3

import pandas as pd
import csv

def nameOrigin():

    # List of files that are accessed according to user input 
    files = ['sortedFiles/sortedMaleAus.csv', 
             'sortedFiles/sortedFemaleAus.csv', 
             'sortedFiles/sortedMaleCali.csv', 
             'sortedFiles/sortedFemaleCali.csv']
    
    # List of file that are accessed according to user input 
    namesorFiles = ['uniqueNames/namesorUniqueAus.csv',
                    'uniqueNames/namesorUniqueCali.csv']
    
    # Lists used for input validation 
    locationChoices = ['a', 'A', 'c', 'C']
    genderChoices = ['m', 'M', 'f', 'F']

    # Lists used to assign user input to integer variables, the integer variables are used to index the lists used for the final function print statement 
    australiaLetters = ['a', 'A']
    californiaLetters = ['c', 'C']
    maleLetters = ['m', 'M']
    femaleLetters = ['f', 'F']

    # User input for location 
    print("\t[ENTER INPUT]: Enter a or A for Australia, c or C for California: ", end = ' ')
    locationChoice = input()
    # While loop that will run until the user input is valid 
    while locationChoice not in locationChoices:
        print("\t[ERROR]: Invalid choice, Enter a or A for Australia, c or C for California: ", end = ' ')
        locationChoice = input()
    
    # User input for gender 
    print("\t[ENTER INPUT]: Enter m or M for Male, f or F for Female: ", end = ' ')
    genderChoice = input()
    # While loop that will run until the user input is valid 
    while genderChoice not in genderChoices:
        print("\t[ERROR]: Invalid choice, Enter m or M for Male, f or F for Female: ", end = ' ')
        genderChoice = input()

    # If statements that assign user inputs to integer variables, the integer variables are used for file selection 
    if locationChoice in australiaLetters:
        locationForCSV = 0
        if genderChoice in maleLetters:
            fileSelection = 0
        elif genderChoice in femaleLetters:
            fileSelection = 1
    elif locationChoice in californiaLetters:
        locationForCSV = 1
        if genderChoice in maleLetters:
            fileSelection = 2
        elif genderChoice in femaleLetters:
            fileSelection = 3
    
    # Checks if name exists 
    df = pd.read_csv(files[fileSelection])
    names = list(df["Name"])
    
    print("\t[ENTER INPUT]: Enter a name:", end = ' ')
    nameSearch = input()
    nameSearch = nameSearch.lower()
    
    if nameSearch in names:
        print("\t[OUTPUT]: Name Exists... Searching for origin")
    else:
        print("\t[ERROR]: Name doesn't exist in the file")
        return

    # Searches through namesorUnique files to find the name's country and region origin 
    with open (namesorFiles[locationForCSV]) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            if row[0] == nameSearch:
                print("\t[OUTPUT]: The origin of the name", nameSearch, "is from", end = ' ')
                countryCode = row[4]
                subRegion = row[3]
                # Searches through the countryCodes file with the given country code to print the full country name 
                with open ('uniqueNames/countryCodes.csv') as csvDataFile2:
                    csvReader2 = csv.reader(csvDataFile2, delimiter=',')
                    for row in csvReader2:
                        if row[1] == countryCode:
                            countryCode = row[0]
                print(countryCode + ",", subRegion + ".")
                return