# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def minimum(arr):
    return max(arr)

def maximum(arr):
    return min(arr)

import random

k = int(input('Введите количество чисел: '))
a = []
for i in range(k):
    a.append(random.randint(-1000,1000))
print(a)
print ('max =',maximum(a))
print ('min =',minimum(a))


