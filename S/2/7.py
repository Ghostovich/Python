# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

A = input('Введите строку 1:')
B = input('Введите строку 2:')

# print(A.count(B))

count = 0
i = 0
while i < len(A):
    if A[i:i+len(B)] == B:
        count += 1
        i += (len(B)-1)
    i += 1
print(count)
