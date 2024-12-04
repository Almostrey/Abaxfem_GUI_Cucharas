import numpy as np
from elementosFinitos import elementosFinitos
from temperaturas import temperaturas
from inicializadoTemperaturas import inicializadoTemperaturas
from Creador_Historia import Creador_Historia
from Proceso_Elementos_Finitos_Inf import Proceso_Elementos_Finitos

def fixCell(n):
    try:
        return float(n)
    except:
        return 0
    
def processEF_if_first_time(coladas, pregunta1, CLE,tasaDesgaste, t,Historia):
    NElemTotal, NMateriales, NElemMaterial, NNod, N1, N2, N3, N4, N5, Conec = elementosFinitos ()                                      # Definicion de parámetros del modelo de elementos finitos
    Tamb, Tacero, Tinterna, TinternaCarga=temperaturas ()                                                                              # Definición global de valores de temperatura del modelo
    TInicial=inicializadoTemperaturas (NNod,Tamb)                                                                                      # Iniciado de temperaturas nodales en 20 C    
    Historia=np.zeros((1,NNod+3))
    col = []                                                                                                                   # Vector donde se almacenan las coladas
    temp = [] 
    
    for colada in range (coladas):                                                                                                     # Bucle para iterar las coladas        
        if colada == 0:                                                                                                                # Inicializado de espesores solo en la primera colada
            Long1 = np.array([178. , 15. , 108. , 10. , 40.])                                                                                         # Vector de espesores de materiales     
                                                                                                
        
                                                                                                                                # Paso de tiempo
        
        # if pregunta1 == 1:
        #     if colada == CLE:
        #         TInicial = np.ones ((NNod , 1)) * Tamb
        #         TFinal = TInicial
        #         Long1 [0] = 178
        
                                                                                             # Tiempo de calentado estandar, 10 minutos - 600 segundos
       
#Calentado--------------------------------------------------------------------------------------------------------------------        
        dt = 0.1         
        tiempo = int (fixCell(t[colada,0])+fixCell(t[colada,1]))*60         
        # iteraciones = int (tiempo / dt)     
        
        time_count=0    #################
        while time_count+dt<=tiempo:
            calentado = 1                                                                                                              # Switch para escoger propiedades en funciones
            carga = descarga = 0                                                                                                       # Switch para escoger propiedades en funciones
            rho, Cp, hConvInt, hConvExt,  hRadInt, hRadExt, KG, CG, dx1, dx2, dx3, dx4, dx5,RG,TFinal, TInicial,check=Proceso_Elementos_Finitos(colada,NNod,N1,TInicial,N2,N3,N4,N5,calentado,carga,descarga,TinternaCarga,Tinterna,Tamb,Long1,NElemMaterial,NElemTotal,NMateriales,Conec,dt,Tacero)                                                                        # Evaluación de matrices
            time_count=time_count+dt ##########
            if check:               ##############
                dt=min(dt+dt, 100)      ##########
            
            
        if  time_count<tiempo:
            dt=tiempo-time_count
            calentado = 1                                                                                                              # Switch para escoger propiedades en funciones
            carga = descarga = 0                                                                                                       # Switch para escoger propiedades en funciones
            rho, Cp, hConvInt, hConvExt,  hRadInt, hRadExt, KG, CG, dx1, dx2, dx3, dx4, dx5,RG,TFinal, TInicial,check=Proceso_Elementos_Finitos(colada,NNod,N1,TInicial,N2,N3,N4,N5,calentado,carga,descarga,TinternaCarga,Tinterna,Tamb,Long1,NElemMaterial,NElemTotal,NMateriales,Conec,dt,Tacero)                                                                        # Evaluación de matrices
            time_count=time_count+dt
            
        
       # for iteracion in range (iteraciones):                                                                                          # Bucle para iterar el calentamiento
        #     calentado = 1                                                                                                              # Switch para escoger propiedades en funciones
        #     carga = descarga = 0                                                                                                       # Switch para escoger propiedades en funciones
        #     rho, Cp, hConvInt, hConvExt,  hRadInt, hRadExt, KG, CG, dx1, dx2, dx3, dx4, dx5,RG,TFinal, TInicial,check=Proceso_Elementos_Finitos(colada,NNod,N1,TInicial,N2,N3,N4,N5,calentado,carga,descarga,TinternaCarga,Tinterna,Tamb,Long1,NElemMaterial,NElemTotal,NMateriales,Conec,dt,Tacero)                                                                        # Evaluación de matrices

#Carga----------------------------------------------------------------------------------------------------------------------------------------------   
        tiempo = int (fixCell(t[colada,2])+fixCell(t[colada,3])+fixCell(t[colada,4]))*60                                                                          # Tiempo de carga estandar de acero líquido, 107 minutos - 6420 segundos
        dt=0.1
        time_count=0    #################
        while time_count+dt<=tiempo:
            carga = 1
            calentado = descarga = 0                                                                                                     # Switch para escoger propiedades en funciones
            rho, Cp, hConvInt, hConvExt,  hRadInt, hRadExt, KG, CG, dx1, dx2, dx3, dx4, dx5,RG,TFinal, TInicial,check=Proceso_Elementos_Finitos(colada,NNod,N1,TInicial,N2,N3,N4,N5,calentado,carga,descarga,TinternaCarga,Tinterna,Tamb,Long1,NElemMaterial,NElemTotal,NMateriales,Conec,dt,Tacero)                                                                        # Evaluación de matrices
            time_count=time_count+dt ##########
            if check:               ##############
                dt=min(dt+dt, 100)      ##########
            
            
        if  time_count<tiempo:
            dt=tiempo-time_count
            carga = 1
            calentado = descarga = 0                                                                                                     # Switch para escoger propiedades en funciones
            rho, Cp, hConvInt, hConvExt,  hRadInt, hRadExt, KG, CG, dx1, dx2, dx3, dx4, dx5,RG,TFinal, TInicial,check=Proceso_Elementos_Finitos(colada,NNod,N1,TInicial,N2,N3,N4,N5,calentado,carga,descarga,TinternaCarga,Tinterna,Tamb,Long1,NElemMaterial,NElemTotal,NMateriales,Conec,dt,Tacero)                                                                        # Evaluación de matrices
            time_count=time_count+dt ##########
            
        temp.append (TFinal [-1][0])
        Historia = Creador_Historia(Historia,NNod,colada,Long1,TFinal,tasaDesgaste)
        
        # iteraciones = int (tiempo / dt)
        # for iteracion in range (iteraciones):
        #     carga = 1
        #     calentado = descarga = 0
        #     rho, Cp, hConvInt, hConvExt,  hRadInt, hRadExt, KG, CG, dx1, dx2, dx3, dx4, dx5,RG,TFinal, TInicial,check=Proceso_Elementos_Finitos(colada,NNod,N1,TInicial,N2,N3,N4,N5,calentado,carga,descarga,TinternaCarga,Tinterna,Tamb,Long1,NElemMaterial,NElemTotal,NMateriales,Conec,dt,Tacero)                                                                        # Evaluación de matrices

#Descarga----------------------------------------------------------------------------------------------------------------------------------------------
        if colada<coladas-1:            
            tiempo = int (fixCell(t[colada,5])+fixCell(t[colada,6]))*60                                                                                     # Tiempo de descarga estandar de acero líquido, 15 minutos - 900 segundos
            
            dt=0.1
            time_count=0    #################
            while time_count+dt<=tiempo:
                descarga = 1
                carga = calentado = 0
                rho, Cp, hConvInt, hConvExt,  hRadInt, hRadExt, KG, CG, dx1, dx2, dx3, dx4, dx5,RG,TFinal, TInicial,check=Proceso_Elementos_Finitos(colada,NNod,N1,TInicial,N2,N3,N4,N5,calentado,carga,descarga,TinternaCarga,Tinterna,Tamb,Long1,NElemMaterial,NElemTotal,NMateriales,Conec,dt,Tacero)                                                                        # Evaluación de matrices
    
                time_count=time_count+dt ##########
                if check:               ##############
                    dt=min(dt+dt, 100)      ##########
                
                
            if  time_count<tiempo:
                dt=tiempo-time_count
                descarga = 1
                carga = calentado = 0
                rho, Cp, hConvInt, hConvExt,  hRadInt, hRadExt, KG, CG, dx1, dx2, dx3, dx4, dx5,RG,TFinal, TInicial,check=Proceso_Elementos_Finitos(colada,NNod,N1,TInicial,N2,N3,N4,N5,calentado,carga,descarga,TinternaCarga,Tinterna,Tamb,Long1,NElemMaterial,NElemTotal,NMateriales,Conec,dt,Tacero)                                                                        # Evaluación de matrices
                time_count=time_count+dt ##########
                
            
            
            
            
            
            
            # iteraciones = int (tiempo / dt)
            # for iteracion in range (iteraciones):
            #     descarga = 1
            #     carga = calentado = 0
            #     rho, Cp, hConvInt, hConvExt,  hRadInt, hRadExt, KG, CG, dx1, dx2, dx3, dx4, dx5,RG,TFinal, TInicial,check=Proceso_Elementos_Finitos(colada,NNod,N1,TInicial,N2,N3,N4,N5,calentado,carga,descarga,TinternaCarga,Tinterna,Tamb,Long1,NElemMaterial,NElemTotal,NMateriales,Conec,dt,Tacero)                                                                        # Evaluación de matrices
    
    #--------------------------------------------------------------------------------------------------------------------------------------------------------
    
    
    
    
            Pos_nodo1=np.zeros((NElemMaterial+1,1))  
            Pos_nodo2=np.zeros((NElemMaterial+1,2))
            Eq_Temp=np.zeros((NElemMaterial,2))
            for posi in range(NElemMaterial+1):
                Pos_nodo1[posi,0]=Long1[0]-posi*Long1[0]/NElemMaterial
                Long_new=Long1[0]-tasaDesgaste
                Pos_nodo2[posi,0]=Long_new-posi*(Long_new)/NElemMaterial
                if posi>0:
                    Eq_Temp[posi-1,0]=m=(TInicial[posi-1,0]-TInicial[posi,0])/(Pos_nodo1[posi-1,0]-Pos_nodo1[posi,0])
                    Eq_Temp[posi-1,1]=TInicial[posi-1,0]-m*Pos_nodo1[posi-1,0]
                
            T_prueba=np.copy(TInicial)
            for ti in range (1,NElemMaterial):
                for tj in range (NElemMaterial):
                    if Pos_nodo1[tj,0]>=Pos_nodo2[ti,0] and Pos_nodo1[tj+1,0]<=Pos_nodo2[ti,0] :
                        T_prueba[ti,0]= Eq_Temp[tj,0]*Pos_nodo2[ti,0]+Eq_Temp[tj,1]
                        break
            TInicial=T_prueba 
    #--------------------------------------------------------------------------------------------------------------------------------------------------------
    
                    
                
                
            Long1 [0] = Long1 [0] - tasaDesgaste
                                                                                                                                                    # Actualizacion del espesor del primer refractario a cada colada
        col.append (int(colada+1))                                                                                                                                                              # Guardado de coladas        

        

    Historia2=None    
    Historia=np.delete(Historia, (0), axis=0)
    Historia=Historia.tolist()
 
    return col, temp, tasaDesgaste,Historia,Historia2