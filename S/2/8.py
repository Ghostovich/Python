# По данному целому числу N распечатайте все квадраты натуральных чисел,
# не превосходящие N, в порядке возрастания.
# Входные данные	Выходные данные
# 50	                1
#                     4
#                     9
#                     16
#                     25
#                     36
#                     49


N = int(input('Введите :'))

# count = 0
# i = 1
# while count < N-1:
#     count = i*i
#     print(count)
#     i+=1

# for i in range(N):
#     if i**2 < N:
#         print(i**2)
#     else:
#         break

for i in range(1, int(N ** 0.5)):
    print(i ** 2) #неверно немного
