import numpy as np     

############################################################# Evaluación de matrices
###############################################################################
def evaluacion (CG,KG,dt,TInicial,RG,carga, Tacero):
    
    # global TFinal, TInicial
    
    # T1 = np.matmul (CG - KG * dt , TInicial) + dt * RG                        #Explicito
    T1=np.matmul(CG,TInicial)+RG*dt                                             #Implicito
    if carga == 1:
        T1 [0] = T1 [0] + Tacero * 10**15
    
    CGmodif = CG + 0 
    
    if carga == 1:
        CGmodif [0][0] = CGmodif [0][0] + 10**15
        
    # TFinal = np.matmul (np.linalg.inv(CGmodif) , T1)                           #Explicito 
    
    TFinal=np.matmul(np.linalg.inv(CGmodif + KG * dt),T1)                       #Implicito
    T_difference=np.abs(TFinal-TInicial)
    check=np.all(T_difference<=10)


    TInicial = TFinal
    return TFinal, TInicial,check
    