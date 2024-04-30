import numpy as np
############################################################# Geometría y propiedades físicas del modelo
###############################################################################
def propiedadesFisicas (colada,NNod,N1,TInicial,N2,N3,N4,N5,calentado,carga,descarga):
    
    # global dt, Long1, kCond, rho, Cp, hConvInt, hConvExt
    

        
    # La conductividad térmica se calcula en las matrices de elementos  de conductividad
    rho = np.zeros ((1 , NNod))                                                     # Densidad de cada nodo
    Cp = np.zeros ((1 , NNod))                                                      # Calor específico de cada nodo
    for i in range (NNod):
        if i <= max (N1):                                                           # Sindoform
            rho [0][i] = 2.95 * 10**-9
            Cp [0][i] = (0.0002 * TInicial [i][0] + 0.8296) * 10**9
        elif max (N1) <= i <= max (N2):                                             # Ankerfill
            rho [0][i] = 2.2 * 10**-9
            Cp [0][i] = (1.05 + 0.0003 * TInicial [i][0]) * 10**9
        elif max (N2) <= i <= max (N3):                                             # Resistal   
            rho [0][i] = 2.54 * 10**-9
            Cp [0][i] = (((0.8 + 0.0003 * TInicial [i][0]) + 
                         (0.8 + 0.0004 * TInicial [i][0])) * 10**9) /2
        elif max (N3) <= i <= max (N4):                                             # Silplate
            rho [0][i] = 0.85 * 10**-9
            Cp [0][i] = 1.13 * 10**9
        elif max (N4) <= i <= max (N5):                                             # Acero
            rho [0][i] = 7.85 * 10**-9
            Cp [0][i] = 0.561 * 10**9
   
    if calentado == 1:                                                              # Switch para calentado
        hConvInt = 0.0316595                                                       # Coeficiente de conveccion interna para etapa de calentado
    
    elif carga == 1:                                                                # Switch para carga
        hConvInt = 11.38                                                          # Coeficiente de convección interna para etapa de carga de acero líquido
             
    elif descarga == 1:                                                             # Switch para descarga
        hConvInt = 0.0030556                                                         # Coeficiente de convección interna para etapa de descarga
        
    hConvExt = 0.0053832                                                         # Coeficiente de convección externa para todas las etapas
    return  rho, Cp, hConvInt, hConvExt
