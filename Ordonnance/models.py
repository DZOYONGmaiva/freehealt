from django.db import models

from RendezVous.models import RendezVous
from Medecin.models import Medecin
from Patient.models import Patient

# Create your models here.
class Ordonnance(models.Model):
    idOrdonnance = models.AutoField(primary_key=True)
    idRenvezvousOr = models.ForeignKey(RendezVous, on_delete = models.PROTECT)

