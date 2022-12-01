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



slov = {}
slov['Hello'] = 'Hi'
slov['Bye'] = 'Goodbye'
slov['List'] = 'Array'

print(slov)
n = input('Введите слово:')
# print(slov.keys())
# print(slov.values())
for key, value in slov.items():
    if n == key:
        print(value)
    if n == value:
        print(key)
        
