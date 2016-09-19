import time
from .models import Hazard, Zgrada, Kriva

start_time = time.time()
zgrade=Zgrada.objects.all()
hazardi=Hazard.objects.all()
krive=Kriva.objects.all()


krivaP= []
krivaH= []
krivaAp= []
krivaAh= []

def pgaUzgrade():
    
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
    
    for zgr in zgrade :
        for haz in hazardi:

            if zgr.geom.within(haz.geom) or zgr.geom.overlaps(haz.geom):
                zgr.pga=haz.pga
                #zgr.pga=9
                Zgrada.save(zgr)

    print("--- %s seconds ---" % (time.time() - start_time))        


def interpolacija():
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


	    krivaPlista=Kriva.objects.values_list(keyP)
	    global krivaP
	    for p in krivaPlista:
	    	krivaP+=[p[0]] #t1

	    krivaHlista=Kriva.objects.values_list(keyH)
	    global krivaH
	    for h in krivaHlista:
	        krivaH+=[h[0]]

	    krivaAplista=Kriva.objects.values_list(keyAp)
	    global krivaAp
	    for ap in krivaAplista:
	        krivaAp+=[ap[0]] #t1

	    krivaAhilsta=Kriva.objects.values_list(keyAh)
	    global krivaAh
	    for ah in krivaAhilsta:
	        krivaAh+=[ah[0]] #t1

	    minIndex1h=None
	    minIndex2h=None
	    
	    minIndex1p=None
	    minIndex2p=None

	    if pga in krivaAh:
	        indexH=krivaAh.index(pga)
	        valueH=krivaH[indexH]
	        valueAh=krivaAh[indexH]

	        zgr.ljudi = int(valueH*brojStanara)
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
	        zgr.ljudi = int(ljudi*brojStanara)
	        #zgr.ljudi = 111
	        #Zgrada.save(zgr)


	    if pga in krivaAp:
	        indexP=krivaAp.index(pga)
	        valueP=krivaP[indexP]
	        valueA=krivaAp[indexP]
	        
	        #zapis u polje
	        #zgr.ostecenje=98
	        zgr.ostecenje = valueP*100
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
	        zgr.ostecenje = ostecenje*100
	        #feature['ostecenje'] = 1.1111111
	    Zgrada.save(zgr)
	print("--- %s seconds ---" % (time.time() - start_time))    