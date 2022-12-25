# Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b),
# возвращающая наибольший общий делитель (НОД) двух чисел.
# Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел.
# Ввод чисел продолжается до ввода пустой строки.
# Входные данные    Выходные данные
# 36                    6
# 12
# 144
# 18

import math
from functools import reduce

sp = []

for i in range(100):
    num = input('Введите данные: ')
    num1 = num.isdigit()
    if num1 == True:
        sp.append(int(num))
    elif num == '' or num1 == False:
        break
# for i in range(100):
#     s = math.gcd(sp[i], sp[i+1])
print(reduce(lambda x, y: math.gcd(x, y), sp))
