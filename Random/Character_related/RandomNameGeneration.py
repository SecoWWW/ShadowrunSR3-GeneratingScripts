#!/usr/bin/python3
from random import randint, randrange
import os
import sys, getopt

dictionary = {
    'AA':'African-American',
} 

def generateNames(first, surn, gender, number):
    result = []
    surnameFile = 'Datasets/Last_Names/' + dictionary[surn] + '.txt'
    maleFirsFile = 'Datasets/First_Names/' + dictionary[first] + '-M' + '.txt'
    femaleFirsFile = 'Datasets/First_Names/' + dictionary[first] + '-F' + '.txt'
    with open(surnameFile, 'r') as surnameFile, open(maleFirsFile, 'r') as maleFile, open(femaleFirsFile, 'r') as femaleFile:
        surnameList = surnameFile.readlines()
        maleList = maleFile.readlines()
        femaleList = femaleFile.readlines() 
        surnLen = len(surnameList)
        maleLen = len(maleList)
        femaleLen = len(femaleList)          
        for i in range(0, number):
            if gender == 'C':
                if randint(0,1) == 0:
                    result.append(maleList[randrange(0, maleLen)].rstrip() + ' ' + surnameList[randrange(0, surnLen)].rstrip())
                else:
                    result.append(femaleList[randrange(0, femaleLen)].rstrip() + ' ' + surnameList[randrange(0, surnLen)].rstrip())
            elif gender == 'M':
                result.append(maleList[randrange(0, maleLen)].rstrip() + ' ' + surnameList[randrange(0, surnLen)].rstrip())
            else:
                result.append(femaleList[randrange(0, femaleLen)].rstrip() + ' ' + surnameList[randrange(0, surnLen)].rstrip())
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
        print ('test.py -f <firstnameoption> -s <surnameoption> -g <genderoption> -n <numberofnames>')
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
    listOfNames = generateNames(firstname, surname, gender, namesNumber)
    for name in listOfNames:
        print(name)


if __name__ == '__main__':
    main(sys.argv[1:])