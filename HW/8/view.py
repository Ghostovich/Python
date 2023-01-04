def show_menu():
    print('Выберите команду: \n \
        1 - показать всех сотрудников \n \
        2 - добавить сотрудника \n \
        3 - изменить данные сотрудника \n \
        4 - удалить данные сотрудника  \n \
        5 - экспортировать в txt')
    try:
        select = int(input())
        if not select in [1,2,3,4,5]:
            raise ValueError
        return select
    except Exception:
        print("Все пропало!")
        exit()

def show_employees(sotr):
    print('Список всех сотрудников: ')
    for i, sotrudnik in enumerate(sotr):
        if i == 0:
            print(' ', *sotrudnik)
        else:
            print(i, *sotrudnik)

def add_employees():
    print("Введите Фамилию Имя Телефон и Должность через пробел: ")
    data = input().split()
    return data

def change_employees():
    print("Выберите строку для перезаписи: ")
    change = int(input())
    print("Введите строку: ")
    string = input().split()
    return change, string

def delete():
    print('Напишите номер строки для удаления: ')
    number = int(input())
    return number