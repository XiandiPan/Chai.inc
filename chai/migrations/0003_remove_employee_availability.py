# Generated by Django 4.2.5 on 2023-09-16 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_employee_availability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='availability',
        ),
    ]