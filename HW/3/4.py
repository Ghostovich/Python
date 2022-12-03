# Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

N = int(input('Введите число:'))
sp = []
for i in range(-N, N+1):
    sp.append(i)
print(sp)
path = 'HW/2/file.txt'
data = open(path, 'r')
for line in data:
    A = int(line[0])
    B = int(line[1])
    print(sp[A]*sp[B])
data.close()
