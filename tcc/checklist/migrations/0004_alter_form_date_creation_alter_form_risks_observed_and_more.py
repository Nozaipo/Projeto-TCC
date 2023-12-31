# Generated by Django 4.2.6 on 2023-10-14 22:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0003_form_alter_risk_date_creation_delete_forms_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='date_creation',
            field=models.DateField(default=datetime.datetime(2023, 10, 14, 22, 45, 4, 75201, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='form',
            name='risks_observed',
            field=models.ManyToManyField(related_name='risks_observed', to='checklist.risk'),
        ),
        migrations.AlterField(
            model_name='risk',
            name='date_creation',
            field=models.DateField(default=datetime.datetime(2023, 10, 14, 22, 45, 4, 75201, tzinfo=datetime.timezone.utc)),
        ),
    ]
