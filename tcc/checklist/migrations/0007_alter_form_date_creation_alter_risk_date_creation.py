# Generated by Django 4.2.5 on 2023-10-17 23:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0006_alter_form_date_creation_alter_risk_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='risk',
            name='date_creation',
            field=models.DateField(default=datetime.datetime(2023, 10, 17, 23, 2, 22, 58315, tzinfo=datetime.timezone.utc)),
        ),
    ]