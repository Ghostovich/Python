import view
import model
import logging

logging.basicConfig(filename='S/7/log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO, encoding='utf-8')

def main_function():
    try:
        select = view.greeting()
        if select ==1:
            logging.info('выбран режим калькулятора')
            primer = view.get_math_example()
            result = model.calc(primer)
            view.view_result(result)
            logging.info(f'Введено значение "{result}"')
        elif select == 2:
            logging.info('выбран режим конвентер')
            massa = view.get_massa()
            logging.info(f'Введено значение "{massa}"')
            value = model.conv(massa)
            view.view_res_conv(value)
    
    except Exception as err: 
        logging.warning(f"Ошибка обработки данных {err}") 
