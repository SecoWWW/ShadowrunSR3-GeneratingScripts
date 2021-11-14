#!/usr/bin/python3
from math import e
import random
from RandomNameGeneration import generateName, getPossibleEthnicities
from RandomAge import generateAge


files = []
for i in range(50):
    ethnicity = random.choice(getPossibleEthnicities())
    files.append(generateName(ethnicity, ethnicity,'C'))
    files[i] = files[i] + ', ' + str(generateAge())



print(files)