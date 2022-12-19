# Дан список чисел. Вывести из него только простые числа.
# Ввод	                Вывод
# 15 2 3 31	            2 3 31





# array = [i for i in range(10, 100) i**2+sum]

# list = []

# for i in range(10, 100):
#     if i%9==0:
#         list.append(i)
# print(list)




# sp = [i**2 for i in range(10, 100) if i % 9 == 0]
# print(sum(sp))





res = list(map(lambda x: x**2, filter(lambda i: i % 9 == 0, range(10, 100))))
print(sum(res))
