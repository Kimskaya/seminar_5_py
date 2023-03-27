#Задача 28: Напишите рекурсивную функцию sum(a, b), 
#возвращающую сумму двух целых неотрицательных чисел. 
#Из всех арифметических операций допускаются 
#только +1 и -1. Также нельзя использовать циклы. 
#*Пример:*
#2 2
#    4 
#"""
# вариант 1
def Sum(numA, numB): 
                 
    if (numA > 0 and numB > 0):                               
        return Sum(numA-1, numB+1)
    return (numA+numB)
    
    
numA = int(input("Input the first number   "))
numB = int(input("Input the second number  "))
result = Sum(numA, numB)
print(f"The sum of {numA} and {numB}  equals {result}")