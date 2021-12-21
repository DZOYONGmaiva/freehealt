from Patient.Formulaire import Formulaire
from Patient.models import Patient
from  django.forms import ModelForm
class FormulaireInscriptionPatient(ModelForm):
    class Meta:
        model = Patient
        fields ='__all__'# ['nom', 'prenom', 'date','lieu','email','telephone','password1','password2' ]