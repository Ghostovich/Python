# Oпределите среднее значение всех элементов последовательности, завершающейся числом 0.
# Входные данные	Выходные данные
# 1
# 7
# 9
# 0	                    5.666666666666667

# count = 0
# sum = 0
# A = None
# while A != 0:
#     A = int(input('Введите число:'))
#     count += 1
#     sum+=A
# count-=1
# print(round(sum/count, 2))


A = None
sp = []
while A != 0:
    A = int(input('Введите число:'))
    sp.append(A)
print(round(sum(sp)/(len(sp) - 1), 2))
