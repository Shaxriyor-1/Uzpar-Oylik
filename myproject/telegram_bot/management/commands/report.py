import os

import django
import pandas as pd

# Replace 'your_django_project_name' with the name of your Django project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from telegram_bot.models import EmployeeReport


def create_employee_reports_from_excel(excel_file_path):
    # Read the Excel file into a Pandas DataFrame
    df = pd.read_excel(excel_file_path, sheet_name='Sheet1', skiprows=[0])

    # Iterate through each row in the DataFrame
    for _, row in df.iterrows():
        user_id = row['User']  # Assuming 'User' is a column in your Excel file containing user IDs
        salary = row['Salary']
        prepayment = row['Premayment']  # Assuming you changed 'avans' to 'prepayment' in the Excel file
        fine = row['Fine']
        remain = row['Remain']
        password = row['Password']  # Assuming you have a 'Password' column in the Excel file


        # Create an EmployeeReport object and save it to the database
        user_report = EmployeeReport.objects.create(
            user_id=user_id,
            salary=salary,
            prepayment=prepayment,
            fine=fine,
            remain=remain,
            password=password,
        )
        user_report.save()

# Replace 'oylik.xlsx' with the path to your Excel file
create_employee_reports_from_excel('D:/oylik.xlsx')
