#!/usr/bin/env python3

import pandas as pd

def userSelectionxLetterUniqueNames():

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
    if (locationChoice == 'a' or locationChoice == 'A'):
        australia(genderChoice)
    if (locationChoice == 'c' or locationChoice == 'C'):
        california(genderChoice)



#function for australia
def australia(genderChoice):
    
    #if statement to validate the input for males (m/M)
    if(genderChoice == 'm' or genderChoice == 'M'):
        #takes user input for the wanted length
        length = input("\t[ENTER INPUT]: Enter the amount of letters: ")
        
        #input validation
        while length.isdigit() == False:
            print("\t[ERROR]: Invalid choice. ", end = ' ')
            length = input("\t[ENTER INPUT]: Enter the amount of letters in name: ")
            
        #reads from the specified csv file
        df = pd.read_csv("sortedFiles/sortedMaleAus.csv")
        
        #adds a new column so it can store the length
        df["Name Length"] = df["Name"].str.len() 
        
        #filters the dataframe and only takes the rows that match the length
        df = df.loc[df["Name Length"] == int(length)]
        
        #adds up the unique names
        Names = df["Name"].values.tolist()
        uniqueName = []
        for x in Names:
            if x not in uniqueName:
                uniqueName.append(x)
                
        #total count of unique names
        Total = len(uniqueName)
        
        #print
        print("\t[OUTPUT]: There are "+str(Total)+" unique names in this files that have "+length+" characters and they are all printed below")
        uniqueName = [i.title() for i in uniqueName]
        for x in uniqueName:
            print(x)
    
    
    
    #if statement to validate the input for females (f/F)
    if(genderChoice == 'f' or genderChoice == 'F'):
        #takes user input for the wanted length
        length = input("Enter the amount of letters: ")
        
        #input validation
        while length.isdigit() == False:
            print("\t[ERROR]: Invalid choice.")
            length = input("\t[ENTER INPUT]: Enter the amount of letters in name: ")
            
        #reads from the specified csv file
        df = pd.read_csv("sortedFiles/sortedFemaleAus.csv")
        
        #adds a new column so it can store the length
        df["Name Length"] = df["Name"].str.len() 
        
        #filters the dataframe and only takes the rows that match the length
        df = df.loc[df["Name Length"] == int(length)]
        
        #adds up the unique names
        Names = df["Name"].values.tolist()
        uniqueName = []
        for x in Names:
            if x not in uniqueName:
                uniqueName.append(x)
                
        #total count of unique names
        Total = len(uniqueName)
        
        #print
        print("\t[ENTER INPUT]: There are "+str(Total)+" unique names in this files that have "+length+" characters and they are all printed below")
        uniqueName = [i.title() for i in uniqueName]
        for x in uniqueName:
            print(x)




#function for california, the same concept as above. 
#Only changed the file it was reading and function call name.
def california(genderChoice):

    #if statement to validate the input for males (m/M)
    if(genderChoice == 'm' or genderChoice == 'M'):
        length = input("Enter the amount of letters: ")
        while length.isdigit() == False:
            print("Invalid choice. ", end = ' ')
            length = input("Enter the amount of letters in name: ")
        df = pd.read_csv("sortedFiles/sortedMaleCali.csv")
        df["Name Length"] = df["Name"].str.len() 
        df = df.loc[df["Name Length"] == int(length)]
        Names = df["Name"].values.tolist()
        uniqueName = []
        for x in Names:
            if x not in uniqueName:
                uniqueName.append(x)
        Total = len(uniqueName)
        print("There are "+str(Total)+" unique names in this files that have "+length+" characters and they are all printed below")
        uniqueName = [i.title() for i in uniqueName]
        for x in uniqueName:
            print(x)
    
    
    
    #if statement to validate the input for females (f/F)
    if(genderChoice == 'f' or genderChoice == 'F'):
        length = input("Enter the amount of letters: ")
        while length.isdigit() == False:
            print("Invalid choice. ", end = ' ')
            length = input("Enter the amount of letters in name: ")
        df = pd.read_csv("sortedFiles/sortedFemaleCali.csv")
        df["Name Length"] = df["Name"].str.len() 
        df = df.loc[df["Name Length"] == int(length)]
        Names = df["Name"].values.tolist()
        uniqueName = []
        for x in Names:
            if x not in uniqueName:
                uniqueName.append(x)
        Total = len(uniqueName)
        print("There are "+str(Total)+" unique names in this files that have "+length+" characters and they are all printed below")
        uniqueName = [i.title() for i in uniqueName]
        for x in uniqueName:
            print(x)