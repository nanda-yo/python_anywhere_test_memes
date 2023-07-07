from rest_framework import serializers
from .models import fake_accounts

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = fake_accounts
        fields = ["firstName",
                  "lastName",
                  "creationDate",
                  "accountEmail",
                  "fake_ccNumber",
                  "fake_ccIssuer",
                  "fake_currencyName",
                  "fake_currencyCode"
                  ]
