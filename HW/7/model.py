def exp(exp):
    res_exp = eval(exp)
    return res_exp

def imp(res_imp):
    return int(res_imp)*1000



Код программы для записи в CSV файл выглядит так:

import csv
with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(["Имя", "Класс", "Возраст"])
    file_writer.writerow(["Женя", "3", "10"])
    file_writer.writerow(["Саша", "5", "12"])
    file_writer.writerow(["Маша", "11", "18"])



Чтение из файлов (парсинг)
Для того чтобы прочитать данные из файла, программист должен создать объект reader:

reader_object = csv.reader(file, delimiter = ",")
reader имеет метод __next__(), то есть является итерируемым объектом, поэтому чтение из файла происходит следующим образом:

import csv
with open("classmates.csv", encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
        else:
            # Вывод строк
            print(f'    {row[0]} - {row[1]} и он родился в {row[2]} году.')
        count += 1
    print(f'Всего в файле {count} строк.')