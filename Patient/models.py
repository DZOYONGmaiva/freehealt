from django.db import models

# Create your models here.
from Personne.models import Personne


class Patient(Personne):
    caracteristiquePatient = models.TextField()

    #blank veut dire que la validation du formulaire permet la saisie valeur vide
    # null veut dire que lors de l enregistrement dans la BD s'il n ya rien la valeur sera null
    #max_length peut aussi prendre la valeur none