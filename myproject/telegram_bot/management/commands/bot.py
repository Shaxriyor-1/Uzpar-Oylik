import datetime
import logging

import pandas as pd
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from telebot import TeleBot, types
# Enable logging
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.util import quick_markup

# from .report import create_employee_reports_from_excel
from telegram_bot.models import EmployeeReport

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Объявление переменной бота
bot = TeleBot(settings.TELEGRAM_BOT_TOKEN, threaded=False)

User = get_user_model()

# Load the Excel file into a DataFrame
# excel_file_path = 'D:/oylik.xlsx'

# df = pd.read_excel(excel_file_path)

# Function to search for user data based on the provided phone number
# def get_user_data_by_phone_number(phone_number):
#     row = df[df['User'] == phone_number]
#     if not row.empty:
#         user_name = row.iloc[0]['Name']
#         user_salary = row.iloc[0]['Salary']
#         return user_name, user_salary
#     else:
#         return None


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
            phone_number = message.contact.phone_number
            user = User.objects.filter(phone_number=phone_number).first()
            print("user---", user)
            keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            get_report_button = KeyboardButton(text="Hisobotni olish")
            keyboard.add(get_report_button)
            if user:
                user.tg_chat_id = message.chat.id
                user.save()
                # todo get first_name, last_name from user
                bot.send_message(message.chat.id, f"Salom, first_name last_name! Hisobotni olishingiz mumkin",
                                 reply_markup=keyboard)
            else:
                bot.send_message(message.chat.id,
                                 f"Bu {phone_number} raqam bilan malumot topilmadi")

    @bot.message_handler(func=lambda message: message.text == "Hisobotni olish")
    def handle_get_report(message):
        user = User.objects.filter(tg_chat_id=message.chat.id).first()
        if user:
            report = EmployeeReport.objects.filter(user=user).order_by("created_at").first()
            if report:
                return_mess = f"""
                Oylik: {report.salary},
                Avans: {report.prepayment},
                Jarima: {report.fine},
                Qoldiq: {report.remain},
                """
                bot.send_message(message.chat.id, return_mess)
            else:
                return_mess = f"""
                                Malumot topilmadi
                                """
                bot.send_message(message.chat.id, return_mess)
        else:
            bot.send_message(message.chat.id, "Bunday foydalanivchi topilmadi")


    # @bot.message_handler(commands=['get_data'])  # Custom command to get user data
    # def get_user_data(message):
    #     phone_number = message.text.split(' ')[1]  # Extract the phone number from the command
    #     user_data = get_user_data_by_phone_number(phone_number)
    #     if user_data:
    #         user_name, user_salary = user_data
    #         response_message = f"User: {user_name}\nSalary: {user_salary}"
    #     else:
    #         response_message = "User not found in the database."
    #
    #     bot.reply_to(message, response_message)

    # @bot.message_handler(func=lambda message: True)
    # def echo_message(message):
    #     bot.reply_to(message, message.text)

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
        
