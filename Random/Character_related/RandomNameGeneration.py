#!/usr/bin/python3
from random import randint, randrange
import os
import sys, getopt

dictionary = {
    '20':['20th-Century-Modern', 'Single'],
    'AA':['African-American', 'Single'],
    'AM':['Arabic-Muslim', 'Single'],
    'CH':['Chinese', 'Single'],
    'CR':['Croatian', 'Single'],
    'CZ':['Czech', 'Multiple'],
    'DU':['Dutch', 'Single'],
    'FI':['Filipino', 'Long'],
    'GE':['German', 'Single'],
    'HI':['Hispanic', 'Single'],
    'HU':['Hungary', 'Single'],
    'IR':['Irish', 'Single'],
    'IT':['Italian', 'Single'],
    'JM':['Jamaican', 'Single'],
    'JP':['Japan', 'Single'],
} 

class NamesFiles:
    def __init__(self, first, surname):
        self.male = 'Datasets/First_Names/' + dictionary[first][0] + '-M.txt'
        self.female = 'Datasets/First_Names/' + dictionary[first][0] + '-F.txt'
        if (dictionary[surname][1] == 'Single'):
            self.surname = 'Datasets/Last_Names/' + dictionary[surname][0] + '.txt'
        elif(dictionary[surname][1] == 'Multiple'):
            self.surnameMale = 'Datasets/Last_Names/' + dictionary[surname][0] + '-M.txt'
            self.surnameFemale = 'Datasets/Last_Names/' + dictionary[surname][0] + '-F.txt'   
        elif(dictionary[surname][1] == 'Long'):
            self.surnameMiddle = 'Datasets/Last_Names/' + dictionary[surname][0] + '-M.txt'
            self.surnameLong = 'Datasets/Last_Names/' + dictionary[surname][0] + '-L.txt'   

class NameList:
    firstFemaleList = []
    firstFemaleLen = 0
    firstMaleList = []
    firstMaleLen = 0
    surnameMiddleList = []
    surnameMiddleLen = 0
    surnameMaleList = []
    surnameMaleLen = 0
    surnameFemaleList = []
    surnameFemaleLen = 0
    surnameLongList = []
    surnameLongLen = 0
    def __init__(self) -> None:
        pass
    
    def SinglesFile(self, surnameMiddleFile, maleFile, femaleFile):
        self.firstFemaleList = femaleFile.readlines()
        self.firstFemaleLen = len(self.firstFemaleList)
        self.firstMaleList = maleFile.readlines()
        self.firstMaleLen = len(self.firstMaleList)
        self.surnameMiddleList = surnameMiddleFile.readlines()
        self.surnameMiddleLen = len(self.surnameMiddleList)
    
    def MultiplesFile(self, surnameMaleFile, surnameFemaleFile, maleFile, femaleFile):
        self.firstFemaleList = femaleFile.readlines()
        self.firstFemaleLen = len(self.firstFemaleList)
        self.firstMaleList = maleFile.readlines()
        self.firstMaleLen = len(self.firstMaleList)
        self.surnameFemaleList = surnameFemaleFile.readlines()
        self.surnameFemaleLen = len(self.surnameFemaleList)
        self.surnameMaleList = surnameMaleFile.readlines()
        self.surnameMaleLen = len(self.surnameMaleList)
    
    def LongsFile(self, surnameLongFile, surnameMiddleFile, maleFile, femaleFile):
        self.firstFemaleList = femaleFile.readlines()
        self.firstFemaleLen = len(self.firstFemaleList)
        self.firstMaleList = maleFile.readlines()
        self.firstMaleLen = len(self.firstMaleList)
        self.surnameMiddleList = surnameMiddleFile.readlines()
        self.surnameMiddleLen = len(self.surnameMiddleList)
        self.surnameLongList = surnameLongFile.readlines()
        self.surnameLongLen = len(self.surnameLongList)

def constructSinglesName(firstNamesList, firstNamesLen, lastNamesList, lastNamesLen):
    return firstNamesList[randrange(0, firstNamesLen)].rstrip() + ' ' + lastNamesList[randrange(0, lastNamesLen)].rstrip()

def constructMultiplesName(firstNamesList, firstNamesLen, lastNamesList, lastNamesLen):
    return constructSinglesName(firstNamesList, firstNamesLen, lastNamesList, lastNamesLen)

def constructLongsName(firstNamesList, firstNamesLen, middleNamesList, middleNamesLen, lastNamesList, lastNamesLen):
    return firstNamesList[randrange(0, firstNamesLen)].rstrip()+ ' ' + firstNamesList[randrange(0, firstNamesLen)].rstrip() + ' ' + middleNamesList[randrange(0, middleNamesLen)].rstrip() + ' ' + lastNamesList[randrange(0, lastNamesLen)].rstrip()

def generateNames(first: str, surn: str, gender: str, number: int):
    result = []    
    files = NamesFiles(first, surn)
    lists = NameList()
    if (dictionary[surn][1] == 'Single'):
        with open(files.surname, 'r') as surnameFile, open(files.male, 'r') as maleFile, open(files.female, 'r') as femaleFile:              
            lists.SinglesFile(surnameFile, maleFile, femaleFile)
            for i in range(0, number):
                if gender == 'C':
                    if randint(0,1) == 0:
                        result.append(constructSinglesName(lists.firstMaleList, lists.firstMaleLen, lists.surnameMiddleList, lists.surnameMiddleLen))
                    else:
                        result.append(constructSinglesName(lists.firstFemaleList, lists.firstFemaleLen, lists.surnameMiddleList, lists.surnameMiddleLen))
                elif gender == 'M':
                    result.append(constructSinglesName(lists.firstMaleList, lists.firstMaleLen, lists.surnameMiddleList, lists.surnameMiddleLen))
                else:
                    result.append(constructSinglesName(lists.firstFemaleList, lists.firstFemaleLen, lists.surnameMiddleList, lists.surnameMiddleLen))
            
    elif (dictionary[surn][1] == 'Multiple'):
        with open(files.surnameMale, 'r') as surnameMaleFile, open(files.surnameFemale, 'r') as surnameFemaleFile, open(files.male, 'r') as maleFile, open(files.female, 'r') as femaleFile:
            lists.MultiplesFile(surnameMaleFile, surnameFemaleFile, maleFile, femaleFile)
            for i in range(0, number):
                if gender == 'C':
                    if randint(0,1) == 0:
                        result.append(constructMultiplesName(lists.firstMaleList, lists.firstMaleLen, lists.surnameMaleList, lists.surnameMaleLen))
                    else:
                        result.append(constructMultiplesName(lists.firstFemaleList, lists.firstFemaleLen, lists.surnameFemaleList, lists.surnameFemaleLen))
                elif gender == 'M':
                    result.append(constructMultiplesName(lists.firstMaleList, lists.firstMaleLen, lists.surnameMaleList, lists.surnameMaleLen))
                else:
                    result.append(constructMultiplesName(lists.firstFemaleList, lists.firstFemaleLen, lists.surnameFemaleList, lists.surnameFemaleLen))
    elif (dictionary[surn][1] == 'Long'):
        with open(files.surnameLong, 'r') as surnameLongFile, open(files.surnameMiddle, 'r') as surnameMiddleFile, open(files.male, 'r') as maleFile, open(files.female, 'r') as femaleFile:
            lists.LongsFile(surnameLongFile, surnameMiddleFile, maleFile, femaleFile)
            for i in range(0, number):
                if gender == 'C':
                    if randint(0,1) == 0:
                        result.append(constructLongsName(lists.firstMaleList, lists.firstMaleLen, lists.surnameMiddleList, lists.surnameMiddleLen, lists.surnameLongList, lists.surnameLongLen))
                    else:
                        result.append(constructLongsName(lists.firstFemaleList, lists.firstFemaleLen, lists.surnameMiddleList, lists.surnameMiddleLen, lists.surnameLongList, lists.surnameLongLen))
                elif gender == 'M':
                    result.append(constructLongsName(lists.firstMaleList, lists.firstMaleLen, lists.surnameMiddleList, lists.surnameMiddleLen, lists.surnameLongList, lists.surnameLongLen))
                else:
                    result.append(constructLongsName(lists.firstFemaleList, lists.firstFemaleLen, lists.surnameMiddleList, lists.surnameMiddleLen, lists.surnameLongList, lists.surnameLongLen))
    return result




def main(argv):
    # initialize variables
    firstname = ''
    surname = ''
    gender = 'M'
    namesNumber = 10
    try:
      opts, args = getopt.getopt(argv,"hf:s:g:n:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('Some error happened, please consult -h for more information')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ("""
            Script generates a number of names, with combination of first name and surname of your choosing.
            This script was created to generate number, combination names of different nationalities, like firstname African-American and surname Irish.
            -f      option of which first names to generate.
            -s      option of which surnames to generate, if this option is not specified then it will generate the same ethnicity as first name.
            -g      gender of names to choose. If not specified, it will create male names. (M - male, F - female, C - combo) #Will be changed to make a combo.
            -n      number of names that will be generated. Default is set to 10.

            options 
                20 - 20th century American-English names
                AA - African-American                
            """)
            sys.exit(0)
        if opt == '-f':
            firstname = arg
            surname = arg
        if opt == '-s':
            surname = arg
        if opt == '-g':
            gender = arg
        if opt == '-n':
            namesNumber = arg
    listOfNames = generateNames(firstname, surname, gender, int(namesNumber))
    for name in listOfNames:
        print(name)


if __name__ == '__main__':
    main(sys.argv[1:])