import numpy as np
def Matriz_tasaDesgaste(nlineas, limite_sup,limite_inf):
    tasaDesgaste=np.zeros(nlineas,dtype=float)                                 #se crea una matriz llamada tasaDEsgaste 
    tasaDesgaste_M=np.zeros(nlineas,dtype=float)                               #se crea una matriz llamada tasaDEsgasteM que se mantendra constante    
    for i in range (nlineas):                                                  #Para i en el rango de nlineas 
        tasaDesgaste[i]=float(i*(limite_sup-limite_inf)/(nlineas-1)+limite_inf)       #la tasa de desgaste esta dada por la funcion   i*(limite_sup-limite_inf)/(nlineas-1)+limite_inf                         
        tasaDesgaste_M[i]=float(i*(limite_sup-limite_inf)/(nlineas-1)+limite_inf)     #la tasa de desgaste esta dada por la funcion   i*(limite_sup-limite_inf)/(nlineas-1)+limite_inf                                 
    return tasaDesgaste,tasaDesgaste_M                                  