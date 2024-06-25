import os 
import pandas as pd
import re
import numpy as np
from dataManager import getColadasRiesgos
import matplotlib.pyplot as plt

def grafico_espesores(path):
    
    # path=r"/Historial/CUCHARA_1/CUCHARA_1_CAMPANA_1"
    start = path.find(r"Historial/CUCHARA_") + len(r"Historial/CUCHARA_")
    end = len(path)
    path_aux=path[start:end]
    
    start = 0
    end = path_aux.find(r"/CUCHARA")
    nameCuchara=path_aux[start:end]
    
    start=path.find(r"_CAMPANA_")+len(r"_CAMPANA_")
    end=len(path)-1
    nameCampana=path[start:end]
        
    # nameCampana=1
    # nameCuchara=1    
        
    [coladas, FSup, FMed, FInf, TSup, TMed, TInf] = getColadasRiesgos(f"{nameCuchara}", f"{nameCampana}")
    Remanentes=[FSup,FMed,FInf,TSup,TMed,TInf]
    colors = ['tab:pink', 'tab:blue', 'tab:green', 'tab:red', 'tab:purple', 
              'tab:brown']
    fig=plt.figure()
    ax = fig.gca()
    coladas.insert(0,0)
    for i in range (len(Remanentes)):
        if i==2 or i==5:    
            for j in range(len(coladas)-1):
                Remanentes[i][j]=172-(Remanentes[i][j]*(172-50)/100)
            Remanentes[i].insert(0,172.0)
        else:
            for j in range(len(coladas)-1):
                Remanentes[i][j]=152-(Remanentes[i][j]*(152-50)/100)
            Remanentes[i].insert(0,152.)
        
        plt.plot(coladas,Remanentes[i], color=colors[i],linewidth=0.5, marker="D",ms=2)
    
    plt.legend(["Zona 1 Frontal", "Zona 2 Frontal","Zona 3 Frontal","Zona 1 Trasera","Zona 2 Trasera","Zona 3 Trasera"], loc="lower left",fontsize=7)
    
        
    plt.suptitle('Historial de Espesor Remanente')
    plt.xlabel('Número de Colada')
    plt.ylabel('Espesor Remanente [mm]')
    ax.set_xticks(np.arange(0, coladas[-1]+10, 10))
    ax.set_yticks(np.arange(0, 180, 10))
    ax.grid()
    plt.savefig("Historial/CUCHARA_"+f"{nameCuchara}"+"/CUCHARA_"+f"{nameCuchara}"+"_CAMPANA_"+f"{nameCampana}"+"/Historial_Espesores"+".png")  

    
    