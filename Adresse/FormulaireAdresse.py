from django import forms


class FormulaireAdresse(forms.Form):
    pays = forms.CharField(max_length=15, help_text="Pays")
    Ville = forms.CharField(max_length=15, help_text="Ville")
    quartier = forms.CharField(max_length=15, help_text="Quartier")
    indication = forms.CharField(max_length=15, help_text="Indication sur quartier")


