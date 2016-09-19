from django.contrib.gis import admin
from .models import Hazard, Zgrada, Kriva
from leaflet.admin import LeafletGeoAdmin
from leaflet.admin import LeafletGeoAdminMixin


from django.contrib import admin



admin.site.register(Zgrada, LeafletGeoAdmin)
admin.site.register(Hazard, LeafletGeoAdmin)
admin.site.register(Kriva)
# Register your models here.
