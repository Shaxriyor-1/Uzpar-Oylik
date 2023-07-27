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
        share_contact_button = KeyboardButton(text="Телефон ракамни юбориш", request_contact=True)
        keyboard.add(share_contact_button)
        welcome_text = """
            Ассалому алейкум, Uzparavtotrans AJ даги ойликларни ҳисоби ботига уланганингиз билан табриклаймиз! Биз билан иш ҳақи миқдорларини билиб олинг. Иш ҳақини кўриш учун телефон рақамингизни юборинг.
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
            get_report_button = KeyboardButton(text="Ҳисоботни олиш - Июл.2023")
            keyboard.add(get_report_button)
            if user:
                user.tg_chat_id = message.chat.id
                user.save()

                # Get first name and last name from the contact message
                first_name = message.contact.first_name
                last_name = message.contact.last_name

                
                bot.send_message(message.chat.id, f"Ассалому алейкум, {first_name} {last_name} ! Ҳисоботни олишингиз мумкин",
                             reply_markup=keyboard)
            else:
                bot.send_message(message.chat.id,
                                 f"Бу {phone_number} рақам билан малумот топилмади, ёки бу рақам егаси 'Uzparavtotrans' AJ ходими эмас!")

    @bot.message_handler(func=lambda message: message.text == "Ҳисоботни олиш - Июл.2023")
    def handle_get_report(message):
        user = User.objects.filter(tg_chat_id=message.chat.id).first()
        if user:
            # Get all unique years from the EmployeeReport model
            unique_years = EmployeeReport.objects.filter(user=user).values_list('year', flat=True).distinct()
            report = EmployeeReport.objects.filter(user=user).order_by("-created_at").first()
            if report:
                return_mess = f"""
            Aссалому алейкум 'Uzparavtotrans' AJ ходими. Сизда Июл ойи бўйича қуйидаги маълумотлар топилди:
            Расчетный листок за Июль 2023г.
    
    Телефон : {report.user}
    Сотрудник: {report.user.first_name} {report.user.last_name} {report.user.middle_name}
    Подразделение : {report.department}
    Должност : {report.position}

            Итого начислено: {report.salary} :
"""
            fields_to_check = [
                ("Премия 'Курбан Хайит'", report.premium_general),
                ("Часовой тариф", report.hourly_rate),
                ("Оклад", report.oclade),
                ("Оклад за ремонт", report.oclade_repairment),
                ("Классност", report.clasify),
                ("Отпуск", report.vacation_1),
                ("Отпуск", report.vacation_2),
                ("Отпуск доп.", report.vacation_3),
                ("Выслугу лет", report.loyalty),
                ("Месячная премия", report.premium_monthly),
                ("Премия (Командировочные)", report.premium_travel),
                ("Премия о стим. раб.", report.premium_motivation),
                ("Районный коэффициент 50", report.region),
                ("Материалный помош", report.material_help),
                ("Материальная помош к отп.", report.material_help_retire),

            ]

  
            for field_name, field_value in fields_to_check:
                if field_value and field_value > 0:
                    return_mess += f"{field_name}: {field_value}, "         

            return_mess += f"""

                    Премия 'Курбан Хайит' : {report.premium_general}
                Часовой тариф : {report.hourly_rate}
                Оклад : {report.oclade}
                Оклад за ремонт : {report.oclade_repairment}
                Классност : {report.clasify}
                Отпуск : {report.vacation_1}
                Отпуск : {report.vacation_2}
                Отпуск доп. : {report.vacation_3}
                Выслугу лет : {report.loyalty}
                Месячная премия : {report.premium_monthly}
                Премия (Командировочные) : {report.premium_travel}
                Премия о стим. раб. : {report.premium_motivation}
                Питание : {report.nutrition}
                Районный коэффициент 50 : {report.region}
                Материалный помош  : {report.material_help}
                Материальная помош к отп. : {report.material_help_retire}


            Итого удержание : {report.fine}
                Подоходный налог : {report.tax}
                Взносы в пенсионный фонд : {report.fee}
                Взносы в профсоюз : {report.fee_prof}

                                
            К выплату : {report.remain}
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
        
