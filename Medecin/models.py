from django.db import models

# Create your models here.
from ServiceHopital.models import ServiceHopital
from GradeMedecin.models import GradeMedecin
from Personne.models import Personne


class Medecin(Personne):
    specialite= models.ForeignKey(ServiceHopital, on_delete=models.PROTECT)
    gradeMedecin= models.ForeignKey(GradeMedecin, on_delete=models.PROTECT)
    numeroCNI : models.IntegerField();
    #blank veut dire que la validation du formulaire permet la saisie valeur vide
    # null veut dire que lors de l enregistrement dans la BD s'il n ya rien la valeur sera null
    #max_length peut aussi prendre la valeur none