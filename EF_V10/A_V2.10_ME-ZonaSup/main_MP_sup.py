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
from processEF_if_first_time import processEF_if_first_time
from processEF_if_not_first_time import processEF_if_not_first_time
from read_historia import read_historia
import time 
import os
import math
import main_MP_Inf
import main_MP_Med
#num_process=int(os.environ["OMP_NUM_THREADS"])
num_process=8
os.environ["OMP_NUM_THREADS"]="1"

def main (args):
    coladas, pregunta1, CLE,tasaDesgaste, t,pregunta2,Historia=args                                                                             
    if pregunta2==1:
       col, temp, tasaDesgaste,Historia=processEF_if_first_time(coladas, pregunta1, CLE,tasaDesgaste, t,Historia) 
    elif pregunta2==2:
       col, temp, tasaDesgaste,Historia=processEF_if_not_first_time(coladas, pregunta1, CLE,tasaDesgaste, t, Historia)
    
    return col, temp, tasaDesgaste,Historia
        
#__________________________________________________________________________________________________________________________________________________________       
def EF_sup(coladas_DADA_DIEGO, temp_medidas, pregunta2:bool, Historia, t):
#_Informacion inicial--------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    Riesgo = 0
    observacion = 0
    #t=read_times_estudi_de_vida()                                                                          #Lectura de tiempos de archivos de excel       
    coladas=np.shape(t)[0]                                                                                 #Esta variable se sebe confirmar con la dada por diego en su código                    
    #print(coladas)
    #coladas_DADA_DIEGO=np.shape(t)[0]
    #### ################################[Colada, TempMaxZonaSup] = temp_medidas
    #temp_medidas=read_temps_medidas()                                               #################### Esta matriz me la debe dar diego de las temepreaturas que se encuentren de cada imagen y el numero correspondiente de la colada de cada imagen
    #pregunta2=1                                                                                         #Pregunta 2 es 1 si es la primera vez que se analiza la colada y es 2 si ya existe una historia de la colada
    
    
    if coladas ==coladas_DADA_DIEGO and coladas==temp_medidas[-1,0]:
        if not(511.632<int (t[0,0]+t[0,1])<928.37) or not(any(73.05<int (t[:,2]+t[:,3]+t[:,4])<130.95)) or not(any(10.74<int (t[:,5])<19.26)) or not(any(170.544<int (t[:,6])<309.456)) :
            #print("Tiempos no son los estandar, ERROR en la aproximación del riesgo")
            observacion = 1
        
        if (t[-5,6]>=170.544 and all(t[-4:,6]<=0)) or all(t[-4:,6]==0):
            pregunta1=2                                                                     #################### Esta variable la debo pedir al programa de diego Hubo cambio de linea de escoria si 1 no 2    
            CLE=97                                                                        #################### Esta variable la debo pedir al codigo de diego 
            temp_obj=temp_medidas[-1,1]
            start_time = time.time()                                                                           #Inicio de cronometro para saber tiempo de procesamiento
            colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:purple', 
                      'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']     #Se crea matriz de colores
              
    
            if pregunta2==2:
                #Historia=read_historia() 
                col_general=np.zeros((coladas-np.shape(Historia)[0],1))
                temp_general=np.zeros((coladas-np.shape(Historia)[0],1))
                limite_superior_max=(Historia[-1,1] )/(coladas-len(Historia))
                limite_sup=min(1.5,limite_superior_max )
            
            elif pregunta2==1:
                Historia=None
                col_general=np.zeros((coladas,1))                                                                                                           #Se crea matriz de las columnas que se evaluan de tamano [coladas,1]
                temp_general=np.zeros((coladas,1))
                limite_superior_max=152./coladas
                limite_sup=min(1.5, limite_superior_max)
            
            nlineas=num_process                                                                                         #Numero de lineas qeu se van a dibujar
            limite_inf=0 
    
            tasaDesgaste,tasaDesgaste_M=Matriz_tasaDesgaste(nlineas, limite_sup,limite_inf)                    #Se llama  a la funcion para que se creen dos matrices identicas de las tasas de desgaste   
    
    #Aproximacion1---------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                              #Se crea matriz de las temperaturas de cada colada evaluada de tamano [coladas,1]            
            #Multiprocesos Aproximacion 1
            with multiprocessing.Pool (processes=nlineas) as pool:
                results = pool.map(main, [(coladas, pregunta1, CLE,tasaDesgaste_M[i], t,pregunta2,Historia) for i in range(nlineas)])        
            
                #Orden de las variables de los resultados de main
                col_results=0
                temp_results=1
                tasaDesgaste_results=2
                Historia_results=3
                
                
                for tD in range(nlineas):                                                                                                                  #Para i en el rango nlineas     
                    col=np.array(results[tD][col_results])
                    temp=np.array(results[tD][temp_results])                                                                                                                 
                    col_general=np.column_stack((col_general,col))                                                                                             #se guardan las variables col de cada proceso en una matriz general de col_general                          
                    temp_general=np.column_stack((temp_general,temp))                                                                                      #se guardan las variables temp de cada proceso en una matriz general temp_general              
                    #plt.plot(col, temp, color=colors[tD % len(colors)],linewidth=0.5)                                                                       #se grafica la temperatura del nodo externo en funcion de del numero de coladas para cada proceso i                                              
                col_general=np.delete(col_general,0,1)                                                                                                     #Se elimina la primera columna de col_general ya que esta se uso solo como referencia para poder hacer un stack              
                temp_general=np.delete(temp_general,0,1)
                       
                #if pregunta2==2:
                    #plt.plot(Historia[:,0]+1,Historia[:,-2],color="red",linewidth=0.5)
                    #for tD in range(nlineas):
                        #plt.plot([len(Historia),len(Historia)+1],[Historia[-1,-2],temp_general[0,tD]],color=colors[tD % len(colors)],linewidth=0.5)
                
                
    
                '''plt.xlabel('# de Colada')                                                                                                                  #Leyenda Eje x 
                plt.ylabel('Temperatura [ºC]')                                                                                                             #Leyenda eje Y      
                plt.title('Curvas desgaste (Aproximación 1)')
               
                
                plt.plot(temp_medidas[:,0], temp_medidas[:,1],  color='black',linewidth=0.5)                                                             #Se grafica recta horizontal de la temperatura objetivo en la colada evaluada                                                  
                
                plt.xticks(np.arange(1,int(math.ceil(coladas/10.)*10.+10),step=10))
                plt.yticks(np.arange(int(np.min(temp_general))-5,int(np.max(temp_general))+25,step=25))
                plt.grid()
                plt.show() '''                                                                                                                  
                
                #print (" %s seconds" % (time.time() - start_time))                                                                                         #Se imprime el tiempo de procesamiento     
    #Aproximacion 2-------------------------------------------------------------------------------------------------------------------------
                if limite_sup==limite_superior_max and temp_medidas[-1,1]>results[-1][temp_results][-1]:
                    #print("Error:No queda espesor")
                    Riesgo=100
                    
                else:
                    W,tasaDesgaste,tasaDesgaste_M,coladas=Aproximacion2(tasaDesgaste_M,col_general,temp_general,nlineas,temp_obj,coladas,limite_superior_max)                     #Se llama a la funcion para hacer una segunda aproximacion 
                    if W==0:                                                                                                                                  #Si la variable de apoyo W es 0 se repite el proceso seguido para la Aproximacion 1 
                        if pregunta2==2:
                            col_general2=np.zeros((coladas-len(Historia),1))
                            temp_general2=np.zeros((coladas-len(Historia),1))
                        elif pregunta2==1:
                            Historia=None
                            col_general2=np.zeros((coladas,1))                                                                                                           #Se crea matriz de las columnas que se evaluan de tamano [coladas,1]
                            temp_general2=np.zeros((coladas,1))    
                        
                        results2 = pool.map(main, [(coladas, pregunta1, CLE,tasaDesgaste[i], t,pregunta2,Historia) for i in range(nlineas)])        
                                                                              
                        for tD in range(nlineas):                                                                                                                  #Para i en el rango nlineas     
                            col2=np.array(results2[tD][col_results])
                            temp2=np.array(results2[tD][temp_results])                                                                                                                 
                            col_general2=np.column_stack((col_general2,col2))                                                                                             #se guardan las variables col de cada proceso en una matriz general de col_general                          
                            temp_general2=np.column_stack((temp_general2,temp2))                                                                                      #se guardan las variables temp de cada proceso en una matriz general temp_general              
                            #plt.plot(col2, temp2, color=colors[tD % len(colors)],linewidth=0.5)                                                                       #se grafica la temperatura del nodo externo en funcion de del numero de coladas para cada proceso i                                              
                        col_general2=np.delete(col_general2,0,1)                                                                                                     #Se elimina la primera columna de col_general ya que esta se uso solo como referencia para poder hacer un stack              
                        temp_general2=np.delete(temp_general2,0,1)                                                                                                   #Se elimina la primera columna de temp_general ya que esta se uso solo como referencia para poder hacer un stack                  
           
                        '''if pregunta2==2:
                            plt.plot(Historia[:,0]+1,Historia[:,-2],color="red",linewidth=0.5)
                            for tD in range(nlineas):
                                plt.plot([len(Historia),len(Historia)+1],[Historia[-1,-2],temp_general[0,tD]],color=colors[tD % len(colors)],linewidth=0.5)       
                        '''
    
    
                
                
    
                        '''plt.xlabel('# de Colada')                                                                                                                  #Leyenda Eje x 
                        plt.ylabel('Temperatura [ºC]')                                                                                                             #Leyenda eje Y      
                        plt.title('Curvas desgaste (Aproximación 2)')
                        plt.plot(temp_medidas[:,0], temp_medidas[:,1],  color='black',linewidth=0.5)                                                                    #Se grafica recta horizontal de la temperatura objetivo en la colada evaluada                                                  
                        
                        plt.xticks(np.arange(1,int(math.ceil(coladas/10.)*10.+10),step=10))
                        plt.yticks(np.arange(int(np.min(temp_general))-5,int(np.max(temp_general))+25,step=25))
                        plt.grid()
                        plt.show()    '''
                                                                                                                     
                
                        #print (" %s seconds" % (time.time() - start_time)) 
                        
                      
                        Tasa_Desgaste_encontrada,index_TD=determinacion_tasa_desgaste(tasaDesgaste_M,temp_general2,nlineas,temp_obj,coladas)                           #Despues de seguir el mismo proceso que la aproximacion 1 se llama a la funcion que busca cual es la tasa de desgaste encontrada                                                                   
                        Historia=np.array(results2[index_TD[0]][Historia_results])
                        #GUARDADO EN EXCEL; LO DEBE HACER DIEGO______________________________________________________________________________________________________________________________                
                        #path=r'S:\23-003-01 CalculoTermicoCucharas\FaseIII Validación\Información Procesada\Documentos\Simulacion_Prueba_En_Planta\Historia.xlsx'
                        #********************* Guardar HISTORIA**********
                        Historia_Excel=pd.DataFrame(Historia)
                        #print(Historia)
                        #Historia_Excel.to_excel(path,index=False,header=False)      
                        Riesgo=(152.-Historia[-1,1])*100/102
                        #print("riesgo:")
                        #print(Riesgo)
                        return [Historia, Riesgo, observacion]
    
                    elif W==1:                                                                                                                                #Si la variable de apoyo W es 1 se determina e imprime que la tasa de desgaste es negativa (Error)
                        #print ('Error: Tasa de Desgaste Negativa')
                        #print (" %s seconds" % (time.time() - start_time))                                                                                        #Se imprime el tiempo que tomo todo el proceso desde la aproximacion 1  
                        observacion = 2
                        return [Historia, Riesgo, observacion]
        else:
            #print("No se puede hacer la predicción de riesgo, existe una parada o cambio de turno en una de las últimas coladas")
            observacion = 3
            return [Historia, Riesgo, observacion]
    else:
        #print("Error: Matriz de temperaturas y tiempos inconsistente")  
        observacion = 4      
        return [Historia, Riesgo, observacion]
#os.environ["OMP_NUM_THREADS"]=f"{num_process}"

def returnObs(numObs:int):
    if numObs == 1:
        observacion = "Tiempos no son los estandar, ERROR en la aproximación del riesgo"
    elif numObs == 2:
        observacion = 'Error: Tasa de Desgaste Negativa'
    elif numObs == 3:
        observacion = "No se puede hacer la predicción de riesgo, existe una parada o cambio de turno en una de las últimas coladas"
    elif numObs == 4:
        observacion = "Error: Matriz de temperaturas y tiempos inconsistente"
    else:
        observacion = ""
    return observacion

def getRiesgo(cantColadas, coladas, tempZonasTodasF, tempZonasTodasT, Nuevo1Viejo2, HistoriaPreviaF, HistoriaPreviaT):
    HistoriaF = []
    HistoriaT = []
    RiesgoF = []
    RiesgoT = []
    observacionF = []
    observacionT = []
    Riesgo = 0
    t=read_times_estudi_de_vida()
    if Nuevo1Viejo2 == 1:
        # Frontal
        [Historia, Riesgo, numObs] = EF_sup(cantColadas, np.column_stack((coladas,tempZonasTodasF[0])), Nuevo1Viejo2, HistoriaPreviaF, t)
        HistoriaF.append(numpy2float(Historia))
        RiesgoF.append(Riesgo)
        observacionF.append(returnObs(numObs))
        [Historia, Riesgo, numObs] = main_MP_Med.EF_med(cantColadas, np.column_stack((coladas,tempZonasTodasF[1])), Nuevo1Viejo2, HistoriaPreviaF, t)
        HistoriaF.append(numpy2float(Historia))
        RiesgoF.append(Riesgo)
        observacionF.append(returnObs(numObs))
        [Historia, Riesgo, numObs] = main_MP_Inf.EF_inf(cantColadas, np.column_stack((coladas,tempZonasTodasF[2])), Nuevo1Viejo2, HistoriaPreviaF, t)
        HistoriaF.append(numpy2float(Historia))
        RiesgoF.append(Riesgo)
        observacionF.append(returnObs(numObs))
        #### Trasera
        [Historia, Riesgo, numObs] = EF_sup(cantColadas, np.column_stack((coladas,tempZonasTodasT[0])), Nuevo1Viejo2, HistoriaPreviaT, t)
        HistoriaT.append(numpy2float(Historia))
        RiesgoT.append(Riesgo)
        observacionT.append(returnObs(numObs))
        [Historia, Riesgo, numObs] = main_MP_Med.EF_med(cantColadas, np.column_stack((coladas,tempZonasTodasT[1])), Nuevo1Viejo2, HistoriaPreviaT, t)
        #HistoriaT.append(numpy2float(Historia))
        HistoriaT.append(Historia)
        RiesgoT.append(Riesgo)
        observacionT.append(returnObs(numObs))
        [Historia, Riesgo, numObs] = main_MP_Inf.EF_inf(cantColadas, np.column_stack((coladas,tempZonasTodasT[2])), Nuevo1Viejo2, HistoriaPreviaT, t)
        HistoriaT.append(Historia)
        RiesgoT.append(Riesgo)
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
        [Historia, Riesgo, numObs] = EF_sup(cantColadas, np.column_stack((coladas,tempZonaSupF)), Nuevo1Viejo2, HistoriaPreviaF[0], t)
        HistoriaF.append(numpy2float(Historia))
        RiesgoF.append(Riesgo)
        observacionF.append(returnObs(numObs))
        [Historia, Riesgo, numObs] = main_MP_Med.EF_med(cantColadas, np.column_stack((coladas,tempZonaMedF)), Nuevo1Viejo2, HistoriaPreviaF[1], t)
        HistoriaF.append(numpy2float(Historia))
        RiesgoF.append(Riesgo)
        observacionF.append(returnObs(numObs))
        [Historia, Riesgo, numObs] = main_MP_Inf.EF_inf(cantColadas, np.column_stack((coladas,tempZonaInfF)), Nuevo1Viejo2, HistoriaPreviaF[2], t)
        HistoriaF.append(numpy2float(Historia))
        RiesgoF.append(Riesgo)
        observacionF.append(returnObs(numObs))
        #### Trasera
        [Historia, Riesgo, numObs] = EF_sup(cantColadas, np.column_stack((coladas,tempZonaSupT)), Nuevo1Viejo2, HistoriaPreviaT[0], t)
        HistoriaT.append(numpy2float(Historia))
        RiesgoT.append(Riesgo)
        observacionT.append(returnObs(numObs))
        [Historia, Riesgo, numObs] = main_MP_Med.EF_med(cantColadas, np.column_stack((coladas,tempZonaMedT)), Nuevo1Viejo2, HistoriaPreviaT[1], t)
        HistoriaT.append(numpy2float(Historia))
        RiesgoT.append(Riesgo)
        observacionT.append(returnObs(numObs))
        [Historia, Riesgo, numObs] = main_MP_Inf.EF_inf(cantColadas, np.column_stack((coladas,tempZonaInfT)), Nuevo1Viejo2, HistoriaPreviaT[2], t)
        HistoriaT.append(numpy2float(Historia))
        RiesgoT.append(Riesgo)
        observacionT.append(returnObs(numObs))
    return [HistoriaF, HistoriaT, RiesgoF, RiesgoT, observacionF, observacionT]

def numpy2float(numnumpy):
    aux = []
    for i in numnumpy:
        for j in i:
            aux.append(float(j))
    return aux
    
if __name__ == "__main__":
    ######### colada 13
    Historia = 0
    Nuevo1Viejo2 = 1
    cantColadas = 13
    coladas = 13
    tempZonasTodasF = 	[309.6307134456634, 299.93680474662784, 288.4576970062256]
    TempZonasTodasT = [308.6515882320404, 298.32552148437503, 269.47895961952213]
    [HistoriaF, HistoriaT, RiesgoF, RiesgoT, observacionF, observacionT] = getRiesgo(cantColadas, coladas, tempZonasTodasF, TempZonasTodasT, Nuevo1Viejo2, 0, 0)
    print("Fin Unooo*****************************")
    print(HistoriaF)
    print(type(HistoriaF))
    print(len(HistoriaF))

    '''print(type(np.reshape(HistoriaF, [18, 13])))
    print(type(RiesgoF))
    print(type(observacionF))'''
    print("Fin Unooo*****************************")
    
    '''######### Colada 13 y 157
    Nuevo1Viejo2 = 2
    cantColadas = 157
    coladas = [13, 157]
    tempZonasTodasF = [[309.6307134456634, 299.93680474662784, 288.4576970062256], [341.280529586792, 337.98867680740364, 332.9791482925415]]
    TempZonasTodasT = [[308.6515882320404, 298.32552148437503, 269.47895961952213], [341.280529586792, 337.98867680740364, 332.9791482925415]]
    [HistoriaF, HistoriaT, RiesgoF, RiesgoT, observacionF, observacionT] = getRiesgo(cantColadas, coladas, tempZonasTodasF, TempZonasTodasT, Nuevo1Viejo2, HistoriaF, HistoriaT)
    print("Fin doooos#####################################")
    print(RiesgoF)
    print(RiesgoT)
    print(observacionF)
    print(observacionT)
    print(len(HistoriaF))
    print(len(HistoriaT))
    print("Fin doooos#####################################")
    ######### Colada 13 y 157 y 200
    Nuevo1Viejo2 = 2
    cantColadas = 200
    coladas = [13, 157, 200]
    tempZonasTodasF = [[309.6307134456634, 299.93680474662784, 288.4576970062256], [341.280529586792, 337.98867680740364, 332.9791482925415], [330.28267187500006, 335.6421003723144, 331.3871125183106]]
    TempZonasTodasT = [[308.6515882320404, 298.32552148437503, 269.47895961952213], [341.280529586792, 337.98867680740364, 332.9791482925415], [325.8370326423645, 319.9554247512817, 316.9370900421143]]
    [HistoriaF, HistoriaT, RiesgoF, RiesgoT, observacionF, observacionT] = getRiesgo(cantColadas, coladas, tempZonasTodasF, TempZonasTodasT, Nuevo1Viejo2, HistoriaF, HistoriaT)
    print("Fin Treeees#####################################")
    print(RiesgoF)
    print(RiesgoT)
    print(observacionF)
    print(observacionT)
    print(len(HistoriaF))
    print(len(HistoriaT))
    print("Fin Treeeees#####################################")'''






    '''######### Colada 13 y 200
    Nuevo1Viejo2 = 2
    cantColadas = 200
    coladas = [13, 200]
    tempZonasTodasF = [[309.6307134456634, 299.93680474662784, 288.4576970062256], [330.28267187500006, 335.6421003723144, 331.3871125183106]]
    TempZonasTodasT = [[308.6515882320404, 298.32552148437503, 269.47895961952213], [325.8370326423645, 319.9554247512817, 316.9370900421143]]
    [HistoriaF, HistoriaT, RiesgoF, RiesgoT, observacionF, observacionT] = getRiesgo(cantColadas, coladas, tempZonasTodasF, TempZonasTodasT, Nuevo1Viejo2, HistoriaF, HistoriaT)
    print("Fin doooos#####################################")
    print(RiesgoF)
    print(RiesgoT)
    print(observacionF)
    print(observacionT)
    print(len(HistoriaF))
    print(len(HistoriaT))
    print("Fin doooos#####################################")'''