from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Pharmacien/pageAcceuilPharmacien.html')

def modifierCompte(request):
    return render(request, 'Pharmacien/pageModifierComptePharmacien.html')

def gererMedicament(request):
    return render(request, 'Pharmacien/pageGererMedicamentPharmacien.html')