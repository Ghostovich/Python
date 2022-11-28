# Даны два целых числа A и В, A>B.
# Выведите все нечётные числа от A до B включительно,
# в порядке убывания. В этой задаче можно обойтись без инструкции if.
# Входные данные	Выходные данные
# 7
# 1	                7 5 3 1


number1 = int(input('Введите число A:'))
number2 = int(input('Введите число B:'))
# while number1 >= number2:
#     number1 -= (number1-1) % 2
#     print(number1)
#     number1 -= 2

for i in range(number1 - (number1-1) % 2, number2 - 1, -2):
    print(i)
