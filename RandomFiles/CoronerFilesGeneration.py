
# generate random integer values
from random import randint
import os

path_to_datasets = '../Datasets/'

# random names
firstName = []
lastName = []


# generate some integers
print("Security: " + str(randint(1,3)+2))
print("Access: " + str(randint(1,3)+5))
print("Control: " + str(randint(1,3)+5))
print("Index: " + str(randint(1,3)+5))
print("File: " + str(randint(1,3)+5))
print("Slave: " + str(randint(1,3)+5))