import telegram
from telegram.ext import CommandHandler, Updater


def start(update, context):
      context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, welcome to your Telegram bot!")

def setup_telegram_bot(token):
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()
