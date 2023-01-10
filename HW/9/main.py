import logging
import sqlite3
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

conn = sqlite3.connect('HW/9/contacts.db')
cursor = conn.cursor()

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
    # # показать всех студентов
    cursor.execute("select * from contacts")
    results = cursor.fetchall()
    update.message.reply_text(results)
    print(results)


# def add(update, context):
#     return 1

# def add1(update, context):
#     # добавить студента
#     name = 'Степан'
#     surname = 'Степанов'
#     phone = 45648
#     description = 'Инженер'
#     cursor.execute(
#         f"insert into students (name, surname, phone, description) "
#         f"values ('{name}', '{surname}', {phone}, '{description}')")
#     conn.commit()


# def delete(update, context):
#     return 1

# def delete1(update, context):
    # # удалить студента
    # id = 5
    # cursor.execute(
    #     f"delete from students where id={id}"
    # )
    # conn.commit()


# def change(update, context):
#     return 1

# def change1(update, context):
    # # обновить данные о студенте
    # id = 3
    # cursor.execute(
    #     f"update students set name='Юрий' where id={id}"
    # )
    # conn.commit()
    # conn.close()


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

    # add_handler = ConversationHandler(
    #     entry_points=[CommandHandler('add', add)],
    #     states={
    #         1: [MessageHandler(Filters.text & ~Filters.command, add1)], },
    #     fallbacks=[CommandHandler('stop', stop)]

    # change_handler = ConversationHandler(
    #     entry_points=[CommandHandler('change', change)],
    #     states={
    #         1: [MessageHandler(Filters.text & ~Filters.command, change1)], },
    #     fallbacks=[CommandHandler('stop', stop)]
    # )

    # delete_handler = ConversationHandler(
    #     entry_points=[CommandHandler('delete', delete)],
    #     states={
    #         1: [MessageHandler(Filters.text & ~Filters.command, delete1)], },
    #     fallbacks=[CommandHandler('stop', stop)]
    # )

    start_handler = CommandHandler('start', start)

    dp.add_handler(start_handler)
    dp.add_handler(show_handler)
    # dp.add_handler(add_handler)
    # dp.add_handler(change_handler)
    # dp.add_handler(delete_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
