import os

y = 0
ans = 0

while(1):
    os.system('cls')
    Match1 = [3,2,4,7,6,5,1]
    Match2 = []
    
    for x in range(7):
        number2 = int(input("Please enter " + str(x)+ " number(the second one):"))
        Match2.append(number2)
    for item in Match1:         
         ans += Match1[y] * Match2[y]
         y = y+1
    ans = str(ans)
    
    print('')
    print("Match is :"+ans)

    os.system('pause')
         
    
            
