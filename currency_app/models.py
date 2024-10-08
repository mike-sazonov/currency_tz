from django.db import models

# Create your models here.
class CurrencyModel(models.Model):
    valute = models.CharField(default='USD-RUB', max_length=50)
    value = models.FloatField()
    create = models.DateTimeField(auto_now=True)