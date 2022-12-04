# Дан список чисел. 
# Выведите все элементы списка, 
# которые больше предыдущего элемента.
# Входные данные	Выходные данные
# 1 5 2 4 3	        5
#                     4   


number1 = int(input('Введите число 1:'))
number2 = int(input('Введите число 2:'))
number3 = int(input('Введите число 3:'))
if number1 == number2 == number3:
    print('3')
elif number1 == number2 or number2 == number3 or number1 == number3:
    print('2')
else:
    print("0")
