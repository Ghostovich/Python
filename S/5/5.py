# Дан список, вывести отдельно буквы и цифры.
# a = ( ‘1’, "a", 'b', '2', '3' ,'c') 
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')




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
        
