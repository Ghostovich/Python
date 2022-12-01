# #Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

sp = []
pr = 0
spn = []
n = int(input('Введите количество элементов:'))
print('Введите данные:')
for i in range(n):
    sp.append(int(input()))
print(sp)
for i in range(int(len(sp)/2)):
    if len(sp)%2 == 1:
        pr=sp[i]*sp[-i-1]
        spn.append(pr)
    else:
        pr=sp[i]*sp[-i-1]
        spn.append(pr)
if len(sp)%2 == 1:
    se = sp[int(len(sp)/2)] * sp[int(len(sp)/2)]
    spn.append(se)
print(spn)
    
    
