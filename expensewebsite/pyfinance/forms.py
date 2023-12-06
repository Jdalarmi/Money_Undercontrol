from django import forms
from .models import Compras

class ComprasForm(forms.ModelForm):
    class Meta:
        model = Compras
        fields = "__all__"

        widgets = {
            'date':forms.DateInput(attrs={'type':'date'})
        }