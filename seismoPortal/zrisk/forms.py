from django import forms
from .models import Zgrada
from django.views.generic import UpdateView
from django.contrib.gis import forms

class EditForma(forms.ModelForm):

    class Meta:
        model = Zgrada
        widgets = {
            'geom': forms.Textarea(attrs={'cols': 40, 'rows': 10 } )
        }
        #geom = forms.PolygonField(widget=
        #forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))
        fields = ( 'naziv', 'brstanara', 'krivapovr', 'krivljudi','zgradeID', 'geom',)



