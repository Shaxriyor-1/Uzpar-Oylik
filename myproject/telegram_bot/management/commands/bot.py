import datetime
import logging

import pandas as pd
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from telebot import TeleBot, types
# Enable logging
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from telebot.util import quick_markup
# from .report import create_employee_reports_from_excel
from telegram_bot.models import EmployeeReport

User = get_user_model()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Объявление переменной бота
bot = TeleBot(settings.TELEGRAM_BOT_TOKEN, threaded=False)

User = get_user_model()


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
        # Create a custom keyboard with a "Share Contact" button
        keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        share_contact_button = KeyboardButton(text="Telefon raqamni yuborish", request_contact=True)
        keyboard.add(share_contact_button)
        welcome_text = """
            Assalomu aleykum, UzparAvtotrans AJ dagi oyliklarni hisobi botiga ulanganingiz bilan tabriklaymiz! Biz bilan ish haqi miqdorlarini bilib oling! Ish haqini ko'rish uchun telefon raqamingizni yuboring.
        """
        # Send a welcome message with the custom keyboard
        bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)

    @bot.message_handler(content_types=['contact'])
    def handle_contact(message):
        print("message.chat.id", message.chat.id)
        if message.contact is not None:
            phone_number = message.contact.phone_number.lstrip('+')
            user = User.objects.filter(phone_number=phone_number).first()
            print("user---", user)
            keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            get_report_button = KeyboardButton(text="Hisobotni olish - Iyul.2023")
            keyboard.add(get_report_button)
            if user:
                user.tg_chat_id = message.chat.id
                user.save()

                # Get first name and last name from the contact message
                first_name = message.contact.first_name
                last_name = message.contact.last_name


                
                bot.send_message(message.chat.id, f"Salom, {first_name} {last_name} ! Hisobotni olishingiz mumkin",
                             reply_markup=keyboard)
            else:
                bot.send_message(message.chat.id,
                                 f"Bu {phone_number} raqam bilan malumot topilmadi, yoki bu raqam egasi 'Uzparavtotrans' AJ xodimi emas!")

    @bot.message_handler(func=lambda message: message.text == "Hisobotni olish - Iyul.2023")
    def handle_get_report(message):
        user = User.objects.filter(tg_chat_id=message.chat.id).first()
        if user:
            # Get all unique years from the EmployeeReport model
            unique_years = EmployeeReport.objects.filter(user=user).values_list('year', flat=True).distinct()
            report = EmployeeReport.objects.filter(user=user).order_by("-created_at").first()
            if report:
                return_mess = f"""
            Assalomu aleykum Uzparavtotrans AJ xodimi. Sizda Iyul oyi bo'yicha quyidagi ma'lumotlar topildi:
    Bo'linma : {report.department},
    Lavozim : {report.position},
    Xodim: {report.user.first_name} {report.user.last_name} {report.user.middle_name}

            Oylik: {report.salary}
                  Shu jumladan : 
            Pitaniy: {report.nutrition},
            """

            # Check and add Premiya if it is greater than 0
            if report.premium and report.premium > 0:
                return_mess += f"Premiya : {report.premium}, "

            # Check and add Visluga if it is greater than 0
            if report.loyalty and report.loyalty > 0:
                return_mess += f"Visluga: {report.loyalty}, "

            # Check and add Rayonniy koeffitsient if it is greater than 0
            if report.region and report.region > 0:
                return_mess += f"Rayonniy koeffitsient : {report.region}, "

            return_mess += f"""

            Сакланган (удержание): {report.fine}
                  Shu jumladan : 
            Солик (налог): {report.tax},
            Взнос: {report.fee}.

            Qoldiq (остаток): {report.remain},
            """
                          
            bot.send_message(message.chat.id, return_mess)
        else:
            bot.send_message(message.chat.id, "Bunday foydalanuvchi ishchilar ro'yxatida mavjud emas! Agar bu xatolik bo'lsa bosing : /start")



    # @bot.message_handler(commands=['url'])
    # def url(message):
    #     markup = types.InlineKeyboardMarkup()
    #     btn_my_site = types.InlineKeyboardButton(text='Наш сайт', url='https://habrahabr.ru')
    #     markup.add(btn_my_site)
    #     bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup=markup)

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
    

    # @bot.callback_query_handler(func=lambda call: True)
    # def test_callback(call):  # <- passes a CallbackQuery type object to your function
    #     logger.info(call)

    # @bot.inline_handler(lambda query: query.query == 'text')
    # def query_text(inline_query):
    #     logger.info(inline_query)
        
