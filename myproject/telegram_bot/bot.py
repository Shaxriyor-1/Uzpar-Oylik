import logging

from django.conf import settings
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    logger.info("Received /start command")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, this is your Telegram bot!")


def setup_telegram_bot():
    updater = Updater(token=settings.TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()

