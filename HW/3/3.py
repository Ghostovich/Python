# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

sp = []
spn = []
n = int(input('Введите количество элементов:'))
print('Введите данные:')
for i in range(n):
    sp.append(float(input()))

for i in range(n):
    spn.append(float(sp[i] - int(sp[i])))

max = spn[0]
for i in range(n):
    if spn[i] >= max:
        max = spn[i]
    else:
        continue

min = spn[0]
for i in range(n):
    if spn[i] <= min:
        min = spn[i]
    else:
        continue

raz = max - min
print(raz)
