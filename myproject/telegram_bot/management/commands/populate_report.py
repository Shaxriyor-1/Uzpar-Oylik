import os

import openpyxl
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from telegram_bot.models import EmployeeReport

User = get_user_model()


class Command(BaseCommand):

    def add_arguments(self, parser):
        # Add any command-specific arguments here
        parser.add_argument('file_name', type=str, help='Excel report file name')

    def handle(self, *args, **options):
        file_name = options['file_name']
        file_path = os.path.join(os.path.dirname(__file__) + f"/../../reports/{file_name}")

        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        report_list = []
        for index, row in enumerate(sheet.iter_rows(min_row=2, values_only=True)):
            print(f"Populating--", row)
            phone_number, user_name, salary, fine, remain, department, position, premium_general, hourly_rate, oclade, oclade_repairment, clasify, loyalty, premium_monthly, premium_travel, premium_motivation, material_help, material_help_retire, vacation_1, vacation_2, vacation_3, nutrition, region, tax, fee, fee_prof, year, month, *_ = row
            if phone_number:
                # def evaluate_formulas(worksheet):
                #     worksheet = 'reports/oylik.xslx'
                #     for row in worksheet.iter_rows(values_only=True):
                #         for cell in row:
                #             if cell is not None and isinstance(cell, str) and cell.startswith("="):
                #                 cell.value = worksheet[cell.coordinate].value
                # # todo get value of remain from its excel formula
                # remain_val = sheet.cell(row=index + 1, column=6).value
                # remain_val = 0


                # Get first name and last name from the contact message
                name_parts = user_name.split(" ")
                first_name = name_parts[0]
                last_name = name_parts[1]
                middle_name = " ".join(name_parts[2:]) if len(name_parts) >= 4 else ""
                
                try:
                    user = User.objects.get(phone_number=str(phone_number))
                    # Update the user's first_name and last_name
                    user.first_name = first_name
                    user.last_name = last_name
                    user.middle_name = middle_name  # Set the middle_name
                    user.save()
                    created = False  # Set created to False since the user already existed
                except User.DoesNotExist:
                    # If the user doesn't exist, create a new one
                    user = User.objects.create(phone_number=str(phone_number), first_name=first_name, last_name=last_name)
                    created = True
                user, created = User.objects.get_or_create(phone_number=str(phone_number), first_name=first_name, last_name=last_name, middle_name=middle_name)

                print("User--", user.phone_number, "Created---", created)
                report = EmployeeReport(
                    user=user,
                    salary=salary,
                    fine=fine,
                    remain=remain,
                    department=department,
                    position=position,
                    premium_general=premium_general,
                    hourly_rate=hourly_rate,
                    oclade=oclade,
                    oclade_repairment=oclade_repairment,
                    clasify=clasify,
                    loyalty=loyalty,
                    premium_monthly=premium_monthly,
                    premium_travel=premium_travel,
                    premium_motivation=premium_motivation,
                    material_help=material_help,
                    material_help_retire=material_help_retire,
                    vacation_1=vacation_1,
                    vacation_2=vacation_2,
                    vacation_3=vacation_3,
                    nutrition=nutrition,
                    region=region,
                    tax=tax,
                    fee=fee,
                    fee_prof=fee_prof,
                    year=year,
                    month=month,

                )
                report_list.append(report)
            else:
                print(f"phone number is required. Now it is - {phone_number}")
        print(f"Populating {len(report_list)} reports")
        EmployeeReport.objects.bulk_create(report_list)
