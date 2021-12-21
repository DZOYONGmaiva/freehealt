from django.http import HttpResponse
from django.shortcuts import render, redirect

from Adresse.FormulaireInscriptionAdresse import FormulaireInscriptionAdresse
from Patient.FormulaireConnectionPatient import UserForm
from Patient.FormulaireInscriptionPatient import FormulaireInscriptionPatient
from Patient.models import Patient


def home(request):
    formulaireConnexion = UserForm(request.POST)
    context = {"cleConnexion":formulaireConnexion,}
    return render(request, 'Patient/home.html', context)


def pageprofil(request):
    return render(request, 'Patient/pageAnnulerRendezVousPatient.html')
def modifierAnnulerRendezVous(request):
    return render(request, 'Patient/pageAnnulerRendezVousPatient.html')

def prendreRendezVous(request):
    return render(request, 'Patient/pagePrendreRendezVousPatient.html')

def modifierCompte(request):
    return render(request, 'Patient/pageModifierComptePatient.html')

def inscription(request):
    formulaireInscription = FormulaireInscriptionPatient()
    formulaireInscriptionAdresse = FormulaireInscriptionAdresse()
    if request.method=='POST':
        formulaireInscription = FormulaireInscriptionPatient(request.POST)
        formulaireInscriptionAdresse = FormulaireInscriptionAdresse(request.POST)
        #if formulaireInscriptionAdresse.is_valid():
         #   formulaireInscriptionAdresse.save()
        if FormulaireInscriptionPatient.is_valid():
            FormulaireInscriptionPatient.save()
            #FormulaireInscriptionPatient
            return redirect('../')
    context2 = {"cleInscription":formulaireInscription}
    #contextAdresse = {"cleInscriptionAdresse":formulaireInscriptionAdresse}
    return render(request, 'Patient/inscription.html', context2)

def supprimerObjectCC(request,pk):
    formulairecc = Patient.objects.get(nomPersonne=pk)
    if request.method=='POST':
        formulairecc.delete()
        return redirect('../patient')
    contexts={'item': formulairecc}
    return render(request, 'Compte/supprimer_Object.html', contexts)

