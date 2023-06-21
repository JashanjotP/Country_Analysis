import pandas as pd

def userSelectionStartName():

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

    print("\t[ENTER INPUT]: Enter a letter to find the names that start with that letter: ", end = ' ')
    letter = input().lower()
    while len(letter) != 1 or not letter.isalpha():
        print("\t[ERROR]: Invalid choice, Enter a single letter: ", end = ' ')
        letter = input().lower()
    
    # #function calls    
    if (locationChoice == 'a' or locationChoice == 'A'):
        australia(genderChoice, letter)
    if (locationChoice == 'c' or locationChoice == 'C'):
        california(genderChoice, letter)



#function for australia
def australia(genderChoice, letter):

    #if statement to validate the input for males (m/M)
    if(genderChoice == 'm' or genderChoice == 'M'):
        #reads the CSV file from the given directory
        df = pd.read_csv("sortedFiles/sortedMaleAus.csv")
        
        #goes through the df and filters it depending on the condititon (the letter)
        df = df[df['Name'].str.startswith(letter, na=False)]
        
        #creates a list on the names that meet the condition
        names = list(df["Name"].unique())
        
        #prints the results
        if len(names) > 0:
            print("\t[OUTPUT]: Male names that start with", letter, "are:")
            for name in names:
                print("\t", name.capitalize())
        else:
        #will print this if there were none found
            print("\t[OUTPUT]: No male names were found that start with", letter)

    
    
    #if statement to validate the input for females (f/F)
    if(genderChoice == 'f' or genderChoice == 'F'):
        #reads the CSV file from the given directory
        df = pd.read_csv("sortedFiles/sortedFemaleAus.csv")
        
        #goes through the df and filters it depending on the condititon (the letter)
        df = df[df['Name'].str.startswith(letter, na=False)]
        
        #creates a list on the names that meet the condition
        names = list(df["Name"].unique())
        
        #prints the results
        if len(names) > 0:
            print("\t[OUTPUT]: female names that start with", letter, "are:")
            for name in names:
                print("\t", name.capitalize())
        else:
        #will print this if there were none found
            print("\t[OUTPUT]: No female names were found that start with", letter)




#function for california, the same concept as above. 
#Only changed the file it was reading and function call name.
def california(genderChoice, letter):

    #if statement to validate the input for males (m/M)
    if(genderChoice == 'm' or genderChoice == 'M'):
        df = pd.read_csv("sortedFiles/sortedMaleCali.csv")
        df = df[df['Name'].str.startswith(letter, na=False)]
        names = list(df["Name"].unique())
        
        if len(names) > 0:
            print("\t[OUTPUT]: Male names that start with", letter, "are:")
            for name in names:
                print("\t", name.capitalize())
        else:
            print("\t[OUTPUT]: No male names were found that start with", letter)

    
    
    #if statement to validate the input for females (f/F)
    if(genderChoice == 'f' or genderChoice == 'F'):
        df = pd.read_csv("sortedFiles/sortedFemaleCali.csv")
        df = df[df['Name'].str.startswith(letter, na=False)]
        names = list(df["Name"].unique())
    
        if len(names) > 0:
            print("\t[OUTPUT]: female names that start with", letter, "are:")
            for name in names:
                print("\t", name.capitalize())
        else:
            print("\t[OUTPUT]: No female names were found that start with", letter)