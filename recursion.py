# пользователь вводит N выводим числа фибоначчи до N
def fib (n):
    if n in [1,2]:   # если N - это 1 или 2
        return 1
    return fib (n-1)+ fib (n-2)
list_1= []
for i in range (1,10):
    list_1.append(fib())  # Добавляем в конец
    print (list_1)

    def quick_sort (array):
        if len(array)<=1:
            return array
        else:
            pivot = array[0]
        less = [i for i in array [1:] if i <= pivot ]
        more = [i for i in array [1:] if i >= pivot ]
        return  quick_sort(less) + [pivot] + quick_sort(more) # через [] для pivot преобразуем число в список
    print(quick_sort([10,5,2]))

def merge_sort (nums):
    if len(nums)>1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)

    



