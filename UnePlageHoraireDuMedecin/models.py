from django.db import models

# Create your models here.
from Medecin.models import Medecin
from PlageHoraire.models import PlageHoraire


class UnePlageHoraireDuMedecin(models.Model):
    idUnePlageHoraireDuMedecin = models.AutoField(primary_key=True)
    idPlageHoraireTotal = models.ForeignKey(PlageHoraire, on_delete = models.PROTECT)
    idMedecinPH = models.ForeignKey(Medecin, on_delete=models.PROTECT)
    HeureDebut = models.TimeField();
    HeureFin = models.TimeField();
