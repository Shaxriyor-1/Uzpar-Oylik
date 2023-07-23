import os
import openpyxl
from django.contrib.auth import get_user_model

from django.core.management.base import BaseCommand

from telegram_bot.models import EmployeeReport

User = get_user_model()


class Command(BaseCommand):
    # todo fix this command for creating super user

    def handle(self, *args, **options):
        user = User.objects.filter(email="admin@gmail.com").first()
        if not user:
            User.objects.create_superuser(
                email="admin@gmail.com",
                password="admin",
            )
            print(f"user - {user.email} is created")
        else:
            print(f"user - {user.email} is already exists")
        # user, created = User.objects.get_or_create(
        #     email="admin@gmail.com",
        #     password="admin",
        #     is_superuser=True,
        #     is_active=True,
        #     is_staff=True,
        # )
        # print(user, created)
        # if created:
        #     print(f"User - {user.email} is created")
        # else:
        #     print(f"User - {user.email} is already exists")
