from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class EmployeeReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.IntegerField()
    prepayment = models.IntegerField()
    fine = models.IntegerField()
    remain = models.IntegerField()
    password = models.CharField(max_length=100, default='')  # Add the default value as an empty string
    
    def __str__(self):
        return f"{self.user.username}'s Report"
