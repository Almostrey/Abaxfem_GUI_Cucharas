import numpy as np
############################################################# Definición de elementos finitos
###############################################################################
def elementosFinitos ():
    
    # global NElemTotal, NMateriales, NElemMaterial, NNod, N1, N2, N3, N4, N5, Conec
    
    NElemTotal = int (15)                                                           # Número de elementos finitos totales en la pared #15
    NMateriales = int (5)                                                           # Número de materiales en la pared
    NElemMaterial = int (NElemTotal / NMateriales)                                  # Número de elementos finitos en cada material de la pared
    NNod = int (NElemTotal + 1)                                                     # Número de nodos
    
    N1 = []                                                                         # Nodos pertenecientes al refractario Sindoform
    N2 = []                                                                         # Nodos pertenecientes al refractario Ankerfill                                                                         # 
    N3 = []                                                                         # Nodos pertenecientes al refractario Resistal
    N4 = []                                                                         # Nodos pertenecientes al refractario Silplate
    N5 = []                                                                         # Nodos pertenecientes al refractario Acero
    
    for nodo in range (NNod):                                                       # Bucle para definir los nodos de cada material
        if 0 * NElemTotal / NMateriales <= nodo <= 1 * NElemTotal / NMateriales:    
            N1.append(nodo)
        if 1 * NElemTotal / NMateriales <= nodo <= 2 * NElemTotal / NMateriales:
            N2.append(nodo)
        if 2 * NElemTotal / NMateriales <= nodo <= 3 * NElemTotal / NMateriales:
            N3.append(nodo)
        if 3 * NElemTotal / NMateriales <= nodo <= 4 * NElemTotal / NMateriales:
            N4.append(nodo)
        if 4 * NElemTotal / NMateriales <= nodo <= 5 * NElemTotal / NMateriales:
            N5.append(nodo)
            
    Conec = np.zeros ((NElemTotal , 2))                                             # Conectividad de elementos finitos
    for i in range (NElemTotal):
        for j in range (2):
            Conec [i][j] = int (i+j)
    return NElemTotal, NMateriales, NElemMaterial, NNod, N1, N2, N3, N4, N5, Conec