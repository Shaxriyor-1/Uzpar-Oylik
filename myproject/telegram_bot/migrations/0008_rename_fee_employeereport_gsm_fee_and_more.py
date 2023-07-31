# Generated by Django 4.2.3 on 2023-07-31 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0007_alter_employeereport_clasify_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeereport',
            old_name='fee',
            new_name='GSM_fee',
        ),
        migrations.RenameField(
            model_name='employeereport',
            old_name='fee_prof',
            new_name='Gosposhlina_fee',
        ),
        migrations.RenameField(
            model_name='employeereport',
            old_name='hourly_rate',
            new_name='Sogspravki_fee',
        ),
        migrations.RenameField(
            model_name='employeereport',
            old_name='material_help',
            new_name='afghan_war_people',
        ),
        migrations.RenameField(
            model_name='employeereport',
            old_name='material_help_retire',
            new_name='alimony',
        ),
        migrations.RenameField(
            model_name='employeereport',
            old_name='premium_general',
            new_name='anniversaryx12',
        ),
        migrations.RenameField(
            model_name='employeereport',
            old_name='vacation_1',
            new_name='compensation_unused_vac',
        ),
        migrations.RenameField(
            model_name='employeereport',
            old_name='vacation_2',
            new_name='compensation_work_stop',
        ),
        migrations.RenameField(
            model_name='employeereport',
            old_name='vacation_3',
            new_name='cumilative_surcharge',
        ),
        migrations.AddField(
            model_name='employeereport',
            name='day_off',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='harmfullness',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='hospitalAUP',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='hospitalGen',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='hotel_live_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='injury',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='insurance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='insurance_life',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='inventarization_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='loan_credeit_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='loan_credit_ipoteka',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='material_help_cure',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='material_help_death',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='material_help_marriage',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='material_help_pansion',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='material_help_retire_injury',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='material_help_vac',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='maternity_leave',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='night_shift',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='nutrition_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='oclade_tarif',
            field=models.CharField(blank=True, default='Uzpar', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='partly_union_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='per_day_full_limit',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='per_day_limit',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='phone_monthly_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='premium_9May',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='premium_Navruz',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='premium_anniversary',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='premium_constitution',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='premium_executives',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='premium_holiday',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='premium_house',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='premium_independentDay',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='premium_kurban',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='premium_order_advice',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='premium_ramadan',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='premium_womenDay',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='repairment',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='report_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='sanatorium_vouchers_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='speacial_uniform_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='study',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='study_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='surcharge',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='tariff',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='tmz_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='travel',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='union_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='vacation',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='vacation_add',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]
