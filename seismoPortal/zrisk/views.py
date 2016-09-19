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


# Create your views here.
def dajZriska(request):
#def createForma(request):
	form= EditForma(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		#return HttpResponseRedirect(instance.get_absolute_url())
	context = { 'form': form}
	return render(request, 'zrisk/index.html', context)

def dajZrisk(request ):
	form=None
	zgradeID=request.POST.get('zgradeID')
	if zgradeID==None:
		instance=Zgrada.objects.get(zgradeID=8780)
		form=EditForma(request.POST or None, instance=instance)
		print (instance)
	else:
		instance=get_object_or_404(Zgrada, zgradeID=request.POST.get('zgradeID'))
		form=EditForma(request.POST or None, instance=instance)
		print (instance)
	if form.is_valid():
		print (instance)
		instance=form.save(commit=False)
		instance.save()
		#return HttpResponseRedirect(instance.get_absolute_url())
	context = { 'form': form}
	return render(request, 'zrisk/index.html', context)
	#return render(request, 'zrisk/index.html')



