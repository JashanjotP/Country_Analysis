#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

def printGraph():
    
    
    # List of files that are accessed according to user input 
    files = ['sortedFiles/sortedMaleAus.csv', 
             'sortedFiles/sortedFemaleAus.csv', 
             'sortedFiles/sortedMaleCali.csv', 
             'sortedFiles/sortedFemaleCali.csv']

    # Lists used for the graph 
    regions = ['Australia', 'California']
    
    # Lists used for input validation 
    locationChoices = ['a', 'A', 'c', 'C']
    genderChoices = ['m', 'M', 'f', 'F']

    # Lists used to assign user input to integer variables 
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

    # If statements that assign user inputs to integer variables, the integer variables are used for file selection and the graph 
    if locationChoice in australiaLetters:
        regionPrint = 0
        if genderChoice in maleLetters:
            fileSelection = 0
        elif genderChoice in femaleLetters:
            fileSelection = 1
    elif locationChoice in californiaLetters:
        regionPrint = 1
        if genderChoice in maleLetters:
            fileSelection = 2
        elif genderChoice in femaleLetters:
            fileSelection = 3
    
    # Lists with the years for Australia and California which are used to assign a number of people that have the inputted name to each year 
    if locationChoice in australiaLetters:
        array = ([1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 
                  1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 
                  1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 
                  1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 
                  2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])
    elif locationChoice in californiaLetters:
        array = ([1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 
                  1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 
                  1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 
                  2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 
                  2016, 2017, 2018, 2019, 2020, 2021])

    # Checks if name exists 
    df = pd.read_csv(files[fileSelection])
    names = list(df["Name"])
    
    print("\t[ENTER INPUT]: Enter a name:", end = ' ')
    nameSearch = input()
    nameSearch = nameSearch.lower()
    
    if nameSearch in names:
        print("\t[OUTPUT]: Name Exists, generating graph")
    else:
        print("\t[ERROR]: Name doesn't exist in the file")
        return

    nameCount = []
    year = array[-1]
    counter = 1
    nameChanged = 0

    # Goes through the entire name data file and finds the inputted name and the amount of people that have the name each year  
    with open (files[fileSelection]) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            if counter != 1:
                if int(row[4]) == year:
                    if row[1] == nameSearch:
                        nameCount.append(int(row[2]))
                        nameChanged = 1
                else:
                    year -= 1
                    if row[1] == nameSearch:
                        nameCount.append(int(row[2]))
                        nameChanged = 1
                    if nameChanged == 0:
                        nameCount.append(0)
                    nameChanged = 0

            else:
                counter += 1

    # Makes sure list of names and list of amount of people with the name are the same length 
    while len(array) != len(nameCount):
        if len(array) > len(nameCount):
            array.pop(-1)
        else:
            nameCount.pop(-1)

    #print(nameCount)
    
    array.reverse()

    nameSearch = nameSearch.capitalize()

    # Graph the data 
    x = np.array(array)    
    y = np.array(nameCount)
    plt.plot(x, y, label = nameSearch + " (" + regions[regionPrint] + ")")
    plt.legend(loc="upper right")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Popularity of entered name(s) over time")
    plt.savefig("graph/graph.png")

    print("\t[OUTPUT]: Graph has been generated in graph folder \n")
