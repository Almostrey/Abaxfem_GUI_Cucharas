import numpy as np
def determinacion_tasa_desgaste(tasaDesgaste_M,temp_general2,nlineas,temp_obj,coladas):                                                                             
    dif_Array=np.zeros((nlineas,1))                                                                         #se crea matriz que almacenara la diferencia entre la temp en la colada evualuada, para cada tasa de desgaste y la temp obj o medida   

    for i in range (nlineas):                                                                               #Se llena la matriz de diferencias
        dif_Array[i] = (temp_general2[-1,i]-temp_obj)                                                # para cada tasa de desgaste i, temp calculada-temp_obj                             
    dif_Array=np.nan_to_num(dif_Array)                                                                      #Los valores nan se eliminan de la matriz de diferencias       
    dif_Array_pos =np.abs(np.where(dif_Array > 0, dif_Array, 0))                                            #Se crea matriz que contiene solo los valores positivos de la matriz de diferencias                                  
    dif_Array_neg =np.abs(np.where(dif_Array < 0, dif_Array, 0))                                            #Se crea matriz que contiene solo los valores negativos de la matriz de diferencias  y se los convierte en valor absoluto                                  
    temp_support_matrix=temp_general2[-1,:][~np.isnan(temp_general2[-1,:])] 


#CASO1------------------------------------------------------------------------------------------------------------                                                                             
    if temp_support_matrix[-1]>temp_support_matrix[0]:                                            #El caso uno se da cuando la temp calculada para la tasa de desgaste maxima en la colada evaluada es > que la temp calculada para la tasa de desgaste minima en la colada evaluada                               
        if all((x <= 0 or np.isnan(x)) for x in dif_Array):                                                 #Si todos los valores son negativos, es decir la temp obejtivo se ecucentra sobre las temp calculadas para cada tasa de desgaste                            
            Tasa_Desgaste_encontrada=np.min(tasaDesgaste_M[(np.where( dif_Array_neg==np.min(dif_Array_neg[np.nonzero(dif_Array_neg)]))[0])])        #Se busca las coordenadas en las cuales la diferencia es minima                                                                     
            print(f'tasa desgaste mayor a {Tasa_Desgaste_encontrada}')                                                                             
            
        else:                                                                                               #Si la temp objetivo/medida, se ubica entre dos valores, se selecciona la tasa de desgaste mayor, por seguridad
            Tasa_Desgaste_encontrada=np.max(tasaDesgaste_M[(np.where( dif_Array_pos==np.min(dif_Array_pos[np.nonzero(dif_Array_pos)]))[0])])                                                                             
            print(f'tasa desgaste aproximada a {Tasa_Desgaste_encontrada}')                                                                             
            
         
#CASO2------------------------------------------------------------------------------------------------------------    
    if temp_support_matrix[-1]<temp_support_matrix[0]:                                             #El caso uno se da cuando la temp calculada para la tasa de desgaste maxima en la colada evaluada es < que la temp calculada para la tasa de desgaste minima en la colada evaluada                                      
        if all((x >= 0 or np.isnan(x)) for x in dif_Array):                                                 #Si todos los valores son positivos, es decir la temp obejtivo se ecucentra debajo de las temp calculadas para cada tasa de desgaste                              
            Tasa_Desgaste_encontrada = np.max(tasaDesgaste_M[(np.where( dif_Array_pos==np.min(dif_Array_pos[np.nonzero(dif_Array_pos)]))[0])])        #Se busca las coordenadas en las cuales la diferencia es minima                                                                             
            print(f'tasa desgaste mayor a {Tasa_Desgaste_encontrada}')                                                                             
            
        else:                                                                                
            Tasa_Desgaste_encontrada=np.min(tasaDesgaste_M[(np.where( dif_Array_neg==np.min(dif_Array_neg[np.nonzero(dif_Array_neg)]))[0])])        #Si la temp objetivo/medida, se ubica entre dos valores, se selecciona la tasa de desgaste mayor, por seguridad                                                                     
            print(f'tasa desgaste aproximada a {Tasa_Desgaste_encontrada}')                                                                             
            

    index_TD=np.where(tasaDesgaste_M==Tasa_Desgaste_encontrada)[0]

            
        
    
    return Tasa_Desgaste_encontrada,index_TD
