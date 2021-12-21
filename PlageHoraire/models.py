from django.db import models
from Jour.models import Jour

# Create your models here.

class PlageHoraire(models.Model):
    idPlageHoraire = models.AutoField(primary_key=True)
    idDatejour = models.ForeignKey(Jour, on_delete = models.PROTECT)