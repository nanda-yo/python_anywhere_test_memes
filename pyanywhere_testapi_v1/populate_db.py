import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyanywhere_testapi.settings')

import django

django.setup()

import random
from test_memes_api.models import fake_accounts
from faker import Faker

faker = Faker()

def populate(i=20):
    for entry in range(i):
        firstName = faker.first_name()
        lastName = faker.last_name()
        accountEmail = faker.ascii_safe_email()
        fake_ccNumber = faker.credit_card_number()
        fake_ccIssuer = faker.credit_card_provider()
        fake_currencyName = faker.currency_name()
        fake_currencyCode = faker.currency_code()

        population = fake_accounts.objects.get_or_create(firstName=firstName,
                                                         lastName=lastName,
                                                         accountEmail=accountEmail,
                                                         fake_ccNumber=fake_ccNumber,
                                                         fake_ccIssuer=fake_ccIssuer,
                                                         fake_currencyName=fake_currencyName,
                                                         fake_currencyCode=fake_currencyCode)[0]




if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")