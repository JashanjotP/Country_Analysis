import pandas as pd

def userSelectionPopularNames():

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
  
    #function calls based
    if (locationChoice == 'a' or locationChoice == 'A'):
        australia(genderChoice)
    if (locationChoice == 'c' or locationChoice == 'C'):
        california(genderChoice)


#function for australia
def australia(genderChoice):

    #if statement to validate the input for males (m/M)
    if(genderChoice == 'm' or genderChoice == 'M'):
        #reads the specified csv file
        df = pd.read_csv("sortedFiles/sortedMaleAus.csv")
        
        #will filter the dataframe and only includes the rank coloumn
        df = df.loc[df['Rank'] == 1]
        
        #sorts the data by count in descending order
        df = df.sort_values(['Count'],ascending = False)
        
        #takes the first name in the list and prints it out
        names = list(df["Name"])
        print("\t[OUTPUT]: The most popular male name in Australia is:",names[0].capitalize())
        
        
        
    #if statement to validate the input for males (f/F)
    elif(genderChoice == 'f' or genderChoice == 'F'):
        #reads the specified csv file
        df = pd.read_csv("sortedFiles/sortedFemaleAus.csv")
        
        #will filter the dataframe and only includes the rank coloumn
        df = df.loc[df['Rank'] == 1]
        
        #sorts the data by count in descending order
        df = df.sort_values(['Count'],ascending = False)
        
        #takes the first name in the list and prints it out
        names = list(df["Name"])
        print("\t[OUTPUT]: The most popular female name in Australia is:",names[0].capitalize())




#function for california, the same concept as above. 
#Only changed the file it was reading and function call name.
def california(genderChoice):

    #if statement to validate the input for males (m/M)
    if(genderChoice == 'm' or genderChoice == 'M'):
        df = pd.read_csv("sortedFiles/sortedMaleCali.csv")
        df = df.loc[df['Rank'] == 1]
        df = df.sort_values(['Count'],ascending = False)
        names = list(df["Name"])
        print("\t[OUTPUT]: The most popular male name in California is:",names[0].captialize())
    
    
    
    #if statement to validate the input for males (f/F)
    elif(genderChoice == 'f' or genderChoice == 'F'):
        df = pd.read_csv("sortedFiles/sortedFemaleCali.csv")
        df = df.loc[df['Rank'] == 1]
        df = df.sort_values(['Count'],ascending = False)
        names = list(df["Name"])
        print("\t[OUTPUT]: The most popular female name in California is:",names[0].captialize())


