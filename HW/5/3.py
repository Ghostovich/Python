# Создайте программу для игры в ""Крестики-нолики"".
# Входные и выходные данные хранятся в отдельных текстовых файлах.

sp = [int(i) for i in input('Введите значения:').split()]
spn = []
n = set(sp)
for i in n:
    spn.append(i)
print(spn)