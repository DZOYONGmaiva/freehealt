
from django.contrib.auth.models import User
from Compte.Formulaire import Formulaire

class UserFormulaire(Formulaire):
    class meta:
        model = User
        fields = ['nom', 'prenom', 'date','lieu','email','telephone','password1','password2','pays','ville','quartier','indication' ]