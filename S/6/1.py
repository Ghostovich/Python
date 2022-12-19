# Напишите программу для построения горизонтальных столбчатых диаграмм с помощью символа звёздочки.
# Ввод	            Вывод
# 3 7 1 10 8	           ***
#                        *******
#                         *
#                         **********
#                         ********


path = 'S/5/1.txt'

data = open(path, 'r')
a = data.read().split()
a = list(map(int, a))
print(a)
data.close()

for i in range(1, len(a)):
    if a[i] != a[i-1]+1:
        print(a[i-1]+1)
