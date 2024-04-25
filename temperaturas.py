############################################################# Definición de temperaturas del modelo
###############################################################################
def temperaturas ():
    
    # global Tamb, Tacero, Tinterna, TinternaCarga
    
    Tamb = 20                                                                       # Temperatura de ambiente externo de la cuchara
    Tacero = 1585                                                                  # Temperatura del acero líquido
    Tinterna = 110                                                              # Temperatura de ambiente interno de la cuchara
    TinternaCarga = 1191.708                                                         # Temperatura de ambiente interno de la cuchara al usar el calentador
    return Tamb, Tacero, Tinterna, TinternaCarga
############################################################# Preguntas para cambiar las etapas de colado
###############################################################################
