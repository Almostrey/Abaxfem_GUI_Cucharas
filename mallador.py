import numpy as np
from pandas import ExcelFile, read_excel
from cv2 import imread, circle, line

NumRef = 18

def leerDatos2 (pathColada):
    path = ExcelFile(pathColada+".xlsx")       # Ruta de archivos Excel
    imagen = imread(pathColada+".jpg", 1)     # Ruta de la imagen
    data = read_excel(path)                                                                                                                                              # Transformacion a matriz
    datos = data.to_numpy()
    MTemp = datos[9:,1:]                                                                                                                                                    # Matriz de temperaturas
    DimTemp = np.shape(MTemp)                                                                                                                                               # Dimension de matriz de temperaturas
    DimImg = np.shape(imagen)                                                                                                                                               # Dimension de la imagen
    datos = 0                                                                                                                                                               # Encerado de la variable auxiliar
    if DimTemp [0] == DimImg [0] and DimTemp [1] == DimImg [1] and DimImg [2] == 3:                                                                                         # Validacion
        return [imagen, MTemp, DimImg]
    else: return False

def procesamientoInicial (imagen, MTemp, DimImg):
    zonaSup = int (0.25 * DimImg [0])                                                               # Limite, en pixeles, para analizar la zona superior
    zonaMed = int (0.65 * DimImg [0])                                                               # Limite, en pixeles, para analizar la zona media
    zonaInf = int (1.00 * DimImg [0])                                                               # Limite, en pixeles, para analizar la zona inferior
    imagen [zonaSup,0:DimImg[1]]=(0,255,0)                                                          # Lineas en las zona superior
    imagen [zonaMed,0:DimImg[1]]=(0,255,0)                                                          # Lineas en las zona media
    imagen [zonaInf - 1,0:DimImg[1]]=(0,255,0)                                                      # Lineas en las zona inferior
    TMaxSup = np.max (MTemp [ :zonaSup , int(0.2 * DimImg [1]) : int(0.8 * DimImg [1])])            # Temperaturas maximas en la zona superior
    TMaxMed = np.max (MTemp [ zonaSup:zonaMed , int(0.2 * DimImg [1]) : int(0.8 * DimImg [1])])     # Temperaturas maximas en la zona media 
    TMaxInf = np.max (MTemp [ zonaMed:zonaInf , int(0.2 * DimImg [1]) : int(0.8 * DimImg [1])])     # Temperaturas maximas en la zona inferior
    
    for i in range (DimImg[0]):                                                                     # Bucle para encerar valores en imagen y matriz de temperaturas
        for j in range (DimImg[1]):
            if i <= zonaSup:                                                                        # Zona superior
                if MTemp [i][j] < TMaxSup * 0.60:                                                   # Valor minimo para comparar
                    MTemp [i][j] = 0
                    imagen [i][j][0] = 0
                    imagen [i][j][1] = 0
                    imagen [i][j][2] = 0
            elif zonaSup <= i < zonaMed:                                                            # Zona media
                if MTemp [i][j] < TMaxMed * 0.70:                                                   # Valor minimo para comparar
                    MTemp [i][j] = 0
                    imagen [i][j][0] = 0
                    imagen [i][j][1] = 0
                    imagen [i][j][2] = 0
            elif zonaMed <= i < zonaInf:                                                            # Zona inferior
                if MTemp [i][j] < TMaxInf * 0.60:                                                   # Valor minimo para comparar
                    MTemp [i][j] = 0
                    imagen [i][j][0] = 0
                    imagen [i][j][1] = 0
                    imagen [i][j][2] = 0
    return [imagen, MTemp, zonaSup , zonaMed , zonaInf]

def mallado (imagen, MTemp, DimImg, zonaSup, zonaMed, zonaInf, pathColada):
    #global I , II , C , ID , D , NumRef
    
    try:                                                                                                                                    # Intenta mallar, si no logra analizar la termografía o los datos, retorna y el programa termina.
        k0 = 0
        k1 = 0
        for i in range (zonaMed , zonaInf , 1):                                                                                             # Bucle para hallar los puntos iniciales para hallar la pendiente
            for j in range (int(DimImg [1] / 2)):
                if MTemp [i][j] != 0 and k0 == 0:
                    PIzqAux = [i , j]                       # Punto izquierdo auxiliar
                    k0 = 1
                elif MTemp [i][-j] != 0 and k1 == 0:
                    PDerAux = [i , DimImg[1]-j]             # Punto derecho auxiliar
                    k1 = 1
                if k0 == k1 == 1:
                    break
            if k0 == k1 == 1:
                break

        k0 = 0
        k1 = 0
        for i in range (zonaMed , zonaInf - 10, 1):                                                                                         # Bucle para hallar los puntos donde inicia la curvatura inferior
            for j in range (int(DimImg [1] / 2)):
                if MTemp [i][j] != 0 and k0 == 0:
                    if MTemp [i+5][j+1] == 0 and MTemp [i+5][j+2] != 0:
                        PiCurvAux = [i , j]                             # Punto izquierdo auxiliar en la curvatura
                        k0 = 1
                elif MTemp [i][-j] != 0 and k1 == 0:
                    if MTemp [i+5][-j-1] == 0 and MTemp [i+5][-j-2] == 0:
                        PdCurvAux = [i , DimImg[1]-j]                   # Punto derecho auxiliar en la curvatura
                        k1 = 1
                if k0 == k1 == 1:
                    break
            if k0 == k1 == 1:
                break
        
        AnilloInferior = PdCurvAux [1] - PiCurvAux [1]                                                                                      # Anillo inferior en pixeles
        DiametroInferior = 2595.9                                                                                                           # Diámetro mayor en la zona de barolado del plano en mm
        AlturaBisel = 2095                                                                                                                  # Altura al bisel desde el diámetro mayor en la zona de barolado del plano en mm
        AlturaBase = 400                                                                                                                    # Altura de la base en mm
        AlturaRefractario = 100                                                                                                             # Altura del refractario en mm
        RelacionAltura = AnilloInferior / DiametroInferior                                                                                  # Relación hallada para corregir la percepcepcion en pixeles / mm
        Bisel = int(AlturaBisel * RelacionAltura)                                                                                           # Tamano del bisel en pixeles
        Base = int(AlturaBase * RelacionAltura)                                                                                             # Tamano de la base en pixeles
        Refractario = int(AlturaRefractario * RelacionAltura)                                                                               # Tamano del refractario

        PcCurvAux = [int((PiCurvAux[0] + PdCurvAux[0])/2) , int((PiCurvAux[1] + PdCurvAux[1])/2)]                                           # Punto central auxiliar en la curvatura
        PCenAux = [int((PIzqAux[0] + PDerAux[0])/2) , int((PIzqAux[1] + PDerAux[1])/2)]                                                     # Punto central auxiliar

        mIzq = (PiCurvAux[1] - PIzqAux[1]) / (PiCurvAux[0] - PIzqAux[0])                                                                    # Pendiente izquierda
        mIIzq = ((PiCurvAux[1] - PIzqAux[1]) / (PiCurvAux[0] - PIzqAux[0]) + (PcCurvAux[1] - PCenAux[1]) / (PcCurvAux[0] - PCenAux[0])) / 2 # Pendiente intermedia izquierda
        mDer = (PdCurvAux[1] - PDerAux[1]) / (PdCurvAux[0] - PDerAux[0])                                                                    # Pendiente Derecha
        mIDer = ((PdCurvAux[1] - PDerAux[1]) / (PdCurvAux[0] - PDerAux[0]) + (PcCurvAux[1] - PCenAux[1]) / (PcCurvAux[0] - PCenAux[0])) / 2 # Pendiente intermedia derecha
        mCen = (PcCurvAux[1] - PCenAux[1]) / (PcCurvAux[0] - PCenAux[0])                                                                    # Pendiente central

        PI1 = [PiCurvAux[0] - Base , int(mIzq * (PiCurvAux[0] - Base - PiCurvAux[0])) + PiCurvAux[1]]                                       # Punto izquierdo (Inferior)
        PC1 = [PcCurvAux[0] - Base + 17, int(mCen * (PcCurvAux[0] - Base - PcCurvAux[0])) + PcCurvAux[1]]                                   # Punto central (Inferior)
        PD1 = [PdCurvAux[0] - Base , int(mDer * (PdCurvAux[0] - Base - PdCurvAux[0])) + PdCurvAux[1]]                                       # Punto derecho (Inferior)
        PII1 = [int((PI1[0] + PC1[0])/2) + 5, int((PI1[1] + PC1[1])/2) - 15]                                                                # Punto intermedio izquierdo (inferior)
        PID1 = [int((PD1[0] + PC1[0])/2) + 5, int((PD1[1] + PC1[1])/2) + 15]                                                                # Punto intermedio derecho (inferior)
        
        a_ = PI1
        b_ = PD1
        c_ = PC1
        d_ = PII1
        e_ = PID1
        I = []                                                                                                                              # Coordenadas izquierdas
        D = []                                                                                                                              # Coordenadas derechas
        C = []                                                                                                                              # Coordenadas centrales
        II = []                                                                                                                             # Coordenadas intermedias izquierdas
        ID = []                                                                                                                             # Coordenadas intermedias derechas
        for i in range (NumRef + 1):                                                                                                        # Bucle para definir coordenadas nodales intermedias
            if i == 0:
                I.append ([PI1[0] ,  PI1[1]]) 
                D.append ([PD1[0] ,  PD1[1]])
                C.append ([PC1[0] ,  PC1[1]])
                II.append ([PII1[0] ,  PII1[1]])
                ID.append ([PID1[0] ,  PID1[1]])
            elif i != 0:
                I.append ([(a_[0] - Refractario) - 1 ,  (mIzq * (a_[0] - Refractario - a_[0]) + a_[1])])
                D.append ([(b_[0] - Refractario) - 1 ,  (mDer * (b_[0] - Refractario - b_[0]) + b_[1])])
                C.append ([(c_[0] - Refractario) - 3.25 ,  (mCen * (c_[0] - Refractario - c_[0]) + c_[1])])
                II.append ([(d_[0] - Refractario) - 2.75 ,  (mIIzq * (d_[0] - Refractario - d_[0]) + d_[1])])
                ID.append ([(e_[0] - Refractario) - 2.75 ,  (mIDer * (e_[0] - Refractario - e_[0]) + e_[1])])
                a_ = I[i]
                b_ = D[i]
                c_ = C[i]
                d_ = II[i]
                e_ = ID[i]

        for i in range (len (I)):                                                                                                           # Bucle para graficar nodos
            circle(imagen, (int (I[i][1]) , int (I[i][0])), 3, (0, 0, 255), -1)
            circle(imagen, (int (D[i][1]) , int (D[i][0])), 3, (0, 0, 255), -1)
            circle(imagen, (int (C[i][1]) , int (C[i][0])), 3, (0, 0, 255), -1)
            circle(imagen, (int (II[i][1]) , int (II[i][0])), 3, (0, 0, 255), -1)
            circle(imagen, (int (ID[i][1]) , int (ID[i][0])), 3, (0, 0, 255), -1)

        for i in range (NumRef + 1):                                                                                                        # Bucle para graficar lineas horizontales de refractarios
            line(imagen , (int (I[i][1]) , int (I[i][0])) , (int (II[i][1]) , int (II[i][0])), (0,0,255) , 1)
            line(imagen , (int (II[i][1]) , int (II[i][0])) , (int (C[i][1]) , int (C[i][0])), (0,0,255) , 1)
            line(imagen , (int (C[i][1]) , int (C[i][0])) , (int (ID[i][1]) , int (ID[i][0])), (0,0,255) , 1)
            line(imagen , (int (ID[i][1]) , int (ID[i][0])) , (int (D[i][1]) , int (D[i][0])), (0,0,255) , 1)

        for i in range (NumRef):                                                                                                            # Bucle para graficar lineas verticales de refractarios
            line(imagen , (int (I[i][1]) , int (I[i][0])) , (int (I[i + 1][1]) , int (I[i + 1][0])), (0,0,255) , 1)
            line(imagen , (int (II[i][1]) , int (II[i][0])) , (int (II[i + 1][1]) , int (II[i + 1][0])), (0,0,255) , 1)
            line(imagen , (int (C[i][1]) , int (C[i][0])) , (int (C[i + 1][1]) , int (C[i + 1][0])), (0,0,255) , 1)
            line(imagen , (int (ID[i][1]) , int (ID[i][0])) , (int (ID[i + 1][1]) , int (ID[i + 1][0])), (0,0,255) , 1)
            line(imagen , (int (D[i][1]) , int (D[i][0])) , (int (D[i + 1][1]) , int (D[i + 1][0])), (0,0,255) , 1)
        return [I , II , C , ID , D]
    except IndexError:                                                                                                                      # Si no logra mallar, indica que termografía tiene problema y el programa termina.
        if pathColada[-1] == 'F':
            print (f'\n\nLa imagen no se pudo procesar, tome una nueva termografía y repita el proceso.\n\n')
        elif pathColada[-1] == 'T':
            print (f'\n\nLa imagen no se pudo procesar, tome una nueva termografía y repita el proceso.\n\n')
        return False

def temperaturasMaximas (MTemp, I, II, C, ID, D):

    global TmaxRef, TmaxZonas, TmaxCuchara

    try:                                                                    # Intenta analizar las temperaturas de cada refractario en funcion de la malla.
        PI = []                                                             # Puntos verticales izquierdos que conectan dos nodos
        PII = []                                                            # Puntos verticales intermedios izquierdos que conectan dos nodos
        PC = []                                                             # Puntos verticales centrales que conectan dos nodos
        PID = []                                                            # Puntos verticales intermedios derechos que conectan dos nodos
        PD = []                                                             # Puntos verticales derechos que conectan dos nodos

        I_II = []                                                           # Puntos horizontales que conectan dos nodos izquierdo - intermedio izquierdo
        II_C = []                                                           # Puntos horizontales que conectan dos nodos intermedio izquierdo - central
        C_ID = []                                                           # Puntos horizontales que conectan dos nodos central - intermedio derecho
        ID_D = []                                                           # Puntos horizontales que conectan dos nodos intemedio derecho - derecho

        for i in range (NumRef):                                            # Bucle para guardado de coordenadas verticales intermedias
            PI.append (intermedios (np.array (([[int(I[i][0]) , int(I[i][1])] , [int (I[i + 1][0]) , int (I[i + 1][1])]]))))
            PII.append (intermedios (np.array (([[int(II[i][0]) , int(II[i][1])] , [int (II[i + 1][0]) , int (II[i + 1][1])]]))))
            PC.append (intermedios (np.array (([[int(C[i][0]) , int(C[i][1])] , [int (C[i + 1][0]) , int (C[i + 1][1])]]))))
            PID.append (intermedios (np.array (([[int(ID[i][0]) , int(ID[i][1])] , [int (ID[i + 1][0]) , int (ID[i + 1][1])]]))))
            PD.append (intermedios (np.array (([[int(D[i][0]) , int(D[i][1])] , [int (D[i + 1][0]) , int (D[i + 1][1])]]))))
        
        for i in range (NumRef):                                            # Bucle para igualado de dimensiones de coordenadas verticales intermedias
            while len (PII [i]) != len (PI [i]):
                PII[i] = np.delete(PII[i],7,0)
            while len (PC [i]) != len (PI [i]):
                PC[i] = np.delete(PC[i],7,0)
            while len (PID [i]) != len (PI [i]):
                PID[i] = np.delete(PID[i],7,0)
            while len (PD [i]) != len (PI [i]):
                PD[i] = np.delete(PD[i],7,0)
        
        for k in range (np.shape(PI)[0]):                                   # Bucle para guardado de coordenadas horizontales intermedias
            for l in range (np.shape(PI)[1]):
                I_II.append (intermedios (np.array(([PI[k][l][0] , PI[k][l][1]] , [PII[k][l][0] , PII[k][l][1]]))))
                II_C.append (intermedios (np.array(([PII[k][l][0] , PII[k][l][1]] , [PC[k][l][0] , PC[k][l][1]]))))
                C_ID.append (intermedios (np.array(([PC[k][l][0] , PC[k][l][1]] , [PID[k][l][0] , PID[k][l][1]]))))
                ID_D.append (intermedios (np.array(([PID[k][l][0] , PID[k][l][1]] , [PD[k][l][0] , PD[k][l][1]]))))
        
        Error2 = 0
    
    except IndexError:                                                      # Si aparece un error de indice en la foto, retorna pidiendo que se suba de nuevo una termografía nueva.
        if pathColada[-1] == 'F':
            print (f'\n\nLa imagen no se pudo procesar, tome una nueva termografía y repita el proceso.\n\n')
        elif pathColada[-1] == 'T':
            print (f'\n\nLa imagen no se pudo procesar, tome una nueva termografía y repita el proceso.\n\n')
        return 'ImagenNoValida'
    ############################################################
    ################### Temperaturas máximas de cada refractario
    ############################################################
    TempTemporal = []                                                   # Vector para guardar temperaturas de cada refractario
    TmaxRef = []                                                        # Vector que guarda la temperatura maxima de cada refractario
    
    k0 = 0
    for k in range (len(I_II)):                                         # Bucle para el lado izquierdo
        k0 = k0 + 1
        for l in range (len(I_II[k])):
            TempTemporal.append (MTemp[I_II[k][l][0]][I_II[k][l][1]])
        if k0 == np.shape(PI)[1] :
            k0 = 0
            TmaxRef.append (max(TempTemporal))
            TempTemporal = []
    
    k0 = 0
    for k in range (len(II_C)):                                         # Bucle para el lado intermedio izquierdo
        k0 = k0 + 1
        for l in range (len(II_C[k])):
            TempTemporal.append (MTemp[II_C[k][l][0]][II_C[k][l][1]])
        if k0 == np.shape(PI)[1] :
            k0 = 0
            TmaxRef.append (max(TempTemporal))
            TempTemporal = []
    
    k0 = 0
    for k in range (len(C_ID)):                                         # Bucle para el lado intermedio derecho
        k0 = k0 + 1
        for l in range (len(C_ID[k])):
            TempTemporal.append (MTemp[C_ID[k][l][0]][C_ID[k][l][1]])
        if k0 == np.shape(PI)[1] :
            k0 = 0
            TmaxRef.append (max(TempTemporal))
            TempTemporal = []
    
    k0 = 0
    for k in range (len(ID_D)):                                         # Bucle para el lado derecho
        k0 = k0 + 1
        for l in range (len(ID_D[k])):
            TempTemporal.append (MTemp[ID_D[k][l][0]][ID_D[k][l][1]])
        if k0 == np.shape(PI)[1] :
            k0 = 0
            TmaxRef.append (max(TempTemporal))
            TempTemporal = []
    
    if pathColada[-1] == 'F':                                                      # Verificador de imagenes frontales
        for k in range (NumRef * 4):                                    # Bucle para almacenaje de temperaturas máximas de cada refractario en la matriz de historicos
            HTmaxRefF [k][-1] = TmaxRef [k]
    
    elif pathColada[-1] == 'T':                                                    # Verificador de imagenes posteriores
        for k in range (NumRef * 4):                                    # Bucle para almacenaje de temperaturas máximas de cada refractario en la matriz de historicos
            HTmaxRefT [k][-1] = TmaxRef [k]
    

    #####################################################
    ################### Temperaturas máximas de cada zona
    #####################################################
    zonas = [1,2,3]
    NoZonas = len (zonas)

    Z1 = []                                                             # Nodos zona 1
    Z2 = []                                                             # Nodos zona 2
    Z3 = []                                                             # Nodos zona 3

    for i in range (6):                                                 # Buclea para definir nodos de zona 1
        Z1.append (12 + i)
        Z1.append (30 + i)
        Z1.append (48 + i)
        Z1.append (66 + i)

    for i in range (5):                                                 # Buclea para definir nodos de zona 2
        Z2.append (7 + i)
        Z2.append (25 + i)
        Z2.append (43 + i)
        Z2.append (61 + i)

    for i in range (7):                                                 # Buclea para definir nodos de zona 3
        Z3.append (0 + i)
        Z3.append (18 + i)
        Z3.append (36 + i)
        Z3.append (54 + i)

    TmaxZonas = np.zeros ((3,1))                                        # Vector que guarda la temperatura máxima de cada zona
    TempTemporal = []                                                   # Vector para guardar temperaturas de cada refractario

    for nodo in Z1:                                                     # Bucle para guardar la temperatura de cada refractario de la zona
        TempTemporal.append (TmaxRef [nodo])
    TmaxZonas [0] = max (TempTemporal)                                  # Guardado de valor máximo de zona 1
    TempTemporal = []

    for nodo in Z2:                                                     # Bucle para guardar la temperatura de cada refractario de la zona
        TempTemporal.append (TmaxRef [nodo])
    TmaxZonas [1] = max (TempTemporal)                                  # Guardado de valor máximo de zona 1
    TempTemporal = []
    
    for nodo in Z3:                                                     # Bucle para guardar la temperatura de cada refractario de la zona
        TempTemporal.append (TmaxRef [nodo])
    TmaxZonas [2] = max (TempTemporal)                                  # Guardado de valor máximo de zona 1
    TempTemporal = []

    if pathColada[-1] == 'F':                                                      # Verificador de imagenes frontales
        for k in range (3):                                             # Bucle para almacenaje de temperaturas máximas de cada zona en la matriz de historicos
            HTmaxZonasF [k][-1] = TmaxZonas [k][0]
    
    elif pathColada[-1] == 'T':                                                    # Verificador de imagenes posteriores
        for k in range (3):                                             # Bucle para almacenaje de temperaturas máximas de cada zona en la matriz de historicos
            HTmaxZonasT [k][-1] = TmaxZonas [k][0]
    
    ####################################################
    ################### Temperatura máxima de la cuchara
    ####################################################
    TmaxCuchara = np.max (MTemp[50:-50 , 50:-50])
    
    if pathColada[-1] == 'F': 
        HTmaxCucharaF [0][-1] = TmaxCuchara                            # Almacenaje de temperaturas máximas de la cuchara en la matriz de historicos
    
    elif pathColada[-1] == 'T':                                                    # Verificador de imagenes posteriores
        HTmaxCucharaT [0][-1] = TmaxCuchara                            # Almacenaje de temperaturas máximas de la cuchara en la matriz de historicos
    return [TmaxRef, TmaxZonas, TmaxCuchara]

def intermedios (extremos):
            
    d0, d1 = np.abs(np.diff(extremos, axis=0))[0]
    if d0 > d1: 
        return np.c_[np.linspace(extremos[0, 0], extremos[1, 0], d0+1, dtype=np.int32), np.round(np.linspace(extremos[0, 1], extremos[1, 1], d0+1)).astype(np.int32)]
    else:
        return np.c_[np.round(np.linspace(extremos[0, 0], extremos[1, 0], d1+1)).astype(np.int32) , np.linspace(extremos[0, 1], extremos[1, 1], d1+1, dtype=np.int32)]

if __name__ =="__main__":
    ColadaACT = 151 # Num termografia a añadir (int)
    Q2 = 1 #Escoria (1:SI 2:NO) (int)
    ColadaCLE = 0 # Num de colada donde se puso la escoria (int)
    cantidadDatos = 0 # Cuantas termografias tiene la campaña (int)
    ColF=[] # Nombre de las coladas anteriores [20, 30, 40]
    ColT=[] # Nombre de las coladas anteriores [20, 30, 40]
    HTmaxRefF=[]
    HTmaxRefT=[]
    HTmaxZonasF=[]
    HTmaxZonasT=[]
    HTmaxCucharaF=[]
    HTmaxCucharaT=[]
    pathColada = "Archivos Fuente/Fotografias y archivos de termografias/151"
    [imagenF, MTempF, DimImgF] = leerDatos2(pathColada+"F")
    [imagenT, MTempT, DimImgT] = leerDatos2(pathColada+"T")
    [imagenF, MTempF, zonaSupF , zonaMedF, zonaInfF] = procesamientoInicial(imagenF, MTempF, DimImgF)
    [imagenT, MTempT, zonaSupT , zonaMedT, zonaInfT] = procesamientoInicial(imagenT, MTempT, DimImgT)
    [IF , IIF , CF , IDF , DF] = mallado (imagenF, MTempF, DimImgF, zonaSupF, zonaMedF, zonaInfF, pathColada+"F")
    [IT , IIT , CT , IDT , DT] = mallado (imagenF, MTempF, DimImgF, zonaSupF, zonaMedF, zonaInfF, pathColada+"T")
    [TmaxRefF, TmaxZonasF, TmaxCucharaF] = temperaturasMaximas(MTempF, IF, IIF, CF, IDF, DF)
    [TmaxRefT, TmaxZonasT, TmaxCucharaT] = temperaturasMaximas(MTempT, IT, IIT, CT, IDT, DT)
