import numpy as np 
############################################################# Definición de matriz de cargas globales
###############################################################################
def matrizRG (NNod,Tamb,hConvExt,hRadExt, calentado, carga, descarga, TinternaCarga,hConvInt,hRadInt,Tinterna):
    
    # global RG
    
    RG = np.zeros ((NNod , 1))                                                      # Matriz de cargas globales
    
    RG [-1] = Tamb * hConvExt + Tamb * hRadExt                                      # Actualilzado del nodo externo con valores de conveccion y radiación externos
    
    if calentado == 1:                                                              # Switch para calentado
        RG [0] = RG [0] + TinternaCarga * hConvInt + TinternaCarga * hRadInt        # Actualilzado del nodo interno con valores de conveccion y radiación internos
    
    elif carga == 1:                                                                # Switch para carga
        RG [0] = RG [0]                                                             # Actualilzado del nodo interno
        
    elif descarga == 1:                                                             # Switch para descarga
        RG [0] = RG [0] + Tinterna * hConvInt                                       # Actualilzado del nodo interno con valores de conveccion y radiación internos
    return RG