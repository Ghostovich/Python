# Задача Измените код одной-двух решенных ранее задач 
# (с прошлых семинаров или домашних работ), применив лямбды, 
# filter, map, zip, enumerate, списочные выражения.


# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ 
# и выведите на экран их сумму.

# n = int(input('Введите n:'))
# s=0
# for i in range(1, n):
#     s += (1+(1/i))**i
# print(s)


# NEW

# sp = [i for i in range(1, int(input()))]
# s = list(map(lambda x: (1+(1/x))**x, sp))
# print(sum(s))








# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# Примеры:
# o	5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# N = int(input("Add number:"))

# for i in range (-N, N+1):
#     print(i, end = " ")



# NEW

# sp = [i for i in range((-int(input())), (int(input())+1))]
# print(sp)



