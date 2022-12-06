# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


sp = []
sum = 0
print('Введите данные:')
for i in range(5):
    sp.append(int(input()))
print(sp)
for i in range(5):
    if i % 2 == 1:
        sum+=sp[i]
print(sum)
