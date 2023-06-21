#!/usr/bin/env python3
# Libraries
import pandas as pd

def userSelectionHowManyNames():

    locationChoices = ['a', 'A', 'c', 'C']
    genderChoices = ['m', 'M', 'f', 'F']

    print("\t[ENTER INPUT]: Enter a or A for Australia, c or C for California: ", end = ' ')
    locationChoice = input()
    while locationChoice not in locationChoices:
        print("\t[ERROR]: Invalid choice, Enter a or A for Australia, c or C for California: ", end = ' ')
        locationChoice = input()
    
    print("\t[ENTER INPUT]: Enter m or M for Male, f or F for Female: ", end = ' ')
    genderChoice = input()
    while genderChoice not in genderChoices:
        print("\t[ERROR]: Invalid choice, Enter m or M for Male, f or F for Female: ", end = ' ')
        genderChoice = input()
  
    #function calls
    if locationChoice == 'a' or locationChoice == "A":
        austrliaHowMany(genderChoice)
    if locationChoice == 'c' or locationChoice == 'C':
        californiaHowMany(genderChoice)



#function for australia
def austrliaHowMany(genderChoice):

    #if statement to validate the input for males (m/M)
    if(genderChoice == "m" or genderChoice == "M"):
        #reads from the specified .csv file
        df = pd.read_csv("sortedFiles/sortedMaleAus.csv")
        
        #gets the total amount of names in the dataframe
        count = df['Name'].count()
        
        #print
        print("\t[OUTPUT]: There are", count, "non-unique Australian Male names.")



    #if statement to validate the input for females (f/F)
    if(genderChoice == "f" or genderChoice == "F"):
        #reads from the specified .csv file
        df = pd.read_csv("sortedFiles/sortedFemaleAus.csv")
        
        #gets the total amount of names in the dataframe
        count = df['Name'].count()
        
        #print
        print("\t[OUTPUT]: There are", count, "non-unique Australian Female names.")




#function for california, the same concept as above. 
#Only changed the file it was reading and function call name.
def californiaHowMany(genderChoice):

    #if statement to validate the input for males (m/M)
    if(genderChoice == "m" or genderChoice == "M"):
        df = pd.read_csv("sortedFiles/sortedMaleCali.csv")
        count = df['Name'].count()
        print("\t[OUTPUT]: There are", count, "non-unique Californian Male names.")



    #if statement to validate the input for females (f/F)
    if(genderChoice == "f" or genderChoice == "F"):
        df = pd.read_csv("sortedFiles/sortedFemaleCali.csv")
        count = df['Name'].count()
        print("\t[OUTPUT]: There are", count, "non-unique Californian Female names.")




