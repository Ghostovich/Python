# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

N = int(input('Введите число:'))
sp = []
spn = []

f = 0
sp.append(f)
s = 1
sp.append(s)
for i in range(2, N+1):
    sp.append(sp[i-1]+sp[i-2])

fm1 = 1
spn.append(fm1)

for i in range(2, N+1):
    spn.append(((-1)**(i+1))*sp[i])
spn.reverse()

print(spn+sp)
