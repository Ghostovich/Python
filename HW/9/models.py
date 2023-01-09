# import csv


# def get_list():
#     with open("S/8/file.csv", encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile, delimiter=";")
#         # title = next(reader)
#         d = list(reader)
#         return d


# def add_employ_to_list(data):
#     with open("S/8/file.csv", 'a', encoding='utf-8', newline='') as csvfile:
#         writer = csv.writer(csvfile, delimiter = ";")
#         writer.writerow(data)

# def update_employees(number, string):
#     try:
#         with open("S/8/file.csv", encoding='utf-8', newline='') as csvfile:
#             reader = csv.reader(csvfile, delimiter = ";")
#             data = list(reader)
#             data[number] = string
#         with open("S/8/file.csv", 'w', encoding='utf-8', newline='') as csvfile:
#             writer = csv.writer(csvfile, delimiter = ";")
#             for i in data:
#                 writer.writerow(i)
#     except IndexError:
#         print('Вы вышли за границу списка!')
#         exit()
#     except Exception:
#         print('Появилась ошибка')

# def delete(number):
#     with open("S/8/file.csv", encoding='utf-8', newline='') as csvfile:
#         reader = csv.reader(csvfile, delimiter = ";")
#         data = list(reader)
#         del data[number]
#     with open("S/8/file.csv", 'w', encoding='utf-8', newline='') as csvfile:
#         writer = csv.writer(csvfile, delimiter = ";")
#         for i in data:
#             writer.writerow(i)

# def export():
#     path = 'HW/8/1.txt'
#     data = open(path, 'a', encoding='utf-8')
#     exp = get_list()
#     data.writelines("\n".join(map(str,exp)))
#     data.close()
