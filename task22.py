#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
#Затем пользователь вводит сами элементы множеств.

set_1 =[]
N = int(input("Input the number of elements in the first array  "))
for i in range (N):
     num = int(input("input the numbers in the first set    "))
     set_1.append(num)
print (set_1)
set_2=[]
M = int(input("Input the number of elements in the second array  "))
for i in range (M):
     num =  int(input("input the numbers in the second set    "))
     set_2.append(num)
print (set_2)

set_3 = set_1+set_2

print(set_3)
similar_nums_list = []
result = []
for i in set_3:
    if set_3.count(i) > 1 and i not in similar_nums_list:
        similar_nums_list.append(i)
        result.append(i)
print("the similar numbers in rwo sets are",result)