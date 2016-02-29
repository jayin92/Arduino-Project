import os
import csv
import math

with open('prime.txt', 'r') as f:
    prime = [line.strip() for line in f]
prime = list(map(int, prime))
number = 8
isPrime = True
while(1):
    isPrime = True
    for x in range(2, int(number**0.5)+1):
        if number % x == 0:
            isPrime = False
            number = number + 1
            break
    if isPrime:
        prime.append(number)
        number = number + 1
    if len(prime) % 10 == 0:
        file = open('prime.txt', 'w')
        file.truncate()
        for item in prime:
            file.write("%s\n" % item)
        file.close()
    os.system('cls')
    
    
