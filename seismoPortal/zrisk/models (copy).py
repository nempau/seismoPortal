from django.contrib.gis.db import models

# Create your models here.
class Zgrade(models.Model):
    building = models.CharField(max_length=11)
    type = models.CharField(max_length=254)
    structure = models.CharField(max_length=32)
    wall_type = models.CharField(max_length=32)
    roof_type = models.CharField(max_length=32)
    levels = models.CharField(max_length=2)
    admin = models.CharField(max_length=32)
    roof_acces = models.CharField(max_length=32)
    capacity = models.CharField(max_length=32)
    religion = models.CharField(max_length=9)
    osm_type = models.CharField(max_length=32)
    full_addre = models.CharField(max_length=32)
    house_no = models.CharField(max_length=5)
    street = models.CharField(max_length=60)
    name = models.CharField(max_length=88)
    amenity = models.CharField(max_length=16)
    leisure = models.CharField(max_length=13)
    use = models.CharField(max_length=32)
    office = models.CharField(max_length=32)
    brstanara = models.IntegerField()
    krivapovr = models.CharField(max_length=10)
    krivljudi = models.CharField(max_length=10)
    ostecenje = models.FloatField()
    ljudi = models.FloatField()
    pga = models.FloatField()
    geom = models.PolygonField()

class Hazard(models.Model):
    lower = models.FloatField()
    upper = models.FloatField()
    pga = models.FloatField()
    geom = models.MultiPolygonField()





