# Реализуйте алгоритм перемешивания списка
# (shuffle использовать нельзя, другие методы из библиотеки random - можно).
import random

sp = [1, 2, 3, 4]
spn = sorted(sp, key=lambda A: random.random())
print(spn)