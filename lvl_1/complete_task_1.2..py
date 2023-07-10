# Задача 1.2

# Пункт A,B,C 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
Try = len(my_favorite_songs)
import random

a = []
n = 3
for i in range(n):
    r = random.randint(0,Try-1)
    if i == 0:
        a.append(r)
    else:
        f = 1
        while f > 0:
            f = 0
            r = random.randint(0,Try-1)
            for j in range(i):
                if a[j] == r:
                    f = 1
        a.append(r)
m = 0
s = 0
for i in range(n):
    m = m + int(my_favorite_songs [int(a[i])][1])
    s = s + round(((my_favorite_songs [int(a[i])][1])%1),2)
if s >= 0.6:
    m = m + int(s/0.6)
    s = s - (0.6*int(s/0.6))
s = round(s,2)
v = m + s
print("Три песни звучат","%.2f" % v,"минут.")

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime

import datetime

t = datetime.time(00,m,int(s*100))
print("Три песни звучат", t.strftime("%M:%S"),"минут.")
