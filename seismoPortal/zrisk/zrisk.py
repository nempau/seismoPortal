import time, math
from .models import Hazard, Zgrada, Kriva


zgrade=Zgrada.objects.all()
hazardi=Hazard.objects.all()



dicPovredljivost={}
preskoci=True
for field in Kriva._meta.get_fields():
    f=field.name
    vrednosti=[]
    if preskoci is True:
        preskoci=False
        pass
    else:   
        for featureP in Kriva.objects.all():
            vrednost=featureP.__dict__[f]
            vrednosti+=[vrednost]
             #print vrednosti
        dicPovredljivost[f]=vrednosti

krivaP= []
krivaH= []
krivaAp= []
krivaAh= []

def pgaUzgrade():
    start_time = time.time()
    for zgr in zgrade :
        for haz in hazardi:
            if type(zgr.pga) is type(None):
                if zgr.geom.within(haz.geom) or zgr.geom.overlaps(haz.geom):
                    zgr.pga=haz.pga
                    #zgr.pga=9
                    Zgrada.save(zgr)
            else:
                break

    print("--- %s seconds ---" % (time.time() - start_time))

def pgaUzgrade1():
    start_time = time.time()
    for zgr in zgrade :
        for haz in hazardi:

            if zgr.geom.within(haz.geom) or zgr.geom.overlaps(haz.geom):
                zgr.pga=haz.pga
                #zgr.pga=9
                Zgrada.save(zgr)

    print("--- %s seconds ---" % (time.time() - start_time))        


def interpolacija():
	start_time = time.time()
	##--Pronalazenje PGA za krivu povredljivosti i krivu ostecenja--##

	for zgr in zgrade:
	    brojStanara=zgr.brstanara
	    keyP=zgr.krivapovr #test1
	    keyH=zgr.krivljudi

	    keyAp='a'+keyP[-1] #t1
	    keyAh='a'+keyH[-1]

	    #print (keyH)
	    #print ('a'+keyH[-1])

	    pga=zgr.pga

	    krivaP=dicPovredljivost[keyP] #t1
	    krivaH=dicPovredljivost[keyH]

	    krivaAp=dicPovredljivost[keyAp] #t1
	    krivaAh=dicPovredljivost[keyAh]

	    minIndex1h=None
	    minIndex2h=None
	    
	    minIndex1p=None
	    minIndex2p=None

	    if pga in krivaAh:
	        indexH=krivaAh.index(pga)
	        valueH=krivaH[indexH]
	        valueAh=krivaAh[indexH]

	        zgr.ljudi = math.ceil(valueH*brojStanara)
	        #zgr.ljudi = 999
	        #Zgrada.save(zgr)
	        
	    else:
	        #print 'nema'
	        minIndex1h=min(range(len(krivaAh)), key=lambda i: abs(krivaAh[i]-pga))
	        if pga>krivaAh[minIndex1h]:
	            minIndex2h=minIndex1h+1
	            
	            
	        else:
	            minIndex2h=minIndex1h
	            minIndex1h=minIndex2h-1


	        ##--Interpolacija##
	        
	        #princip slicnosti u pravouglom trouglu 
	        #odsecak hx nalazi se na stranici h
	        #odsecak ax nalazi se na stranici a
	        #iz slicnosti sledi
	        # a:ax=h:hx
	        # hx=ax*h/a
	        #ljudi=valueH1+px
	        
	        valueA2h=krivaAh[minIndex2h]
	        valueA1h=krivaAh[minIndex1h]
	        valueH2=krivaH[minIndex2h]
	        valueH1=krivaH[minIndex1h]
	        a=valueA2h-valueA1h
	        h=valueH2-valueH1
	        ax=pga-valueA1h
	        hx=ax*h/a
	        ljudi=valueH1+hx
	        
	        #print ljudi
	        zgr.ljudi = math.ceil(ljudi*brojStanara)
	        #zgr.ljudi = 111
	        #Zgrada.save(zgr)


	    if pga in krivaAp:
	        indexP=krivaAp.index(pga)
	        valueP=krivaP[indexP]
	        valueA=krivaAp[indexP]
	        
	        #zapis u polje
	        #zgr.ostecenje=98
	        zgr.ostecenje = math.ceil(valueP*100)
	        #Zgrada.save(zgr)
	    else:
	        
	        minIndex1p=min(range(len(krivaAp)), key=lambda i: abs(krivaAp[i]-pga))
	        
	        if pga>krivaAp[minIndex1p]:
	            minIndex2p=minIndex1p+1
	            
	            
	        else:
	            minIndex2p=minIndex1p
	            minIndex1p=minIndex2p-1
	            

	        
	        ##--Interpolacija##
	        
	        #princip slicnosti u pravouglom trouglu 
	        #odsecak px nalazi se na stranici p
	        #odsecak ax nalazi se na stranici a
	        #iz slicnosti sledi
	        # a:ax=p:px
	        # px=ax*p/a
	        #ostecenje=valueP1+px
	        
	        valueA2p=krivaAp[minIndex2p]
	        valueA1p=krivaAp[minIndex1p]
	        valueP2=krivaP[minIndex2p]
	        valueP1=krivaP[minIndex1p]
	        
	        a=valueA2p-valueA1p
	        p=valueP2-valueP1
	        ax=pga-valueA1p
	        px=ax*p/a
	        ostecenje=valueP1+px
	    
	        #zapis u polje
	        #zgr.ostecenje=2
	        zgr.ostecenje = math.ceil(ostecenje*100)
	        #feature['ostecenje'] = 1.1111111
	    Zgrada.save(zgr)
	print("--- %s seconds ---" % (time.time() - start_time))    