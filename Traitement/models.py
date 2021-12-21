from django.db import models

# Create your models here.
from Ordonnance.models import Ordonnance


class Traitement(models.Model):
    idOrdonnanceTr = models.ForeignKey(Ordonnance, on_delete = models.PROTECT)
    descriptionDuTraitement = models.TextField()