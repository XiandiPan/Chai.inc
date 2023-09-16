# Generated by Django 4.2.5 on 2023-09-16 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='availability',
            field=models.CharField(choices=[('MO-AM', 'Monday AM'), ('MO-PM', 'Monday PM'), ('TU-AM', 'Tuesday AM'), ('TU-PM', 'Tuesday PM')], default='MO-AM', max_length=5),
        ),
    ]
