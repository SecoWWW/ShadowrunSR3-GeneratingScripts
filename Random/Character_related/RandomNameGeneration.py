#!/usr/bin/python3
from random import randint, randrange
import os
import sys, getopt

dictionary = {
    '20':['20th-Century-Modern', 'Dual'],
    'AA':['African-American', 'Dual'],
    'AM':['Arabic-Muslim', 'Dual'],
    'CH':['Chinese', 'Dual'],
    'CR':['Croatian', 'Dual'],
    'CZ':['Czech', 'Multiple'],
    'DU':['Dutch', 'Dual'],
    'FI':['Filipino', 'Long'],
    'GE':['German', 'Dual'],
    'HI':['Hispanic', 'Dual'],
    'HU':['Hungary', 'Dual'],
    'IR':['Irish', 'Dual'],
    'IT':['Italian', 'Dual'],
    'JM':['Jamaican', 'Dual'],
    'JP':['Japan', 'Dual'],
    'NA':['Native-American', 'Simple'],
    'NO':['Norwegian', 'Dual'],
    'PA':['Pakistani', 'Dual'],
    'PO':['Polish', 'Multiple'],
    'RU':['Russia', 'Multiple'],
    'SC':['Scottish', 'Dual'],
    'VE':['Vietnamese', 'Dual'],
    'WE':['Welsh', 'Dual']
} 

def getPossibleEthnicities():
    return list(dictionary.keys())

class NamesFiles:
    def __init__(self, first, surname):
        self.male = 'Datasets/First_Names/' + dictionary[first][0] + '-M.txt'
        self.female = 'Datasets/First_Names/' + dictionary[first][0] + '-F.txt'
        if (dictionary[surname][1] == 'Dual'):
            self.surname = 'Datasets/Last_Names/' + dictionary[surname][0] + '.txt'
        elif(dictionary[surname][1] == 'Multiple'):
            self.surnameMale = 'Datasets/Last_Names/' + dictionary[surname][0] + '-M.txt'
            self.surnameFemale = 'Datasets/Last_Names/' + dictionary[surname][0] + '-F.txt'   
        elif(dictionary[surname][1] == 'Long'):
            self.surnameMiddle = 'Datasets/Last_Names/' + dictionary[surname][0] + '-M.txt'
            self.surnameLong = 'Datasets/Last_Names/' + dictionary[surname][0] + '-L.txt'   
        elif(dictionary[surname][1] == 'Long-Multiple'):
            self.malePatronymic = 'Datasets/First_Names/' + dictionary[first][0] + '-M-P.txt'
            self.femalePatronymic = 'Datasets/First_Names/' + dictionary[first][0] + '-F-P.txt'
            self.surnameMale = 'Datasets/Last_Names/' + dictionary[surname][0] + '-M.txt'
            self.surnameFemale = 'Datasets/Last_Names/' + dictionary[surname][0] + '-F.txt'   
            

class NameList:
    # First names
    firstFemaleList = []
    firstFemaleLen = 0
    firstMaleList = []
    firstMaleLen = 0
    # Just Surnames, but Filipino have a middle surname
    surnameMiddleList = []
    surnameMiddleLen = 0
    # Surnames for different gender
    surnameMaleList = []
    surnameMaleLen = 0
    surnameFemaleList = []
    surnameFemaleLen = 0
    # Surnames, second surname - Filipino
    surnameLongList = []
    surnameLongLen = 0    
    # Patronymic - Russian names contain this
    malePatronymicList = []
    malePatronymicLen = 0
    femalePatronymicList = []
    femalePatronymicLen = 0
    def __init__(self) -> None:
        pass
    
    def DualsFile(self, surnameMiddleFile, maleFile, femaleFile):
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
    
    def SimplesFile(self, firstMaleFile, firstFemaleFile):
        self.firstMaleList = firstMaleFile.readlines()
        self.firstMaleLen = len(self.firstMaleList)
        self.firstFemaleList = firstFemaleFile.readlines()
        self.firstFemaleLen = len(self.firstFemaleList)

    def PatronymicsFile(self, firstMaleFile, firstFemaleFile, patronymicMaleFile, patronymicFemaleFile, surnameMaleFile, surnameFemaleFile):
        self.firstMaleList = firstMaleFile.readlines()
        self.firstMaleLen = len(self.firstMaleList)
        self.firstFemaleList = firstFemaleFile.readlines()
        self.firstFemaleLen = len(self.firstFemaleList)
        self.surnameFemaleList = surnameFemaleFile.readlines()
        self.surnameFemaleLen = len(self.surnameFemaleList)
        self.surnameMaleList = surnameMaleFile.readlines()
        self.surnameMaleLen = len(self.surnameMaleList)
        self.patronymicFemaleList = patronymicFemaleFile.readlines()
        self.patronymicFemaleLen = len(self.patronymicFemaleList)
        self.patronymicMaleList = patronymicMaleFile.readlines()
        self.patronymicMaleLen = len(self.patronymicMaleList)


def constructDualsName(firstNamesList, firstNamesLen, lastNamesList, lastNamesLen):
    return firstNamesList[randrange(0, firstNamesLen)].rstrip() + ' ' + lastNamesList[randrange(0, lastNamesLen)].rstrip()

def constructMultiplesName(firstNamesList, firstNamesLen, lastNamesList, lastNamesLen):
    return constructDualsName(firstNamesList, firstNamesLen, lastNamesList, lastNamesLen)

def constructLongsName(firstNamesList, firstNamesLen, middleNamesList, middleNamesLen, lastNamesList, lastNamesLen):
    return firstNamesList[randrange(0, firstNamesLen)].rstrip()+ ' ' + firstNamesList[randrange(0, firstNamesLen)].rstrip() + ' ' + middleNamesList[randrange(0, middleNamesLen)].rstrip() + ' ' + lastNamesList[randrange(0, lastNamesLen)].rstrip()

def constructSimpleName(firstNamesList, firstNamesLen):
    return firstNamesList[randrange(0, firstNamesLen)].rstrip()

def constructMultipleLongName(firstNamesList, firstNamesLen, lastNamesList, lastNamesLen, patronymicNameList, patronymicNameLen):
    return firstNamesList[randrange(0, firstNamesLen)].rstrip() + ' ' + patronymicNameList[randrange(0, patronymicNameLen)].rstrip() + ' ' + lastNamesList[randrange(0, lastNamesLen)].rstrip()

def generateNames(first: str, surn: str, gender: str, number: int):
    result = []    
    files = NamesFiles(first, surn)
    lists = NameList()
    if (dictionary[surn][1] == 'Dual'):
        with open(files.surname, 'r') as surnameFile, open(files.male, 'r') as maleFile, open(files.female, 'r') as femaleFile:              
            lists.DualsFile(surnameFile, maleFile, femaleFile)
            for i in range(0, number):
                if gender == 'C':
                    if randint(0,1) == 0:
                        result.append(constructDualsName(lists.firstMaleList, lists.firstMaleLen, lists.surnameMiddleList, lists.surnameMiddleLen))
                    else:
                        result.append(constructDualsName(lists.firstFemaleList, lists.firstFemaleLen, lists.surnameMiddleList, lists.surnameMiddleLen))
                elif gender == 'M':
                    result.append(constructDualsName(lists.firstMaleList, lists.firstMaleLen, lists.surnameMiddleList, lists.surnameMiddleLen))
                else:
                    result.append(constructDualsName(lists.firstFemaleList, lists.firstFemaleLen, lists.surnameMiddleList, lists.surnameMiddleLen))
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
    elif (dictionary[surn][1] == 'Simple'):
        with open(files.male, 'r') as maleFile, open(files.female, 'r') as femaleFile:
            lists.SimplesFile(maleFile, femaleFile)
            for i in range(0, number):
                if gender == 'C':
                    if randint(0,1) == 0:
                        result.append(constructSimpleName(lists.firstMaleList, lists.firstMaleLen))
                    else:
                        result.append(constructSimpleName(lists.firstFemaleList, lists.firstFemaleLen))
                elif gender == 'M':
                    result.append(constructSimpleName(lists.firstMaleList, lists.firstMaleLen))
                else:
                    result.append(constructSimpleName(lists.firstFemaleList, lists.firstFemaleLen))
    elif (dictionary[surn][1] == 'Multiple-Long'):
        with open(files.male, 'r') as maleFile, open(files.female, 'r') as femaleFile, open(files.surnameMale, 'r') as surnameMaleFile, open(files.surnameFemale, 'r') as surnameFemaleFile, open(files.malePatronymic, 'r') as patronymicMaleFile, open(files.femalePatronymic, 'r') as patronymicFemaleFile:
            lists.PatronymicsFile(maleFile, femaleFile, patronymicMaleFile, patronymicFemaleFile, surnameMaleFile, surnameFemaleFile)
            for i in range(0, number):
                if gender == 'C':
                    if randint(0,1) == 0:
                        result.append(constructMultipleLongName(lists.firstMaleList, lists.firstMaleLen, lists.surnameMaleList, lists.surnameMaleLen, lists.patronymicMaleList, lists.patronymicMaleLen))
                    else:
                        result.append(constructMultipleLongName(lists.firstFemaleList, lists.firstFemaleLen, lists.surnameFemaleList, lists.surnameFemaleLen, lists.patronymicFemaleList, lists.patronymicFemaleLen))
                elif gender == 'M':
                    result.append(constructMultipleLongName(lists.firstMaleList, lists.firstMaleLen, lists.surnameMaleList, lists.surnameMaleLen, lists.patronymicMaleList, lists.patronymicMaleLen))
                else:
                    result.append(constructMultipleLongName(lists.firstFemaleList, lists.firstFemaleLen, lists.surnameFemaleList, lists.surnameFemaleLen, lists.patronymicFemaleList, lists.patronymicFemaleLen))
    return result

def generateName(first: str, surn: str, gender: str):
    return generateNames(first, surn, gender, 1)[0]
    


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