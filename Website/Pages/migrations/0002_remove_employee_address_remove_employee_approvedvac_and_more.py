# Generated by Django 4.0.4 on 2022-05-19 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='address',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='approvedvac',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='availablevac',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='dateofBirth',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='maritalstatus',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='phoneNum',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='salary',
        ),
    ]
