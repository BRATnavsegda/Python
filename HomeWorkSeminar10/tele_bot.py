from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging
import my_bot

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO, filename="my_log.log", filemode="a")


TOKEN = 'TOKEN_________________'
# получаем экземпляр `Updater`
updater = Updater(token=TOKEN, use_context=True)
# получаем экземпляр `Dispatcher`
dispatcher = updater.dispatcher

# Обратите внимание, что из обработчика в функцию
# передаются экземпляры `update` и `context`


def start(update, context):
    # `bot.send_message` это метод Telegram API
    # `update.effective_chat.id` - определяем `id` чата,
    # откуда прилетело сообщение
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Я бот, который может посчитать\nсколько времени ты взираешь на этот Мир!\n\n"
                                  "Для этого введите команду:\n /data <Ваш день рождения>\n"
                                  "Пример:\n"
                                  "/data 01.01.1999 01:01 ")
# импортируем обработчик CommandHandler,
# который фильтрует сообщения с командами

# говорим обработчику, если увидишь команду `/start`,
# то вызови функцию `start()`


start_handler = CommandHandler('start', start)

# добавляем этот обработчик в `dispatcher`
dispatcher.add_handler(start_handler)

# функция обратного вызова
def echo(update, context):
    # добавим в начало полученного сообщения строку 'ECHO: '
    text = 'Неопознанная команда...\n' \
           'Доступные команды:\n' \
           '/start\n' \
           '/data число.месяц.год час:минуты'  # + update.message.text (вернуть пользователю его сообщение)
    # `update.effective_chat.id` - определяем `id` чата,
    # откуда прилетело сообщение
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text)
# говорим обработчику `MessageHandler`, если увидишь текстовое
# сообщение (фильтр `Filters.text`)  и это будет не команда
# (фильтр ~Filters.command), то вызови функцию `echo()`


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# регистрируем обработчик `echo_handler` в экземпляре `dispatcher`
dispatcher.add_handler(echo_handler)


def data(update, context):
    # если аргументы присутствуют
    logging.info(f'ID {update.effective_chat.id} {context.args} ')
    if context.args:
        # передаем аргументы в свою функцию
        text_diff = my_bot.get_your_age(context.args)
        # `update.effective_chat.id` - определяем `id` чата,
        # откуда прилетело сообщение
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=text_diff)
    else:
        # если в команде не указан аргумент
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='В команде не указана дата')
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Пример: /data число.месяц.год час:минуты')


# обработчик команды '/data'
caps_handler = CommandHandler('data', data)
# регистрируем обработчик в диспетчере
dispatcher.add_handler(caps_handler)

# говорим экземпляру `Updater`,
# слушай сервера Telegram.
updater.start_polling()
