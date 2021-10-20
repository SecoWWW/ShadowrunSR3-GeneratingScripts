
# generate random integer values
from random import randint

# generate some integers
print("Security: " + str(randint(1,3)+5))
print("Access: " + str(randint(1,3)+randint(1,3)+7))
print("Control: " + str(randint(1,3)+randint(1,3)+7))
print("Index: " + str(randint(1,3)+randint(1,3)+7))
print("File: " + str(randint(1,3)+randint(1,3)+7))
print("Slave: " + str(randint(1,3)+randint(1,3)+7))