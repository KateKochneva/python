#1
result_list = [2, 'text', 456, 45.3]
for i in result_list:
    print(type(i))

#2
result_list = list(input('Введите список '))
j = 0
for i in range(int(len(result_list) / 2)):
    result_list[j], result_list[j + 1] = result_list[j + 1], result_list[j]
    j += 2

print(result_list)

#3-1
seasons = {'Winter': (1, 2, 12),
           'Sping': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}

month = int(input('Choose a month: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)

#3-2
month = int(input('Choose a month: '))

Winter = [1, 2, 12]
for i in Winter:
    if month == i:
        print('Winter')

Sping = [3, 4, 5]
for i in Sping:
    if month == i:
        print('Sping')

Summer = [6, 7, 8]
for i in Summer:
    if month == i:
        print('Summer')

Autumn = [9, 10, 11]
for i in Autumn:
    if month == i:
        print('Autumn')

#4
result_list = input('Введите список ')
result_list = result_list.split()
num = 0
for i in result_list:
    if len(i) < 10:
        num = num + 1
        print(str(num) + '. ' + i)

#5
my_list = [7, 5, 3, 3, 2]
print(my_list)
new = int(input('Введите новый элемент рейтинга '))

max_value = max(my_list)
if new > max_value:
    my_list.insert(0, new)
elif new in my_list:
    my_list.insert(my_list.index(new), new)
else:
    my_list.append(new)
    my_list.sort(reverse=True)
print(my_list)










