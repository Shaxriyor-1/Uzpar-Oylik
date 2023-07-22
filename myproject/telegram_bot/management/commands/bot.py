import datetime
import logging

from django.conf import settings
from django.core.management.base import BaseCommand
from telebot import TeleBot, types
# Enable logging
from telebot.util import quick_markup

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Объявление переменной бота
bot = TeleBot(settings.TELEGRAM_BOT_TOKEN, threaded=False)


# Название класса обязательно - "Command"
class Command(BaseCommand):
    # Используется как описание команды обычно
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)  # Сохранение обработчиков
        bot.load_next_step_handlers()  # Загрузка обработчиков
        bot.infinity_polling()

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        logger.info("-------start pressed---")
        bot.reply_to(message, """\
        Assalomu aleykum, UzparAvtotrans AJ dagi oyliklarni hisobi botiga ulanganingiz bilan tabriklaymiz!
Biz bilan ish haqi miqdorlarini bilib oling! Ish haqini ko'rish uchun telefon raqamingizni / belgisi bilan 9 raqamlik qilib jo'nating. ( /XXYYYYYYY = /901234567)\
        """)
        
    @bot.message_handler(commands=['997052366'])
    def send_welcome(message):
        logger.info("-------start pressed---")
        bot.reply_to(message, """\
        Assalomu aleykum, Bahronov Shaxriyor. Avgust oyidagi oylikni bilish uchun parolingizni / belgisi bilan kiriting! (/parol)\
        """)
        
    @bot.message_handler(commands=['41wy7d'])
    def send_welcome(message):
        logger.info("-------start pressed---")
        bot.reply_to(message, """\
        Sizning Avgust oyidagi oyligingiz : 
        Hisoblandi (Начислено) : 5 430 000
        Ushlandi (Удержано) : 0
        Avans oldingiz (Партянка) : 2 820 000
        Yana olishingiz kerak (Остаток) : 2 610 000
        \
        """)

    # @bot.message_handler(func=lambda message: True)
    # def echo_message(message):
    #     bot.reply_to(message, message.text)

    @bot.message_handler(commands=['url'])
    def url(message):
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Наш сайт', url='https://habrahabr.ru')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup=markup)

    @bot.message_handler(commands=['switch'])
    def switch(message):
        # markup = types.InlineKeyboardMarkup()
        markup = quick_markup({
            'Twitter': {'url': 'https://twitter.com'},
            'Facebook': {'url': 'https://facebook.com'},
            'Back': {'callback_data': 'whatever'}
        }, row_width=2)
        switch_button = types.InlineKeyboardButton(text='Try', switch_inline_query="Telegram")
        markup.add(switch_button)
        bot.send_message(message.chat.id, "Выбрать чат", reply_markup=markup)
    

    @bot.callback_query_handler(func=lambda call: True)
    def test_callback(call):  # <- passes a CallbackQuery type object to your function
        logger.info(call)

    @bot.inline_handler(lambda query: query.query == 'text')
    def query_text(inline_query):
        logger.info(inline_query)
        