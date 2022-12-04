# Даны два списка чисел. 
# Найдите все числа, которые входят как в первый, 
# так и во второй список и выведите их в порядке возрастания.
# Входные данные	Выходные данные
# 1 3 2
# 4 3 2	                2 3


number1 = int(input('Введите число 1:'))
number2 = int(input('Введите число 2:'))
number3 = int(input('Введите число 3:'))
if number1 == number2 == number3:
    print('3')
elif number1 == number2 or number2 == number3 or number1 == number3:
    print('2')
else:
    print("0")
