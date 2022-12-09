# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
k = int(input('Введите число:'))
sp = []
sp2 = []
sp3 = []
sp4 = []

for i in range(k+1):
    n = random.randint(0, 100)
    sp.append(n)

for i in range(k+1):
    v = random.randint(0, 100)
    sp4.append(v)

for i in range(k+1):
    m = f'{sp[i]} *x** {(k-i)} + '
    sp2.append(m)
sp2.append('0=0')

for i in range(k+1):
    m = f'{sp4[i]} *x** {(k-i)} + '
    sp3.append(m)
sp3.append(' 0=0')

path = 'HW/4/file1.txt'
data = open(path, 'w')
data.writelines(sp2)
data.close()

path = 'HW/4/file2.txt'
data = open(path, 'w')
data.writelines(sp3)
data.close()
