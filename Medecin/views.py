from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Medecin/pageAcceuilMedecin.html')


def modifierCompte(request):
    return render(request, 'Medecin/modifierCompteMedecin.html')

def rendezVousAnnuler(request):
    return render(request, 'Medecin/rendezVousAnnulerMedecin.html')

