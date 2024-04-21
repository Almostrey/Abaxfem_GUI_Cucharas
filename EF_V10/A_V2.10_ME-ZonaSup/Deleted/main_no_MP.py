# Librerias
import numpy as np
import matplotlib.pyplot as plt
from elementosFinitos import elementosFinitos
from temperaturas import temperaturas
from preguntas import preguntas 
from inicializadoTemperaturas import inicializadoTemperaturas
from propiedadesFisicas import propiedadesFisicas
from radiacion import radiacion
from matrizKGyCG import matrizKGyCG
from matrizRG import matrizRG
from evaluacion import evaluacion
# from multiprocessing import Process,Queue




def main (coladas, tCalentamiento, tCarga, tDescarga, pregunta1, CLE,tasaDesgaste):
    
    # global dt, calentado, carga, descarga, Long1, colada, coladas, tasaDesgaste, TInicial, TFinal, tempObjetivo, verif
    
    NElemTotal, NMateriales, NElemMaterial, NNod, N1, N2, N3, N4, N5, Conec=elementosFinitos ()                                                         # Definicion de parámetros del modelo de elementos finitos
    Tamb, Tacero, Tinterna, TinternaCarga=temperaturas ()                                                             # Definición global de valores de temperatura del modelo
    
    TInicial=inicializadoTemperaturas (NNod,Tamb)                                                 # Iniciado de temperaturas nodales en 20 C    
    
                                                                # Tasa de desgaste en mm/colada
    
    # colObjetivo = coladas
    # tempObjetivo = float(input ('Temperatura? '))
    
    # verif = 0
    # tempRef = 0
    # while tempObjetivo - tempRef > 1 or tempObjetivo - tempRef < -1: 
        
    k0 = 0
    TInicial=inicializadoTemperaturas (NNod,Tamb)                                                 # Iniciado de temperaturas nodales en 20 C    
    for colada in range (coladas):                                              # Bucle para iterar las coladas        
        if colada == 0:                                                                 # Inicializado de espesores solo en la primera colada
            Long1 = [152 , 15 , 108 , 10 , 40]                                          # Vector de espesores de materiales
            col = []                                                                                # Vector donde se almacenan las coladas
            temp = []                                                                               # Vector donde esta la temperatura del nodo externo al final de cada colada
        
        dt = 2                                                                  # Paso de tiempo
        
        k1 = 0
        if k1 == 1:
            if Long1 [0] < 60:                                                  # Actualizacion del paso de tiempo para convergencia del modelo de elementos finitos
                dt = 1                                                          # Nuevo paso de tiempo por cada iteración
                if Long1 [0] < 10:
                    dt = 0.1                                                    # Nuevo paso de tiempo por cada iteración
        k1 = 1
        
        #print ('\nColada:',colada+1)
        if pregunta1 == 1:
            if colada == CLE:
                TInicial = np.ones ((NNod , 1)) * Tamb
                TFinal = TInicial
                Long1 [0] = 152
                k0=0
        
        tiempo = int (tCalentamiento)                                           # Tiempo de calentado estandar, 10 minutos - 600 segundos
        
        if k0 == 0:
            tiempo = int(43200)                                                 # Tiempo de calentado inicial, 12 horas - 43200 segundos
            k0 = 1
            
        iteraciones = int (tiempo / dt)                                         # Iteraciones a realizar
        for iteracion in range (iteraciones):                                   # Bucle para iterar el calentamiento
            calentado = 1                                                       # Switch para escoger propiedades en funciones
            carga = descarga = 0                                                # Switch para escoger propiedades en funciones
            rho, Cp, hConvInt, hConvExt=propiedadesFisicas (colada,NNod,N1,TInicial,N2,N3,N4,N5,calentado,carga,descarga)                                               # Define los parámetros geométricos y propiedades físicas del modelo
            hRadInt, hRadExt=radiacion (TInicial,Tamb,calentado,carga,descarga,TinternaCarga,Tinterna)                                                     # Calcula el coeficiente de radiación térmico
            KG, CG, dx1, dx2, dx3, dx4, dx5=matrizKGyCG (Long1,NElemMaterial,NNod,NElemTotal,NMateriales,TInicial,Cp,rho,Conec,hConvExt,hRadExt,hConvInt,hRadInt,calentado,carga,descarga)                                                     # Cálculo de la matriz de conductividad y la de capacitancia
            RG= matrizRG (NNod,Tamb,hConvExt,hRadExt, calentado, carga, descarga, TinternaCarga,hConvInt,hRadInt,Tinterna)                                                     # Definición de matriz de cargas globales
            TFinal, TInicial=evaluacion (CG,KG,dt,TInicial,RG,carga, Tacero)                                                       # Evaluación de matrices
        #print (round(TFinal [-1][0],2),'-> Calentado')
        #print (round(TFinal [-1][0],2))
        
        tiempo = int (tCarga)                                                   # Tiempo de carga estandar de acero líquido, 107 minutos - 6420 segundos
        iteraciones = int (tiempo / dt)
        for iteracion in range (iteraciones):
            carga = 1
            calentado = descarga = 0
            rho, Cp, hConvInt, hConvExt=propiedadesFisicas (colada,NNod,N1,TInicial,N2,N3,N4,N5,calentado,carga,descarga)
            hRadInt, hRadExt=radiacion (TInicial,Tamb,calentado,carga,descarga,TinternaCarga,Tinterna) 
            KG, CG, dx1, dx2, dx3, dx4, dx5=matrizKGyCG (Long1,NElemMaterial,NNod,NElemTotal,NMateriales,TInicial,Cp,rho,Conec,hConvExt,hRadExt,hConvInt,hRadInt,calentado,carga,descarga)
            RG= matrizRG (NNod,Tamb,hConvExt,hRadExt, calentado, carga, descarga, TinternaCarga,hConvInt,hRadInt,Tinterna)
            TFinal, TInicial=evaluacion (CG,KG,dt,TInicial,RG,carga, Tacero)
        #print (round(TFinal [-1][0],2),'-> Carga')
        #print (round(TFinal [-1][0],2))
        
        tiempo = int (tDescarga)                                                # Tiempo de descarga estandar de acero líquido, 15 minutos - 900 segundos
        '''
        if colada == 12 or colada == 12 * 2 or colada == 12 * 3 or colada == 12 * 4 or colada == 12 *  5 or colada == 12 * 6 or colada == 12 * 7 or colada == 12 * 8 or colada == 12 * 9 or colada == 12 * 10 or colada == 12 * 11 or colada == 12 * 12 or colada == 12 * 13 or colada == 12 * 14 or colada == 12 * 15:
            tiempo = int (16200)                # 4.5 hr.
        '''
        '''
        if colada <= 12:
            tiempo = tiempo + 23723
        elif colada <= 14:
            tiempo = tiempo + 24780
        elif colada <= 18:
            tiempo = tiempo + 13710
        elif colada <= 23:
            tiempo = tiempo + 9912
        elif colada <= 42:
            tiempo = tiempo + 5962
        elif colada <= 49:
            tiempo = tiempo + 5665
        elif colada <= 54:
            tiempo = tiempo + 9192
        elif colada <= 60:
            tiempo = tiempo + 6140
        elif colada <= 66:
            tiempo = tiempo + 6740
        elif colada <= 70:
            tiempo = tiempo + 9690
        elif colada <= 79:
            tiempo = tiempo + 21700
        elif colada <= 85:
            tiempo = tiempo + 5760
        elif colada <= 88:
            tiempo = tiempo + 30780
        elif colada <= 99:
            tiempo = tiempo + 36425
        elif colada <= 105:
            tiempo = tiempo + 6760
        elif colada <= 112:
            tiempo = tiempo + 5065
        elif colada <= 129:
            tiempo = tiempo + 33589
        elif colada <= 143:
            tiempo = tiempo + 9355
        elif colada <= 150:
            tiempo = tiempo + 5494
        elif colada <= 156:
            tiempo = tiempo + 5610
        '''
        iteraciones = int (tiempo / dt)
        for iteracion in range (iteraciones):
            descarga = 1
            carga = calentado = 0
            rho, Cp, hConvInt, hConvExt=propiedadesFisicas (colada,NNod,N1,TInicial,N2,N3,N4,N5,calentado,carga,descarga)
            hRadInt, hRadExt=radiacion (TInicial,Tamb,calentado,carga,descarga,TinternaCarga,Tinterna)
            KG, CG, dx1, dx2, dx3, dx4, dx5=matrizKGyCG (Long1,NElemMaterial,NNod,NElemTotal,NMateriales,TInicial,Cp,rho,Conec,hConvExt,hRadExt,hConvInt,hRadInt,calentado,carga,descarga)
            RG= matrizRG (NNod,Tamb,hConvExt,hRadExt, calentado, carga, descarga, TinternaCarga,hConvInt,hRadInt,Tinterna)
            TFinal, TInicial=evaluacion (CG,KG,dt,TInicial,RG,carga, Tacero)
        #print (round(TFinal [-1][0],2),'-> Descarga')
        #print (round(TFinal [-1][0],2))
        
        #perfilTemperaturas ()                                                  # Grafica el perfil de temperaturas
        # col, temp=graficas (col,temp,colada,TFinal,coladas)
        
        # graficasDesgaste (col,temp,verif,coladas,tempObjetivo)                                                     # Grafica las líneas que buscan la temperatura objetivo
        
        Long1 [0] = Long1 [0] - tasaDesgaste                                    # Actualizacion del espesor del primer refractario a cada colada
        col.append (int(colada+1))                                                                  # Guardado de coladas        
        temp.append (TFinal [-1][0])
    
         
    # tempRef = TFinal [-1]
    
    # print (tempObjetivo - TFinal [-1])
    # print (tempObjetivo, TFinal [-1])
    # print (tasaDesgaste)
    #print (TFinal [-1])
    # if tempObjetivo - TFinal [-1] > 0:
    #     tasaDesgaste = tasaDesgaste + 0.25
       
    
    # elif tempObjetivo - TFinal [-1] < 0 and Long1 [0] > 1:
    #     tasaDesgaste = tasaDesgaste - 0.20
       
        
    # if tasaDesgaste < 0 or Long1 [0] > 152 or Long1 [0] < 0:
    #     if tasaDesgaste < 0:
    #         print ('Tasa de desgaste negativa.')
    #     if Long1 [0] > 152:
    #         print ('Espesor mayor al original.')
    #     if Long1 [0] < 0:
    #         print ('Espesor negativo.')
    #     break
    # verif = 1
    # graficasDesgaste (col,temp,verif,coladas,tempObjetivo)                                                             # Grafica las líneas que buscan la temperatura objetivo
    # tasaReal = tasaDesgaste
    return col, temp, tasaDesgaste


coladas, tCalentamiento, tCarga, tDescarga, pregunta1, CLE=preguntas ()                                                                # Preguntas para variar los parametros de las coladas
tasaDesgaste1 = float(input ('Tasa de desgaste? '))                                                                                    # Tasa de desgaste en mm/colada
tasaDesgaste2 = float(input ('Tasa de desgaste? '))
col1, temp1, tasaDesgaste1=main(coladas, tCalentamiento, tCarga, tDescarga, pregunta1, CLE,tasaDesgaste1)
col2, temp2, tasaDesgaste2=main(coladas, tCalentamiento, tCarga, tDescarga, pregunta1, CLE,tasaDesgaste2)
plt.plot (col1, temp1,label = str(tasaDesgaste1), color = 'tab:red')
plt.plot (col2, temp2,label = str(tasaDesgaste2), color = 'tab:blue')
plt.show
    



# if __name__ == '__main__':
    
#     coladas, tCalentamiento, tCarga, tDescarga, pregunta1, CLE=preguntas ()                                                                # Preguntas para variar los parametros de las coladas
#     tasaDesgaste1 = float(input ('Tasa de desgaste? '))                                                                                    # Tasa de desgaste en mm/colada
#     tasaDesgaste2 = float(input ('Tasa de desgaste? '))

#     queue1 = Queue()
#     queue2 = Queue()
#     p = Process(target=main, args=(coladas, tCalentamiento, tCarga, tDescarga, pregunta1, CLE,tasaDesgaste1,queue1,))
#     q = Process(target=main, args=(coladas, tCalentamiento, tCarga, tDescarga, pregunta1, CLE,tasaDesgaste2,queue2,))
#     p.start()
#     q.start()
#     p.join()
#     q.join
#     col1, temp1, tasaDesgaste1 = queue1.get()
#     col2, temp2, tasaDesgaste2 = queue2.get()
#     plt.plot (col1, temp1,label = str(tasaDesgaste1), color = 'tab:red')
#     plt.plot (col2, temp2,label = str(tasaDesgaste2), color = 'tab:blue')
#     plt.show
