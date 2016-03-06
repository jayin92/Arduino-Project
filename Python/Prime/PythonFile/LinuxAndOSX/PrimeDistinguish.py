while(1):
    number = int(input("type number =>"))
    number1 = 1
    for x in range(1,number):
        number1 = number1 * x
    if(number == 1):
        print("1 is not prime number, but it's not composite number, too.")         
    if(number1 % number == number - 1 & number > 1):
        print("Prime number")
    if not(number1 % number == number - 1):
        print("Composite number")


