# Import modula LayerMapping
from django.contrib.gis.utils import LayerMapping
# Import definisanog modela
from .models import Hazard, Zgrade

# Rečnik korespodentnih polja
# Ključ naziv poja u bazi
# Vrednost polje u .shp fajlu

hazard_mapping = {
    'lower' : 'Lower',
    'upper' : 'Upper',
    'pga' : 'PGA',
    'geom' : 'MULTIPOLYGON',
}

zgrade_mapping = {
    'building' : 'BUILDING',
    'type' : 'TYPE',
    'structure' : 'STRUCTURE',
    'wall_type' : 'WALL_TYPE',
    'roof_type' : 'ROOF_TYPE',
    'levels' : 'LEVELS',
    'admin' : 'ADMIN',
    'roof_acces' : 'ROOF_ACCES',
    'capacity' : 'CAPACITY',
    'religion' : 'RELIGION',
    'osm_type' : 'OSM_TYPE',
    'full_addre' : 'FULL_ADDRE',
    'house_no' : 'HOUSE_NO',
    'street' : 'STREET',
    'name' : 'NAME',
    'amenity' : 'AMENITY',
    'leisure' : 'LEISURE',
    'use' : 'USE',
    'office' : 'OFFICE',
    'brstanara' : 'br.stanara',
    'krivapovr' : 'krivapovr',
    'krivljudi' : 'krivljudi',
    'ostecenje' : 'ostecenje',
    'ljudi' : 'ljudi',
    'pga' : 'PGA',
    'geom' : 'POLYGON',
}

#apsolutna putanja do podataka
hazard_shp = '/home/nemanja/Fakultet/masterRad/seismoPortal/data/475hazard.shp'
zgrade_shp = '/home/nemanja/Fakultet/masterRad/seismoPortal/data/zgrade.shp'


#metod za prepisivaje podataka u bazu
def run1(verbose=True):

	lm_hazard = LayerMapping(
    	Hazard, hazard_shp , hazard_mapping,
    	transform=False, encoding='iso-8859-5',
	)
	lm_hazard.save(strict=True, verbose=verbose)



	lm_zgrade = LayerMapping(
    	Zgrade, zgrade_shp, zgrade_mapping,
    	transform=False,
    	encoding='iso-8859-5',
    )
	lm_zgrade.save(strict=True, verbose=verbose)