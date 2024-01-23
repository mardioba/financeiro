import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "controle_financas.settings")

import django

django.setup()

from faker import Faker
from financas.models import Despesa, Receita
from decimal import Decimal
from random import randint

fake = Faker()

# Insira despesas aleatórias
for _ in range(10):
    Despesa.objects.create(
        descricao=fake.text(50),
        valor=Decimal(randint(1, 1000)),
        data=fake.date_between(start_date="-30d", end_date="today"),
    )

# Insira receitas aleatórias
for _ in range(10):
    Receita.objects.create(
        descricao=fake.text(50),
        valor=Decimal(randint(1, 1000)),
        data=fake.date_between(start_date="-30d", end_date="today"),
    )
