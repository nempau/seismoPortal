from django.contrib import admin
from django.contrib.gis import admin as geoadmin
from .models import Hazard, Zgrada, Kriva, Korisnik
from leaflet.admin import LeafletGeoAdmin
from leaflet.admin import LeafletGeoAdminMixin

from .forms import RegistracijaForma


admin.site.register(Zgrada, LeafletGeoAdmin)
admin.site.register(Hazard, LeafletGeoAdmin)
admin.site.register(Kriva)

class KorisnikAdmin(admin.ModelAdmin):
	list_display=["email", "ime", "prezime", "telefon", "datumRegistracije"]
	form=RegistracijaForma
	'''class Meta:

		model=Korisnik'''

	
admin.site.register(Korisnik, KorisnikAdmin)

