import numpy as np 
############################################################# Desarrollo de la matriz de conductividad y la de capacitancia
###############################################################################
def matrizKGyCG (Long1,NElemMaterial,NNod,NElemTotal,NMateriales,TInicial,Cp,rho,Conec,hConvExt,hRadExt,hConvInt,hRadInt,calentado,carga,descarga):
    
    # global KG, CG, dx1, dx2, dx3, dx4, dx5
    
    dx1 = Long1 [0] / NElemMaterial                                                 # Espesor de cada elemento finito del material Sindoform
    dx2 = Long1 [1] / NElemMaterial                                                 # Espesor de cada elemento finito del material Ankerfill
    dx3 = Long1 [2] / NElemMaterial                                                 # Espesor de cada elemento finito del material Resistal
    dx4 = Long1 [3] / NElemMaterial                                                 # Espesor de cada elemento finito del material Silplate
    dx5 = Long1 [4] / NElemMaterial                                                 # Espesor de cada elemento finito del material Acero
    
    KG = np.zeros ((NNod , NNod))
    CG = np.zeros ((NNod , NNod))
    
    for i in range (NElemTotal):                                                                                                                # Bucle para la matriz de conductividad y masa de cada elemento finito
        if 0 * NElemTotal / NMateriales <= i < 1 * NElemTotal / NMateriales:                                                                    # Matrices del material Sindoform
            if i == 0 * NElemTotal / NMateriales:
                ke = np.array (([1,-1],[-1,1])) * ((- 0.0015 * TInicial [i][0] + 4.5 - 0.0015 * TInicial [i+1][0] + 4.5) / 2) / dx1      # Matriz de conductividad
                ce = np.array (([2,1],[1,2])) * (rho [0][i+1]) * (Cp [0][i+1]) * dx1 / 6                                                        # Matriz de capacitancia
                
            elif i != 0 * NElemTotal / NMateriales and i < 1 * NElemTotal / NMateriales - 1:
                ke = np.array (([1,-1],[-1,1])) * ((- 0.0015 * TInicial [i][0] + 4.5 - 0.0015 * TInicial [i+1][0] + 4.5) / 2) / dx1
                ce = np.array (([2,1],[1,2])) * ((rho [0][i] + rho [0][i+1]) / 2) * ((Cp [0][i] + Cp [0][i+1]) / 2) * dx1 / 6
                
            elif i == 1 * NElemTotal / NMateriales - 1:
                ke = np.array (([1,-1],[-1,1])) * ((- 0.0015 * TInicial [i][0] + 4.5 - 0.0015 * TInicial [i+1][0] + 4.5) / 2) / dx1
                ce = np.array (([2,1],[1,2])) * (rho [0][i-1]) * (Cp [0][i-1]) * dx1 / 6
                
       
        
        
        
        elif 1 * NElemTotal / NMateriales <= i <= 2 * NElemTotal / NMateriales - 1:                                                             # Matrices del material Ankerfill
            if i == 1 * NElemTotal / NMateriales:
                ke = np.array (([1,-1],[-1,1])) * ((1.2345 * 10**-6 * TInicial [i][0]**2 - 0.0037380952* TInicial [i][0] + 4.2854285714 + 1.2345 * 10**-6 * 
                                                    TInicial [i+1][0]**2 - 0.0037380952 * TInicial [i+1][0] + 4.2854285714) / 2) / dx2
                ce = np.array (([2,1],[1,2])) * (rho [0][i+1]) * (Cp [0][i+1]) * dx2 / 6
                
            elif i != 1 * NElemTotal / NMateriales and i < 2 * NElemTotal / NMateriales - 1:
                ke = np.array (([1,-1],[-1,1])) * ((1.2345 * 10**-6 * TInicial [i][0]**2 - 0.0037380952* TInicial [i][0] + 4.2854285714 + 1.2345 * 10**-6 * 
                                                    TInicial [i+1][0]**2 - 0.0037380952 * TInicial [i+1][0] + 4.2854285714) / 2) / dx2
                ce = np.array (([2,1],[1,2])) * ((rho [0][i] + rho [0][i+1]) / 2) * ((Cp [0][i] + Cp [0][i+1]) / 2) * dx2 / 6
                
            elif i == 2 * NElemTotal / NMateriales - 1:
                ke = np.array (([1,-1],[-1,1])) * ((1.2345 * 10**-6 * TInicial [i][0]**2 - 0.0037380952* TInicial [i][0] + 4.2854285714 + 1.2345 * 10**-6 * 
                                                    TInicial [i+1][0]**2 - 0.0037380952 * TInicial [i+1][0] + 4.2854285714) / 2) / dx2
                ce = np.array (([2,1],[1,2])) * (rho [0][i-1]) * (Cp [0][i-1]) * dx2 / 6
                
     
        
        
        elif 2 * NElemTotal / NMateriales <= i <= 3 * NElemTotal / NMateriales - 1:                                                             # Matrices del material Resistal
            if i == 2 * NElemTotal / NMateriales:
                ke = np.array (([1,-1],[-1,1])) * ((5.1905 * 10**-7 * TInicial [i][0]**2 - 0.00089404762 * TInicial [i][0] + 1.83028571429 + 5.1905 * 10**-7 * 
                                                    TInicial [i+1][0]**2 - 0.00089404762 * TInicial [i+1][0] + 1.83028571429) / 2) / dx3
                ce = np.array (([2,1],[1,2])) * (rho [0][i+1]) * (Cp [0][i+1]) * dx3 / 6
                
            elif i != 2 * NElemTotal / NMateriales and i < 3 * NElemTotal / NMateriales - 1:
                ke = np.array (([1,-1],[-1,1])) * ((5.1905 * 10**-7 * TInicial [i][0]**2 - 0.00089404762 * TInicial [i][0] + 1.83028571429 + 5.1905 * 10**-7 * 
                                                    TInicial [i+1][0]**2 - 0.00089404762 * TInicial [i+1][0] + 1.83028571429) / 2) / dx3
                ce = np.array (([2,1],[1,2])) * ((rho [0][i] + rho [0][i+1]) / 2) * ((Cp [0][i] + Cp [0][i+1]) / 2) * dx3 / 6
                
            elif i == 3 * NElemTotal / NMateriales - 1:
                ke = np.array (([1,-1],[-1,1])) * ((5.1905 * 10**-7 * TInicial [i][0]**2 - 0.00089404762 * TInicial [i][0] + 1.83028571429 + 5.1905 * 10**-7 * 
                                                    TInicial [i+1][0]**2 - 0.00089404762 * TInicial [i+1][0] + 1.83028571429) / 2) / dx3
                ce = np.array (([2,1],[1,2])) * (rho [0][i-1]) * (Cp [0][i-1]) * dx3 / 6
 
       
        elif 3 * NElemTotal / NMateriales <= i <= 4 * NElemTotal / NMateriales - 1:                                                             # Matrices del material Silplate
            if i == 3 * NElemTotal / NMateriales:
                ke = np.array (([1,-1],[-1,1])) * ((1.438 * 10**-7 * TInicial [i][0]**2 - 0.0000423929 * TInicial [i][0] + 0.1548000000 + 1.438 * 10**-7 * 
                                                    TInicial [i+1][0]**2 - 0.0000423929* TInicial [i+1][0] + 0.1548000000) / 2) / dx4
                ce = np.array (([2,1],[1,2])) * (rho [0][i+1]) * (Cp [0][i+1]) * dx4 / 6
                
            elif i != 3 * NElemTotal / NMateriales and i < 4 * NElemTotal / NMateriales - 1:
                ke = np.array (([1,-1],[-1,1])) * ((1.438 * 10**-7 * TInicial [i][0]**2 - 0.0000423929 * TInicial [i][0] + 0.1548000000 + 1.438 * 10**-7 * 
                                                    TInicial [i+1][0]**2 - 0.0000423929* TInicial [i+1][0] + 0.1548000000) / 2) / dx4
                ce = np.array (([2,1],[1,2])) * ((rho [0][i] + rho [0][i+1]) / 2) * ((Cp [0][i] + Cp [0][i+1]) / 2) * dx4 / 6
                
            elif i == 4 * NElemTotal / NMateriales - 1:
                ke = np.array (([1,-1],[-1,1])) * ((1.438 * 10**-7 * TInicial [i][0]**2 - 0.0000423929 * TInicial [i][0] + 0.1548000000 + 1.438 * 10**-7 * 
                                                    TInicial [i+1][0]**2 - 0.0000423929* TInicial [i+1][0] + 0.1548000000) / 2) / dx4
                ce = np.array (([2,1],[1,2])) * (rho [0][i-1]) * (Cp [0][i-1]) * dx4 / 6
        
              
        
        
        elif 4 * NElemTotal / NMateriales <= i <= 5 * NElemTotal / NMateriales - 1:                                                             # Matrices del material Acero
            ke = np.array (([1,-1],[-1,1])) * ((-0.0437134146 * TInicial [i][0] + 73.9823170732 - 0.0437134146 * TInicial [i+1][0] + 73.9823170732) / 2) / dx5
            ce = np.array (([2,1],[1,2])) * ((rho [0][i] + rho [0][i+1]) / 2) * ((Cp [0][i] + Cp [0][i+1]) / 2) * dx5 / 6
            

            
        for k in range (2):
            for l in range (2):
                KG [int (Conec[i][k])][int (Conec[i][l])] = KG [int (Conec[i][k])][int (Conec[i][l])] + ke [k][l]                               # Ensamble de la matriz de conductividad
                CG [int (Conec[i][k])][int (Conec[i][l])] = CG [int (Conec[i][k])][int (Conec[i][l])] + ce [k][l]                               # Ensamble de la matriz de capacitancia
    
    KG [-1][-1] = KG [-1][-1] + hConvExt + hRadExt                                  # Actualizado del nodo externo con valores de convección y radiación externos
    
    if calentado == 1:                                                              # Switch para calentado
        KG [0][0] = KG [0][0] + hConvInt + hRadInt                                  # Actualizado del nodo interno con valores de convección y radiación internos
        
    elif carga == 1:                                                                # Switch para carga de acero líquido
        KG [0][0] = KG [0][0]                                                       # Actualizado del nodo interno
        
    elif descarga == 1:                                                             # Switch para descarga
        KG [0][0] = KG [0][0] + hConvInt                                            # Actualizado del nodo interno con valores de convección y radiación internos
    return KG, CG, dx1, dx2, dx3, dx4, dx5