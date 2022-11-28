# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ 
# и выведите на экран их сумму.


num1 = int(input('Введите X:'))
num2 = int(input('Введите Y:'))
if num1>0 and num2>0:
    print("1")
elif num1<0 and num2>0:
    print('2')
elif num1<0 and num2<0:
    print('3')
elif num1>0 and num2<0:
    print('4')
else:
    print("Неверно!")