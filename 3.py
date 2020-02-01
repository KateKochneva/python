#1
def numbers(numbers1, numbers2):
    if numbers2 != 0:
        num = str(numbers1/numbers2)
        print(num)
    else:
        print('Деление на ноль!')

numbers1 = int(input('Введите первое число '))
numbers2 = int(input('Введите второе число '))
numbers(numbers1, numbers2)

#2
def data_of_user(name, surname, year, city, email, phone):
    print(f'Данные пользователя: {name}, {surname}, {year}, {city}, {email}, {phone}')

data_of_user(surname='Ivanov', name='Ivan', year='1960', city='Moscow', email='Ivan@mail.ru', phone='909909909909')

#3
def my_func(seq):
    m1 = None
    m2 = None
    for i in seq:
        if m2 is None:
            m2 = i
        elif m1 is None:
            if i > m2:
                m1, m2 = m2, i
            else:
                m1 = i
        elif i > m2:
            m1, m2 = m2, i
        elif i > m1:
            m1 = i

    return (m1+m2)

seq = (5, 6, 10)
print(my_func(seq))

#4
def my_func(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x  #res = res * 3
    if y >= 0:
        return res
    else:
        return 1 / res

print(my_func(float(input("Первое значение - ")), int(input("Второе значение - "))))

#5
while 1:
    i = input("Введите строку чисел, разделенных пробелом: ")
    i = i.split(" ") #Делим по пробелам
    a = 0
    while a<len(i):
        try:
            i[a] = int(i[a])#строки в числа
        except ValueError:
            print("Value Error")#при ошибке пишем ошибку и останавливаем цикл
            break
        a = a + 1
    z = 0#Переменная с результатом
    for c in i:
        z = z + c #Считаем все
    print(z)#Выводим результат

#6
def int_func(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]

source = input('Введите строку в нижнем регистре: ').split()
res = []
for word in source:
    res.append(int_func(word))
print(' '.join(res))