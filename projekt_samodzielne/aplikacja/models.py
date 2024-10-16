from django.db import models

# Create your models here.
class klucz_obc1(models.Model):
    klucz = models.FloatField()
class model_1(models.Model):
    tekst = models.CharField(max_length=100)
    liczba = models.IntegerField()
    klucz_obc = models.ForeignKey('klucz_obc1',on_delete=models.CASCADE)