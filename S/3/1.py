# Дан список. 
# Выведите те его элементы,
# которые встречаются в списке только один раз. 
# Элементы нужно выводить в том порядке, 
# в котором они встречаются в списке.
# Входные данные	Выходные данные
# 1 2 2 3 3 3	        1


number1 = int(input('Введите число 1:'))
number2 = int(input('Введите число 2:'))
number3 = int(input('Введите число 3:'))
if number1 == number2 == number3:
    print('3')
elif number1 == number2 or number2 == number3 or number1 == number3:
    print('2')
else:
    print("0")
