#!/usr/bin/env python3
# Libraries
import pandas as pd

def userSelectionHowManyUniqueNames():

    #valid choices
    locationChoices = ['a', 'A', 'c', 'C']
    genderChoices = ['m', 'M', 'f', 'F']

    #input verifification
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
        austrliaHowManyUnique(genderChoice)
    if locationChoice == 'c' or locationChoice == 'C':
        californiaHowManyUnique(genderChoice)



#function for australia
def austrliaHowManyUnique(genderChoice):

    #if statement to validate the input for males (m/M)
    if(genderChoice == "m" or genderChoice == "M"):
        #reads the CSV file from the given directory
        df = pd.read_csv("sortedFiles/sortedMaleAus.csv")

        #counts the unique names in the name column
        uniqueCount = df['Name'].nunique()
        
        #prints the count
        print("\t[OUTPUT]: There are", uniqueCount, "unqiue Australian Male names.")



    #if statement to validate the input for males (f/F)
    if(genderChoice == "f" or genderChoice == "F"):
        #reads the CSV file from the given directory
        df = pd.read_csv("sortedFiles/sortedFemaleAus.csv")
        
        #counts the unique names in the name column
        uniqueCount = df['Name'].nunique()
        
        #prints the count
        print("\t[OUTPUT]: There are", uniqueCount, "unqiue Australian Female names.")




#function for california, the same concept as above. 
#Only changed the file it was reading and function call name.
def californiaHowManyUnique(genderChoice):

    #if statement to validate the input for males (m/M)
    if(genderChoice == "m" or genderChoice == "M"):
        df = pd.read_csv("sortedFiles/sortedMaleCali.csv")
        uniqueCount = df['Name'].nunique()
        print("\t[OUTPUT]: There are", uniqueCount, "unqiue Californian Male names.")



    #if statement to validate the input for males (f/F)
    if(genderChoice == "f" or genderChoice == "F"):
        df = pd.read_csv("sortedFiles/sortedFemaleCali.csv")
        uniqueCount = df['Name'].nunique()
        print("\t[OUTPUT]: There are", uniqueCount, "unqiue Californian Female names.")





