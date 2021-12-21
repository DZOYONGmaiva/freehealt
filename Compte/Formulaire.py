from django import forms


class Formulaire(forms.Form):
    nom = forms.CharField(max_length=20, help_text="Nom")
    prenom = forms.CharField(max_length=20, help_text="Prenom")
    date = forms.DateField( help_text="date de naissance")
    lieu = forms.CharField(max_length=20, help_text="Lieu de naissance")
    sexe = forms.CharField(max_length=10, help_text="Sexe")
    email = forms.EmailField(help_text="Email")
    telephone = forms.IntegerField(help_text="Telephone")
    password1 = forms.CharField(widget=forms.PasswordInput(), help_text="Mot de passe")
    password2 = forms.CharField(widget=forms.PasswordInput(), help_text="Reécrire le mot de passe")
    pays = forms.CharField(max_length=15, help_text="Pays")
    Ville = forms.CharField(max_length=15, help_text="Ville")
    quartier = forms.CharField(max_length=15, help_text="Quartier")
    indication = forms.CharField(max_length=15, help_text="Indication sur quartier")


