import random
import time
ageRange = [(5,14),(15,24),(25,34),(35,44),(45,54),(55,64),(65,74),(75,100)]
weightOfAges = [3,15,25,20,15,5,3,5]

def generateAge():
    array = random.choices(population=ageRange, weights=weightOfAges, k=1)
    min, max = array[0]
    return random.randint(min,max)


def randomDate(start, end):
    prop = random.random()
    time_format = '%m.%d.%Y-%I:%M::%p'
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))



