import logging
from token1 import token2

from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

token = token2


def start(update, context):
    update.message.reply_text(
        "Привет. Выберите /calc - калькулятор или /conv - конвертер")


def calc(update, context):
    update.message.reply_text("Введите выражение: ")
    return 1


def calculate(update, context):
    try:
        value = eval(update.message.text)
        update.message.reply_text(value)
        return ConversationHandler.END
    except Exception:
        update.message.reply_text('Введите правильное выражение!')


def conv(update, context):
    update.message.reply_text("Введите массу в килограммах: ")
    return 1


def converter(update, context):
    try:
        value = int(update.message.text)
        update.message.reply_text(value*1000)
        return ConversationHandler.END
    except Exception:
        update.message.reply_text('Введите целое число!')


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def main():
    updater = Updater(token)
    dp = updater.dispatcher
    calc_handler = ConversationHandler(
        entry_points=[CommandHandler('calc', calc)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, calculate)], },
        fallbacks=[CommandHandler('stop', stop)]
    )

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('conv', conv)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, converter)], },
        fallbacks=[CommandHandler('stop', stop)]
    )

    start_handler = CommandHandler('start', start)

    dp.add_handler(start_handler)
    dp.add_handler(calc_handler)
    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
