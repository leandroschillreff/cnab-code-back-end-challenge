from django.db import models


class FinancialTransaction(models.Model):
    type = models.CharField(max_length=1)
    date = models.DateField()
    value = models.FloatField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField()
    store_owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)
