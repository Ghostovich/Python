# Задача Измените код одной-двух решенных ранее задач 
# (с прошлых семинаров или домашних работ), применив лямбды, 
# filter, map, zip, enumerate, списочные выражения.

import random

dict = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}
f = False

print(dict['1'], dict['2'], dict['3'])
print(dict['4'], dict['5'], dict['6'])
print(dict['7'], dict['8'], dict['9'])

ro = int(input('Орел(1) или решка(2)? '))
ro1 = random.randint(1, 2)

if ro == ro1:
    i = 0
    while i < 10:

        n1 = input('Игрок1, выберите позицию: ')
        dict[n1] = 'X'

        print(dict['1'], dict['2'], dict['3'])
        print(dict['4'], dict['5'], dict['6'])
        print(dict['7'], dict['8'], dict['9'])

        if dict['1'] == 'X' and dict['2'] == 'X' and dict['3'] == 'X' \
            or dict['4'] == 'X' and dict['5'] == 'X' and dict['6'] == 'X' \
            or dict['7'] == 'X' and dict['8'] == 'X' and dict['9'] == 'X' \
            or dict['1'] == 'X' and dict['4'] == 'X' and dict['7'] == 'X' \
            or dict['2'] == 'X' and dict['5'] == 'X' and dict['8'] == 'X' \
            or dict['3'] == 'X' and dict['6'] == 'X' and dict['9'] == 'X' \
            or dict['1'] == 'X' and dict['5'] == 'X' and dict['9'] == 'X' \
            or dict['3'] == 'X' and dict['5'] == 'X' and dict['7'] == 'X':
            print('Победил Игрок1')
            f = True
            break

        n2 = input('Игрок2, выберите позицию: ')
        dict[n2] = 'O'

        print(dict['1'], dict['2'], dict['3'])
        print(dict['4'], dict['5'], dict['6'])
        print(dict['7'], dict['8'], dict['9'])

        if dict['1'] == 'O' and dict['2'] == 'O' and dict['3'] == 'O' \
            or dict['4'] == 'O' and dict['5'] == 'O' and dict['6'] == 'O' \
            or dict['7'] == 'O' and dict['8'] == 'O' and dict['9'] == 'O' \
            or dict['1'] == 'O' and dict['4'] == 'O' and dict['7'] == 'O' \
            or dict['2'] == 'O' and dict['5'] == 'O' and dict['8'] == 'O' \
            or dict['3'] == 'O' and dict['6'] == 'O' and dict['9'] == 'O' \
            or dict['1'] == 'O' and dict['5'] == 'O' and dict['9'] == 'O' \
            or dict['3'] == 'O' and dict['5'] == 'O' and dict['7'] == 'O':
            print('Победил Игрок2')
            f = True
            break

        i += 1
        if f == True:
            dict = {
                '1': 1,
                '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9
            }


   

if ro != ro1:
    i = 0
    while i < 10:

        n2 = input('Игрок2, выберите позицию: ')
        dict[n2] = 'O'

        print(dict['1'], dict['2'], dict['3'])
        print(dict['4'], dict['5'], dict['6'])
        print(dict['7'], dict['8'], dict['9'])

        if dict['1'] == 'O' and dict['O'] == 'O' and dict['3'] == 'O' \
            or dict['4'] == 'O' and dict['5'] == 'O' and dict['6'] == 'O' \
            or dict['7'] == 'O' and dict['8'] == 'O' and dict['9'] == 'O' \
            or dict['1'] == 'O' and dict['4'] == 'O' and dict['7'] == 'O' \
            or dict['2'] == 'O' and dict['5'] == 'O' and dict['8'] == 'O' \
            or dict['3'] == 'O' and dict['6'] == 'O' and dict['9'] == 'O' \
            or dict['1'] == 'O' and dict['5'] == 'O' and dict['9'] == 'O' \
            or dict['3'] == 'O' and dict['5'] == 'O' and dict['7'] == 'O':
            print('Победил Игрок2')
            f = True
            break

        n1 = input('Игрок1, выберите позицию: ')
        dict[n1] = 'X'

        print(dict['1'], dict['2'], dict['3'])
        print(dict['4'], dict['5'], dict['6'])
        print(dict['7'], dict['8'], dict['9'])

        if dict['1'] == 'X' and dict['2'] == 'X' and dict['3'] == 'X' \
            or dict['4'] == 'X' and dict['5'] == 'X' and dict['6'] == 'X' \
            or dict['7'] == 'X' and dict['8'] == 'X' and dict['9'] == 'X' \
            or dict['1'] == 'X' and dict['4'] == 'X' and dict['7'] == 'X' \
            or dict['2'] == 'X' and dict['5'] == 'X' and dict['8'] == 'X' \
            or dict['3'] == 'X' and dict['6'] == 'X' and dict['9'] == 'X' \
            or dict['1'] == 'X' and dict['5'] == 'X' and dict['9'] == 'X' \
            or dict['3'] == 'X' and dict['5'] == 'X' and dict['7'] == 'X':
            print('Победил Игрок1')
            f = True
            break

        i += 1
        if f == True:
            dict = {
                '1': 1,
                '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9
            }






