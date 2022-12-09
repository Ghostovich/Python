# Напишите функцию triangle(a, b, c), которая принимает на вход три длины отрезков и определяет, 
# можно ли из этих отрезков составить треугольник. 
# Входные данные	            Выходные данные
# triangle(1, 1, 2)	        Это не треугольник
# triangle(7, 6, 10)
# 	                            Это треугольник


import math
A, B, C = [int(i) for i in input("Введите значения:").split()]
d = B**2 - 4*A*C
if d>0:
    x1 = (-B - math.sqrt(d))/2*A
    x2 = (-B + math.sqrt(d))/2*A
    print(f"корни: {x1}, {x2}")
elif d == 0:
    x = (-B/2)*A
    print(f"корни: {x}")
else:
    print("корней нет")

