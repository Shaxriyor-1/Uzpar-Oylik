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
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Всего начислено
    fine = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)   #Всего удержано
    remain = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #К выплату
    department = models.CharField(max_length=100, default="Uzpar", blank=True, null=True)    #Подразделение
    position = models.CharField(max_length=100, default="Xodim", blank=True, null=True)        #Должность 
    premium_general = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  #Гос. Праздник
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Часовой тариф
    oclade = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Оклад
    oclade_repairment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Оклад за ремонт
    clasify = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Классност
    loyalty = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)    # Выслугу лет (018)
    premium_monthly = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Месячная премия (040)
    premium_travel = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Премия (Командировочные) (063)
    premium_motivation = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)  # Премия о стим. раб. (064)
    material_help = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #Материалный помош
    material_help_retire = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Материальная помощь к отпуску (110)
    vacation_1 = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Отпуск
    vacation_2 = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Отпуск (дополн.)
    vacation_3 = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  #  Отпуск (доп)
    nutrition = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Питание (Доплата за питание) (067)
    region = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Районный коэффициент (100)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)   # Подоходный налог (001)
    fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  # Взнос
    fee_prof = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00, blank=True, null=True)  # Взнос в профсоюз
    year = models.PositiveIntegerField(null=True, blank=True)
    month = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"Id - {self.id}, {self.user.phone_number}'s Report"
