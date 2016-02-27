import os
import csv
import math

with open('primary.txt', 'r') as f:
    primary = [line.strip() for line in f]
primary = list(map(int, primary))
number = max(primary)+1
        
print(primary)
print(number)
status_number = 1
confrim_number = 1
i = 0

while(1):
       
    i = min(primary, key = lambda x:abs(x-number))   
    number2 = primary.index(i)    
    for x in primary[0:number2]:
        if status_number:
            if number % x > 0:
                status_number = 1
            if number % x == 0:
                status_number = 0
                confrim_number = 1        
    if confrim_number == 0:
        primary.append(number)
        number = number + 1
        os.system('cls')
        print(primary)
    if confrim_number == 1:
        number = number + 1
        status_number = 1
        confrim_number = 0
    if len(primary) % 100 == 0:
        file = open('primary.txt', 'w')
        file.truncate()
        for item in primary:
            file.write("%s\n" % item)
        file.close()            
    
    


            
    
