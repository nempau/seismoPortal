# Import modula LayerMapping
from django.contrib.gis.utils import LayerMapping
# Import definisanog modela
from .models import Hazard, Zgrada, Kriva
import csv
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
def run(verbose=True):

	lm_hazard = LayerMapping(
    	Hazard, hazard_shp , hazard_mapping,
    	transform=False, encoding='iso-8859-5',
	)
	lm_hazard.save(strict=True, verbose=verbose)



	lm_zgrade = LayerMapping(
    	Zgrada, zgrade_shp, zgrade_mapping,
    	transform=False,
    	encoding='iso-8859-5',
    )
	lm_zgrade.save(strict=True, verbose=verbose)

def run2():
    csv_file = '/home/nemanja/Fakultet/masterRad/seismoPortal/data/povredljivost.csv'
    reader = csv.DictReader(open(csv_file, 'rt'), delimiter=",")
    i=0
    for line in reader:
        a1=  float(line.pop('a1'))
        p1=  float(line.pop('p1'))
        h1=  float(line.pop('h1'))
        a2=  float(line.pop('a2'))
        p2=  float(line.pop('p2'))
        h2=  float(line.pop('h2'))
        a3=  float(line.pop('a3'))
        p3=  float(line.pop('p3'))
        h3=  float(line.pop('h3'))
        a4=  float(line.pop('a4'))
        p4=  float(line.pop('p4'))
        h4=  float(line.pop('h4'))

        Kriva (a1=a1, a2=a2, a3=a3, a4=a4, p1=p1, p2=p2, p3=p3, p4=p4, h1=h1, h2=h2, h3=h3, h4=h4).save()
        i=i+1
        print(i)
    print ("Krive su uspešno prepisane u bazu.")  