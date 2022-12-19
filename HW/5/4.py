# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

path = 'HW/5/1.txt'
data = open(path, 'r')
for line in data:
    a = list(line)
data.close()

b = ''
c = ''
count = 1
if not a:
    c = ''
for i in a:
    if i != b:
        if b:
            c += str(count) + b
        count = 1
        b = i
    else:
        count += 1
else:
    c += str(count) + b


path = 'HW/5/2.txt'
data = open(path, 'w')
data.writelines(c)
data.close()

path = 'HW/5/1.txt'
data = open(path, 'r')
for line in data:
    d = str(line)
data.close()

e = ''
f = 1
for x in d:
    if str(x).isdigit():
        f += x
        print(x)
    else:
        e += x * int(f)
        f = 1

path = 'HW/5/3.txt'
data = open(path, 'w')
data.writelines(e)
data.close()
