# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

count = 0
sp = []
path = 'HW/5/1.txt'
data = open(path, 'r')
for line in data:
    a = str(line)
data.close()


i = 0
while i < len(a)+1:
    if a[i] == a[i+1]:
        count += 1
        a1 = (f'{count}{a[i]}')
    sp.append(a1)
    i+=1





# path = 'HW/5/2.txt'
# data = open(path, 'w')
# data.writelines(sp)
# data.close()

# path = 'HW/5/1.txt'
# data = open(path, 'r')
# for line in data:
#     b = str(line)
# data.close()



# i = 0
# while i < len(A)-4:
#     C = int(A[i])+int(B[i])
#     C = str(f'{C} ')
#     sp.append(C)
#     i+=2
# print(sp)





# path = 'HW/5/3.txt'
# data = open(path, 'w')
# data.writelines(sp)
# data.close()
