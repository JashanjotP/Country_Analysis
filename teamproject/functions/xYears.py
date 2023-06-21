#!/usr/bin/env python3

import pandas as pd

def xYears():

    # List of files that are accessed according to user input 
    files = ['sortedFiles/sortedMaleAus.csv', 
             'sortedFiles/sortedFemaleAus.csv', 
             'sortedFiles/sortedMaleCali.csv', 
             'sortedFiles/sortedFemaleCali.csv']

    # Lists used for the final function print statement 
    locations = ['Australia', 'California']
    gender = ['male', 'female']
    yearRanges = ['1952 - 2021', '1960 - 2021']
    
    # Lists used for input validation 
    locationChoices = ['a', 'A', 'c', 'C']
    genderChoices = ['m', 'M', 'f', 'F']
    
    # Lists used to assign user input to integer variables, the variables are used to index the lists used for the final function print statement 
    australiaLetters = ['a', 'A']
    californiaLetters = ['c', 'C']
    maleLetters = ['m', 'M']
    femaleLetters = ['f', 'F']

    # Variables used to index lists for the final function print statement 
    locationPrint = 0
    fileSelection = 0
    genderPrint = 0

    # User input for location 
    print("\t[ENTER INPUT]: Enter a or A for Australia, c or C for California: ", end = ' ')
    locationChoice = input()
    # While loop that will run until the user input is valid 
    while locationChoice not in locationChoices:
        print("\t[ERROR]:Invalid choice, Enter a or A for Australia, c or C for California: ", end = ' ')
        locationChoice = input()
    
    # User input for gender 
    print("\t[ENTER INPUT]: Enter m or M for Male, f or F for Female: ", end = ' ')
    genderChoice = input()
    # While loop that will run until the user input is valid 
    while genderChoice not in genderChoices:
        print("\t[ERROR]: Invalid choice, Enter m or M for Male, f or F for Female: ", end = ' ')
        genderChoice = input()

    # If statements that assign user inputs to integer variables, the integer variables are used to index lists that are a part of the final print statement 
    if locationChoice in australiaLetters:
        locationPrint = 0
        if genderChoice in maleLetters:
            fileSelection = 0
            genderPrint = 0
        elif genderChoice in femaleLetters:
            fileSelection = 1
            genderPrint = 1
    elif locationChoice in californiaLetters:
        locationPrint = 1
        if genderChoice in maleLetters:
            fileSelection = 2
            genderPrint = 0
        elif genderChoice in femaleLetters:
            fileSelection = 3
            genderPrint = 1

    repeatLoop = 0
    
    # User input for year 
    # If user chooses Australia 
    if locationPrint == 0:
        year = input("\t[ENTER INPUT]: Year that you would like to search [Range: " + yearRanges[locationPrint]+"]: ")
        if year.isdigit() == True:
            if int(year) not in range(1952, 2022):
                repeatLoop = 1
        while (year.isdigit() == False) or (repeatLoop == 1):
            print("\t[ERROR]: Invalid choice. ")
            year = input("\t[ENTER INPUT]: Year that you would like to search [Range: " + yearRanges[locationPrint]+"]: ")
            if (year.isdigit() == True) and int(year) in range(1952, 2022):
                repeatLoop = 0
            else:
                repeatLoop = 1

    # If user chooses California         
    elif locationPrint == 1:
        year = input("\t[ENTER INPUT]: Year that you would like to search [Range: " + yearRanges[locationPrint]+"]: ")
        if year.isdigit() == True:
            if int(year) not in range(1960, 2022):
                repeatLoop = 1
        while (year.isdigit() == False) or (repeatLoop == 1):
            print("\t[ERROR]: Invalid choice. ")
            year = input("\t[ENTER INPUT]: Year that you would like to search: [Range: " + yearRanges[locationPrint]+"]: ")
            if year.isdigit() == True:
                if int(year) in range(1960, 2022):
                    repeatLoop = 0
                else:
                    repeatLoop = 1


    df = pd.read_csv(files[fileSelection])

    df = df.loc[df['Year'] == int(year)]

    # Total number of names for X year 
    total = df.Count.sum()

    # Final function print statement 
    print("\t[OUTPUT]: There are " + str(total) + " " + gender[genderPrint] + " non unqiue names on the file for the year " + year + " in " + locations[locationPrint] + " (" + yearRanges[locationPrint] + ") " )

    