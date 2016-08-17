from django import forms
from appli.models import Planets
class  PlanetForm(forms.ModelForm):
    class Meta:
        model = Planets 
        fields = ('__all__')  