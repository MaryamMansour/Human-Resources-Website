# Generated by Django 4.0.4 on 2022-05-22 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0021_alter_employee_gender_alter_employee_maritalstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6),
        ),
        migrations.AlterField(
            model_name='employee',
            name='maritalstatus',
            field=models.CharField(choices=[('S', 'Single'), ('M', 'Married')], max_length=7),
        ),
    ]
