from django import forms
from .models import Zgrada
from django.views.generic import UpdateView





class EditForma(forms.ModelForm):

    class Meta:
        model = Zgrada
        fields = ( 'naziv', 'brstanara', 'krivapovr', 'krivljudi','zgradeID' )


