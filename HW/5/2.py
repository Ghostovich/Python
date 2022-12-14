# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

can = int(input('Количество конфет: '))
pl = int(input('Количество игроков(1 или 2): '))
ro = int(input('Орел(1) или решка(2)? '))
# ro1 = random.randint(1, 2)
ro1 = 1

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
            
            
            if 28 < can < 57:
                
                while can1 == 29:
                    can1 = can
                    can1 -= i
                    i += 1
                n2 = i

            elif can <= 28:
                i = 0
                can1 = can
                while can1 == 0:
                    can1 = can
                    can1 -= i
                    i += 1
                n2 = i

            else:
                n2 = random.randint(0, 29)

            print(f'Ход второго игрока: {n2}')
            can -= n2
            print(f'Остаток: {can}')
            if can == 0:
                print('Победил второй игрок!')
                break

    # elif ro != ro1:
    #     while can > 0:

    #         if 28 < can < 57:
    #             n2 = 0
    #             while can == 29:
    #                 can -= n2
    #                 n2 += 1
    #         elif can <= 28:
    #             n2 = 0
    #             while can == 0:
    #                 can -= n2
    #                 n2 += 1
    #         else:
    #             n2 = random.randint(0, 28)

    #         print(f'Ход второго игрока: {n2}')
    #         can -= n2
    #         print(f'Остаток: {can}')
    #         if can == 0:
    #             print('Победил второй игрок!')
    #             break

    #         n1 = int(input('Ход первого игрока: '))
    #         can -= n1
    #         print(f'Остаток: {can}')
    #         if can == 0:
    #             print('Победил первый игрок!')
    #             break
