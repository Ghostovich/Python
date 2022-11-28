# Напишите программу, которая проверяет пятизначное число на палиндром.

N = input('Введите пятизначное число:')

# if N[0] == N[-1] and N[1] == N[-2]:
#     print('true')
# else:
#     print('false')

i = 0
for i in range(len(N) // 2):
    if N[i] == N [-i -1]:
        M = 1
    else:
        M = 0
if M == 1:
    print('true')
else:
    print('false')
