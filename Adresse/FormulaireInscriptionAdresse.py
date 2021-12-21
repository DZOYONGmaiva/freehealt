from Adresse.FormulaireAdresse import FormulaireAdresse
from Adresse.models import Adresse
from  django.forms import ModelForm
class FormulaireInscriptionAdresse(ModelForm):
    class Meta:
        model = Adresse
        fields ='__all__' #['nomPays', 'nomVille','nomQuartier','Indication']