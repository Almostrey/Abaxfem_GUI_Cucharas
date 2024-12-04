import os 
import pandas as pd
import re
import numpy as np
from dataManager import getColadasRiesgos, getColadasRiesgosAC

def NO_VALOR(Zona,path,coladas,Riesgo,pregunta1,CLE):
    #print(f"Riesgo{Riesgo}")
    start = path.find(r"Historial/CUCHARA_") + len(r'Historial/CUCHARA_')
    end = len(path)
    path_aux=path[start:end]
    
    coladas_last=coladas[-1]
    
    start = 0
    end = path_aux.find(r"/CUCHARA")
    nameCuchara=path_aux[start:end]
    
    start=path.find(r'_CAMPANA_')+len(r'_CAMPANA_')
    end=len(path)-1
    nameCampana=path[start:end]
    
    
    
    
    
    # print(coladas)
    [coladas, FSup, FMed, FInf, TSup, TMed, TInf] = getColadasRiesgos(f"{nameCuchara}", f"{nameCampana}")
    [RiesgoCaraA, RiesgoCaraC] = getColadasRiesgosAC(nameCuchara, nameCampana)
    RiesgoPond=0.0
    Sumcoladas=0.0
    
    if   Zona=="HistoriaInfF":
        RiesgosPasados=FInf
        pregunta1=2
    elif Zona=="HistoriaSupF":
        RiesgosPasados=FSup
    elif Zona=="HistoriaMedF":
        RiesgosPasados=FMed
        pregunta1=2
    elif   Zona=="HistoriaInfT":
        RiesgosPasados=TInf
        pregunta1=2
    elif Zona=="HistoriaSupT":
        RiesgosPasados=TSup
    elif Zona=="HistoriaMedT":
        RiesgosPasados=TMed
        pregunta1=2
    elif Zona=="HistoriaCaraA":
        RiesgosPasados=RiesgoCaraA
        pregunta1=2
    elif Zona=="HistoriaCaraC":
        RiesgosPasados=RiesgoCaraC
        pregunta1=2
    
    index_del=[]
    for i in range(len(coladas)):
        if RiesgosPasados[i]!=0:
            index_del.append(i)
    RiesgosPasados=[RiesgosPasados[i] for i in index_del]
    coladas=[coladas[i] for i in index_del]
    
    
    tot_simulado=min(4,len(coladas))
            
        
    # print(f"Riesgos pasados{RiesgosPasados}")
    # print(f"Coladas {coladas}")
    if pregunta1==2:    
        if (len(coladas)!=0 and Riesgo==0):
            for i in range (tot_simulado):
                RiesgoPond=RiesgosPasados[-i]*coladas[-i]+RiesgoPond
                Sumcoladas=Sumcoladas+coladas[-i]
            taza_Riesgo=(RiesgoPond/Sumcoladas)/coladas[-1]
            Riesgo=taza_Riesgo*coladas_last
        elif (len(coladas)!=0 and Riesgo<RiesgosPasados[-1] and Riesgo!=0):
            for i in range (tot_simulado):
                RiesgoPond=RiesgosPasados[-i]*coladas[-i]+RiesgoPond
                Sumcoladas=Sumcoladas+coladas[-i]
            Riesgo=(RiesgoPond+Riesgo*coladas_last)/(Sumcoladas+coladas_last)
    
    elif pregunta1==1:
        if len(coladas)!=0:
            for g in range (len(coladas)):
                if coladas[-g-1]<CLE:
                    index=-g-1+1
                    if index!=0:
                        coladas=coladas[index:]
                        # print(f"Coladas Modif {coladas}")
                        RiesgosPasados=RiesgosPasados[index:]
                        # print(f"Riesgos pasados Modif {RiesgosPasados}")
                        
                    elif index==0:
                        coladas=[]
                        # print(coladas)
                        RiesgosPasados=[]
                        # print(RiesgosPasados)
                    tot_simulado=min(4,len(coladas))
                    break
                
        if (len(coladas)!=0 and Riesgo==0):
            # print("CASO1: (len(coladas)!=0 and Riesgo==0)")
            for i in range (tot_simulado):
                RiesgoPond=RiesgosPasados[-i]*coladas[-i]+RiesgoPond
                Sumcoladas=Sumcoladas+coladas[-i]
            taza_Riesgo=(RiesgoPond/Sumcoladas)/coladas[-1]
            Riesgo=taza_Riesgo*(coladas_last-CLE)
        elif (len(coladas)!=0 and Riesgo<RiesgosPasados[-1] and Riesgo!=0):
            # print ("CASO2: (len(coladas)!=0 and Riesgo<RiesgosPasados[-1] and Riesgo!=0)")
            for i in range (tot_simulado):
                RiesgoPond=RiesgosPasados[-i]*(coladas[-i]-CLE)+RiesgoPond
                Sumcoladas=Sumcoladas+(coladas[-i]-CLE)
            taza_Riesgo=((RiesgoPond+Riesgo*(coladas_last-CLE))/(Sumcoladas+coladas_last-CLE))/(coladas_last-CLE)
            Riesgo=taza_Riesgo*(coladas_last-CLE)
        
            
        
    return Riesgo
