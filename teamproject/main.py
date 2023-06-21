#!/usr/bin/env python3

#run command: ./main.py -a aus.csv -b cali.csv

# Libraries
import os
import sys
import getopt
import csv
import termios
import pandas as pd
import signal

# Reading files and functions 
from reader.scriptCalifornia import readFromFile
from reader.scriptAustralia import readFromFile2
from functions.sameName import californiaSameName, australiaSameName
from functions.xLetters import xLetters
from functions.xYears import xYears
from functions.howManyUniqueNames import userSelectionHowManyUniqueNames
from functions.howManyNames import userSelectionHowManyNames
from functions.popularNames import userSelectionPopularNames
from functions.graph import printGraph
from functions.xStartName import userSelectionStartName
from functions.xLetterUnqiueNames import userSelectionxLetterUniqueNames
from functions.nameOrigin import nameOrigin

def main (argv):
    
    # Blocks user input durring file read
    s = signal.signal(signal.SIGINT, signal.SIG_IGN)
    os.system("stty -echo")

    # Read command line
    if argv != ['-a', 'aus.csv', '-b', 'cali.csv']:
        print ( "[ERROR] Usage: ./main.py -a <input file name> -b <input file name>" )
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt ( argv,"a:b:",["input="] )
    except getopt.GetoptError:
        print ( "[ERROR] Usage: ./main.py -a <input file name> -b <input file name>" )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./main.py -a <input file name> -b <input file name>" )
            sys.exit()
        elif opt in ( "-a", "--input1"):
            inputFileName1 = arg #passed into function
        elif opt in ( "-b", "--input2"):
            inputFileName2 = arg #passed into function
            
    print("[READER]: Reading from aus.csv") 
    readFromFile2(inputFileName1) #function call read from aus.csv
    print("[READER]: Reading from cali.csv") 
    readFromFile(inputFileName2) #function call read from cali.csv 

    userChoice = 'y'
    userNumChoice = 0
    
    os.system("stty echo")
    termios.tcflush(sys.stdin, termios.TCIOFLUSH)
	
    whileLoopChoices = ['y', 'Y']

    # User input and validation
    while userChoice in whileLoopChoices:
        
        print("Choose a function [1->11]:")
        print("\t[Function 1]: Prints the names that start with 'x' letter.")
        print("\t[Function 2]: Prints the total number of names from both male and females.")
        print("\t[Function 3]: Prints the most popular name in the country/province.")
        print("\t[Function 4]: Prints the names that appear in both male and female lists of a country.")
        print("\t[Function 5]: Prints the number of unique names from both male and females.")
        print("\t[Function 6]: Prints the number of non-unique names specified year.")
        print("\t[Function 7]: Prints the total number of names that are 'x' letters long.")
        print("\t[Function 8]: Prints the number of unique names that are 'x' letters long.")
        print("\t[Function 9]: Prints a graph of the amount of people that have 'x' name(s) over time.")
        print("\t[Function 10]: Prints the origin of 'x' name using Namsor.")
        print("\t[Exit]: Press 11 to exit the program")
        userNumChoice = input("[ENTER INPUT]: Enter a value between [1->11] ")
        
        if userNumChoice == '1':
            userSelectionStartName() 
        elif userNumChoice == '2':
            userSelectionHowManyNames() 
        elif userNumChoice == '3':
            userSelectionPopularNames() 
        elif userNumChoice == '4':
            californiaSameName() 
            australiaSameName() 
        elif userNumChoice == '5':
           userSelectionHowManyUniqueNames() 
        elif userNumChoice == '6':
            xYears() 
        elif userNumChoice == '7':
            xLetters() 
        elif userNumChoice == '8':
            userSelectionxLetterUniqueNames() 
        elif userNumChoice == '9':
            printGraph() 
        elif userNumChoice == '10':
            nameOrigin() 
        elif userNumChoice == '11':
            sys.exit()
        else:
            print("[ERROR]: Invalid input")
        
        print("[ENTER INPUT]: Do you want to continue or exit? (enter y or Y for yes, n or N for no):", end = ' ')
        
        userChoice = input()
        possibleChoices = ['y', 'Y', 'n', 'N']
        
        while userChoice not in possibleChoices:
            print("[ERROR]: Invalid choice, enter choice again (Type y or Y for yes, n or N for no):", end = ' ')
            userChoice = input()

        signal.signal(signal.SIGINT, s)

#End of main
if __name__ == "__main__":
    main ( sys.argv[1:] )
    