#!/usr/bin/env python3

import pandas as pd

def xLetters():
    
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
        print("\t[ERROR]: Invalid choice, Enter a or A for Australia, c or C for California: ", end = ' ')
        locationChoice = input()
    
    # User input for gender 
    print("\t[ENTER INPUT]: Enter m or M for Male, f or F for Female: ", end = ' ')
    genderChoice = input()
    # While loop that will run until the user input is valid 
    while genderChoice not in genderChoices:
        print("\t[ERROR]: Invalid choice, Enter m or M for Male, f or F for Female: ", end = ' ')
        genderChoice = input()

    # If statements that assign user inputs to integer variables, the integer variables are used for file selection and the final print statement 
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

    # User input for the number of letters in a name 
    length = input("\t[ENTER INPUT]: Enter the length of a name: ")
    while length.isdigit() == False:
        print("\t[ERROR]: Invalid choice.\n")
        length = input("\t[ENTER INPUT]: Enter the length of a name: ")

    df = pd.read_csv(files[fileSelection])
	
    df["Name Length"] = df["Name"].str.len() 
	
    df = df.loc[df["Name Length"] == int(length)]
	
    # The total number of names with X amount of letters 
    total = df.Count.sum()

    # Final function print statement (gender[], locations[], yearRanges[] are all lists that are indexed according to the integer variables assigned in lines 46 - 61)
    print("\t[OUTPUT] There are " + str(total) + " " + gender[genderPrint] + " names with " + length + " letter names in " + locations[locationPrint] + " (" + yearRanges[locationPrint] + ") \n")