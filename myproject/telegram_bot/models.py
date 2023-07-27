from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class EmployeeReport(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    prepayment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fine = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    remain = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    department = models.CharField(max_length=100, default="Uzpar")
    position = models.CharField(max_length=100, default="Xodim")
    premium = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    loyalty = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    nutrition = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00)
    region = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00)
    fee = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00)
    year = models.PositiveIntegerField(null=True, blank=True)
    month = models.PositiveIntegerField(null=True, blank=True)
    days = models.CharField(max_length=100, default="Ishlamagan")
    
    def __str__(self):
        return f"Id - {self.id}, {self.user.phone_number}'s Report"
