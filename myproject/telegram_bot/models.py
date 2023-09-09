import calendar
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class EmployeeReport(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)     #Телефон
    position = models.CharField(max_length=100, default="Xodim", blank=True, null=True)        #Должность 
    department = models.CharField(max_length=100, default="Uzpar", blank=True, null=True)    #Подразделение
    oclade_tarif = models.CharField(max_length=100, default="Uzpar", blank=True, null=True)    #Оклад/Тариф
    militar_regist = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Военкомат () 
    compensation_unused_vac = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Компенсация за неиспользованный отпуск ()
    study = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Учеба  ()
    premium_9May = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Премия " 9 МАЯ " ()
    injury = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Увечье ()
    premium_womenDay = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Премия к 8 марта ()
    premium_Navruz = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Премия " Навруз" ()
    premium_kurban = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Премия "Курбон Хайит"
    premium_constitution_retire = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Приказ к дню КонституцииПенсионеры () 
    health_problem_one = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Единоврем компенс по потери здоровья () 
    lose_feeder_help_Xodjiyev = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Мат/помощь по потере кормильца   (Хожиев У.) () 
    premium_independentDay = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Премия "Мустакиллик"
    compensation_work_stop = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Компенсация  при прекрашении трудового договора
    compensation_household_products = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Компенсация на сельхоз/продукты ()
    prochi_nachisleniya = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Приказ на прочие начисления ()
    hospitalAUP = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Больничный АУП ()
    trudovoy_kodeks = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Приказ "Трудовой кодекс 109 статья" ()
    premium_womenDay_retire = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  # Премия к 8 марта ( пенсионеры) ()
    material_help_retire_injury = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Матер/ная помощь пенсионерам и инвалидам
    premium_constitution = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Приказ к дню Конституции
    prikaz_product = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Приказ на Сельхоз/продукты ()
    school_items = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Школьные,учебники ()
    lose_feeder_help = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Мат/помощь по потере кормильца () 
    otpusk_ligotniy = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Отпуск льготный ()
    oclade_WTF = models.CharField(max_length=100, default="oklad", blank=True, null=True)  # Оклад (001)
    oclade_repairment_WTF = models.CharField(max_length=100, default="oklad", blank=True, null=True)  #Оклад за дни ремонта (001)
    Saturday_work_WTF = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Субботник (001)
    tariff_WTF = models.CharField(max_length=100, default="oklad", blank=True, null=True)  # Тариф (002)
    Sdelno = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Сдельно (003)
    hospital_WTF = models.CharField(max_length=100, default="oklad", blank=True, null=True)  # Больничные (004)
    vacation_WTF = models.CharField(max_length=100, default="oklad", blank=True, null=True)  #  Отпуск (005)
    vacation_add_WTF = models.CharField(max_length=100, default="oklad", blank=True, null=True)  #  Отпуск дополнительный (006)
    vacation_pregnancy = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #Отпуск по беременности и родам (007)
    night_shift_WTF = models.CharField(max_length=100, default="oklad", blank=True, null=True)  #  Ночные часы (010)
    surcharge = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Надбавка % (013)
    surcharge_ragional_coef = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Надбавка % (учавствует в расчете Районного Коэффицента) (013)
    surcharge_acc_ord = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Надбавка по приказу (014)
    clasify = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Классность (014)
    harmfulness = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Вредность (015)
    surcharge_advance_pay = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  # Доплата Надбавка (надбавка за личный вклад) (016)
    loyalty = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Выслугу лет (018)
    neyavka = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Неявка (020)
    cumulative_surcharge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Доплата за совмещение (025)
    material_help_pansion = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Материальная помощь (пенсионерам) (026)
    material_help_marriage = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Материальная помощь по  (бракосочетание) (026)
    material_help = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Материальная помощь (026)
    material_help_cure = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Мат. пом. на лечение (раздел 9 пункт 9.16 стац лечение) (026)
    material_help_tough_situation = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Материальная помощь в связи с тяжелым материальными положением (026)
    pansion = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Пенсия (027)
    childcare_2_and_3 = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Пособие по уходу за ребенком от 2 до 3 лет (028)
    childcare_upto_2 = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Пособие по уходу за ребенком до 2-х лет (028)
    travel = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Командировочные (030)
    premium_ramadan = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # ПРЕМИЯ Руза хайит (033)
    premium_one_time_racism = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Единовременная премия за рац. предложение (033)
    premium_anniversary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Единовременная премия к юбилею (033)
    last_month_account = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Перерасчет за предыдущий месяц (037)
    premium_house = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Премия по хоз деятельности (040)
    premium_monthly = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Месячная премия (040)
    premium_executives = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Премия исполнительному Органу АО "Узпаравтотранс" (040)
    day_off = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Выходные (040)
    premium_award_diploma = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Премия награждение почетной граммотой (045)
    labor_agreement = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Трудовое соглашение (045)
    premium_holiday = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Премия к празднику (045)
    premium_quarters = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Квартальная премия (050)
    last_month_account_loyalty = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Перерасчет выслуги лет (054)
    surcharge_harm_repairment_WTF = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Надбавка за вредность во время ремонта техники (055)
    vacation_contract = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Отпускные по кол. договору (056)
    premium_order_advice = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Приказ № наблюдат/совет (057)
    afghan_war_people = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Доплата участникам афганской войны (058)
    premium_PMM = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Премия РММ (059)
    repairment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Ремонт (060)
    per_day_limit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Суточные по лимиту (061)
    salary_13month = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Зарплата  13 Я (062)
    premium_travel = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Премия (Командировочные) (063)
    premium_general = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Премия (063)
    per_day_full_limit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Суточные  сверх лимита (064)
    premium_motivation = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Премия о стим. раб. (064)
    maternity_leave_WTF = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Декр. больничные (065)
    material_help_pansion_starting = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  # Материальная помощь раздел Х пункт 9,4 (уход на пенсию) (066)
    nutrition_WTF = models.CharField(max_length=100, default="oklad", blank=True, null=True)   # Питание (Доплата за питание) (067)
    premium_skvajini = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Премия по приказу за скважины (068)
    premium_contract = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Премия кол.договор (068)
    premium_svet = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Премия за цвет мет. (068)
    material_help_death = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  # Материальная помощь в связи со смертью (068)
    premium_TB = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Премия за ТБ (070)
    schooler = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Школьный (071)
    New_Year = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Новый год (072)
    region = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Районный коэффициент (100)
    material_help_vac = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  # Материальная помощь к отпуску (110)
    anniversaryx12 = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  # Юбиляры до 12минЗП (С1)
    salary_13th = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #13 зарплата (С3)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Всего начислено
    communal_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)   #Удержание за коммунальные услуги ()
    vozvrat_debitor_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)   #Возврат дебиторской задолжности ()
    tax_free_education = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)   #Возврат под/налога за обучение ()
    book_take_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)   #Удержание за приобретения книг ()
    inventarization_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание  по акту инвентаризации
    usherb_return_1 = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)   #Возврат возмещение ущерба ()
    insurance_life = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Страхование  жизни  ()
    sog_zayav_Rakhimov = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)   #Сог.заявлению Рахимов Г. ()
    yuridik_uslugi = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)   #Удержание за юридические услуги ()
    return_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)   #Возврат з/ты ()
    zarabotnaya_plata = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)   #Зароботная плата ()
    dogovor_dostovMizrob = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)   #Договор № 3 от 7/02/18г Дустов Мизроб ()
    accumulator_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)   #Удержание за аккумуляторы ()
    tmz_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание за приобретения ТМЦ ()
    Sogspravki_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Сог.справки ()
    income_tax_manual = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержано из з/п подоходный налог ()
    Gosposhlina_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Гос/пошлина ()
    telephone_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание за телефон ()
    driver_licence_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание на водит/е права ()
    avtouslugi_worker_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание с работников за автоуслуги ()
    insurance = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание Страхование ()
    usherb_return_2 = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)   #Возврат возмещение ущерба ()
    postal_expenditures = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)   #Почтовые расходы ()
    vozmesheni_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)   #Возмещение по з/п ()
    militar_regist_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Удержание Военкомат ()
    JO_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Удержание Ж/О № 3 ()
    contract_return = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Возврат (контракт) ()
    car_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Удержание за автошины ()
    micro_loan = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Микрокредит ()
    recovery_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Удержание за лечение ()
    water_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Удержание за Воду ()
    dogovor_Buxoro_EKO_TUR = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Договор № 6 Бухоро ЭКО тур ()
    dogovor_5135LGM = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Договор № 5135-08 ( ЛГМ) ()
    jurnal_order3_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #журнал ордер № 3 удерж,из з/п ()
    tax = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Подоходный налог (001)
    vznos_pensiya = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Взносы в пенсионный фонд (002)
    vznos_profsoyuz = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Взносы в профсоюз (003)
    reluctant_INPS = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Добровольный ИНПС (004)
    plastik_karta = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   #Пласт. карточка (Заработная плата на пл.карту) (005)
    alimony = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Алименты (009)
    alimony_postal_gain = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Алименты почтовый сбор (010)
    uchebnoy_zavedeniya_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   #Удержание в пользу учебного заведения (011)
    clasify_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   #Классность (014)
    viplata_otpusk = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   #Выплата отпускных (015)
    viplata_otpusk_dogovor = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   #Выплата отпускных по кол договору (016)
    hostel_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   #Общежите (017)
    vznos_partly = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   #Партийные взносы 0,5% (018)
    pereraschot = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   #Перерасчет (019)
    saturday_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   #Субботник (023)
    campus_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   #Удержание за путевки в лагерь (024)
    sanatorium_vouchers_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание за санаторные  путевки (024)
    fee_general = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание (025)
    hotel_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание за проживание в гостинице (025)
    bank_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   #Удержание банк (026)
    phone_monthly_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание за Сотовую связь (027)
    GSM_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание за ГСМ (027)
    GorGaz_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание Гор/Газ (027)
    land_owe_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание за землю (028)
    nutrition_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание за питание (029)
    electricity_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание за электроэнергию  (030)
    loan_credit_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание кредит (031)
    loan_credit_ipoteka_no_ligota = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание Ипотечный кредит ( без льгот) (031)
    loan_credit_OVERDRAFT = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание  кредит " Овердрафт"  (031)
    loan_credit_ipoteka = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   #Удержание Ипотечный кредит (031)
    study_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание За обучение (уменьшает НОБ) (031)
    loan_credit_consume = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Потребительский кредит (031)
    special_uniform_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание спец.одежды (033)
    sanksium_fee_charge_workers = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Штрафные  санкции с работников (Наказание) (034)
    sanksium_general = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   #Штрафные санкции (034)
    canteen_rent = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   #за аренду столовой (035)
    report_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание согласно Акта проверки (035)
    home_connect_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание за домашнюю связь (С4)
    fine = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)   #Всего удержано
    remain = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #К выплату
    year = models.PositiveIntegerField(null=True, blank=True)
    month = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"Id - {self.id}, {self.user.phone_number}'s Report"
    
    def save(self, *args, **kwargs):
        # Get the current date
        current_date = datetime.now()

         # Calculate the last month
        last_month = current_date.month - 1 if current_date.month > 1 else 12
        last_year = current_date.year if current_date.month > 1 else current_date.year - 1

        # Set the month and year fields
        self.month = last_month
        self.year = last_year

        super(EmployeeReport, self).save(*args, **kwargs)

    def get_month_name(self):
        if self.month:
            return calendar.month_name[self.month]
        return "Unknown"
