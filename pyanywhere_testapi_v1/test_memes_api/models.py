import datetime
from django.db import models
from django.contrib.auth.models import User
class fake_accounts(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    creationDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    accountEmail = models.EmailField()
    fake_ccNumber = models.IntegerField(blank=True)
    fake_ccIssuer = models.CharField(max_length=64)
    fake_currencyName = models.CharField(max_length=128)
    fake_currencyCode = models.CharField(max_length=10)
    def __str__(self):
        return "%s (%s %s)" % (self.id, self.firstName, self.lastName)