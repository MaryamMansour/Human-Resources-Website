# Generated by Django 4.0.4 on 2022-05-19 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0011_rename_id_vacations_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacations',
            name='employee',
        ),
    ]