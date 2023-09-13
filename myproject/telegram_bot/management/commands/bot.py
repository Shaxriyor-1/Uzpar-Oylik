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


def format_number_with_spaces(number):
    # Convert the number to a string
    number_str = str(number)
    
    # Extract the last 3 characters (decimal part)
    decimal_part = number_str[-3:]
    
    # Remove the last 3 characters
    number_str = number_str[:-3]
    
    # Initialize an empty result string
    result = ""
    
    # Iterate through the characters in the reversed number string
    for i, char in enumerate(reversed(number_str)):
        # Add the character to the result string
        result = char + result
        
        # Add a space after every 3 digits, except for the last group
        if i % 3 == 2 and i != len(number_str) - 1:
            result = " " + result
    
    # Add the decimal part
    result += decimal_part
    
    return result


    
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
    if message.contact is not None and message.contact.user_id == message.from_user.id:
        # The contact was sent using the bot's button
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
    else:
        # The contact was sent through another method, not the bot's button
        bot.send_message(message.chat.id, "Рухсат этилмаган уриниш! Хурматли ходим, сиз факат узингизни ракамингиз билан маьлумот олиб биласиз!")
















    # @bot.message_handler(content_types=['contact'])
    # def handle_contact(message):
    #     print("message.chat.id", message.chat.id)
    #     if message.contact is not None:
    #         phone_number = message.contact.phone_number.lstrip('+')
    #         user = User.objects.filter(phone_number=phone_number).first()
    #         print("user---", user)
    #         keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    #         report_button_July = KeyboardButton(text="Ҳисоботни олиш")
    #         back_to_the_start = KeyboardButton(text="Кайта Бошлаш")
    #         keyboard.add(report_button_July, back_to_the_start)

    #         if user:
    #             user.tg_chat_id = message.chat.id
    #             user.save()

    #             # Get first name and last name from the contact message
    #             first_name = message.contact.first_name
    #             last_name = message.contact.last_name

                
    #             bot.send_message(message.chat.id, f"Ассалому алейкум, {first_name} {last_name} ! Телефон ракамингиз кабул килинди. Иш хаки хисоботини олишингиз мумкин.",
    #                          reply_markup=keyboard)
                
    #         else:
    #             bot.send_message(message.chat.id,
    #                              f"Бу {phone_number} рақам билан малумот топилмади, ёки бу рақам егаси 'Uzparavtotrans' AJ ходими эмас.")







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
        # Assuming 'report' is an instance of your 'EmployeeReport' model

        if report.plastik_karta is not None:
            if report.kassa is not None:
                if report.avans is not None:
                    actual_fine = report.fine - report.kassa - report.plastik_karta - report.avans
                else:
                    actual_fine = report.fine - report.kassa - report.plastik_karta
            elif report.avans is not None:
                actual_fine = report.fine - report.plastik_karta - report.avans
            else:
                actual_fine = report.fine - report.plastik_karta
        elif report.kassa is not None:
            if report.avans is not None:
                actual_fine = report.fine - report.kassa - report.avans
            else:
                actual_fine = report.fine - report.kassa
        elif report.avans is not None:
            actual_fine = report.fine - report.avans
        else:
            actual_fine = report.fine


        return_mess = f"""
        Aссалому алейкум 'Uzparavtotrans' AJ ходими. Сизда {report.month}.{report.year} сана бўйича қуйидаги маълумотлар топилди:
        
    Расчетный листок за {report.month}.{report.year}г.
        
    I. *Обшие данные* : \n  
*Телефон* : `{report.user}`
*Сотрудник* : __{report.user.first_name} {report.user.last_name} {report.user.middle_name}__
*Подразделение* : {report.department}
*Должност* : __{report.position}__
*Оклад/Тариф* : __{report.oclade_tarif}__
"""
        
        return_mess += f""" 
    II.   *За дни/часы* :  \n
"""
        fields_to_check = [
            ("Оклад  ", report.oclade_WTF),
            ("Оклад за дни ремонта", report.oclade_repairment_WTF),
            ("Субботник", report.Saturday_work_WTF),
            ("Тариф", report.tariff_WTF),
            ("Больничные", report.hospital_WTF),
            ("Отпуск ", report.vacation_WTF),
            ("Отпуск дополнительный", report.vacation_add_WTF),
            ("Ночные часы", report.night_shift_WTF),
            ("Надбавка за вредность во время ремонта техники", report.surcharge_harm_repairment_WTF),
            ("Декр. больничные", report.maternity_leave_WTF),
            ("Доплата за питание", report.nutrition_WTF),
        ]
        
        for field_name, field_value in fields_to_check:
            if (field_value is not None) and (field_value != 0):
            # Check if the field_name ends with '_WTF'
                if not field_name.endswith('_WTF'):
                    formatted_value = format_number_with_spaces(field_value)
                    return_mess += f"{field_name}: {formatted_value}, \n"
                else:
                    return_mess += f"{field_name}: {field_value}, \n"
        
        return_mess += f""" 
    III.   *Итого начислено* : `{format_number_with_spaces(report.salary)}` : \n
"""
                    
        fields_to_check = [
            ("Военкомат ", report.militar_regist),
            ("Компенсация за неиспользованный отпуск ", report.compensation_unused_vac),
            ("Учеба", report.study),
            ('*Премия " 9 МАЯ "*', report.premium_9May),
            ("Увечье", report.injury),
            ("*Премия к 8 марта *", report.premium_womenDay),
            ("*Премия 'Навруз'*", report.premium_Navruz),
            ("*Премия 'Курбан Хайит'*", report.premium_kurban),
            ("Приказ к дню КонституцииПенсионеры ", report.premium_constitution_retire),
            ("Единоврем компенс по потери здоровья", report.health_problem_one),
            ("Мат/помощь по потере кормильца   (Хожиев У.)", report.lose_feeder_help_Xodjiyev),
            ("*Премия 'Мустакиллик'*", report.premium_independentDay),
            ("Компенсация  при прекрашении трудового договора", report.compensation_work_stop),
            ("Компенсация на сельхоз/продукты", report.compensation_household_products),
            ("Приказ на прочие начисления ", report.prochi_nachisleniya),
            ("Больничный АУП", report.hospitalAUP),
            ("Приказ Трудовой кодекс 109 статья", report.trudovoy_kodeks),
            ("Премия к 8 марта ( пенсионеры) ", report.premium_womenDay_retire),
            ("Матер/ная помощь пенсионерам и инвалидам", report.material_help_retire_injury),
            ("*Приказ к дню Конституции*", report.premium_constitution),
            ("Приказ на Сельхоз/продукты", report.prikaz_product),
            ("Школьные,учебники", report.school_items),
            ("Мат/помощь по потере кормильца ", report.lose_feeder_help),
            ("Отпуск льготный  ", report.otpusk_ligotniy),
            ("Оклад ", report.oclade_WWF),
            ("Оклад за дни ремонта ", report.oclade_repairment_WWF),
            ("Субботник ", report.Saturday_work_WWF),
            ("Тариф ", report.tariff_WWF),
            ("Сдельно ", report.Sdelno),
            ("Больничные ", report.hospital_WWF),
            ("Отпуск  ", report.vacation_WWF),
            ("Отпуск дополнительный ", report.vacation_add_WWF),
            ("Отпуск по беременности и родам ", report.vacation_pregnancy),
            ("Ночные часы ", report.night_shift_WWF),
            ("Надбавка", report.surcharge),
            ("Надбавка % (учавствует в расчете Районного Коэффицента) ", report.surcharge_ragional_coef),
            ("Надбавка по приказу", report.surcharge_acc_ord),
            ("Классность", report.clasify),
            ("Вредность", report.harmfulness),
            ("Доплата Надбавка (надбавка за личный вклад)", report.surcharge_advance_pay),
            ("Выслугу лет", report.loyalty),
            ("Неявка", report.neyavka),
            ("Доплата за совмещение", report.cumulative_surcharge),
            ("Материальная помощь (пенсионерам)", report.material_help_pansion),
            ("Материальная помощь по  (бракосочетание)", report.material_help_marriage),
            ("Материальная помощь", report.material_help),
            ("Мат. пом. на лечение (раздел 9 пункт 9.16 стац лечение)", report.material_help_cure),
            ("Материальная помощь в связи с тяжелым материальными положением", report.material_help_tough_situation),
            ("Пенсия", report.pansion),
            ("Пособие по уходу за ребенком от 2 до 3 лет", report.childcare_2_and_3),
            ("Пособие по уходу за ребенком до 2-х лет", report.childcare_upto_2),
            ("Командировочные ", report.travel),
            ("*ПРЕМИЯ Руза хайит*", report.premium_ramadan),
            ("*Единовременная премия за рац. предложение*", report.premium_one_time_racism),
            ("*Единовременная премия к юбилею*", report.premium_anniversary),
            ("Перерасчет за предыдущий месяц", report.last_month_account),
            ("Премия по хоз деятельности", report.premium_house),
            ("Месячная премия", report.premium_monthly),
            ("Премия исполнительному Органу АО 'Узпаравтотранс'", report.premium_executives),
            ("Выходные", report.day_off),
            ("Премия награждение почетной граммотой ", report.premium_award_diploma),
            ("Трудовое соглашение ", report.labor_agreement),
            ("Премия к празднику", report.premium_holiday),
            ("Квартальная премия", report.premium_quarters),
            ("Перерасчет выслуги лет", report.last_month_account_loyalty),
            ("Надбавка за вредность во время ремонта техники ", report.surcharge_harm_repairment_WWF),
            ("Отпускные по кол. договору", report.vacation_contract),
            ("Приказ № наблюдат/совет", report.premium_order_advice),
            ("*Доплата участникам афганской войны*", report.afghan_war_people),
            ("*Премия РММ*", report.premium_PMM),
            ("Ремонт", report.repairment),
            ("Суточные по лимиту", report.per_day_limit),
            ("Зарплата  13 Я", report.salary_13month),
            ("Премия (Командировочные)", report.premium_travel),
            ("Премия ", report.premium_general),
            ("Суточные  сверх лимита", report.per_day_full_limit),
            ("Премия о стим. раб.", report.premium_motivation),
            ("Декр. больничные ", report.maternity_leave_WWF),
            ("Материальная помощь раздел Х пункт 9,4 (уход на пенсию)", report.material_help_pansion_starting),
            ("Питание (Доплата за питание) ", report.nutrition_WWF),
            ("*Премия по приказу за скважины*", report.premium_skvajini),
            ("*Премия кол.договор*", report.premium_contract),
            ("*Премия за цвет мет. *", report.premium_svet),
            ("Материальная помощь в связи со смертью", report.material_help_death),
            ("*Премия за ТБ*", report.premium_TB),
            ("Школьный", report.schooler),
            ("Новый год ", report.New_Year),
            ("Районный коэффициент", report.region),
            ("Материальная помощь к отпуску", report.material_help_vac),
            ("*Юбиляры до 12минЗП*", report.anniversaryx12),
            ("*13 зарплата*", report.salary_13th),
            

            ]


        
                    
        for field_name, field_value in fields_to_check:
            if (field_value is not None) and (field_value != 0):
            # Check if the field_name ends with '_WTF'
                if not field_name.endswith('_WTF'):
                    formatted_value = format_number_with_spaces(field_value)
                    return_mess += f"{field_name}: {formatted_value}, \n"
                else:
                    return_mess += f"{field_name}: {field_value}, \n"
        
        
        return_mess += f""" 
    IV.   *Итого удержание* : `{format_number_with_spaces(actual_fine)}` \n
"""
        fields_to_check = [
            ("Удержание за коммунальные услуги", report.communal_fee),
            ("Возврат дебиторской задолжности", report.vozvrat_debitor_fee),
            ("Возврат под/налога за обучение", report.tax_free_education),
            ("Удержание за приобретения книг", report.book_take_fee),
            ("Удержание  по акту инвентаризации", report.inventarization_fee),
            ("Возврат возмещение ущерба", report.usherb_return_1),
            ("Страхование  жизни", report.insurance_life),
            ("Сог.заявлению Рахимов Г.", report.sog_zayav_Rakhimov),
            ("Удержание за юридические услуги", report.yuridik_uslugi),
            ("Возврат з/ты", report.return_salary),
            ("Зароботная плата", report.zarabotnaya_plata),
            ("Договор № 3 от 7/02/18г Дустов Мизроб", report.dogovor_dostovMizrob),
            ("Удержание за аккумуляторы", report.accumulator_fee),
            ("Удержание за приобретения ТМЦ'", report.tmz_fee),
            ("Сог.справки", report.Sogspravki_fee),
            ("Удержано из з/п подоходный налог", report.income_tax_manual),
            ("Гос/пошлина", report.Gosposhlina_fee),
            ("Удержание за телефон", report.telephone_fee),
            ("Удержание на водит/е права", report.driver_licence_fee),
            ("Удержание с работников за автоуслуги", report.avtouslugi_worker_fee),
            ("Удержание Страхование", report.insurance),
            ("Возврат возмещение ущерба ", report.usherb_return_2),
            ("Почтовые расходы ", report.postal_expenditures),
            ("Возмещение по з/п ", report.vozmesheni_salary),
            ("Удержание Военкомат ", report.militar_regist_fee),
            ("Удержание Ж/О № 3 ", report.jurnal_order3_fee),
            ("Возврат (контракт) ", report.contract_return),
            ("Удержание за автошины ", report.car_fee),
            ("Микрокредит ", report.micro_loan),
            ("Удержание за лечение ", report.recovery_fee),
            ("Удержание за Воду ", report.water_fee),
            ("Договор № 6 Бухоро ЭКО тур ", report.dogovor_Buxoro_EKO_TUR),
            ("Договор № 5135-08 ( ЛГМ) ", report.dogovor_5135LGM),
            ("журнал ордер № 3 удерж,из з/п ", report.jurnal_order3_fee),
            ("Подоходный налог", report.tax),
            ("Взносы в пенсионный фонд", report.vznos_pensiya),
            ("Взносы в профсоюз", report.vznos_profsoyuz),
            ("Добровольный ИНПС", report.reluctant_INPS),
            ("Алименты", report.alimony),
            ("Алименты почтовый сбор", report.alimony_postal_gain),
            ("Удержание в пользу учебного заведения", report.uchebnoy_zavedeniya_fee),
            ("Классность", report.clasify_fee),
            ("Выплата отпускных", report.viplata_otpusk),
            ("Выплата отпускных по кол договору", report.viplata_otpusk_dogovor),
            ("Общежите", report.hostel_fee),
            ("Партийные взносы 0,5%", report.vznos_partly),
            ("Перерасчет ", report.pereraschot),
            ("Субботник  ", report.saturday_fee),
            ("Удержание за путевки в лагерь ", report.campus_fee),
            ("Удержание за санаторные  путевки", report.sanatorium_vouchers_fee),
            ("Удержание", report.fee_general),
            ("Удержание за проживание в гостинице", report.hotel_fee),
            ("Удержание банк ", report.bank_fee),
            ("Удержание за Сотовую связь", report.phone_monthly_fee),
            ("Удержание за ГСМ", report.GSM_fee),
            ("Удержание Гор/Газ ", report.GorGaz_fee),
            ("Удержание за землю  ", report.land_owe_fee),
            ("Удержание за питание", report.nutrition_fee),
            ("Удержание за электроэнергию ", report.electricity_fee),
            ("Удержание кредит", report.loan_credit_fee),
            ("Удержание Ипотечный кредит ( без льгот) ", report.loan_credit_ipoteka_no_ligota),
            ("Удержание  кредит Овердрафт  ", report.loan_credit_OVERDRAFT),
            ("Удержание Ипотечный кредит", report.loan_credit_ipoteka),
            ("Удержание За обучение (уменьшает НОБ)", report.study_fee),
            ("Потребительский кредит", report.loan_credit_consume),
            ("Удержание спец.одежды", report.special_uniform_fee),
            ("Штрафные  санкции с работников (Наказание)", report.sanksium_fee_charge_workers),
            ("Штрафные санкции", report.sanksium_general),
            ("за аренду столовой", report.canteen_rent),
            ("Удержание согласно Акта проверки", report.report_fee),
            ("Удержание за домашнюю связь", report.home_connect_fee),
            

            ]
        for field_name, field_value in fields_to_check:
            if (field_value is not None) and (field_value != 0):
            # Check if the field_name ends with '_WTF'
                if not field_name.endswith('_WTF'):
                    formatted_value = format_number_with_spaces(field_value)
                    return_mess += f"{field_name}: {formatted_value}, \n"
                else:
                    return_mess += f"{field_name}: {field_value}, \n"
   

        
        return_mess += f""" 
    V.   *К выплату* : `{format_number_with_spaces(report.salary - actual_fine)}`
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
    

        