# Импортируем нужные комопненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

# Proxy
#PROXY = {'proxy_url': '',
#         '': {'username': '','password': ''}}

def greet_user(update, context):
    print('Вызван /start')
    #print(1/0)
    update.message.reply_text('Hello Dear User!')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():

    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Бот стартовал!')
    mybot.start_polling()
    mybot.idle()

# Вызываем функцию main() - именно эта строчка запускает бота
if __name__ == '__main__':
    main()