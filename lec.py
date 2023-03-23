# функция, которая считает сумму от 1 до N
def sumNumbers(N):
  summa = 0
  for i in range (1, N+1):
    summa += i
    return summa 
  a = sumNumbers(5)
  print (a) 

def sum_str(*args) # Хотим передать неограниченное количество аргументов
res = ""
for i in args:
  res +=1
  return res
print (sum_str("q","w","e"))
  
