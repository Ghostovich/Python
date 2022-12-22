# Дан список чисел. Вывести из него только простые числа.
# Ввод	                Вывод
# 15 2 3 31	            2 3 31

sp = [15, 2, 3, 31]

def fun(n):
    count = 0
    for i in range(2, n//2+1):
        if n%i ==0:
            count+=1
    if count>0:
        return False
    return True

result = list(filter(fun, sp))
print(result)


