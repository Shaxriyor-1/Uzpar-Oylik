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
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Всего начислено
    fine = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)   #Всего удержано
    remain = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #К выплату
    premium_kurban = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Премия "Курбон Хайит"
    compensation_work_stop = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Компенсация  при прекрашении трудового договора
    premium_independentDay = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Премия "Мустакиллик"
    material_help_retire_injury = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Матер/ная помощь пенсионерам и инвалидам
    premium_constitution = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Приказ к дню Конституции
    premium_womenDay = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Премия к 8 марта ()
    injury = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Увечье ()
    premium_Navruz = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Премия " Навруз" ()
    premium_9May = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Премия " 9 МАЯ " ()
    study = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Учеба  ()
    compensation_unused_vac = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Компенсация за неиспользованный отпуск ()
    hospitalAUP = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Больничный АУП ()
    oclade_repairment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Часовой тариф
    oclade = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Оклад (001)
    tariff = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Тариф (002)
    hospitalGen = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Больничные (004)
    vacation = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Отпуск (005)
    vacation_add = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Отпуск дополнительный (006)
    night_shift = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Ночные часы (010)
    surcharge = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Надбавка % (013)
    clasify = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Классность (014)
    harmfulness = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Вредность (015)
    loyalty = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Месячная премия (040)
    cumulative_surcharge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Доплата за совмещение (025)
    material_help_cure = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Мат. пом. на лечение (раздел 9 пункт 9.16 стац лечение) (026)
    material_help_marriage = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Мат. пом. на лечение (раздел 9 пункт 9.16 стац лечение) (026)
    travel = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Командировочные (030)
    premium_anniversary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Единовременная премия к юбилею (033)
    premium_ramadan = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # ПРЕМИЯ Руза хайит (033)
    premium_monthly = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Месячная премия (040)
    premium_executives = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Премия исполнительному Органу АО "Узпаравтотранс" (040)
    day_off = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Выходные (040)
    premium_house = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Премия по хоз деятельности (040)
    premium_holiday = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Премия к празднику (045)
    premium_order_advice = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Приказ № наблюдат/совет (057)
    afghan_war_people = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Доплата участникам афганской войны (058)
    repairment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Ремонт (060)
    per_day_limit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Суточные по лимиту (061)
    premium_travel = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Премия (Командировочные) (063)
    premium_motivation = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Премия о стим. раб. (064)
    per_day_full_limit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Суточные  сверх лимита (064)
    maternity_leave = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Декр. больничные (065)
    material_help_pansion = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  # Материальная помощь раздел Х пункт 9,4 (уход на пенсию) (066)
    nutrition = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Питание (Доплата за питание) (067)
    material_help_death = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  # Материальная помощь в связи со смертью (068)
    region = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Районный коэффициент (100)
    material_help_vac = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  # Материальная помощь к отпуску (110)
    anniversaryx12 = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  # Юбиляры до 12минЗП (С1)
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
