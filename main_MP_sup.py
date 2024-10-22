# Librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import multiprocessing
from read_times_estudi_de_vida import read_times_estudi_de_vida
from Matriz_tasaDesgaste import Matriz_tasaDesgaste
from Aproximacion2 import Aproximacion2
from determinacion_tasa_desgaste import determinacion_tasa_desgaste
from read_temps_medidas import read_temps_medidas
from processEF_if_first_time_Sup import processEF_if_first_time
from processEF_if_not_first_time_Sup import processEF_if_not_first_time
from read_historia import read_historia
from NO_VALOR import NO_VALOR
from dataManager import getColadasRiesgos
import time 
import os
import math
import main_MP_Inf
import main_MP_Med
#num_process=int(os.environ["OMP_NUM_THREADS"])
num_process=os.cpu_count()
#num_process=6
#print(num_process)
os.environ["OMP_NUM_THREADS"]="1"

def main (args):
    coladas, pregunta1, CLE,tasaDesgaste, t,pregunta2,Historia=args                                                                             
    if pregunta2==1:
        col, temp, tasaDesgaste,Historia,Historia2=processEF_if_first_time(coladas, pregunta1, CLE,tasaDesgaste, t,Historia) 
    elif pregunta2==2:
        col, temp, tasaDesgaste,Historia,Historia2=processEF_if_not_first_time(coladas, pregunta1, CLE,tasaDesgaste, t, Historia)
							   
    
    return col, temp, tasaDesgaste,Historia,Historia2
        
#__________________________________________________________________________________________________________________________________________________________       
def EF_sup(coladas_DADA_DIEGO, temp_medidas, pregunta2:bool, path, t,pregunta1,CLE):
													   		  
#_Informacion inicial--------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    Riesgo = 0
    observacion = 0
    coladas_T=np.shape(t)[0]                                                                                 #Esta variable se sebe confirmar con la dada por diego en su código                    
    coladas=coladas_DADA_DIEGO
    end=path.find(".xlsx")
    seccion= path[end-1]
    

        
    if (coladas_T >= coladas and coladas<=temp_medidas[-1,0]) and (coladas-CLE)>=10:
        if not(511.632<int (t[0,0]+t[0,1])<928.37) or not(any(73.05<int (t[:,2]+t[:,3]+t[:,4])<130.95)) or not(any(10.74<int (t[:,5])<19.26)) or not(any(170.544<int (t[:,6])<309.456)) :
            print("Tiempos no son los estandar, ERROR en la aproximación del riesgo")
            observacion = 1
        
        #print("sup3.2")
        if all(t[-4:,6]<=999999999):
            temp_obj=temp_medidas[-1,1]
            start_time = time.time()                                                                           #Inicio de cronometro para saber tiempo de procesamiento
            colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:purple', 
                      'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']     #Se crea matriz de colores
              
    
            limite_sup=1.5
            if pregunta2==2:
                Historia=read_historia(path) 
                col_general=np.zeros((coladas-np.shape(Historia)[0],1))
                temp_general=np.zeros((coladas-np.shape(Historia)[0],1))
            
            elif pregunta2==1:
                Historia=None
                col_general=np.zeros((coladas,1))                                                                                                           #Se crea matriz de las columnas que se evaluan de tamano [coladas,1]
                temp_general=np.zeros((coladas,1))
            col_general2=np.copy(col_general)
            temp_general2=np.copy(temp_general)
            nlineas=num_process*2                                                                                        #Numero de lineas qeu se van a dibujar
            limite_inf=0 
    
            tasaDesgaste,tasaDesgaste_M=Matriz_tasaDesgaste(nlineas, limite_sup,limite_inf)                    #Se llama  a la funcion para que se creen dos matrices identicas de las tasas de desgaste   
            while tasaDesgaste_M [-1]*coladas>152:
                tasaDesgaste_M=np.delete(tasaDesgaste_M,-1,0)
#----------------------------------------------Seccion F------------------------------------------------------            
            if seccion=="F":
                if len (tasaDesgaste_M)==num_process*2:
                    nlineas=num_process
                    nlineas_2=num_process
                elif len (tasaDesgaste_M)<num_process*2 and len (tasaDesgaste_M)>num_process:
                    nlineas= math.ceil(len (tasaDesgaste_M)/2)
                    nlineas_2=len (tasaDesgaste_M)-nlineas
                elif len (tasaDesgaste_M)<=num_process :
                    nlineas=len (tasaDesgaste_M)
                    nlineas_2=None
                if pregunta2 ==2:
                    Historia_orig=np.copy(Historia)
                    Historia=Historia[:,:(len(tasaDesgaste_M)*19)]                    #19=NNod+3    
        #Aproximacion1---------------------------------------------------------------------------------------------------------------------------------------------------------
        #Orden de las variables de los resultados de main
                col_results=0
                temp_results=1
                tasaDesgaste_results=2
                Historia_results=3  
                Historia2_results=4
                if nlineas_2==None:
                    with multiprocessing.Pool (processes=nlineas) as pool:
                        results = pool.map(main, [(coladas, pregunta1, CLE,tasaDesgaste_M[i], t,pregunta2,Historia) for i in range(nlineas)])     
                               
                else:
                    with multiprocessing.Pool (processes=nlineas) as pool:
                        results = pool.map(main, [(coladas, pregunta1, CLE,tasaDesgaste_M[:nlineas][i], t,pregunta2,Historia) for i in range(nlineas)])       
                    with multiprocessing.Pool (processes=nlineas_2) as pool:
                        results2 = pool.map(main, [(coladas, pregunta1, CLE,tasaDesgaste_M[nlineas:][i], t,pregunta2,Historia) for i in range(nlineas_2)])        
                    
                for tD in range(nlineas):                                                                                                                  #Para i en el rango nlineas     
                    col=np.array(results[tD][col_results])
                    temp=np.array(results[tD][temp_results])                                                                                                                 
                    col_general=np.column_stack((col_general,col))                                                                                             #se guardan las variables col de cada proceso en una matriz general de col_general                          
                    temp_general=np.column_stack((temp_general,temp))                                                                                      #se guardan las variables temp de cada proceso en una matriz general temp_general              
                    # plt.plot(col, temp, color=colors[tD % len(colors)],linewidth=0.5)                                                                       #se grafica la temperatura del nodo externo en funcion de del numero de coladas para cada proceso i                                              
                col_general=np.delete(col_general,0,1)                                                                                                     #Se elimina la primera columna de col_general ya que esta se uso solo como referencia para poder hacer un stack              
                temp_general=np.delete(temp_general,0,1)
                
                if nlineas_2!=None:    
                    for tD in range(nlineas_2):                                                                                                                  #Para i en el rango nlineas     
                        col2=np.array(results2[tD][col_results])
                        temp2=np.array(results2[tD][temp_results])                                                                                                                 
                        col_general2=np.column_stack((col_general2,col2))                                                                                             #se guardan las variables col de cada proceso en una matriz general de col_general                          
                        temp_general2=np.column_stack((temp_general2,temp2))                                                                                      #se guardan las variables temp de cada proceso en una matriz general temp_general              
                        # plt.plot(col2, temp2, color=colors[tD % len(colors)],linewidth=0.5)                                                                       #se grafica la temperatura del nodo externo en funcion de del numero de coladas para cada proceso i                                              
                    col_general2=np.delete(col_general2,0,1)                                                                                                     #Se elimina la primera columna de col_general ya que esta se uso solo como referencia para poder hacer un stack              
                    temp_general2=np.delete(temp_general2,0,1)
                if pregunta2==2:
                    for tD in range(int(np.shape(Historia_orig)[1]/19)):
                        colH=Historia_orig[:,0]+1
                        tempH=Historia_orig[:,tD*19+17]                                                                                                               
                        # plt.plot(colH, tempH, color=colors[tD % len(colors)],linewidth=0.5)                                                                       #se grafica la temperatura del nodo externo en funcion de del numero de coladas para cada proceso i                                              
                   
                    
                # plt.xlabel('# de Colada')                                                                                                                  #Leyenda Eje x 
                # plt.ylabel('Temperatura [ºC]')                                                                                                             #Leyenda eje Y      
                # plt.title('Curvas desgaste (Aproximación 1)')
               
                
                # plt.plot(temp_medidas[:,0], temp_medidas[:,1],  color='black',linewidth=0.5)                                                             #Se grafica recta horizontal de la temperatura objetivo en la colada evaluada                                                  
                
                # plt.xticks(np.arange(1,int(math.ceil(coladas/10.)*10.+10),step=10))
                # plt.yticks(np.arange(int(np.min(temp_general))-5,int(np.max(temp_general))+25,step=25))
                # plt.grid()
                                                                                                                   
                
                # print (" %s seconds" % (time.time() - start_time))                                                                                         #Se imprime el tiempo de procesamiento     
                if nlineas_2!=None:
                    results.extend(results2) 
                    col_general=np.hstack((col_general,col_general2))
                    temp_general=np.hstack((temp_general,temp_general2))
                    del results2, col_general2, temp_general2                                                                                     #Se imprime el tiempo de procesamiento     
            
            
#--------------------------------------------Seccion T--------------------------------------            
            elif seccion=="T":


                path_seccion_frontal=path[:-6]+"F.xlsx"
                Seccion_Frontal_datos=read_historia(path_seccion_frontal)
                Seccion_Frontal_datos_orig=np.copy(Seccion_Frontal_datos)
                for i in range(int(np.shape(Seccion_Frontal_datos)[1])):
                    index=int(-i-1)
                    if Seccion_Frontal_datos[-1,index]!=0:
                        break
                if index+1!=0:
                    Seccion_Frontal_datos=Seccion_Frontal_datos[:,:index+1]
                num_lines=int((np.shape(Seccion_Frontal_datos)[1])/19)
                indexs_col=np.linspace(0,int(np.shape(Seccion_Frontal_datos)[1]-19),num_lines)
                indexs_col=indexs_col.astype(int)
                indexs_temp=indexs_col+17
                indexs_temp=indexs_temp.astype(int)
                
                if pregunta2==1:
                    col_general=Seccion_Frontal_datos[:,indexs_col]+1
                    temp_general=Seccion_Frontal_datos[:,indexs_temp]
                if pregunta2==2:
                    start = path.find(r"Historial/CUCHARA_") + len(r'Historial/CUCHARA_')
                    end = len(path)
                    path_aux=path[start:end]
                    start = 0
                    end = path_aux.find(r"/CUCHARA")
                    nameCuchara=path_aux[start:end]
                    start=path.find(r'_CAMPANA_')+len(r'_CAMPANA_')
                    end=len(path)-18
                    nameCampana=path[start:end]
                    [coladas_PASADAS, FSup, FMed, FInf, TSup, TMed, TInf] = getColadasRiesgos(f"{nameCuchara}", f"{nameCampana}")
                    col_general=Seccion_Frontal_datos[:,indexs_col]
                    temp_general=Seccion_Frontal_datos[:,indexs_temp]
                    
                
            # print("Punto de control 1")    
            W,T_desgaste=Aproximacion2(tasaDesgaste_M,col_general,temp_general,temp_obj)
            # print ("Punto de Control 2")
            if W==0 and pregunta1==2:
                if T_desgaste*coladas>=102:
                    # print("Error: Espesor crítico")
                    Riesgo=100
                else:
                    Riesgo=(T_desgaste*coladas)*100/102
        #AGREGADO ESTO-----------------------------------------------
            elif  W==0 and pregunta1==1:
                if T_desgaste*(coladas-CLE)>=102:
                    # print("Error: Espesor crítico")
                    Riesgo=100
                else:
                    Riesgo=(T_desgaste*(coladas-CLE))*100/102
        #---------------------------------------------------------
                    
            elif W==1:                                                                                                                                #Si la variable de apoyo W es 1 se determina e imprime que la tasa de desgaste es negativa (Error)
                #print ('Error: Tasa de Desgaste Negativa')
                # print (" %s seconds" % (time.time() - start_time))                                                                                        #Se imprime el tiempo que tomo todo el proceso desde la aproximacion 1  
                observacion = 2
                
            
            
            if pregunta2==1 and seccion =="F":
                Historia=np.zeros((coladas,1))
                for c in range (len(tasaDesgaste_M)):
                    Historia=np.hstack((Historia,(np.array(results[c][Historia_results]))))
                Historia=np.delete(Historia,0,1)
                
            elif pregunta2==2 and seccion=="F":
                Historia2=np.zeros((coladas-len(Historia),1))
                for c in range (len(tasaDesgaste_M)):
                    Historia2=np.hstack((Historia2,(np.array(results[c][Historia2_results]))))
                Historia2=np.delete(Historia2,0,1)
                # for tD in range (int(np.shape(Historia2)[1]/19)):
                #     plt.plot(([Historia_orig[-1,0]+1],[Historia2[0,0]+1]),([Historia_orig[-1,tD*19+17]],[Historia2[0,tD*19+17]]),color=colors[tD % len(colors)],linewidth=0.5)

                if np.shape(Historia_orig)[1]!=np.shape(Historia2)[1]:
                    Fill=np.zeros((len(Historia2),(np.shape(Historia_orig)[1]-np.shape(Historia2)[1])))
                    Historia2=np.hstack((Historia2,Fill))
                Historia=np.vstack((Historia_orig,Historia2))
                
                
            elif seccion=="T":
                Historia=np.copy(Seccion_Frontal_datos_orig)
                # GUARDADO EN EXCEL; LO DEBE HACER DIEGO______________________________________________________________________________________________________________________________                
                    
            Historia_Excel=pd.DataFrame(Historia)
            Historia_Excel.to_excel(path,index=False,header=False)   
            # print("Punto de Control 3")
            return [Riesgo, observacion]
            
            
        else:
            #print("No se puede hacer la predicción de riesgo, existe una parada o cambio de turno en una de las últimas coladas")
            observacion = 3
            return [Riesgo, observacion]
    else:
        #print("Error: Matriz de temperaturas y tiempos inconsistente o estimación de riesgo temprana")  
        observacion = 4      
        return [Riesgo, observacion]
os.environ["OMP_NUM_THREADS"]=f"{num_process}"







def returnObs(numObs:int):
    if numObs == 1:
        observacion = "Tiempos no son los estandar, ERROR en la aproximación del riesgo"
    elif numObs == 2:
        observacion = 'Error: Tasa de Desgaste Negativa'
    elif numObs == 3:
        observacion = "No se puede hacer la predicción de riesgo, existe una parada o cambio de turno en una de las últimas coladas"
    elif numObs == 4:
        observacion = "Error: Matriz de temperaturas y tiempos inconsistente o estimación de riesgo temprana"
    else:
        observacion = ""
    return observacion

def getRiesgo(cantColadas, coladas, tempZonasTodasF, tempZonasTodasT, Nuevo1Viejo2, path, CLE):
    if CLE == 0:
        pregunta1=2
    else:
        pregunta1=1
    RiesgoF = []
    RiesgoT = []
    observacionF = []
    observacionT = []
    numObservacionesF = []
    numObservacionesT = []
    Riesgo = 0
    t=read_times_estudi_de_vida()
    if Nuevo1Viejo2 == 1:
        # Frontal
        [Riesgo, numObs] = EF_sup(cantColadas, np.column_stack((coladas,tempZonasTodasF[0])), haveHistory(cantColadas, path+"HistoriaSupF.xlsx"), path+f"HistoriaSupF.xlsx", t,pregunta1,CLE)
        if Riesgo>100:
            Riesgo=100
         
        RiesgoF.append(Riesgo)
        numObservacionesF.append(numObs)
        observacionF.append(returnObs(numObs))
        print(np.column_stack((coladas,tempZonasTodasF[1])))
        [Riesgo, numObs] = main_MP_Med.EF_med(cantColadas, np.column_stack((coladas,tempZonasTodasF[1])), haveHistory(cantColadas, path+"HistoriaMedF.xlsx"), path+f"HistoriaMedF.xlsx", t, pregunta1, CLE)
        if Riesgo>100:
            Riesgo=100
         
        RiesgoF.append(Riesgo)
        numObservacionesF.append(numObs)
        observacionF.append(returnObs(numObs))
        [Riesgo, numObs] = main_MP_Inf.EF_inf(cantColadas, np.column_stack((coladas,tempZonasTodasF[2])), haveHistory(cantColadas, path+"HistoriaInfF.xlsx"), path+f"HistoriaInfF.xlsx", t, pregunta1, CLE)
        if Riesgo>100:
            Riesgo=100
         
        RiesgoF.append(Riesgo)
        numObservacionesF.append(numObs)
        observacionF.append(returnObs(numObs))
        #### Trasera
        [Riesgo, numObs] = EF_sup(cantColadas, np.column_stack((coladas,tempZonasTodasT[0])), haveHistory(cantColadas, path+"HistoriaSupT.xlsx"), path+f"HistoriaSupT.xlsx", t,pregunta1, CLE)
        if Riesgo>100:
            Riesgo=100
         
        RiesgoT.append(Riesgo)
        numObservacionesT.append(numObs)
        observacionT.append(returnObs(numObs))
        [Riesgo, numObs] = main_MP_Med.EF_med(cantColadas, np.column_stack((coladas,tempZonasTodasT[1])), haveHistory(cantColadas, path+"HistoriaMedT.xlsx"), path+f"HistoriaMedT.xlsx", t, pregunta1, CLE)
        if Riesgo>100:
            Riesgo=100
         
        RiesgoT.append(Riesgo)
        numObservacionesT.append(numObs)
        observacionT.append(returnObs(numObs))
        [Riesgo, numObs] = main_MP_Inf.EF_inf(cantColadas, np.column_stack((coladas,tempZonasTodasT[2])), haveHistory(cantColadas, path+"HistoriaInfT.xlsx"), path+f"HistoriaInfT.xlsx", t, pregunta1, CLE)
        if Riesgo>100:
            Riesgo=100
         
        RiesgoT.append(Riesgo)
        numObservacionesT.append(numObs)
        observacionT.append(returnObs(numObs))

    
    elif Nuevo1Viejo2 == 2:
        tempZonaSupF = []
        tempZonaMedF = []
        tempZonaInfF = []
        tempZonaSupT = []
        tempZonaMedT = []
        tempZonaInfT = []
        for i in range (len(tempZonasTodasF)):
            tempZonaSupF.append(tempZonasTodasF[i][0])
            tempZonaMedF.append(tempZonasTodasF[i][1])
            tempZonaInfF.append(tempZonasTodasF[i][2])
            tempZonaSupT.append(tempZonasTodasT[i][0])
            tempZonaMedT.append(tempZonasTodasT[i][1])
            tempZonaInfT.append(tempZonasTodasT[i][2])
        # Frontal
        coladasVerdaderas = HistoriaPrevia(coladas, path+"HistoriaSupF.xlsx")
        tempZonaSupF = fixTempZonas(coladasVerdaderas, tempZonaSupF)
        [Riesgo, numObs] = EF_sup(cantColadas, np.column_stack((coladasVerdaderas,tempZonaSupF)), haveHistory(coladasVerdaderas[-2], path+"HistoriaSupF.xlsx"), path+"HistoriaSupF.xlsx", t,pregunta1,CLE)
        Riesgo=NO_VALOR("HistoriaSupF",path,coladas,Riesgo,pregunta1,CLE)
        RiesgoF.append(Riesgo)
        numObservacionesF.append(numObs)
        observacionF.append(returnObs(numObs))
        
        
        coladasVerdaderas = HistoriaPrevia(coladas, path+"HistoriaMedF.xlsx")
        tempZonaMedF = fixTempZonas(coladasVerdaderas, tempZonaMedF)
        [Riesgo, numObs] = main_MP_Med.EF_med(cantColadas, np.column_stack((coladasVerdaderas,tempZonaMedF)), haveHistory(coladasVerdaderas[-2], path+"HistoriaMedF.xlsx"), path+"HistoriaMedF.xlsx", t,pregunta1,CLE)
        Riesgo=NO_VALOR("HistoriaMedF",path,coladas,Riesgo,pregunta1,CLE)
        if Riesgo>100:
            Riesgo=100
        RiesgoF.append(Riesgo)
        numObservacionesF.append(numObs)
        observacionF.append(returnObs(numObs))
        
        
        coladasVerdaderas = HistoriaPrevia(coladas, path+"HistoriaInfF.xlsx")
        tempZonaInfF = fixTempZonas(coladasVerdaderas, tempZonaInfF)
        [Riesgo, numObs] = main_MP_Inf.EF_inf(cantColadas, np.column_stack((coladasVerdaderas,tempZonaInfF)), haveHistory(coladasVerdaderas[-2], path+"HistoriaInfF.xlsx"), path+"HistoriaInfF.xlsx", t,pregunta1,CLE)
        Riesgo=NO_VALOR("HistoriaInfF",path,coladas,Riesgo,pregunta1,CLE)
        if Riesgo>100:
            Riesgo=100
        RiesgoF.append(Riesgo)
        numObservacionesF.append(numObs)
        observacionF.append(returnObs(numObs))
        #### Trasera
        coladasVerdaderas = HistoriaPrevia(coladas, path+"HistoriaSupT.xlsx")
        tempZonaSupT = fixTempZonas(coladasVerdaderas, tempZonaSupT)
        [Riesgo, numObs] = EF_sup(cantColadas, np.column_stack((coladasVerdaderas,tempZonaSupT)), haveHistory(coladasVerdaderas[-2], path+"HistoriaSupT.xlsx"), path+"HistoriaSupT.xlsx", t,pregunta1,CLE)
        Riesgo=NO_VALOR("HistoriaSupT",path,coladas,Riesgo,pregunta1,CLE)
        if Riesgo>100:
            Riesgo=100
        RiesgoT.append(Riesgo)
        numObservacionesT.append(numObs)
        observacionT.append(returnObs(numObs))
        
        
        coladasVerdaderas = HistoriaPrevia(coladas, path+"HistoriaMedT.xlsx")
        tempZonaMedT = fixTempZonas(coladasVerdaderas, tempZonaMedT)
        [Riesgo, numObs] = main_MP_Med.EF_med(cantColadas, np.column_stack((coladasVerdaderas,tempZonaMedT)), haveHistory(coladasVerdaderas[-2], path+"HistoriaMedT.xlsx"), path+"HistoriaMedT.xlsx", t,pregunta1,CLE)
        Riesgo=NO_VALOR("HistoriaMedT",path,coladas,Riesgo,pregunta1,CLE)
        if Riesgo>100:
            Riesgo=100
        RiesgoT.append(Riesgo)
        numObservacionesT.append(numObs)
        observacionT.append(returnObs(numObs))
        
        
        coladasVerdaderas = HistoriaPrevia(coladas, path+"HistoriaInfT.xlsx")
        tempZonaInfT = fixTempZonas(coladasVerdaderas, tempZonaInfT)
        [Riesgo, numObs] = main_MP_Inf.EF_inf(cantColadas, np.column_stack((coladasVerdaderas,tempZonaInfT)), haveHistory(coladasVerdaderas[-2], path+"HistoriaInfT.xlsx"), path+"HistoriaInfT.xlsx", t,pregunta1,CLE)
        Riesgo=NO_VALOR("HistoriaInfT",path,coladas,Riesgo,pregunta1,CLE)
        if Riesgo>100:
            Riesgo=100
        RiesgoT.append(Riesgo)
        numObservacionesT.append(numObs)
        observacionT.append(returnObs(numObs))
    return [RiesgoF, RiesgoT, numObservacionesF, numObservacionesT]
    
def fixTempZonas(coladasVerdaderas:list, tempZona:list):
    if len(coladasVerdaderas) == len(tempZona):return tempZona
    else:
        lista = []
        for i in range(len(coladasVerdaderas)-1):
            lista.append(tempZona[i])
        lista.append(tempZona[-1])
        return lista

def HistoriaPrevia(coladas:list, path:str):
    try:
        coladasVerdaderas = []
        historia = read_historia(path)
        lastColada = historia[-1][0]+1
        for i in range (len(coladas)-1):
            coladasVerdaderas.append(coladas[i])
            if coladas[i]==lastColada:
                coladasVerdaderas.append(coladas[-1])
                break
        return coladasVerdaderas
    except:
        return [0, coladas[-1]]

def haveHistory(colada, path):
    try:
        Historia=pd.read_excel(path,header=None)
        Historia=Historia.to_numpy()
        if Historia[-1][0]+1 == colada: return 2
        else: return 1
    except:
        return 1

if __name__ == "__main__":
    path = "Historial/CUCHARA_1/CUCHARA_1_CAMPANA_11/HistoriaInfT.xlsx"
    coladasVerdaderas = HistoriaPrevia([46, 75], path)
    print(coladasVerdaderas)
