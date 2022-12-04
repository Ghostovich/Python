# Реализуйте алгоритм задания случайных чисел
#  без использования встроенного генератора псевдослучайных чисел.

# Подсказка: можно использовать модуль datetime


number1 = int(input('Введите число 1:'))
number2 = int(input('Введите число 2:'))
number3 = int(input('Введите число 3:'))
if number1 == number2 == number3:
    print('3')
elif number1 == number2 or number2 == number3 or number1 == number3:
    print('2')
else:
    print("0")
