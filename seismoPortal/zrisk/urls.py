from django.conf.urls import url
from . import views
from djgeojson.views import GeoJSONLayerView
from .models import Zgrada
#from djgeojson.views import TiledGeoJSONLayerView

urlpatterns = [
	url(r'^$', views.dajPocetnu, name='pocetna'),
	url(r'^zrisk$', views.dajZrisk, name='zrisk'),
	url(r'^gubitakLjudi$', views.dajGubitak, name='gubitak'),
	url(r'^ostecenje$', views.dajOstecenje, name='ostecenje'),
    url(r'^zgrade.geojson$', GeoJSONLayerView.as_view(model=Zgrada, properties=('brstanara','krivapovr','krivljudi','zgradeID', 'ljudi', 'ostecenje', 'naziv')), name='dajZgrade'),
    
    #url(r'^/create$', views.createForma, name='createForma'),
    #url(r'^zgrade.geojson$', views.dajZgrade, name='dajZgrade'),
    #url(r'^zgrade/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+).geojson$',
    #TiledGeoJSONLayerView.as_view(model=Zgrade), name='dajZgrade'),
]