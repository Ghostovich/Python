# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

sp = [i for i in input('Введите данные:').split(' ')]
sp = list(filter(lambda x: 'абв' not in x, sp))
print(sp)