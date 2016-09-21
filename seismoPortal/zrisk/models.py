from django.contrib.gis.db import models



# Create your models here.
class Zgrada(models.Model):
   
    #zgradeID  = models.AutoField(primary_key=True)
    zgradeID = models.IntegerField(primary_key=True)
    naziv= models.CharField(max_length=200, default=None, blank=True, null=True)
    brstanara = models.IntegerField(default=None, blank=True, null=True)
    krivapovr = models.CharField(max_length=10, default=None, blank=True, null=True)
    krivljudi = models.CharField(max_length=10, default=None, blank=True, null=True)
    ostecenje = models.FloatField( default=None, blank=True, null=True)
    ljudi = models.FloatField( default=None, blank=True, null=True)
    pga = models.FloatField( default=None, blank=True, null=True)
    geom = models.PolygonField( default=None, blank=True, null=True)

    def __str__(self):
        return str(self.zgradeID)

class Hazard(models.Model):
    hazardID = models.AutoField(primary_key=True)
    lower = models.FloatField()
    upper = models.FloatField()
    pga = models.FloatField()
    geom = models.MultiPolygonField()
    def __str__(self):
        return str(self.hazardID)



class Kriva(models.Model):
    vID=  models.AutoField(primary_key=True)
    a1=  models.FloatField()
    p1=  models.FloatField()
    h1=  models.FloatField()
    a2=  models.FloatField()
    p2=  models.FloatField()
    h2=  models.FloatField()
    a3=  models.FloatField()
    p3=  models.FloatField()
    h3=  models.FloatField()
    a4=  models.FloatField()
    p4=  models.FloatField()
    h4=  models.FloatField()

    def __str__(self):
        return str(self.vID)

class Korisnik(models.Model):
    idKorisnika= models.AutoField(primary_key=True)
    ime= models.CharField(max_length=100)
    prezime=models.CharField(max_length=100)
    telefon=models.CharField(max_length=20)
    email=models.EmailField()
    grad= models.CharField(max_length=100)
    opstina= models.CharField(max_length=100)
    adresa=models.CharField(max_length=100)
    datumRegistracije=models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.email)

