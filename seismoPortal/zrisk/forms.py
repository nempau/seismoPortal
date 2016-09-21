from django import forms
from .models import Zgrada, Korisnik
from django.views.generic import UpdateView
from django.contrib.gis import forms

'''from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)'''

class RegistracijaForma(forms.ModelForm):
	
	class Meta:
		model=Korisnik
		fields = ( 'ime', 'prezime', 'email', 'telefon','grad', 'opstina','adresa' )

		#primer valiacije
	'''def celan_email(self):
		email= self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		if not "edu" in email:
			raise forms.ValidationError("Molimo unesite ispravan email.")
		print(self.cleaned_data)
		return email'''





class EditForma(forms.ModelForm):

    class Meta:
        model = Zgrada
        widgets = {
            'geom': forms.Textarea(attrs={'cols': 40, 'rows': 10 } )
        }
        #geom = forms.PolygonField(widget=
        #forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))
        fields = ( 'naziv', 'brstanara', 'krivapovr', 'krivljudi','zgradeID', 'geom',)




