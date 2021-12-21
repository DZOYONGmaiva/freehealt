from django.db import models

# Create your models here.
class GradeMedecin(models.Model):
    idGradeMedecin = models.AutoField(primary_key=True)
    nomDuGrade = models.CharField(max_length=20, null=False, blank=False)
    descriptionDuGrade = models.TextField(max_length=20, null=False, blank=False)
