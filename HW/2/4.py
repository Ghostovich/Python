# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

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
