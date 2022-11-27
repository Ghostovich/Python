# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

#  not(x or y or z) = not x and not y and not z


for i in range(2):
    for j in range(2):
        for k in range(2):
            i or j or k == i and j and k
            print('true')