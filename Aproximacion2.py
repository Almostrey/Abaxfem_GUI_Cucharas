import numpy as np
def Aproximacion2(tasaDesgaste_M,col_general,temp_general,temp_obj):
    # print("Aproximacion2")
    # print(tasaDesgaste_M)
    # print(col_general)
    # print(temp_general)
    nlineas=len(tasaDesgaste_M)
    dif_Array=np.zeros((nlineas,1))                                                                                             #se crea matriz que almacenara la diferencia entre la temp en la colada evualuada, para cada tasa de desgaste y la temp obj o medida
    W=0                                                                                                                         # Variable de apoyo W=0
    for i in range (nlineas):                                                                                                   #Se llena la matriz de diferencias
        dif_Array[i] = (temp_general[-1,i]-temp_obj)                                                                     # para cada tasa de desgaste i, temp calculada-temp_obj                       
    dif_Array=np.nan_to_num(dif_Array)                                                                                          #Los valores nan se eliminan de la matriz de diferencias   
    dif_Array_pos =np.abs(np.where(dif_Array > 0, dif_Array, 0))                                                                #Se crea matriz que contiene solo los valores positivos de la matriz de diferencias
    dif_Array_neg =np.abs(np.where(dif_Array < 0, dif_Array, 0))                                                                #Se crea matriz que contiene solo los valores negativos de la matriz de diferencias  y se los convierte en valor absoluto                           
    temp_support_matrix=temp_general[-1,:][~np.isnan(temp_general[-1,:])] 
    #print("Dentro Aproximacion2")
    #CASO 1----------------------------------------------------------------------------------                                                                                             
    if temp_support_matrix[-1]>temp_support_matrix[0]:                                                                                   #El caso uno se da cuando la temp calculada para la tasa de desgaste maxima en la colada evaluada es > que la temp calculada para la tasa de desgaste minima en la colada evaluada
        #print("Caso 1")                                                                                                         
        #CASO1.1-----------------------------------------------------------------------------
        if all((x >= 0 or np.isnan(x)) for x in dif_Array):                                                                              #Si todos los valroes de dif array son positivos, significa que la temp medida se encuentra por debajo de las temperaturas de la tasa minima de desgaste (0 mm/col) (Error)                        
            #print("Caso1.1")    
            tasaDesgaste_M=None                                                                                                                                                                                          
            # print ('error')                                                                                             
            W=1                                                                                                                           #Variable de apoyo W se vuelve 1                                                                                                 
        #CASO1.2----------------------------------------------------------------------------------------
        elif all((x <= 0 or np.isnan(x)) for x in dif_Array):                                                                             #Si todos los valroes de dif array son negativos, significa que la temp medida se encuentra por encima de las temperaturas de las tasas de desgaste establecidas                          
            #print("Caso1.2")
            tasaDesgaste_M_inf=max(tasaDesgaste_M)    #Se encuentran las coordenadas del punto en el que existe la menor diferencia de temperaturas, pues esta coordenada corresponde a las coordenadas de la tasa de desgaste con mayor similitud                                                                
            extrapolacion=True
            interpolacion=False                                  
            # print('encima')                                                                                             
        #CASO1.3----------------------------------------------------------------------------------------                                                                                             
        else:                                                                                                                              #Este caso se da cuando la temperatura medida se ubica entre las temp calculadas para dos tasas de desgaste   
            #print("Caso1.3")
            tasaDesgaste_M_sup=np.max(tasaDesgaste_M[(np.where( dif_Array_pos==np.min(dif_Array_pos[np.nonzero(dif_Array_pos)]))[0])])       # Se encuentra la tasa de desgaste superior, con respecto al punto o zona en la cual se ubica la temperatura medida                                                               
            tasaDesgaste_M_inf=np.min(tasaDesgaste_M[(np.where( dif_Array_neg==np.min(dif_Array_neg[np.nonzero(dif_Array_neg)]))[0])])       # Se encuentra la tasa de desgaste superior, con respecto al punto o zona en la cual se ubica la temperatura medida                                                               
            extrapolacion=False
            interpolacion=True 
            # print('en el medio')                                                                                             
                                                                                      
                                                                                             
       #CASO 2----------------------------------------------------------------------------------------------
    if temp_support_matrix[-1]<temp_support_matrix[0]:                                                                   #El CASO 2 se da cuando la temp calculada para la tasa de desgaste maxima en la colada evaluada es < que la temp calculada para la tasa de desgaste minima en la colada evaluada                             
        #print ("segundo caso")                                                                                                #Para el CASO 2 Se pueden dar los tres subcasos del CASO 1, siguiendo una logica similar, se llegan a las siguientes lineas de codigo
        # CASO2.1----------------------------------------------------------------------------------------
        if all((x <= 0 or np.isnan(x)) for x in dif_Array):                                                                                             
            #print("Caso2.1")
            tasaDesgaste_M=None                                                                                                                                                                                        
            # print ('error')                                                                                                                                                                                                                                                                                                                                                                                    
            W=1  
        # CASO2.2----------------------------------------------------------------------------------------                                                                                   
        elif all((x >= 0 or np.isnan(x)) for x in dif_Array):                                                                                             
            #print("Caso2.2")
            tasaDesgaste_M_inf = max(tasaDesgaste_M)
            extrapolacion=True
            interpolacion=False                                                                                                                                                                                       
            # print('encima')                                                                                             
        # CASO2.3----------------------------------------------------------------------------------------                                                                                             
        else:                                                                                                                                                                                             
            #print("Caso2.3")
            tasaDesgaste_M_inf = np.max(tasaDesgaste_M[(np.where( dif_Array_pos==np.min(dif_Array_pos[np.nonzero(dif_Array_pos)]))[0])])                                                                                             
            tasaDesgaste_M_sup = np.min(tasaDesgaste_M[(np.where( dif_Array_neg==np.min(dif_Array_neg[np.nonzero(dif_Array_neg)]))[0])])         
            extrapolacion=False
            interpolacion=True                                                                                    
    
    #try:
        #print("tasaDesgaste_M_inf: ", tasaDesgaste_M_inf)
        #print("tasaDesgaste_M_sup: ", tasaDesgaste_M_sup)
    #except: pass
    if W==0 and interpolacion:
        # print(tasaDesgaste_M_sup)
        # print (tasaDesgaste_M_inf)
        # print("interpolacion")
        index_TS=np.where(tasaDesgaste_M==tasaDesgaste_M_sup)[0]
        # print (index_TS)
        index_TI=np.where(tasaDesgaste_M==tasaDesgaste_M_inf)[0]
        # print (index_TI)
        T_sup=temp_general[-1,index_TS]
        T_inf=temp_general[-1,index_TI]
        T_desgaste=((temp_obj-T_inf)/(T_sup-T_inf))*(tasaDesgaste_M_sup-tasaDesgaste_M_inf)+tasaDesgaste_M_inf
        T_desgaste=T_desgaste[0]
        # print("interpolacion")
    elif W==0 and extrapolacion:
        # print("extrapolacion")
        # print (tasaDesgaste_M_inf)
        index_TI=np.where(tasaDesgaste_M==tasaDesgaste_M_inf)[0]
        # print (index_TI)
        index_TII=index_TI-1
        tasaDesgaste_M_sup=tasaDesgaste_M[index_TI]
        tasaDesgaste_M_inf=tasaDesgaste_M[index_TII]
        T_sup=temp_general[-1,index_TI]
        T_inf=temp_general[-1,index_TII]
        T_desgaste=((temp_obj-T_inf)/(T_sup-T_inf))*(tasaDesgaste_M_sup-tasaDesgaste_M_inf)+tasaDesgaste_M_inf
        T_desgaste=T_desgaste[0]
        # print("extrapolacion")
    elif W==1:
        T_desgaste=None
    #print("W:", W, "T_desgaste:", T_desgaste)
    #print("Fuera Aproximacion2")
    return W,T_desgaste                                                                                             
                                                                                                                                                                           
        

    
        
        
        