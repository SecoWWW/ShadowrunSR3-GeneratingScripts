# generate random integer values
from random import randint

steps = [int(randint(1,6)/2)+1 for i in range(0,6)]
sum=0
for i in range(1,len(steps)+1):
    for j in range(i):
        sum+=steps[j]
    print(sum)
    sum=0