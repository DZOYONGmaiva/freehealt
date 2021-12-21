from django.shortcuts import render,redirect

# Create your views here.
from Adresse.FormulaireInscriptionAdresse import FormulaireInscriptionAdresse


def inscriptionAdresse(request):
    formulaireInscriptionAdresse = FormulaireInscriptionAdresse()
    if request.method=='POST':
        formulaireInscriptionAdresse = FormulaireInscriptionAdresse(request.POST)
        if formulaireInscriptionAdresse.is_valid():
            formulaireInscriptionAdresse.save()
            return redirect('../')
    contextAdresse = {"cleInscriptionAdresse":formulaireInscriptionAdresse}
    return render(request, 'Patient/inscription.html', contextAdresse)