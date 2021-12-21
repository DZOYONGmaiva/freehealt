from django.db import models

# Create your models here.
from Personne.models import Personne


class Pharmacien(Personne):
    numeroCNIPharmacien = models.IntegerField()