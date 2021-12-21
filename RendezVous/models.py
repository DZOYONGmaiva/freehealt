from django.db import models

# Create your models here.
from PlageHoraire.models import PlageHoraire
from Patient.models import Patient
from UnePlageHoraireDuMedecin.models import UnePlageHoraireDuMedecin


class RendezVous(models.Model):
    idRendezVous = models.CharField(max_length=8, null=True)
    idPatientRDV = models.ForeignKey(Patient, on_delete = models.PROTECT)
    dateReservation = models.DateField(auto_now_add=True, help_text='la date a laquelle la reservation est faite')
    idUnePlageHoraireDuMedecinRDV = models.ForeignKey(UnePlageHoraireDuMedecin, on_delete=models.CASCADE, null = False)
    heureFinRDV = models.TimeField(blank=True, null=True)
    idMedecin = models.ForeignKey(PlageHoraire, on_delete=models.PROTECT)
    status = models.CharField(max_length=1, null=False)

#CASCADE : si l'objet referencé est supprimé alors l'objet qui reference sera aussi supprimé
#PROTECT : empeche la suppression de l'objet referencé
#RESTRICT :empeche la suppression de l'objet referencé mais entrès compliqué


