import os, random, datetime
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE','projeto_tcc.settings')

import django
django.setup()

from checklist.models import *

django.setup()


fake = Faker()
start_date = datetime.date(year=2023, month=1, day=1)
end_date = datetime.date(year=2023, month=12, day=31)

who_applied_opt = ['Henrique Fernandes', 'Wallace Cavalcante', 'Diego Alves', 'Paulo Henrique']

for _ in range(25):
    form = Form(who_applied=random.choice(who_applied_opt), date_creation=fake.date_between(start_date=start_date, end_date=end_date))
    form.save()
    risks = Risk.objects.all().order_by('?')[:random.randint(1, Risk.objects.count())]
    form.risks_observed.add(*risks)