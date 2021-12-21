from django.db import models

# Create your models here.

class Telephone(models.Model):

    idTelephone = models.AutoField(primary_key=True)
    numeroTelephone = models.BigIntegerField()
