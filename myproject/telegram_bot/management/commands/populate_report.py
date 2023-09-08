import datetime
import os

import openpyxl
from dateutil.relativedelta import relativedelta
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from telegram_bot.models import EmployeeReport

User = get_user_model()

current_date = datetime.datetime.now()
last_month = current_date - relativedelta(months=1)

year_l = last_month.year
month_l = last_month.month
# Convert the numeric month to a string representation
# month_string = month_l.strftime('%B')

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
            # Reset the phone_number variable at the beginning of each iteration
            phone_number = None
            print(f"Populating--", row)
            id, id, user_name, phone_number, position, department, oclade_tarif, id, id, id, id, id, id, id, id, id, id, id, militar_regist, compensation_unused_vac, study, premium_9May, injury, premium_womenDay, premium_Navruz, premium_kurban, premium_constitution_retire, health_problem_one, lose_feeder_help_Xodjiyev, premium_independentDay, compensation_work_stop, compensation_household_products, prochi_nachisleniya, hospitalAUP, trudovoy_kodeks, premium_womenDay_retire, material_help_retire_injury, premium_constitution, prikaz_product, school_items, lose_feeder_help, otpusk_ligotniy, oclade_WTF, id, oclade_repairment_WTF, id, Saturday_work_WTF, id, tariff_WTF, id, Sdelno, hospital_WTF, id, vacation_WTF, id, vacation_add_WTF, id, vacation_pregnancy, night_shift_WTF, id, surcharge, surcharge_ragional_coef, surcharge_acc_ord, clasify, harmfulness, surcharge_advance_pay, loyalty, neyavka, cumulative_surcharge, material_help_pansion, material_help_marriage, material_help, material_help_cure, material_help_tough_situation,  *_ = row
            
                # Check if 'Оклад/Тариф' is divided into two cells
            if isinstance(oclade_tarif, tuple):
                oclade_tarif = oclade_tarif[1]  # Use the second cell
            
             # Evaluate formulas for the columns with Excel formulas
            # Skip if phone_number is empty
            if not phone_number:
                print(f"Skipping row {index + 2} as phone_number is empty")
                continue
            elif phone_number:
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
                    oclade_repairment_WTF=oclade_repairment_WTF,
                    oclade_WTF=oclade_WTF,
                    tariff_WTF=tariff_WTF,
                    hospital_WTF=hospital_WTF,
                    vacation_WTF=vacation_WTF,
                    vacation_add_WTF=vacation_add_WTF,
                    night_shift_WTF=night_shift_WTF,
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
                    maternity_leave_WTF=maternity_leave_WTF,
                    material_help_pansion=material_help_pansion,
                    nutrition_WTF=nutrition_WTF,
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
                    vznos_profsoyuz=vznos_profsoyuz,
                    alimony=alimony,
                    vznos_partly=vznos_partly,
                    sanatorium_vouchers_fee=sanatorium_vouchers_fee,
                    hotel_fee=hotel_fee,
                    phone_monthly_fee=phone_monthly_fee,
                    GSM_fee=GSM_fee,
                    nutrition_fee=nutrition_fee,
                    loan_credit_ipoteka=loan_credit_ipoteka,
                    study_fee=study_fee,
                    loan_credit_fee=loan_credit_fee,
                    special_uniform_fee=special_uniform_fee,
                    report_fee=report_fee,
                    year=year_l,
                    month=month_l,


                )
                report_list.append(report)
                surcharge_advance_pay = 1
                loyalty = 1
                neyavka = 2
                cumulative_surcharge = 23
                material_help_pansion = 3
                material_help_marriage = 3
                material_help = 3
                material_help_cure = 34234
                material_help_tough_situation = 123
                pansion = 12432
                childcare_2_and_3 = 23523
                childcare_upto_2 = 543
                travel = 345
                premium_ramadan = 234
                premium_one_time_racism = 1234
                premium_anniversary = 12345
                last_month_account = 567
                premium_house = 789
                premium_monthly = 890
                premium_executives = 987
                day_off = 876
                premium_award_diploma = 765
                labor_agreement = 654
                premium_holiday = 543
                premium_quarters = 432
                last_month_account_loyalty = 321
                surcharge_harm_repairment_WTF = 210
                vacation_contract = 345
                premium_order_advice = 567
                afghan_war_people = 678
                premium_PMM = 789
                repairment = 890
                per_day_limit = 1234
                salary_13month = 4321
                premium_travel = 5432
                premium_general = 6543
                per_day_full_limit = 7654
                premium_motivation = 8765
                maternity_leave_WTF = 9876
                material_help_pansion = 10987
                nutrition_WTF = 21098
                premium_skvajini = 32109
                premium_contract = 43210
                premium_svet = 54321
                material_help_death = 65432
                premium_TB = 76543
                schooler = 87654
                New_Year = 98765
                region = 109876
                material_help_vac = 210987
                anniversaryx12 = 321098
                salary_13th = 432109
                salary = 543210
                communal_fee = 654321
                vozvrat_debitor_fee = 765432
                tax_free_education = 876543
                book_take_fee = 987654
                inventarization_fee = 1098765
                usherb_return_1 = 2109876
                insurance_life = 3210987
                sog_zayav_Rakhimov = 4321098
                yuridik_uslugi = 5432109
                return_salary = 6543210
                zarabotnaya_plata = 7654321
                dogovor_dostovMizrob = 8765432
                accumulator_fee = 9876543
                tmz_fee = 10987654
                Sogspravki_fee = 21098765
                income_tax_manual = 32109876
                Gosposhlina_fee = 43210987
                telephone_fee = 54321098
                driver_licence_fee = 65432109
                avtouslugi_worker_fee = 76543210
                insurance = 87654321
                usherb_return_2 = 98765432
                postal_expenditures = 109876543
                vozmesheni_salary = 210987654
                militar_regist_fee = 321098765
                JO_fee = 432109876
                contract_return = 543210987
                car_fee = 654321098
                micro_loan = 765432109
                recovery_fee = 876543210
                water_fee = 987654321
                dogovor_Buxoro_EKO_TUR = 1098765432
                dogovor_5135LGM = 2109876543
                jurnal_order3_fee = 3210987654
                tax = 4321098765
                vznos_pensiya = 5432109876
                vznos_profsoyuz = 6543210987
                reluctant_INPS = 7654321098
                alimony = 8765432109
                alimony_postal_gain = 9876543210
                uchebnoy_zavedeniya_fee = 10987654321
                clasify_fee = 21098765432
                viplata_otpusk = 32109876543
                viplata_otpusk_dogovor = 43210987654
                hostel_fee = 54321098765
                vznos_partly = 65432109876
                pereraschot = 76543210987
                saturday_fee = 87654321098
                campus_fee = 98765432109
                sanatorium_vouchers_fee = 109876543210
                fee_general = 210987654321
                hotel_fee = 321098765432
                bank_fee = 432109876543
                phone_monthly_fee = 543210987654
                GSM_fee = 654321098765
                GorGaz_fee = 765432109876
                land_owe_fee = 876543210987
                nutrition_fee = 987654321098
                electricity_fee = 1098765432109
                loan_credit_fee = 2109876543210
                loan_credit_ipoteka_no_ligota = 3210987654321
                loan_credit_OVERDRAFT = 4321098765432
                loan_credit_ipoteka = 5432109876543
                study_fee = 6543210987654
                loan_credit_consume = 7654321098765
                special_uniform_fee = 8765432109876
                sanksium_fee_charge_workers = 9876543210987
                sanksium_general = 10987654321098
                canteen_rent = 21098765432109
                report_fee = 32109876543210
                home_connect_fee = 43210987654321
                fine = 54321098765432
                remain = 65432109876543
                year = 76543210987654
                month = 87654321098765


   
            else:
                print(f"phone number is required. Now it is - {phone_number}")
        print(f"Populating {len(report_list)} reports")
        EmployeeReport.objects.bulk_create(report_list)


