# Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

N = int(input('Введите число:'))
sp = []
while N != 0:
    sp.append(N%2)
    N = N//2
sp.reverse()
print(*sp, end='')


