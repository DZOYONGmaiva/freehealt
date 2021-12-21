from django.db import models

# Create your models here.

class Jour(models.Model):
    idJour = models.AutoField(primary_key=True)
    dateJour = models.DateField()
