# Дан список, вывести отдельно буквы и цифры.
# a = ( ‘1’, "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')

a = ('1', "a", 'b', '2', '3', 'c')

res1 = list(filter(lambda x: x.isdigit(), a))
res2 = list(filter(lambda x: x.isalpha(), a))
print(res1)
print(res2)

