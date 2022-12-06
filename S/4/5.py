# Вам дан словарь, состоящий из пар слов. 
# Каждое слово является синонимом к парному ему слову. 
# Все слова в словаре различны.
# Для слова из словаря, записанного в последней строке, определите его синоним.
# Входные данные	Выходные данные
# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye	            Bye



sp = []
count = 0
f = 0
print('Введите строку:')
for i in range(5):
    sp.append(input())
print(sp)
N = input('Поиск:')
for i in range(5):
    if N in sp[i]:
        count+=1
        if count ==2:
            print(i+1)
            break
    else:
        continue
if count<2:
    print('-1')


