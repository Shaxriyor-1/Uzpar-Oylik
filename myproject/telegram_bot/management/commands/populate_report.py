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
            id, user_name, phone_number, position, department, oclade_tarif, salary, fine, remain, premium_kurban, compensation_work_stop, premium_independentDay, material_help_retire_injury, premium_constitution, premium_womenDay, injury, premium_Navruz, premium_9May, study, compensation_unused_vac, hospitalAUP, oclade_repairment, oclade, tariff, hospitalGen, vacation, vacation_add, night_shift, surcharge, clasify, harmfulness, loyalty, cumulative_surcharge, material_help_cure, material_help_marriage, travel, premium_anniversary, premium_ramadan, premium_monthly, premium_executives, day_off, premium_house, premium_holiday, premium_order_advice, afghan_war_people, repairment, per_day_limit, premium_travel, premium_motivation, per_day_full_limit, maternity_leave, material_help_pansion, nutrition, material_help_death, region, material_help_vac, anniversaryx12, inventarization_fee, Sogspravki_fee, tmz_fee, insurance_life, insurance, Gosposhlina_fee, tax, union_fee, alimony, partly_union_fee, sanatorium_vouchers_fee, hotel_live_fee, phone_monthly_fee, GSM_fee, nutrition_fee, loan_credit_ipoteka, study_fee, loan_credit_fee, special_uniform_fee, report_fee, year, month, *_ = row
            
             # Evaluate formulas for the columns with Excel formulas

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
                    if user:
                        # Update the user's first_name and last_name
                        user.first_name = first_name
                        user.last_name = last_name
                        user.middle_name = middle_name  # Set the middle_name
                        user.save()
                        created = False  # Set created to False since the user already existed
                    else:
                        # If the user doesn't exist, create a new one
                        user = User.objects.create(phone_number=str(phone_number), first_name=first_name, last_name=last_name, middle_name=middle_name)
                        created = True
                except IntegrityError as e:
                    # Handle the integrity error if needed
                    print(f"Error: {e}")
                except User.DoesNotExist:
                    # If the user doesn't exist, create a new one
                    user = User.objects.create(phone_number=str(phone_number), first_name=first_name, last_name=last_name, middle_name=middle_name)
                    created = True
                user, created = User.objects.get_or_create(phone_number=str(phone_number), first_name=first_name, last_name=last_name, middle_name=middle_name)

                print("User--", user.phone_number, "Created---", created)
                report = EmployeeReport(
                    id=id,
                    user=user,
                    position=position,
                    department=department,
                    oclade_tarif=oclade_tarif,
                    salary=salary,
                    fine=fine,
                    remain=remain,
                    premium_kurban=premium_kurban,
                    compensation_work_stop=compensation_work_stop,
                    premium_independentDay=premium_independentDay,
                    material_help_retire_injury=material_help_retire_injury,
                    premium_constitution=premium_constitution,
                    premium_womenDay=premium_womenDay,
                    injury=injury,
                    premium_Navruz=premium_Navruz,
                    premium_9May=premium_9May,
                    study=study,
                    compensation_unused_vac=compensation_unused_vac,
                    hospitalAUP=hospitalAUP,
                    oclade_repairment=oclade_repairment,
                    oclade=oclade,
                    tariff=tariff,
                    hospitalGen=hospitalGen,
                    vacation=vacation,
                    vacation_add=vacation_add,
                    night_shift=night_shift,
                    surcharge=surcharge,
                    clasify=clasify,
                    harmfulness=harmfulness,
                    loyalty=loyalty,
                    cumulative_surcharge=cumulative_surcharge,
                    material_help_cure=material_help_cure,
                    material_help_marriage=material_help_marriage,
                    travel=travel,
                    premium_anniversary=premium_anniversary,
                    premium_ramadan=premium_ramadan,
                    premium_monthly=premium_monthly,
                    premium_executives=premium_executives,
                    day_off=day_off,
                    premium_house=premium_house,
                    premium_holiday=premium_holiday,
                    premium_order_advice=premium_order_advice,
                    afghan_war_people=afghan_war_people,
                    repairment=repairment,
                    per_day_limit=per_day_limit,
                    premium_travel=premium_travel,
                    premium_motivation=premium_motivation,
                    per_day_full_limit=per_day_full_limit,
                    maternity_leave=maternity_leave,
                    material_help_pansion=material_help_pansion,
                    nutrition=nutrition,
                    material_help_death=material_help_death,
                    region=region,
                    material_help_vac=material_help_vac,
                    anniversaryx12=anniversaryx12,
                    inventarization_fee=inventarization_fee,
                    Sogspravki_fee=Sogspravki_fee,
                    tmz_fee=tmz_fee,
                    insurance_life=insurance_life,
                    insurance=insurance,
                    Gosposhlina_fee=Gosposhlina_fee,
                    tax=tax,
                    union_fee=union_fee,
                    alimony=alimony,
                    partly_union_fee=partly_union_fee,
                    sanatorium_vouchers_fee=sanatorium_vouchers_fee,
                    hotel_live_fee=hotel_live_fee,
                    phone_monthly_fee=phone_monthly_fee,
                    GSM_fee=GSM_fee,
                    nutrition_fee=nutrition_fee,
                    loan_credit_ipoteka=loan_credit_ipoteka,
                    study_fee=study_fee,
                    loan_credit_fee=loan_credit_fee,
                    special_uniform_fee=special_uniform_fee,
                    report_fee=report_fee,
                    year=year,
                    month=month,

                )
                report_list.append(report)
            else:
                print(f"phone number is required. Now it is - {phone_number}")
        print(f"Populating {len(report_list)} reports")
        EmployeeReport.objects.bulk_create(report_list)
