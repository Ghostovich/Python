# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

print()
sp1 = []
sp2 = []
sp = []

path = 'HW/4/file1.txt'
data = open(path, 'r')
for line in data:
    A = str(line).split(' ')
    print(A)
data.close()


print()

path = 'HW/4/file2.txt'
data = open(path, 'r')
for line in data:
    B = str(line).split(' ')
    print(B)
data.close()

print()

i = 0
while i < len(A)-4:
    C = int(A[i])+int(B[i])
    C = str(f'{C} ')
    sp.append(C)
    i+=2
print(sp)

path = 'HW/4/file3.txt'
data = open(path, 'w')
data.writelines(sp)
data.close()

print()
