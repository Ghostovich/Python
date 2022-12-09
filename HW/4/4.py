# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
k = int(input('Введите число:'))
sp = []
sp2 = []
for i in range(k):
    n = random.randint(0,100)
    sp.append(n)
for i in range(k):
    m = sp[i]*x**(k-i)
    sp2.append(m)
print(sp2, sep = '+', end = '=0')


