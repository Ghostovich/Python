# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число:'))
sp = []

i = 2
while i*i<=n:
    if n%i == 0:
        sp.append(i)
        n = n//i
    else:
        i+=1
if n>1:
    sp.append(n)
print(sp)

    
    
