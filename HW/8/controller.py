import view
import models
import logging

logging.basicConfig(level=logging.INFO)

def main():
    select = view.show_menu()
    if select == 1:
        logging.info('Выбран 1')
        sotr = models.get_list()
        view.show_employees(sotr)
    elif select == 2:
        data = view.add_employees()
        models.add_employ_to_list(data)
    elif select == 3:
        change, string = view.change_employees()
        models.update_employees(change, string)
    elif select == 4:
        number = view.delete()
        models.delete(number)
    elif select == 5:
        models.export()
    logging.info('Программа отработала корректно')