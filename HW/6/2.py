# Орел и решка

# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". 
# Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. 
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

# Формат входных данных:
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

# Формат выходных данных:
# Программа должна вывести наибольшее количество подряд выпавших Решек.

# Примечание. Если выпавших Решек нет, то необходимо вывести число 0.
# Входные данные                                            Выходные данные
# ОРРОРОРООРРРО                                             3
# ООООООРРРОРОРРРРРРР                                        7
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР      31

import random

can = int(input('Количество конфет: '))
pl = int(input('Количество игроков(1 или 2): '))
ro = int(input('Орел(1) или решка(2)? '))
ro1 = random.randint(1, 2)


if pl == 2:
    if ro == ro1:

        while can > 0:

            n1 = int(input('Ход первого игрока: '))
            can -= n1
            print(f'Остаток: {can}')
            if can == 0:
                print('Победил первый игрок!')
                break

            n2 = int(input('Ход второго игрока: '))
            can -= n2
            print(f'Остаток: {can}')
            if can == 0:
                print('Победил второй игрок!')
                break

    elif ro != ro1:
        while can > 0:

            n2 = int(input('Ход второго игрока: '))
            can -= n2
            print(f'Остаток: {can}')
            if can == 0:
                print('Победил второй игрок!')
                break

            n1 = int(input('Ход первого игрока: '))
            can -= n1
            print(f'Остаток: {can}')
            if can == 0:
                print('Победил первый игрок!')
                break


if pl == 1:
    if ro == ro1:
        while can > 0:

            n1 = int(input('Ход первого игрока: '))
            can -= n1
            print(f'Остаток: {can}')
            if can == 0:
                print('Победил первый игрок!')
                break

            can1 = can
            can2 = can
            if 28 < can < 57:
                i = 0
                while can1 > 30:
                    can1 = can
                    can1 -= i
                    i += 1
                n2 = i

            elif can2 <= 28:
                i = 0
                while can2 > 0:
                    can2 = can
                    can2 -= i
                    if can2 == 0:
                        break
                    i += 1
                n2 = i
            else:
                n2 = 28

            print(f'Ход второго игрока: {n2}')
            can -= n2
            print(f'Остаток: {can}')
            if can == 0:
                print('Победил второй игрок!')
                break

    elif ro != ro1:
        while can > 0:
            can1 = can
            can2 = can
            if 28 < can < 57:
                can1 = can
                if 28 < can1 and can1 < 57:
                    i = 0
                    while can1 > 30:
                        can1 = can
                        can1 -= i
                        i += 1
                n2 = i
            elif can2 <= 28:
                i = 0
                while can2 > 0:
                    can2 = can
                    can2 -= i
                    if can2 == 0:
                        break
                    i += 1
                n2 = i
            else:
                n2 = 28

            print(f'Ход второго игрока: {n2}')
            can -= n2
            print(f'Остаток: {can}')
            if can == 0:
                print('Победил второй игрок!')
                break

            n1 = int(input('Ход первого игрока: '))
            can -= n1
            print(f'Остаток: {can}')
            if can == 0:
                print('Победил первый игрок!')
                break
