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

sp = []

for i in range(5):
    num = input('Введите данные: ')
    num1 = isinstance(num, int)
    if num1 == True:
        sp.append(num)
    elif num == '' or num1 == False:
        break

    # if num1 == False:
    #    sp.append(num)
    # elif num == '' or num1 == True:
    #     break

    # if num.isdigit:
    #     sp.append(num)
    # elif num == ' ':
    #     break
# math.gcd(sp)
print(sp)
