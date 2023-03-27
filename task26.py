#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

#*Пример:*

#A = 3; B = 5 -> 243 (3⁵)
#   A = 2; B = 3 -> 8

def raiseToPower(num, pow): 
    if (pow==0) or (num==0):
        return "there is no solution"

    if (pow > 1):                  
        return (num * raiseToPower(num, pow - 1)) 
    return num
    
num = int(input("Input your number: "))
pow = int(input("Input the power you want to raise your number in: "))
result = raiseToPower(num, pow) 
print(f"{num} in the power of {pow} equals: {result}")