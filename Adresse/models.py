from django.db import models

# Create your models here.

class Adresse(models.Model):
    idAdresse = models.AutoField(primary_key=True)
    nomPays = models.CharField(max_length=15, null=False)
    nomVille = models.CharField(max_length=15, null=False)
    nomQuartier = models.CharField(max_length=15, null=False)
    Indication = models.CharField(max_length=15, null=False)
