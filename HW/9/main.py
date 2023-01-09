import logging
import csv
import models

from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5956752552:AAHT6H3L1H7pz_VBvYU7pK6DqxAW6BphSag'


def start(update, context):
    update.message.reply_text('Выберите команду: \n \
        /show - показать всех сотрудников \n \
        /add - добавить сотрудника \n \
        /change - изменить данные сотрудника \n \
        /delete - удалить данные сотрудника')


def show(update, context):
    return 1


def show1(update, context):
    file = open("HW/9/file.csv", 'r')
    file.read(update.message.reply_text)
    file.close()
    # with open("HW/9/file.csv", encoding='utf-8') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=";")
    # update.message.reply_text(list(reader))


# def calc(update, context):
#     update.message.reply_text("Введите выражение: ")
#     return 1


# def calculate(update, context):
#         value = eval(update.message.text)
#         update.message.reply_text(value)


#         return ConversationHandler.END


# def add_employ_to_list(data):
#     with open("S/8/file.csv", 'a', encoding='utf-8', newline='') as csvfile:
#         writer = csv.writer(csvfile, delimiter = ";")
#         writer.writerow(data)

# def update_employees(number, string):
#         with open("S/8/file.csv", encoding='utf-8', newline='') as csvfile:
#             reader = csv.reader(csvfile, delimiter = ";")
#             data = list(reader)
#             data[number] = string
#         with open("S/8/file.csv", 'w', encoding='utf-8', newline='') as csvfile:
#             writer = csv.writer(csvfile, delimiter = ";")
#             for i in data:
#                 writer.writerow(i)

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


# def conv(update, context):
#     update.message.reply_text("Введите массу в килограммах: ")
#     return 1


# def converter(update, context):
#         value = int(update.message.text)
#         update.message.reply_text(value*1000)
#         return ConversationHandler.END


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    show_handler = ConversationHandler(
        entry_points=[CommandHandler('show', show)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, show1)], },
        fallbacks=[CommandHandler('stop', stop)]
    )
    # calc_handler = ConversationHandler(
    #     entry_points=[CommandHandler('calc', calc)],
    #     states={
    #         1: [MessageHandler(Filters.text & ~Filters.command, calculate)], },
    #     fallbacks=[CommandHandler('stop', stop)]
    # )

    # conv_handler = ConversationHandler(
    #     entry_points=[CommandHandler('conv', conv)],
    #     states={
    #         1: [MessageHandler(Filters.text & ~Filters.command, converter)], },
    #     fallbacks=[CommandHandler('stop', stop)]
    # )

    start_handler = CommandHandler('start', start)

    dp.add_handler(start_handler)
    dp.add_handler(show_handler)
    # dp.add_handler(calc_handler)
    # dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
