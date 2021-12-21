from django.db import models

# Create your models here.
from Personne.models import Personne
from Telephone.models import Telephone


class AvoirTelephone(models.Model):
    idProprietaireTelephone = models.ManyToManyField(Personne)
    idNumeroTelephone = models.ManyToManyField(Telephone)