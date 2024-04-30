import numpy as np

############################################################# Iniciado de temperaturas nodales en 20 C
###############################################################################
def inicializadoTemperaturas (NNod,Tamb):    
    TInicial = np.ones ((NNod , 1)) * Tamb                                          # Temperatura de todos los nodos inicializada en 20 C
    return TInicial