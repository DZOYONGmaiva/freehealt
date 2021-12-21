from django.db import models

# Create your models here.
class ServiceHopital(models.Model):
    idServiceHopital = models.AutoField(primary_key=True)
    descriptionDuService = models.CharField(max_length=20, null=False, blank=False)
