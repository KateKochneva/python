#1
fname = input('Файл: ')
f = open(fname,'w')
while True:
    s = input()
    if s == '': break
    f.write(s+'\n')
f.close()

#2
f = open('text.txt')
line = 0
for i in f:
    line += 1

    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(word, ' сл.')

print(line, ' стр.')
f.close()

#3
with open("text.txt") as f_obj:
    sum = 0
    quantity = 0
    for line in f_obj:

        mydict = dict((fam.strip(), salary.strip()) for fam, salary in (item.split('-') for item in line.split(',')))
        for fam, salary in mydict.items():
            if salary<'20000':
                print(fam)
            sum += int(salary)
            quantity += 1
    print(str(sum/quantity))

#4
with open("text.txt") as f_obj:
    for line in f_obj:
        mydict = dict((a.strip(), b.strip()) for a, b in (item.split('-') for item in line.split(',')))
        for a, b in mydict.items():

            out_f = open("out_file.txt", "w")
            str_list = ['Первый - 1\n', 'второй - 2\n', 'третий - 3\n', 'четвертый - 4']
            out_f.writelines(str_list)
            out_f.close()

#5
sum = 0
out_f = open("out_file.txt", "w")
str_list = ['12 1 7']
out_f.writelines(str_list)
for i in str_list:
    q = i.split(' ')
    for t in q:
        sum  += int(t)
out_f.close()
print(str(sum))

#6
with open("out_file.txt") as f_obj:
    for line in f_obj:
        mydict = dict((a.strip(), b.strip()) for a, b in (item.split(':') for item in line.split(',')))
        for a, b in mydict.items():
            # for d in b:
            #     print(b)
            b = b.split('л')
            #b = b.split('л')

            print(b)



# import json
# with open("my_file.json") as read_f:
#     for line in read_f:
#         data = json.load(read_f)
#         for i in line:
#             print(i)
# print(type(data))

#7


