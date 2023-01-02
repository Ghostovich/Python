def greeting():
    print("Приветствую! Выбери действие: 1 - Экспортировать контакты; 2 - Импрортировать контакты")
    select = int(input())
    return select

def get_export():
    exp = input('Введите данные(Фамилия,Имя,Номер): ')
    return exp

