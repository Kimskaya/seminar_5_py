#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

#*Пример:*

#A = 3; B = 5 -> 243 (3⁵)
#   A = 2; B = 3 -> 8

def raiseInPower(num, pow):
    if pow == 1:
        return num
    if pow!=1:
        return (num*raiseInPower(num,pow-1))
num = int(input("Input your number  "))
pow = input(input("input the power you want to raise your number to  "))
result = raiseInPower (num,pow)

print(num,"in the power of", pow,"equals",raiseInPower (num, pow))

def raisNumberToPower(numberA, numberB): # функция принимает число и его степень
    if (numberB == 1):                   # проверка степень = 1 (число в степени 1 = число)
        return numberA                   # возвращаем возводимое число
    if (numberB != 1):                   # проверка если число не = 1 
# возвращаем число * на рекурсию (накапливаем numberA 
# в количестве = numberB что равно => возведению в степень)
        return (numberA * raisNumberToPower(numberA, numberB - 1)) 
    
numberA = int(input("Введите число A: "))
numberB = int(input("Введите число B: "))
result = raisNumberToPower(numberA, numberB) # вызываем функцию
print(f"Результат возведения чила {numberA} в степень {numberB} равен: {result}")