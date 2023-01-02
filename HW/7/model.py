
import csv

def exp(exp):
    with open("HW/7/list.csv", mode="a", encoding='utf-8') as l_file:
        file_writer = csv.writer(l_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(["Фамилия", "Имя", "Номер"])
        file_writer.writerow(exp)
       

def imp():
    with open("HW/7/list.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        count = 0
        for row in file_reader:
            if count == 0:
                print(f'Файл содержит столбцы: {", ".join(row)}')
            else:
                print(row[0], row[1], row[2])
            count += 1