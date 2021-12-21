from django.shortcuts import render, redirect


# Create your views here.
from Compte.inscription import UserFormulaire
from Patient.FormulaireConnectionPatient import UserForm
from Patient.models import Patient


def home(request):
    formulaire = UserForm(request.POST)
    context = {"cleFormulaire":formulaire,}
    return render(request, 'Compte/pageAcceuil.html', context)

def creerCompte(request):
    formulaireInscription = UserFormulaire()
    if request.method=='POST':
        formulaireInscription = UserFormulaire(request.POST)
        if formulaireInscription.is_valid():
            formulaireInscription.save()
            return redirect('../')
    context2 = {"cle":formulaireInscription}
    return render(request, 'Compte/creerCompte.html', context2)


