# Даны три целых числа. 
# Определите, сколько среди них совпадающих. 
# Программа должна вывести одно из чисел: 3 (если все совпадают), 
#  2 (если два совпадает) или 0 (если все числа различны).
# Входные данные	Выходные данные
# 10
# 5
# 10	                    2

number1 = int(input('Введите число 1:'))
number2 = int(input('Введите число 2:'))
number3 = int(input('Введите число 3:'))
if number1 == number2 == number3:
    print('3')
elif number1 == number2 or number2 == number3 or number1 == number3:
    print('2')
else:
    print("0")