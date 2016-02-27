import os
import csv
import math

with open('prime.txt', 'r') as f:
    prime = [line.strip() for line in f]
prime = list(map(int, prime))
number = max(prime)+1
        
print(prime)
print(number)
status_number = 1
confrim_number = 1
i = 0

while(1):
    number1 = int(math.sqrt(number))  
    i = min(prime, key = lambda x:abs(x-number1))   
    number2 = prime.index(i)+1    
    for x in prime[0:number2]:
        if status_number:
            if number % x > 0:
                status_number = 1
            if number % x == 0:
                status_number = 0
                confrim_number = 1        
    if confrim_number == 0:
        prime.append(number)
        number = number + 1
        os.system('cls')
        print(max(prime))
    if confrim_number == 1:
        number = number + 1
        status_number = 1
        confrim_number = 0
    if len(prime) % 10 == 0:
        file = open('prime.txt', 'w')
        file.truncate()
        for item in prime:
            file.write("%s\n" % item)
        file.close()            
    
    


            
    
