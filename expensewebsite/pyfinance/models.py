from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
        ("Mercado", "Mercado"),
        ("Ifood", "Ifood"),
        ("Casa", "Casa"),
        ("Carro", "Carro")
    )

class Compras(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY)
    date = models.DateField()
    value = models.FloatField()

class Month(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    value_all = models.FloatField()
    payment_number = models.FloatField(null=True, default=0)