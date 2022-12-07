# Задайте два числа. Напишите программу, 
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

N1, N2 = [int(i) for i in input('Введите данные:').split()]
N3 = 0
max = max(N1, N2)
if max%N1 == 0 and max%N2 == 0:
    print(max)
else:
    for N3 in range(2, min(N1, N2)+1):
        if (max*N3)%N1 == 0 and (max*N3)%N2 == 0:
            print(max*N3) 
            break
 

