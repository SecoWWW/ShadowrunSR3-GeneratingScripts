#!/usr/bin/python3
from math import e
import random
import time
import datetime
import csv
from RandomNameGeneration import generateName, getPossibleEthnicities
from SmallScripts import generateAge, randomDate

class CoronerFiles:
    name = ''
    age = ''
    time_of_death = ''
    time_found = ''
    found_location = ''
    notes = ''
    def __init__(self, name):
        self.name = name
        self.found_location = 'Tacoma - random.street'
    
    def report(self):
        print('Name: ' + self.name + ', age: ' + self.age \
            + '\n Found: ' + self.found_location + ' at time: ' + self.time_found\
            + '\n Time of death: ' + self.time_of_death 
            + '\n Notes: ' + self.notes)
    
    def reportCsv(self):
        return [self.name, self.age, self.time_of_death, self.time_found, self.found_location, self.notes]

def randomDateFound(victim: CoronerFiles):
    time_format = '%m.%d.%Y-%I:%M::%p'
    iso_format = '%Y-%m-%d %H:%M:%S'
    if (random.randint(0,1) == 1):
        return victim.time_of_death
    else:
        time_struct = time.strptime(victim.time_of_death, time_format)
        stime = time.mktime(time_struct)
        time_string = time.strftime(iso_format, time_struct)
        datetime_struct = datetime.datetime.strptime(time_string, iso_format)        
        datetime_struct = datetime_struct + datetime.timedelta(days=4)        
        end_string = datetime_struct.isoformat(sep=' ')
        etime = time.mktime(time.strptime(end_string, iso_format))
        ptime = stime + random.random() * (etime - stime)      
    # datetime.timedelta

    return time.strftime(time_format, time.localtime(ptime))

files: CoronerFiles = []
start_date = '01.01.2059-01:00::AM'
end_date = '01.16.2059-10:20::PM'
for i in range(50):
    ethnicity = random.choice(getPossibleEthnicities())
    files.append(CoronerFiles(generateName(ethnicity, ethnicity,'C')))
    files[i].age = str(generateAge())
    files[i].time_of_death = randomDate(start_date, end_date)
    files[i].time_found = randomDateFound(files[i])

header = ['Name', 'Age', 'Time of Death', 'Time body found', 'Body found at', 'Notes']
with open('coronerFile.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for file in files:
        writer.writerow(file.reportCsv())

