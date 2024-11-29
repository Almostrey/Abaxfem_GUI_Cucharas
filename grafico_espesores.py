import os 
import pandas as pd
import re
import numpy as np
from dataManager import getColadasRiesgos
import matplotlib.pyplot as plt
from os import getcwd

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
    #print("Remanentes", Remanentes)
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
    print("Remanentes Milimetros:", Remanentes)
    plt.legend(["Zona 1 Frontal", "Zona 2 Frontal","Zona 3 Frontal","Zona 1 Trasera","Zona 2 Trasera","Zona 3 Trasera"], loc="lower left",fontsize=7)
    
        
    plt.suptitle('Historial de Espesor Remanente')
    plt.xlabel('Número de Colada')
    plt.ylabel('Espesor Remanente [mm]')
    ax.set_xticks(np.arange(0, coladas[-1]+10, 10))
    ax.set_yticks(np.arange(0, 180, 10))
    ax.grid()
    plt.savefig("Historial/CUCHARA_"+f"{nameCuchara}"+"/CUCHARA_"+f"{nameCuchara}"+"_CAMPANA_"+f"{nameCampana}"+"/Historial_Espesores"+".png")  

    ##################################### Modificacion adicional (Grafico Tasas de desgaste) ######################################
    #print("Remanentes", Remanentes[0])
    print("*********************")
    [coladas, FSup, FMed, FInf, TSup, TMed, TInf] = getColadasRiesgos(f"{nameCuchara}", f"{nameCampana}")
    coladas.insert(0,0)
    Remanentes=[FSup,FMed,FInf,TSup,TMed,TInf]
    print("Remanentes", Remanentes)
    for i in range(len(Remanentes)):
        Remanentes[i].insert(0,0)
    plt.figure()
    
    for i in range(len(Remanentes)):
        m = [0]
        print("Tasa ", i, end="")
        for j in range(len(Remanentes[i])-1):
            esp1 = 152 - ((Remanentes[i][j]*(152-50)/100))
            esp2 = 152 - ((Remanentes[i][j+1]*(152-50)/100))
            m.append((esp2-esp1) / (coladas[j]-coladas[j+1]))
        print(m)
        plt.plot(coladas,m, color=colors[i],linewidth=0.5, marker="D",ms=2)
    plt.grid()
    plt.xlabel('Número de Colada')
    plt.legend(["Zona 1 Frontal", "Zona 2 Frontal","Zona 3 Frontal","Zona 1 Trasera","Zona 2 Trasera","Zona 3 Trasera"], loc="lower left",fontsize=7)
    plt.ylabel('TasaDesgaste')
    plt.title("Tasa de Desgaste Utilizadas")
    plt.savefig("Historial/CUCHARA_"+f"{nameCuchara}"+"/CUCHARA_"+f"{nameCuchara}"+"_CAMPANA_"+f"{nameCampana}"+"/Historial_Tasa_Desgaste"+".png")  
    
    
    
if __name__=="__main__":
    grafico_espesores("Z:/23-003-01 CalculoTermicoCucharas/FaseIV/Informacion Procesada/Programa/Codigo Fuente/Historial/CUCHARA_9/CUCHARA_9_CAMPANA_1/")
    
    
    
    
    
    
    
    
    
    
    
    
    