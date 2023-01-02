def greeting():
    print("Приветствую! Выбери действие: 1 - Экспортировать контакты; 2 - Импрортировать контакты")
    select = int(input())
    return select

def get_export():
    exp = input('Введите данные(Фамилия,Имя,Номер): ')
    return exp

def view_res_exp(res_exp):
    print(res_exp)

def get_import():
    imp = input('Введите данные(Фамилия,Имя,Номер): ')
    return imp

def view_res_imp(res_exp):
    print(res_exp)