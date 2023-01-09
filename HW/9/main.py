import logging
import models
import sqlite3

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



# conn = sqlite3.connect('students.db')
# cursor = conn.cursor()

# # показать всех студентов
# cursor.execute("select * from students")
# results = cursor.fetchall()
# print(results)

# # поиск записи
# surname = 'Иванов'
# cursor.execute(f"select * from students where surname like '%{surname}%'")
# results = cursor.fetchall()
# print(results)

# # добавить студента
# name = 'Степан'
# surname = 'Степанов'
# phone = 45648
# description = 'Инженер'
# cursor.execute(
#     f"insert into students (name, surname, phone, description) "
#     f"values ('{name}', '{surname}', {phone}, '{description}')")
# conn.commit()

# # удалить студента
# id = 5
# cursor.execute(
#     f"delete from students where id={id}"
# )
# conn.commit()

# # обновить данные о студенте
# id = 3
# cursor.execute(
#     f"update students set name='Юрий' where id={id}"
# )
# conn.commit()
# conn.close()



# def calc(update, context):
#     update.message.reply_text("Введите выражение: ")
#     return 1


# def calculate(update, context):
#         value = eval(update.message.text)
#         update.message.reply_text(value)
#         return ConversationHandler.END



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
    # dp.add_handler(calc_handler)
    # dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
