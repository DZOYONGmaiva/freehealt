from django.db import models

# Create your models here.
from Adresse.models import Adresse


class Personne(models.Model):
    SEXE = [
        ('M','Masculin'),
        ('F', 'Feminin'),
    ]
    STATUT = [
        ('A','Actif'),
        ('I', 'Inactif'),
    ]

    idPersonne = models.AutoField(primary_key=True)
    nomPersonne = models.CharField(max_length=15, null=True)
    prenomPersonne= models.CharField(max_length=15, null=True)
    dateNaissancePersonne = models.DateField(null=False)
    lieuDeNaissancePersonne = models.CharField(max_length=20, null=True, blank=True)
    sexePersonne = models.CharField(max_length=1, choices=SEXE)
    emailPersonne = models.EmailField(null=True, blank=True)
    telephonePersonne = models.IntegerField(null=True, blank=True)
    motDePasse = models.CharField(max_length=15, null=False)
    statutPersonne =  models.CharField(max_length=1, choices=STATUT, default='A')
    AdressePersonne = models.ForeignKey(Adresse, on_delete=models.PROTECT)


