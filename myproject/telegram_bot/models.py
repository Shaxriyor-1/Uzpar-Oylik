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
    oclade_WTF = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Оклад (001)
    oclade_repairment_WTF = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Оклад за дни ремонта (001)
    Saturday_work_WTF = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Субботник (001)
    tariff_WTF = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Тариф (002)
    Sdelno = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Сдельно (003)
    hospital_WTF = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Больничные (004)
    vacation_WTF = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Отпуск (005)
    vacation_add_WTF = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Отпуск дополнительный (006)
    vacation_pregnancy = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #Отпуск по беременности и родам (007)
    night_shift_WTF = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Ночные часы (010)
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
    material_help_pansion = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  # Материальная помощь раздел Х пункт 9,4 (уход на пенсию) (066)
    nutrition_WTF = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Питание (Доплата за питание) (067)
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
    fine = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)   #Всего удержано
    remain = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #К выплату
    inventarization_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание  по акту инвентаризации
    Sogspravki_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Сог.справки ()
    tmz_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание за приобретения ТМЦ ()
    insurance_life = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Страхование  жизни  ()
    insurance = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание Страхование ()
    Gosposhlina_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Гос/пошлина ()
    tax = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Подоходный налог (001)
    union_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  # Взносы в профсоюз (003)
    alimony = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Алименты
    partly_union_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  # Партийные взносы 0,5% (018)
    sanatorium_vouchers_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание за санаторные  путевки (024)
    hotel_live_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание за проживание в гостинице (025)
    phone_monthly_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание за Сотовую связь (027)
    GSM_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание за ГСМ (027)
    nutrition_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание за питание (029)
    loan_credit_ipoteka = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание Ипотечный кредит (031)
    study_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание За обучение (уменьшает НОБ) (031)
    loan_credit_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание кредит (031)
    special_uniform_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание спец.одежды (033)
    report_fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Удержание согласно Акта проверки (035)
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
