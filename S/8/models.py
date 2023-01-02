import csv

def get_list():
    with open("S/8/file.csv", encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter = ";")
        # title = next(reader)
        return list(reader)

def add_employ_to_list(data):
    with open("S/8/file.csv", 'a', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter = ";")
        writer.writerow(data)

def update_employees(number, string):
    with open("S/8/file.csv", encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter = ";")
        data = list(reader)
        data[number] = string
    with open("S/8/file.csv", 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter = ";")
        for i in data:
            writer.writerow(i)

def delete(number):
    with open("S/8/file.csv", encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter = ";")
        data = list(reader)
        del data[number]
    with open("S/8/file.csv", 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter = ";")
        for i in data:
            writer.writerow(i)
