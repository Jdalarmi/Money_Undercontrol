from django.db import models

CATEGORY = (
        ("Mercado", "Mercado"),
        ("Ifood", "Ifood"),
        ("Casa", "Casa"),
        ("Carro", "Carro")
    )

class Compras(models.Model):
    category = models.CharField(max_length=20, choices=CATEGORY)
    date = models.DateField()
    value = models.FloatField()

class Month(models.Model):
    month = models.CharField(max_length=20)
    value_all = models.FloatField()