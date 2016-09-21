from django.shortcuts import render, get_object_or_404
from .models import Zgrada
from django.http import JsonResponse
from djgeojson.views import GeoJSONLayerView
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseRedirect
#
from .forms import EditForma


def dajPocetnu(request):
	return render(request, 'zrisk/pocetna.html',  {})

def dajGubitak(request):
	return render(request, 'zrisk/gubitak.html',  {})

def dajOstecenje(request):
	return render(request, 'zrisk/ostecenje.html',  {})	



def dajZrisk(request):
	return render(request, 'zrisk/index.html',  {})


def dajZrisk(request):
	form=None
	zgradeID=request.POST.get('zgradeID')
	if zgradeID==None:
		instance2=Zgrada.objects.first()
		form=EditForma(request.POST or None, instance=instance2)
		print (instance2)
	elif Zgrada.objects.filter(zgradeID= request.POST.get('zgradeID')).count()==1:
		instance=get_object_or_404(Zgrada, zgradeID=request.POST.get('zgradeID'))
		form=EditForma(request.POST or None, instance=instance)
	else:
		form= EditForma(request.POST or None)	
	if form.is_valid():
		
		instance=form.save(commit=False)
		instance.save()
	context = { 'form': form}
	return render(request, 'zrisk/index.html', context)
	



