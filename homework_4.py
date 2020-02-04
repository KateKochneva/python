#1
from sys import argv
x, y, c = argv
pay = str(int((x * y) + c)))
print(f'Размер заработной платы составил: {pay}')

#2
a = [int(i) for i in input('Введите список чисел через пробел ').split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])

#3
new_list = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(new_list)

#4
a = [int(i) for i in input('Введите элементы списка ').split()]
for i in a:
   if a.count(i) == 1:
       print(i)

#5
from functools import reduce
def my_func(prev_el, el):
    return prev_el * el

new_list = [el for el in range(100, 1001) if el % 2 == 0 ]
print(reduce(my_func, new_list))

#6
from itertools import count
#6-1
for el in count(0):
    print(el)

#6-2
с = 0
for el in cycle("ABC"):
    if с > 10:
        break
    print(el)
    с += 1

#7
def generator():
    res = 1
    n = int(input('Введите число '))
    for i in range(1, n + 1):
        res *= i
    yield res

g = generator()
print(g)

for el in g:
    print(el)