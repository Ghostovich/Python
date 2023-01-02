
import csv

def expc(exp):
    with open("HW/7/list.csv", mode="a", encoding='utf-8') as l_file:
        file_writer = csv.writer(l_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(["Фамилия", "Имя", "Номер"])
        file_writer.writerow(exp)

def expt(exp):
    path = 'HW/7/1.txt'
    data = open(path, 'a')
    data.writelines(exp)
    data.close()
       

def impcsv():
    with open("HW/7/list.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        for row in file_reader:
            print(*row)

def imptxt():
    path = 'HW/7/1.txt'
    data = open(path, 'r')
    for line in data:
        d = str(line)
    print(d)
    data.close()
    