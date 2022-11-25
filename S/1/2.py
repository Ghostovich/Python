# 2.	Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# o	1, 4, 8, 7, 5 -> 8
# o	78, 55, 36, 90, 2 -> 90

# num1 = int(input('Введите число 1:'))
# num2 = int(input('Введите число 2:'))
# num3 = int(input('Введите число 3:'))
# num4 = int(input('Введите число 4:'))
# num5 = int(input('Введите число 5:'))

i=0
num = int(input('Введите число:'))
max = num
while i<5:
    num = int(input('Введите число:'))
    if num > max:
        max = num
    i+=1

print(max)

# or

x = 1, 5, 8, 9, 4
print(max(x))

# or

sp = list()
for i in range(5):
    n = int(input())
    sp.append(n)
print(max(sp))
