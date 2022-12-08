# Дан текст: в первой строке задано число строк,
# далее идут сами строки. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
# Входные данные	                            Выходные данные
# 1
# apple orange banana banana orange	                 banana

list = ['apple', 'orange', 'banana', 'banana', 'orange']
slov = {}
for el in list:
    slov[el] = slov.get(el, 0) + 1
slov = dict(sorted(slov.items()))
print(slov)
max = max(slov.values())
for key, value in slov.items():
    if value == max:
        print(key)
