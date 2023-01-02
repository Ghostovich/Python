def greeting():
    print("Приветствую! Выберите действие: \n \
            1 - Экспортировать контакты csv; \n \
            2 - Экспортировать контакты txt; \n \
            3 - Импрортировать контакты csv; \n \
            4 - Импрортировать контакты txt")
    select = int(input())
    return select

def get_export_c():
    expc = input('Введите данные(Фамилия,Имя,Номер): ')
    return expc

def get_export_t():
    expt = input('Введите данные(Фамилия,Имя,Номер): ')
    return expt

