# 1
one = 1
two = 2
print(one+two)

number1 = input('Введите первое число: ')
number2 = input('Введите второе число: ')
number3 = input('Введите третье число: ')
string1 = input('Введите первую строку: ')
string2 = input('Введите вторую строку: ')

print(f'Первое число: {int(number1)} второе число: {int(number2)} третье число: {int(number3)} первая строка:'
      f' {string1}, вторая строка: {string2}')

#2
sec = int(input('Enter seconds: '))
h = ((sec // 3600)) % 24
m = (sec // 60) % 60
s = sec % 60

print('%d:%02d:%02d' % (h, m, s))

#3
numberN = input('Введите число: ')
number1 = numberN
number2 = numberN + numberN
number3 = numberN + numberN + numberN
number1 = int(number1)
number2 = int(number2)
number3 = int(number3)
total = number1 + number2 + number3
print(total)

#4
a = int(input('Введите целое положительное число: '))
m = a%10                    #макс цифра
a = a//10
while a > 0:
    if a%10 > m:
        m = a%10
    a = a//10
print(m)

#5
revenue = int(input('Введите выручку: '))
cost = int(input('Введите издержки: '))
if revenue > cost:
    print('прибыль')
else:
    print('издержки')

#6
x = int(input('километров в первый день '))
y = int(input('не менее километров '))
day = 1
while y - x > 0:
    x = x + (x * 0.1)
    day += 1
print(day)
