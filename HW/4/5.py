# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

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
