# Напишите программу, которая проверяет пятизначное число на палиндром.

N = input('Введите пятизначное число:')

if N[0] == N[-1] and N[1] == N[-2]:
    print('true')
else:
    print('false')