# Generated by Django 4.2.6 on 2023-10-12 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0002_forms_observations_forms_risks_observed_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who_applied', models.CharField(max_length=100)),
                ('date_creation', models.DateField(default=datetime.datetime(2023, 10, 12, 17, 56, 25, 536188, tzinfo=datetime.timezone.utc))),
                ('observations', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='risk',
            name='date_creation',
            field=models.DateField(default=datetime.datetime(2023, 10, 12, 17, 56, 25, 536188, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='Forms',
        ),
        migrations.AddField(
            model_name='form',
            name='risks_observed',
            field=models.ManyToManyField(to='checklist.risk'),
        ),
    ]
