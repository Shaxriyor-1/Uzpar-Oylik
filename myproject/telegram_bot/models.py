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
    salary = models.IntegerField()
    prepayment = models.IntegerField()
    fine = models.IntegerField()
    remain = models.IntegerField()
    # password = models.CharField(max_length=100, default='')  # Add the default value as an empty string
    
    def __str__(self):
        return f"Id - {self.id}, {self.user.phone_number}'s Report"
