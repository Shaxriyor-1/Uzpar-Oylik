# Generated by Django 4.2.3 on 2023-09-10 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0009_alter_employeereport_saturday_work_wtf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeereport',
            name='GSM_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='GorGaz_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='Gosposhlina_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='JO_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='New_Year',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='Saturday_work_WTF',
            field=models.CharField(blank=True, default='oklad', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='Sdelno',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='Sogspravki_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='accumulator_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='afghan_war_people',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='alimony',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='alimony_postal_gain',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='anniversaryx12',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='avtouslugi_worker_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='bank_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='book_take_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='campus_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='canteen_rent',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='car_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='childcare_2_and_3',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='childcare_upto_2',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='clasify',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='clasify_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='communal_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='compensation_household_products',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='compensation_unused_vac',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='compensation_work_stop',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='contract_return',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='cumulative_surcharge',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='day_off',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='department',
            field=models.CharField(blank=True, default='Uzpar', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='dogovor_5135LGM',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='dogovor_Buxoro_EKO_TUR',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='dogovor_dostovMizrob',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='driver_licence_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='electricity_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='fee_general',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='fine',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='harmfulness',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='health_problem_one',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='home_connect_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='hospitalAUP',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='hospital_WTF',
            field=models.CharField(blank=True, default='oklad', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='hostel_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='hotel_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='income_tax_manual',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='injury',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='insurance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='insurance_life',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='inventarization_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='jurnal_order3_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='labor_agreement',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='land_owe_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='last_month_account',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='last_month_account_loyalty',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='loan_credit_OVERDRAFT',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='loan_credit_consume',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='loan_credit_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='loan_credit_ipoteka',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='loan_credit_ipoteka_no_ligota',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='lose_feeder_help',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='lose_feeder_help_Xodjiyev',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='loyalty',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='material_help',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='material_help_cure',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='material_help_death',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='material_help_marriage',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='material_help_pansion',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='material_help_pansion_starting',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='material_help_retire_injury',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='material_help_tough_situation',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='material_help_vac',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='maternity_leave_WTF',
            field=models.CharField(blank=True, default='oklad', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='micro_loan',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='militar_regist',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='militar_regist_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='neyavka',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='night_shift_WTF',
            field=models.CharField(blank=True, default='oklad', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='nutrition_WTF',
            field=models.CharField(blank=True, default='nutrition', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='nutrition_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='oclade_WTF',
            field=models.CharField(blank=True, default='oklad', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='oclade_repairment_WTF',
            field=models.CharField(blank=True, default='oklad', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='oclade_tarif',
            field=models.CharField(blank=True, default='Uzpar', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='otpusk_ligotniy',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='pansion',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='per_day_full_limit',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='per_day_limit',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='pereraschot',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='phone_monthly_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='plastik_karta',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='position',
            field=models.CharField(blank=True, default='Xodim', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='postal_expenditures',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_9May',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_Navruz',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_PMM',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_TB',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_anniversary',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_award_diploma',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_constitution',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_constitution_retire',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_contract',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_executives',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_general',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_holiday',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_house',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_independentDay',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_kurban',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_monthly',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_motivation',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_one_time_racism',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_order_advice',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_quarters',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_ramadan',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_skvajini',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_svet',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_travel',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_womenDay',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='premium_womenDay_retire',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='prikaz_product',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='prochi_nachisleniya',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='recovery_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='region',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='reluctant_INPS',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='remain',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='repairment',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='report_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='return_salary',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='salary_13month',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='salary_13th',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='sanatorium_vouchers_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='sanksium_fee_charge_workers',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='sanksium_general',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='saturday_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='school_items',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='schooler',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='sog_zayav_Rakhimov',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='special_uniform_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='study',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='study_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='surcharge',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='surcharge_acc_ord',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='surcharge_advance_pay',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='surcharge_harm_repairment_WTF',
            field=models.CharField(blank=True, default='oklad', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='surcharge_ragional_coef',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='tariff_WTF',
            field=models.CharField(blank=True, default='oklad', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='tax',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='tax_free_education',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='telephone_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='tmz_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='travel',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='trudovoy_kodeks',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='uchebnoy_zavedeniya_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='usherb_return_1',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='usherb_return_2',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='vacation_WTF',
            field=models.CharField(blank=True, default='oklad', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='vacation_add_WTF',
            field=models.CharField(blank=True, default='oklad', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='vacation_contract',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='vacation_pregnancy',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='viplata_otpusk',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='viplata_otpusk_dogovor',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='vozmesheni_salary',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='vozvrat_debitor_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='vznos_partly',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='vznos_pensiya',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='vznos_profsoyuz',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='water_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='yuridik_uslugi',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeereport',
            name='zarabotnaya_plata',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
    ]
