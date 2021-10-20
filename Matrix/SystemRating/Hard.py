
# generate random integer values
from random import randint

# generate some integers
print("Security: " + str(randint(1,3)+randint(1,3)+4))
print("Access: " + str(randint(1,6)+9))
print("Control: " + str(randint(1,6)+9))
print("Index: " + str(randint(1,6)+9))
print("File: " + str(randint(1,6)+9))
print("Slave: " + str(randint(1,6)+9))