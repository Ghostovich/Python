# Задайте список. 
# Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.
# Входные данные	Выходные данные
# 12
# Строка1
# Строка2
# Строка3
# Строка45
# Стр12ка	                да


number1 = int(input('Введите число 1:'))
number2 = int(input('Введите число 2:'))
number3 = int(input('Введите число 3:'))
if number1 == number2 == number3:
    print('3')
elif number1 == number2 or number2 == number3 or number1 == number3:
    print('2')
else:
    print("0")
