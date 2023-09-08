import datetime
import logging
import os

import openpyxl
# import pandas as pd
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

def format_number(number):
    return '{:,}'.format(number).replace(',', ' ')

# verified_secret_codes = {}

# def reset_user_verification(chat_id):
#     verified_secret_codes[chat_id] = False

# def is_valid_secret_code(code):
#     print("code.chat.id", code.chat.id)
#     user = User.objects.filter(tg_chat_id=code.chat.id).first()
#     # Check the secret code against the password in the Excel file
#     if user:
#         unique_years = EmployeeReport.objects.filter(user=user).values_list('year', flat=True).distinct()
#         report = EmployeeReport.objects.filter(user=user).order_by("-created_at").first()
#         excel_password = report.password
#         return code == excel_password

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
        # Reset the verification for the user when they start the bot
        # reset_user_verification(message.chat.id)
        # Create a custom keyboard with a "Share Contact" button
        keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        share_contact_button = KeyboardButton(text="Телефон ракамни юбориш", request_contact=True)
        keyboard.add(share_contact_button)
        welcome_text = """
            Ассалому алейкум, сиз "Uzparavtotrans" AJ даги ойликларни ҳисоби ботига уландингиз. Бу ерда иш ҳақи миқдорини билиб олинг. Иш ҳақини кўриш учун телефон рақамингизни юборинг.
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
            report_button_July = KeyboardButton(text="Ҳисоботни олиш")
            back_to_the_start = KeyboardButton(text="Кайта Бошлаш")
            keyboard.add(report_button_July, back_to_the_start)

            if user:
                user.tg_chat_id = message.chat.id
                user.save()

                # Get first name and last name from the contact message
                first_name = message.contact.first_name
                last_name = message.contact.last_name

                
                bot.send_message(message.chat.id, f"Ассалому алейкум, {first_name} {last_name} ! Телефон ракамингиз кабул килинди. Иш хаки хисоботини олишингиз мумкин.",
                             reply_markup=keyboard)
                
            else:
                bot.send_message(message.chat.id,
                                 f"Бу {phone_number} рақам билан малумот топилмади, ёки бу рақам егаси 'Uzparavtotrans' AJ ходими эмас.")

# Add a handler for secret code message
# @bot.message_handler(func=lambda message: message.text and len(message.text) == 6)
# def handle_secret_code(message):
    # user = User.objects.filter(tg_chat_id=message.chat.id).first()
    # if user:
        # unique_years = EmployeeReport.objects.filter(user=user).values_list('year', flat=True).distinct()
        # report = EmployeeReport.objects.filter(user=user).order_by("-created_at").first()
        # excel_password = report.password
        # if excel_password and message.text == excel_password:
            # verified_secret_codes[message.chat.id] = True
            # keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            # get_year_2022 = KeyboardButton(text="2022")
            # get_year_2023 = KeyboardButton(text="2023")
            # get_year_2024 = KeyboardButton(text="2024")
            # get_year_2025 = KeyboardButton(text="2025")
            # keyboard.add(get_year_2022, get_year_2023, get_year_2024, get_year_2025)
            # bot.send_message(message.chat.id, "Махсус код тасдикланди. Хисобот учун йилни танланг:", reply_markup=keyboard)
        # else:
            # bot.send_message(message.chat.id, "Махсус код нотогри киритилди. Илтимос кайта уриниб куринг")
    # else:
    #     bot.send_message(message.chat.id, "User not found. Please enter your phone number first using the /start command.")

@bot.message_handler(func=lambda message: message.text == "Маълумотлар")
def handle_2023(message):
    # Check if the secret code is verified for the user
    user = User.objects.filter(tg_chat_id=message.chat.id).first()
    # if message.chat.id in verified_secret_codes and verified_secret_codes[message.chat.id]:
        # Create a new keyboard with the "Ҳисоботни олиш - Июл.2023" button
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    # keyboard.add(report_button_July, back_to_the_start)
    # Send the new keyboard as a reply to the "2023" button press
    bot.send_message(message.chat.id, "Керакли булимни танланг:", reply_markup=keyboard)

# Add a handler for other buttons (2022, 2024, 2025)
# @bot.message_handler(func=lambda message: message.text in ["2022", "2024", "2025"])
# def handle_other_years(message):
    # Check if the secret code is verified for the user
    # user = User.objects.filter(tg_chat_id=message.chat.id).first()
    # if message.chat.id in verified_secret_codes and verified_secret_codes[message.chat.id]:
    #     bot.send_message(message.chat.id, "Хозирча малумот мавжуд эмас.")


@bot.message_handler(func=lambda message: message.text == "Кайта Бошлаш")
def handle_restart(message):
    # reset_user_verification(message.chat.id)
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    share_contact_button = KeyboardButton(text="Телефон ракамни юбориш", request_contact=True)
    keyboard.add(share_contact_button)
    welcome_text = """
        Ассалому алейкум, Uzparavtotrans AJ даги ойликларни ҳисоби ботига уланганингиз билан табриклаймиз! Биз билан иш ҳақи миқдорларини билиб олинг. Иш ҳақини кўриш учун телефон рақамингизни юборинг.
    """
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)



@bot.message_handler(func=lambda message: message.text == "Ҳисоботни олиш")
def handle_get_report(message):
     # Check if the secret code is verified for the user
    user = User.objects.filter(tg_chat_id=message.chat.id).first()
    # if message.chat.id in verified_secret_codes and verified_secret_codes[message.chat.id]:
        # user = User.objects.filter(tg_chat_id=message.chat.id).first()
    if user:
            # Get all unique years from the EmployeeReport model
        # unique_years = EmployeeReport.objects.filter(user=user).values_list('year', flat=True).distinct()
        report = EmployeeReport.objects.filter(user=user).order_by("-created_at").first()
        if report :


                return_mess = f"""
        Aссалому алейкум 'Uzparavtotrans' AJ ходими. Сизда {report.month}.{report.year} сана бўйича қуйидаги маълумотлар топилди:
        
    Расчетный листок за {report.month}.{report.year}г.
        
    I.  *Телефон* : `{report.user}`
        *Сотрудник* : __{report.user.first_name} {report.user.last_name} {report.user.middle_name}__
        *Подразделение* : {report.department}
        *Должност* : __{report.position}__
        *Оклад/Тариф* : __{report.oclade_tarif}__
    
    II.   *Итого начислено* : `{format_number(report.salary)}` : \n
"""
        fields_to_check = [
            ("*Премия 'Курбан Хайит'*", report.premium_kurban),
            ("Компенсация  при прекрашении трудового договора", report.compensation_work_stop),
            ("*Премия 'Мустакиллик'*", report.premium_independentDay),
            ("Матер/ная помощь пенсионерам и инвалидам", report.material_help_retire_injury),
            ("*Премия к дню Конституции*", report.premium_constitution),
            ("Увечье", report.injury),
            ("*Премия 'Навруз'*", report.premium_Navruz),
            ('*Премия " 9 МАЯ "*', report.premium_9May),
            ("Учеба", report.study),
            ("Компенсация за неиспользованный отпуск", report.compensation_unused_vac),
            ("Больничный АУП", report.hospitalAUP),
            ("Оклад за дни ремонта", report.oclade_repairment_WTF),
            ("Оклад", report.oclade_WTF),
            ("Тариф", report.tariff_WTF),
            ("Больничные", report.hospital_WTF),
            ("Отпуск ", report.vacation_WTF),
            ("Отпуск дополнительный", report.vacation_add_WTF),
            ("Ночные часы", report.night_shift_WTF),
            ("Надбавка", report.surcharge),
            ("Классность", report.clasify),
            ("Вредность", report.harmfulness),
            ("Выслугу лет", report.loyalty),
            ("Доплата за совмещение", report.cumulative_surcharge),
            ("Мат. пом. на лечение (раздел 9 пункт 9.16 стац лечение)", report.material_help_cure),
            ("Материальная помощь по  (бракосочетание)", report.material_help_marriage),
            ("Командировочные ", report.travel),
            ("*Единовременная премия к юбилею*", report.premium_anniversary),
            ("*ПРЕМИЯ Руза хайит*", report.premium_ramadan),
            ("Месячная премия", report.premium_monthly),
            ("Премия исполнительному Органу АО 'Узпаравтотранс'", report.premium_executives),
            ("Выходные", report.day_off),
            ("Премия по хоз деятельности", report.premium_house),
            ("*Премия к празднику*", report.premium_holiday),
            ("Приказ № наблюдат/совет", report.premium_order_advice),
            ("*Доплата участникам афганской войны*", report.afghan_war_people),
            ("Ремонт", report.repairment),
            ("Суточные по лимиту", report.per_day_limit),
            ("Премия (Командировочные)", report.premium_travel),
            ("Премия о стим. раб.", report.premium_motivation),
            ("Суточные  сверх лимита", report.per_day_full_limit),
            ("Декр. больничные", report.maternity_leave_WTF),
            ("Материальная помощь раздел Х пункт 9,4 (уход на пенсию)", report.material_help_pansion),
            ("Питание (Доплата за питание)", report.nutrition_WTF),
            ("Материальная помощь в связи со смертью", report.material_help_death),
            ("Районный коэффициент", report.region),
            ("Материальная помощь к отпуску", report.material_help_vac),
            ("*Юбиляры до 12минЗП*", report.anniversaryx12),

            ]

        for field_name, field_value in fields_to_check:
            if (field_value is not None) and (field_value != 0) :
                return_mess += f"    {field_name}: {format_number(field_value)}, \n"         

        
        return_mess += f""" 
    III.   *Итого удержание* : `{format_number(report.fine)}` \n
"""
        fields_to_check = [
            ("Удержание  по акту инвентаризации", report.inventarization_fee),
            ("Сог.справки", report.Sogspravki_fee),
            ("Удержание за приобретения ТМЦ'", report.tmz_fee),
            ("Страхование  жизни ", report.insurance_life),
            ("Удержание Страхование", report.insurance),
            ("Гос/пошлина", report.Gosposhlina_fee),
            ("Подоходный налог", report.tax),
            ("Взносы в профсоюз", report.vznos_profsoyuz),
            ("Алименты", report.alimony),
            ("Партийные взносы 0,5%", report.vznos_partly),
            ("Удержание за санаторные  путевки", report.sanatorium_vouchers_fee),
            ("Удержание за проживание в гостинице", report.hotel_fee),
            ("Удержание за Сотовую связь", report.phone_monthly_fee),
            ("Удержание за ГСМ", report.GSM_fee),
            ("Удержание за питание", report.nutrition_fee),
            ("Удержание Ипотечный кредит", report.loan_credit_ipoteka),
            ("Удержание За обучение (уменьшает НОБ)", report.study_fee),
            ("Удержание кредит", report.loan_credit_fee),
            ("Удержание спец.одежды", report.special_uniform_fee),
            ("Удержание согласно Акта проверки", report.report_fee),

            ]
        for field_name, field_value in fields_to_check:
            if (field_value is not None) and (field_value != 0) :
                return_mess += f"    {field_name}: {format_number(field_value)}, \n"         

        
        return_mess += f""" 
    IV.   *К выплату* : `{format_number(report.remain)}`
        """

                        
        bot.send_message(message.chat.id, return_mess, parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "Бундай фойдаланувчи ишчилар руйхатида мавжуд эмас! Агар бу хатолик булса босинг : /start")


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
    

        