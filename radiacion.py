############################################################# Calculo del coeficiente de radiación térmica
###############################################################################
def radiacion (TInicial,Tamb,calentado,carga,descarga,TinternaCarga,Tinterna):
    
    # global hRadInt, hRadExt, hRadIntCarga
    
    emiExt = 0.757977                                                                                                                             # Emisividad externa
    emiInt = 0.467804                                                                                                                                # Emisividad interna
    
    sb = 5.67 * 10**-11                                                                                                                         # Constante de Steffan Boltzmann
    
    hRadExt = sb * emiExt * ((TInicial [-1][0] + 273) + (Tamb + 273)) * ((TInicial [-1][0] + 273)**2 + (Tamb + 273)**2)                         # Coeficiente de radiación externa para todas las etapas
    
    if calentado == 1 and carga == descarga == 0:                                                                                               # Switch para calentado
        hRadInt = sb * emiInt * ((TInicial [0][0] + 273) + (TinternaCarga + 273)) * ((TInicial [0][0] + 273)**2 + (TinternaCarga + 273)**2)     # Coeficiente de radiación interna para etapa de calentado
    
    elif descarga == 1 and carga == calentado == 0:                                                                                             # Switch para descarga
        hRadInt = sb * emiInt * ((TInicial [0][0] + 273) + (Tinterna + 273)) * ((TInicial [0][0] + 273)**2 + (Tinterna + 273)**2)               # Coeficiente de radiación interna para etapa de descarga
    else:
        hRadInt=None
    return hRadInt, hRadExt
    