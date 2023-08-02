import datetime
import logging
import openpyxl
import os
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
                                 f"Бу {phone_number} рақам билан малумот топилмади, ёки бу рақам егаси 'Uzparavtotrans' AJ ходими эмас.")

def format_number(number):
    return '{:,}'.format(number).replace(',', ' ')

@bot.message_handler(func=lambda message: message.text == "Ҳисоботни олиш - Июл.2023")
def handle_get_report(message):
    user = User.objects.filter(tg_chat_id=message.chat.id).first()
    if user:
        # Get all unique years from the EmployeeReport model
        unique_years = EmployeeReport.objects.filter(user=user).values_list('year', flat=True).distinct()
        report = EmployeeReport.objects.filter(user=user).order_by("-created_at").first()
        if report:


            return_mess = f"""
        Aссалому алейкум 'Uzparavtotrans' AJ ходими. Сизда Июль ойи бўйича қуйидаги маълумотлар топилди:
        
    Расчетный листок за Июль 2023г.
        
    I.    *Телефон* : `{report.user}`
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
            ("Оклад за дни ремонта", report.oclade_repairment),
            ("Оклад", report.oclade),
            ("Тариф", report.tariff),
            ("Больничные", report.hospitalGen),
            ("Отпуск ", report.vacation),
            ("Отпуск дополнительный", report.vacation_add),
            ("Ночные часы", report.night_shift),
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
            ("Декр. больничные", report.maternity_leave),
            ("Материальная помощь раздел Х пункт 9,4 (уход на пенсию)", report.material_help_pansion),
            ("Питание (Доплата за питание)", report.nutrition),
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
            ("Взносы в профсоюз", report.union_fee),
            ("Алименты", report.alimony),
            ("Партийные взносы 0,5%", report.partly_union_fee),
            ("Удержание за санаторные  путевки", report.sanatorium_vouchers_fee),
            ("Удержание за проживание в гостинице", report.hotel_live_fee),
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
    

    # @bot.callback_query_handler(func=lambda call: True)
    # def test_callback(call):  # <- passes a CallbackQuery type object to your function
    #     logger.info(call)

    # @bot.inline_handler(lambda query: query.query == 'text')
    # def query_text(inline_query):
    #     logger.info(inline_query)
        