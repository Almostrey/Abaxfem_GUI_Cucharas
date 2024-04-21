import numpy as np
from Matriz_tasaDesgaste import Matriz_tasaDesgaste
def Aproximacion2(tasaDesgaste_M,col_general,temp_general,nlineas,temp_obj,coladas,limite_superior_max):
    dif_Array=np.zeros((nlineas,1))                                                                                             #se crea matriz que almacenara la diferencia entre la temp en la colada evualuada, para cada tasa de desgaste y la temp obj o medida
    W=0                                                                                                                         # Variable de apoyo W=0
    for i in range (nlineas):                                                                                                   #Se llena la matriz de diferencias
        dif_Array[i] = (temp_general[-1,i]-temp_obj)                                                                     # para cada tasa de desgaste i, temp calculada-temp_obj                       
    dif_Array=np.nan_to_num(dif_Array)                                                                                          #Los valores nan se eliminan de la matriz de diferencias   
    dif_Array_pos =np.abs(np.where(dif_Array > 0, dif_Array, 0))                                                                #Se crea matriz que contiene solo los valores positivos de la matriz de diferencias
    dif_Array_neg =np.abs(np.where(dif_Array < 0, dif_Array, 0))                                                                #Se crea matriz que contiene solo los valores negativos de la matriz de diferencias  y se los convierte en valor absoluto                           
    temp_support_matrix=temp_general[-1,:][~np.isnan(temp_general[-1,:])] 
    #CASO 1----------------------------------------------------------------------------------                                                                                             
    if temp_support_matrix[-1]>temp_support_matrix[0]:                                                                                   #El caso uno se da cuando la temp calculada para la tasa de desgaste maxima en la colada evaluada es > que la temp calculada para la tasa de desgaste minima en la colada evaluada
        # print("Caso 1")                                                                                                         
        #CASO1.1-----------------------------------------------------------------------------
        if all((x >= 0 or np.isnan(x)) for x in dif_Array):                                                                              #Si todos los valroes de dif array son positivos, significa que la temp medida se encuentra por debajo de las temperaturas de la tasa minima de desgaste (0 mm/col) (Error)                        
            tasaDesgaste_M=None                                                                                             
            tasaDesgaste=None                                                                                             
            # print ('error')                                                                                             
            W=1                                                                                                                           #Variable de apoyo W se vuelve 1                                                                                                 
        #CASO1.2----------------------------------------------------------------------------------------
        elif all((x <= 0 or np.isnan(x)) for x in dif_Array):                                                                             #Si todos los valroes de dif array son negativos, significa que la temp medida se encuentra por encima de las temperaturas de las tasas de desgaste establecidas                          
            tasaDesgaste_M_inf=max(tasaDesgaste_M)    #Se encuentran las coordenadas del punto en el que existe la menor diferencia de temperaturas, pues esta coordenada corresponde a las coordenadas de la tasa de desgaste con mayor similitud                                                                
            
            tasaDesgaste,tasaDesgaste_M=Matriz_tasaDesgaste(nlineas, min(tasaDesgaste_M_inf+1,  limite_superior_max),tasaDesgaste_M_inf)                              #Se llama a la funcion para crear nuevas matrices de desgaste. Para una segunda aproximacion se suma 1 mm/colada a la tasa de desgaste de las coordenadas previamente encontradas.                                                                                                                                             
            coladas=coladas                                   
            # print('encima')                                                                                             
        #CASO1.3----------------------------------------------------------------------------------------                                                                                             
        else:                                                                                                                              #Este caso se da cuando la temperatura medida se ubica entre las temp calculadas para dos tasas de desgaste   
            tasaDesgaste_M_sup=np.max(tasaDesgaste_M[(np.where( dif_Array_pos==np.min(dif_Array_pos[np.nonzero(dif_Array_pos)]))[0])])       # Se encuentra la tasa de desgaste superior, con respecto al punto o zona en la cual se ubica la temperatura medida                                                               
            tasaDesgaste_M_inf=np.min(tasaDesgaste_M[(np.where( dif_Array_neg==np.min(dif_Array_neg[np.nonzero(dif_Array_neg)]))[0])])       # Se encuentra la tasa de desgaste superior, con respecto al punto o zona en la cual se ubica la temperatura medida                                                               
            tasaDesgaste,tasaDesgaste_M=Matriz_tasaDesgaste(nlineas, tasaDesgaste_M_sup,tasaDesgaste_M_inf)                                  #Se llama a la funcion para crear nuevas matrices de tasa de desgaste, se utiliza el limite superio r e inferior encontrados en las 2 lineas de codigo superiores                                                                              
            # print('en el medio')                                                                                             
                                                                                      
                                                                                             
       #CASO 2----------------------------------------------------------------------------------------------
    if temp_support_matrix[-1]<temp_support_matrix[0]:                                                                   #El CASO 2 se da cuando la temp calculada para la tasa de desgaste maxima en la colada evaluada es < que la temp calculada para la tasa de desgaste minima en la colada evaluada                             
        # print ("segundo caso")                                                                                                #Para el CASO 2 Se pueden dar los tres subcasos del CASO 1, siguiendo una logica similar, se llegan a las siguientes lineas de codigo
        # CASO2.1----------------------------------------------------------------------------------------
        if all((x <= 0 or np.isnan(x)) for x in dif_Array):                                                                                             
            tasaDesgaste_M=None                                                                                             
            tasaDesgaste=None                                                                                             
            # print ('error')                                                                                                                                                                                                                                                                                                                                                                                    
            W=1  
        # CASO2.2----------------------------------------------------------------------------------------                                                                                   
        elif all((x >= 0 or np.isnan(x)) for x in dif_Array):                                                                                             
            tasaDesgaste_M_inf = max(tasaDesgaste_M)
            tasaDesgaste,tasaDesgaste_M=Matriz_tasaDesgaste(nlineas, min (tasaDesgaste_M_inf+1,limite_superior_max),tasaDesgaste_M_inf)                                                                                              
            coladas=coladas                                                                                             
            # print('encima')                                                                                             
        # CASO2.3----------------------------------------------------------------------------------------                                                                                             
        else:                                                                                                                                                                                             
            tasaDesgaste_M_inf = np.max(tasaDesgaste_M[(np.where( dif_Array_pos==np.min(dif_Array_pos[np.nonzero(dif_Array_pos)]))[0])])                                                                                             
            tasaDesgaste_M_sup = np.min(tasaDesgaste_M[(np.where( dif_Array_neg==np.min(dif_Array_neg[np.nonzero(dif_Array_neg)]))[0])])                                                                                             
            tasaDesgaste,tasaDesgaste_M=Matriz_tasaDesgaste(nlineas, tasaDesgaste_M_sup,tasaDesgaste_M_inf)                                                                                             
            # print('en el medio')                                                                                             
                                                                                                 
    return W,tasaDesgaste,tasaDesgaste_M,coladas                                                                                             
                                                                                                                                                                           
        

    
        
        
        