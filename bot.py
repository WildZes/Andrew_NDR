import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

load_dotenv(".env")
updater = Updater(token=os.getenv('token'))  # Токен API к Telegram
dispatcher = updater.dispatcher


# Обработка команд
def start_command(update, context):
    context.bot.sendMessage(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')
def text_message(update, context):
    response = 'Получил Ваше сообщение: ' + update.message.text
    context.bot.sendMessage(chat_id=update.message.chat_id, text=response)


# Хендлеры
start_command_handler = CommandHandler('start', start_command)
text_message_handler = MessageHandler(Filters.text, text_message)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(drop_pending_updates=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
