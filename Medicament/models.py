from django.db import models

# Create your models here.
class Medicament(models.Model):
    idMedicament = models.AutoField(primary_key=True)
    nomMedicament = models.CharField(max_length=15,null = False, blank=False)
    quantiteEnStock = models.IntegerField();
    prixMedicament = models.FloatField();
    descriptionMedicament = models.TextField()