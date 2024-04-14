############################################################################
################### Librerias
from numpy import array, zeros, shape, max, delete, abs, linspace, diff, c_, round, int32, append
from pandas import ExcelFile, read_excel
from cv2 import imread, circle, line, imshow, waitKey, destroyAllWindows, imwrite
import matplotlib.pyplot as plt         # Para hacer graficas
from os import listdir                               # Para leer archivos en carpetas

############################################################################
################### Función principal
def main (numNuevaColada:int, escoria:str, numColadaEscoria:int, cantidadColadas:int, colF:int, colT:int, htmaxcucharaF:float, htmaxcucharaT:float, htmaxzonasF:float, htmaxzonasT:float, htmaxrefF:float, htmaxrefT:float, commonpath:str):
    global verIMG, RT, NT, NumRef, img , FoP , QQ, ColadaACT, Q2, ColadaCLE, cantidadDatos, ColF, ColT, HTmaxCucharaF, HTmaxCucharaT, HTmaxZonasF, HTmaxZonasT, HTmaxRefF, HTmaxRefT, commonPath
    NumRef = 18
    QQ = '2' # Para que ingrese a la funcion
    ColadaACT = numNuevaColada # Numero de colada
    Q2 = escoria # (1: Si hubo escoria, 2: No hubo escoria)
    ColadaCLE = numColadaEscoria # En que colada se hizo la escoria
    cantidadDatos = cantidadColadas # Cuantas coladas tiene la campana
    ColF = colF
    ColT = colT
    HTmaxCucharaF = htmaxcucharaF
    HTmaxCucharaT = htmaxcucharaT
    HTmaxZonasF = htmaxzonasF
    HTmaxZonasT = htmaxzonasT
    HTmaxRefF = htmaxrefF
    HTmaxRefT = htmaxrefT
    commonPath = commonpath
    NT = 'si'
    RT = 'no'

    verif = 'no'
    while verif == 'no':                                                                                                                    # Verificacion del input del usuario de la pregunta principal
        
        if QQ == '2':                                                                                                                       # Añadir una nueva termografía 
            verIMG = 0   
            verif = 'si'

            preguntasIniciales2 ()                                                                                                          # Preguntas de si se desea añadir una nueva colada o analisar las previas
            IniciadoMatricesHistoricos2 ()                                                                                                  # Inicializado de matrices donde se guardaran los historicos de temperatura de la cuchara, de las zonas, y de los refractarios.

            FoP = 'F'
            leerDatos2 ()                                                                                                                   # Función para leer los datos del excel de temperaturas y de la imagen
            if validacion == 0:
                #########################################
                #########################################
                #########################################
                #########################################
                #########################################
                #########################################
                #########################################
                #########################################
                pass
            procesamientoInicial ()                                                                                                         # Elimina valores de temperatura muy bajos en la imagen 
            if mallado () == 'ImagenNoValida':                                                                                              # Realiza el mallado de la imagen detectando la curvatura inferior, realiza una recta corregida por proporciones y calculando las pendientes verticales
                return                                                                                                                      # Si no logra mallar retorna y el programa termina.
            if temperaturasMaximas () == 'ImagenNoValida':                                                                                  # Halla las temperaturas máximas de cada refractario, de cada zona y de la cuchara.
                return                                                                                                                      # Si no logra evaluar las temperaturas de cada termografía retorna indicando que ftermografía actualizar.
            FoP = 'T'
            leerDatos2 ()                                                                                                                   # Función para leer los datos del excel de temperaturas y de la imagen
            if validacion == 0:
                #########################################
                #########################################
                #########################################
                #########################################
                #########################################
                #########################################
                #########################################
                #########################################
                pass
            procesamientoInicial ()                                                                                                         # Elimina valores de temperatura muy bajos en la imagen 
            if mallado () == 'ImagenNoValida':                                                                                              # Realiza el mallado de la imagen detectando la curvatura inferior, realiza una recta corregida por proporciones y calculando las pendientes verticales
                return                                                                                                                      # Si no logra mallar retorna y el programa termina.
            if temperaturasMaximas () == 'ImagenNoValida':                                                                                  # Halla las temperaturas máximas de cada refractario, de cada zona y de la cuchara.
                return                                                                                                                      # Si no logra evaluar las temperaturas de cada termografía retorna indicando que ftermografía actualizar.
            maxZonasF = [HTmaxZonasF[0][1], HTmaxZonasF[1][1], HTmaxZonasF[2][1]]
            maxZonasT = [HTmaxZonasT[0][1], HTmaxZonasT[1][1], HTmaxZonasT[2][1]]
            tempRefractariosF=[]
            tempRefractariosT=[]
            for i in range(72):
                tempRefractariosF.append(HTmaxRefF[i][1])
                tempRefractariosT.append(HTmaxRefT[i][1])
            try:
                datosF = [tempRefractariosF, maxZonasF, HTmaxCucharaF[0][1]]
                datosT = [tempRefractariosT, maxZonasT, HTmaxCucharaT[0][1]]
            except:
                datosF = [tempRefractariosF, maxZonasF, HTmaxCucharaF[0][0]]
                datosT = [tempRefractariosT, maxZonasT, HTmaxCucharaT[0][0]]
            return [datosF, datosT]

        elif QQ == '1':                                                                                                                     # Ver historico 
            verif = 'si'

            numTermografias ()                                                                                                              # Función para verificar cuantas coladas se tiene disponibles 
            preguntasIniciales1 ()                                                                                                          # Preguntas de si se desea añadir una nueva colada o analisar las previas
            IniciadoMatricesHistoricos1 ()                                                                                                  # Inicializado de matrices donde se guardaran los historicos de temperatura de la cuchara, de las zonas, y de los refractarios.

            verIMG = 0   
            FoP = 'F'                                                                                                                       # Verificador para trabajar imagenes frontales
            for img in range (NumImF):                                                                                                      # Bucle para imagenes frontales
                leerDatos1 ()                                                                                                               # Función para leer los datos del excel de temperaturas y de la imagen
                procesamientoInicial ()                                                                                                     # Elimina valores de temperatura muy bajos en la imagen 
                if mallado () == 'ImagenNoValida':                                                                                          # Realiza el mallado de la imagen detectando la curvatura inferior, realiza una recta corregida por proporciones y calculando las pendientes verticales
                    return                                                                                                                  # Si no logra mallar retorna y el programa termina.
                if temperaturasMaximas () == 'ImagenNoValida':                                                                              # Halla las temperaturas máximas de cada refractario, de cada zona y de la cuchara.
                    return                                                                                                                  # Si no logra evaluar las temperaturas de cada termografía retorna indicando que ftermografía actualizar.
                #visgraf ()                                                                                                                 # Función para ver la malla realizada 

            verIMG = 0   
            FoP = 'T'                                                                                                                       # Verificador para trabajar imagenes posteriores
            for img in range (NumImT):                                                                                                      # Bucle para imagenes posteriores
                leerDatos1 ()                                                                                                               # Función para leer los datos del excel de temperaturas y de la imagen
                procesamientoInicial ()                                                                                                     # Elimina valores de temperatura muy bajos en la imagen 
                if mallado () == 'ImagenNoValida':                                                                                          # Realiza el mallado de la imagen detectando la curvatura inferior, realiza una recta corregida por proporciones y calculando las pendientes verticales
                    return                                                                                                                  # Si no logra mallar retorna y el programa termina.
                if temperaturasMaximas () == 'ImagenNoValida':                                                                              # Halla las temperaturas máximas de cada refractario, de cada zona y de la cuchara.
                    return                                                                                                                  # Si no logra evaluar las temperaturas de cada termografía retorna indicando que ftermografía actualizar.
                #visgraf ()                                                                                                                 # Función para ver la malla realizada 

            preguntasRespuesta ()                                                                                                           # Realiza preguntas al usuario para entregar una salida

    #print ('\n\n        Gracias.\n\n')
    
############################################################################
################### Función para hallar el numero de termografias a analizar
def numTermografias ():

    global ColF , ColT , NumImF , NumImT
    
    ColF = []                                                                                                                               # Coladas disponibles para análisis (Imagen frontal)
    ColT = []                                                                                                                               # Coladas disponibles para análisis (Imagen posterior)
    NumImF = 0                                                                                                                              # Número de imagenes frontales
    NumImT = 0                                                                                                                              # Número de imagenes posteriores 

    archivos = listdir("Archivos Fuente/Fotografias y archivos de termografias") 
    for i in range (len(archivos)):                                                                                                         # Bucle para leer todos los archivos de la carpeta 
        if archivos [i][-1] == 'x' and archivos [i][-2] == 's' and archivos [i][-3] == 'l' and archivos [i][-4] == 'x'and archivos [i][-5] == '.':
            if archivos [i][-6] == 'F':
                ColF.append (int(archivos [i].replace('F.xlsx' , '')))
            elif archivos [i][-6] == 'T':
                ColT.append (int(archivos [i].replace('T.xlsx' , '')))
    
    NumImF = len (ColF)                                                                                                                     # Número de coladas frontales en archivo
    NumImT = len (ColT)                                                                                                                     # Número de coladas posteriores en archivo

############################################################################
################### Función para realizar preguntas al usuario para que ingrese información necesaria en la ruta 1
def preguntasIniciales1 ():

    global ColadaCLE , ColadaACT , NT , RT

    verif = 'no'
    while verif == 'no':                                                                                                                    # Verificacion del input del usuario de la pregunta principal
        Q1 = input ('Seleccione 1 o 2. \n1) Anadir una nueva termografía. \n2) Revisar termografias previas.\n          ')
        
        if Q1 == '1':                                                                                                                       # Añadir una nueva termografía 
            NT = 'si'
            RT = 'no'
            verif = 'si'
        
        elif Q1 == '2':                                                                                                                     # Ver historico 
            RT = 'si'
            NT = 'no'
            verif = 'si'

    verif = 'no'
    if Q1 == '1':                                                                                                                           # Ingrese el número de colada actual 
        while verif == 'no':
            try:
                ColadaACT = int (input ('\nIngrese el numero de colada de la termografia que  se desea anadir.\n          '))
            except ValueError:
                verif = 'no'
            if ColadaACT > 0:
                verif = 'si'

    elif Q1 == '2':                                                                                                                         # Colada actual no ingresada, colada actual = 0 
        ColadaACT = 0

    verif = 'no'
    while verif == 'no':                                                                                                                    # Hubo o no cambio de línea de escoria? 
        Q2 = input ('\nSeleccione 1 o 2. \n1) SI se realizo cambio de linea de escoria previamente. \n2) NO se realizo cambio de linea de escoria previamente.\n          ')
        if Q2 == '1' or Q2 == '2':
            verif = 'si'
    
    verif = 'no'
    if Q2 == '1':                                                                                                                           # Colada en la que se realizó el cambio de línea de escoria 
        while verif == 'no':
            try:
                ColadaCLE = int (input ('\nEn que colada se lo realizo?\n          '))
            except ValueError:
                verif = 'no'
            if ColadaCLE > 0:
                verif = 'si'

    elif Q2 == '2':                                                                                                                         # No hubo cambio de línea de escoria, colada cambio línea de escoria = 0
        ColadaCLE = 0

############################################################################
################### Función para realizar preguntas al usuario para que ingrese información necesaria en la ruta 2
def preguntasIniciales2 ():

    global ColadaCLE , ColadaACT , NT , RT , cantidadDatos
    
    verif = 'no'
    while verif == 'no':
        try:
            pass
            #ColadaACT = int (input ('\nIngrese el numero de colada de la termografia que  se desea anadir.\n          '))
        except ValueError:
            verif = 'no'
        if ColadaACT > 0:
            verif = 'si'

    verif = 'no'
    while verif == 'no':                                                                                                                    # Hubo o no cambio de línea de escoria? 
        #Q2 = input ('\nSeleccione 1 o 2. \n1) SI se realizo cambio de linea de escoria previamente. \n2) NO se realizo cambio de linea de escoria previamente.\n          ')
        if Q2 == '1' or Q2 == '2':
            verif = 'si'
    
    verif = 'no'
    if Q2 == '1':                                                                                                                           # Colada en la que se realizó el cambio de línea de escoria 
        while verif == 'no':
            try:
                pass
                #ColadaCLE = int (input ('\nEn que colada se lo realizo?\n          '))
            except ValueError:
                verif = 'no'
            if ColadaCLE > 0:
                verif = 'si'

    elif Q2 == '2':                                                                                                                         # No hubo cambio de línea de escoria, colada cambio línea de escoria = 0
        ColadaCLE = 0

    verif = 'no'
    while verif == 'no':                                                                                                                # Cantidad de datos del historico
        try:
            pass
            #cantidadDatos = int (input ('\nCuantos datos de temperatura tiene el historico?\n          '))
        except ValueError:
            verif = 'no'
        if cantidadDatos >= 0:
            verif = 'si'

############################################################################
################### Función para realizar preguntas al usuario para que ingrese informacióon necesaria
def IniciadoMatricesHistoricos1 (): 

    global HTmaxRefF , HTmaxRefT , HTmaxZonasF , HTmaxZonasT , HTmaxCucharaF , HTmaxCucharaT , NumRef

    NumRef = 18
    
    HTmaxRefF = zeros ((NumRef * 4 , NumImF))                                    # Matriz que almacena historico de datos máximos de temperatura de cada refractaio en imagenes frontales
    HTmaxRefT = zeros ((NumRef * 4 , NumImT))                                    # Matriz que almacena historico de datos máximos de temperatura de cada refractaio en imagenes posteriores

    HTmaxZonasF  = zeros ((3 , NumImF))                                          # Matriz que almacena historico de datos máximos de temperatura de cada zona en imagenes frontales
    HTmaxZonasT  = zeros ((3 , NumImT))                                          # Matriz que almacena historico de datos máximos de temperatura de cada zona en imagenes posteriores

    HTmaxCucharaF  = zeros ((1 , NumImF))                                        # Matriz que almacena historico de datos máximos de temperatura de la cuchara en imagenes frontales
    HTmaxCucharaT  = zeros ((1 , NumImT))                                        # Matriz que almacena historico de datos máximos de temperatura de la cuchara en imagenes posteriores
    
############################################################################
################### Función para realizar preguntas al usuario para que ingrese informacióon necesaria
def IniciadoMatricesHistoricos2 (): 

    global HTmaxRefF , HTmaxRefT , HTmaxZonasF , HTmaxZonasT , HTmaxCucharaF , HTmaxCucharaT , NumRef , ColF , ColT

    NumRef = 18
    
    '''
    ColF = np.zeros ((1 , cantidadDatos + 1))
    HTmaxRefF = np.zeros ((NumRef * 4 , cantidadDatos + 1))                                         # Matriz que almacena historico de datos máximos de temperatura de cada refractaio en imagenes frontales
    HTmaxRefT = np.zeros ((NumRef * 4 , cantidadDatos + 1))                                         # Matriz que almacena historico de datos máximos de temperatura de cada refractaio en imagenes posteriores

    HTmaxZonasF  = np.zeros ((3 , cantidadDatos + 1))                                               # Matriz que almacena historico de datos máximos de temperatura de cada zona en imagenes frontales
    HTmaxZonasT  = np.zeros ((3 , cantidadDatos + 1))                                               # Matriz que almacena historico de datos máximos de temperatura de cada zona en imagenes posteriores

    HTmaxCucharaF  = np.zeros ((1 , cantidadDatos + 1))                                         # Matriz que almacena historico de datos máximos de temperatura de la cuchara en imagenes frontales
    HTmaxCucharaT  = np.zeros ((1 , cantidadDatos + 1))                                         # Matriz que almacena historico de datos máximos de temperatura de la cuchara en imagenes posteriores
    
    

    if cantidadDatos > 0:
        ColF = np.zeros ((1 , cantidadDatos + 1))                                               # Vector para almacenar las coladas ingresadas manualmente y la actual

        for i in range (cantidadDatos + 1):
            if i != cantidadDatos:
                ColF [0][i] = int (input (f'Ingrese el número de colada frontal del dato {i+1}: '))
                HTmaxCucharaF [0][i] = float (input (f'Ingrese el valor de temperatura frontal del dato {i+1}: '))
                for j in range (3):
                    HTmaxZonasF [j][i] = float (input (f'Ingrese el valor de temperatura de la zona {j+1}, del frontal, del dato {i+1}: '))
                
                for k in range (NumRef * 4):
                    HTmaxRefF [k][i] = float (input (f'Ingrese el valor de temperatura del refractario {k+1}, del frontal, del dato {i+1}: '))
            elif i == cantidadDatos:
                ColF [0][i] = ColadaACT
            
    elif cantidadDatos == 0:
        ColF = np.zeros ((1 , cantidadDatos + 1))
        ColF [0][-1] = ColadaACT'''
    '''    
    if cantidadDatos > 0:
        ColT = np.zeros ((1 , cantidadDatos + 1))                                               # Vector para almacenar las coladas ingresadas manualmente y la actual

        for i in range (cantidadDatos + 1):
            if i != cantidadDatos:
                ColT [0][i] = int (input (f'Ingrese el número de colada posterior del dato {i+1}: '))
                HTmaxCucharaT [0][i] = float (input (f'Ingrese el valor de temperatura posterior del dato {i+1}: '))
                
                for j in range (3):
                    HTmaxZonasT [j][i] = float (input (f'Ingrese el valor de temperatura de la zona {j+1}, posterior, del dato {i+1}: '))
                
                for k in range (NumRef * 4):
                    HTmaxRefT [k][i] = float (input (f'Ingrese el valor de temperatura del refractario {j+1}, posterior, del dato {i+1}: '))
                
                
            elif i == cantidadDatos:
                ColT [0][i] = ColadaACT
            
    elif cantidadDatos == 0:
        ColT = np.zeros ((1 , cantidadDatos + 1))
        ColT [0][-1] = ColadaACT'''

############################################################################
################### Función para leer archivos excel, imagenes y validar dimensiones
def leerDatos1 ():

    global imagen ,MTemp , validacion , DimTemp , DimImg
    
    if FoP == 'F':
        path = ExcelFile(f"Archivos Fuente/Fotografias y archivos de termografias/{ColF[img]}F.xlsx")      # Ruta de archivos Excel
        imagen = imread(f"Archivos Fuente/Fotografias y archivos de termografias/{ColF[img]}F.jpg", 1)    # Ruta de la imagen
        print ('Analizando imagen frontal No. ' , ColF[img])

    elif FoP == 'T':                                                                                                                                                # Verificador de imagenes posteriores
        path = ExcelFile(f"Archivos Fuente/Fotografias y archivos de termografias/{ColT[img]}T.xlsx")      # Ruta de archivos Excel
        imagen = imread(f"Archivos Fuente/Fotografias y archivos de termografias/{ColT[img]}T.jpg", 1)    # Ruta de la imagen
        print ('Analizando imagen posterior No. ' , ColT[img])

    data = read_excel(path)                                                                                                                                      # Transformacion a matriz
    datos = data.to_numpy()

    MTemp = datos[9:,1:]                                                                                                                                            # Matriz de temperaturas

    DimTemp = shape(MTemp)                                                                                                                                       # Dimension de matriz de temperaturas
    DimImg = shape(imagen)                                                                                                                                       # Dimension de la imagen

    datos = 0                                                                                                                                                       # Encerado de la variable auxiliar

    if DimTemp [0] == DimImg [0] and DimTemp [1] == DimImg [1] and DimImg [2] == 3:                                                                                 # Validacion
        validacion = 1
    else:
        validacion = 0
        return validacion

############################################################################
################### Función para leer archivos excel, imagenes y validar dimensiones
def leerDatos2 ():

    global imagen ,MTemp , validacion , DimTemp , DimImg, commonPath
    
    if FoP == 'F':
        path = ExcelFile(commonPath+"F.xlsx")       # Ruta de archivos Excel
        imagen = imread(commonPath+"F.jpg", 1)     # Ruta de la imagen
        #print ('Analizando imagen frontal No. ' , int(ColF[0][-1]))

    elif FoP == 'T':                                                                                                                                                        # Verificador de imagenes posteriores
        path = ExcelFile(commonPath+"T.xlsx")       # Ruta de archivos Excel
        imagen = imread(commonPath+"T.jpg", 1)     # Ruta de la imagen
        #print ('Analizando imagen posterior No. ' , int(ColT[0][-1]))

    data = read_excel(path)                                                                                                                                              # Transformacion a matriz
    datos = data.to_numpy()

    MTemp = datos[9:,1:]                                                                                                                                                    # Matriz de temperaturas

    DimTemp = shape(MTemp)                                                                                                                                               # Dimension de matriz de temperaturas
    DimImg = shape(imagen)                                                                                                                                               # Dimension de la imagen

    datos = 0                                                                                                                                                               # Encerado de la variable auxiliar

    if DimTemp [0] == DimImg [0] and DimTemp [1] == DimImg [1] and DimImg [2] == 3:                                                                                         # Validacion
        validacion = 1
    else:
        validacion = 0
        return validacion

############################################################################
################### Función para procesar la imagen
def procesamientoInicial ():

    global zonaSup , zonaMed , zonaInf

    zonaSup = int (0.25 * DimImg [0])                                                               # Limite, en pixeles, para analizar la zona superior
    zonaMed = int (0.65 * DimImg [0])                                                               # Limite, en pixeles, para analizar la zona media
    if QQ == '1' and FoP == 'T':
        zonaMed = int (0.80 * DimImg [0])                                                           # Limite, en pixeles, para analizar la zona media
    zonaInf = int (1.00 * DimImg [0])                                                               # Limite, en pixeles, para analizar la zona inferior
    
    TMaxSup = max (MTemp [ int (0.3 * zonaSup):zonaSup , int(0.20 * DimImg [1]) : int(0.80 * DimImg [1])])           # Temperaturas maximas en la zona superior
    TMaxMed = max (MTemp [ zonaSup : zonaMed , int(0.20 * DimImg [1]) : int(0.80 * DimImg [1])])                     # Temperaturas maximas en la zona media 
    TMaxInf = max (MTemp [ zonaMed : int(0.90 * zonaInf) , int(0.20 * DimImg [1]) : int(0.80 * DimImg [1])])         # Temperaturas maximas en la zona inferior
    
    imagen [int (0.3 * zonaSup),0:DimImg[1]]=(255,0,0)
    imagen [zonaSup,0:DimImg[1]]=(255,0,0)
    imagen [zonaMed,0:DimImg[1]]=(0,255,0)
    imagen [int(0.90 * zonaInf),0:DimImg[1]]=(0,0,255)

    if verIMG == 1:
        visgraf ()
    
    pctjElim = 0.05                                                                                 # Porcentaje de eliminación de datos laterales        
    imagen [0:DimImg[0] , int (DimImg[1] * pctjElim)]=(0,0,255)                                     # Líneas verticales 
    imagen [0:DimImg[0] , int (-DimImg[1] * pctjElim)]=(0,0,255)                                    # Líneas verticales 
    for i in range (DimImg[0]):
        for j in range (int (DimImg[1] * pctjElim)):
            MTemp [i][j] = 0
            MTemp [i][-j] = 0
            
            imagen [i][j][0] = 0
            imagen [i][j][1] = 0
            imagen [i][j][2] = 0
            
            imagen [i][-j][0] = 0
            imagen [i][-j][1] = 0
            imagen [i][-j][2] = 0
    
    if verIMG == 1:
        visgraf ()
    
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
                if MTemp [i][j] < TMaxInf * 0.55:                                                   # Valor minimo para comparar
                    MTemp [i][j] = 0
                    imagen [i][j][0] = 0
                    imagen [i][j][1] = 0
                    imagen [i][j][2] = 0
    if verIMG == 1:
        visgraf ()
    
############################################################################
################### Función para definir el mallado a usar
def mallado ():

    global I , II , C , ID , D , NumRef

    try:                                                                                                                                    # Intenta mallar, si no logra analizar la termografía o los datos, retorna y el programa termina.
        k0 = 0
        k1 = 0
        for i in range (zonaMed , zonaInf , 1):                                                                                             # Bucle para hallar los puntos iniciales para hallar la pendiente
            for j in range (int(DimImg [1] / 3)):
                if MTemp [i][j] != 0 and k0 == 0:
                    PIzqAux = [i , j]                       # Punto izquierdo auxiliar
                    k0 = 1
                if MTemp [i][-j] != 0 and k1 == 0:
                    PDerAux = [i , DimImg[1]-j]             # Punto derecho auxiliar
                    k1 = 1
                if k0 == k1 == 1:
                    break
            if k0 == k1 == 1:
                break
        line(imagen , (PIzqAux[1],PIzqAux[0]) , (PDerAux[1],PDerAux[0]), (0,0,255) , 1)
        
        if verIMG == 1:
            visgraf ()
        
        k0 = 0
        k1 = 0
        for i in range (zonaMed , zonaInf - 2, 1):                                                                                         # Bucle para hallar los puntos donde inicia la curvatura inferior
            for j in range (int(DimImg [1] / 3)):
                if MTemp [i-10][j-5] == 0 and MTemp [i][j-20] == 0 and MTemp [i][j-17] == 0 and MTemp [i][j-15] == 0 and MTemp [i][j-9] == 0 and MTemp [i][j-4] == 0 and MTemp [i][j-3] == 0 and MTemp [i][j-2] == 0 and MTemp [i][j-1] == 0:
                    if k0 == 0 and MTemp [i-1][j] != 0 and MTemp [i][j] == 0 and MTemp [i+1][j] == 0 and MTemp [i][j+1] != 0 and MTemp [i+1][j+1] != 0 and MTemp [i+2][j+1] == 0:
                        PiCurvAux = [i , j]                             # Punto izquierdo auxiliar en la curvatura
                        k0 = 1
                        
                if MTemp [i-10][-j+5] == 0 and MTemp [i][-j+20] == 0 and MTemp [i][-j+17] == 0 and MTemp [i][-j+15] == 0 and MTemp [i][-j+9] == 0 and MTemp [i][-j+4] == 0 and MTemp [i][-j+3] == 0 and MTemp [i][-j+2] == 0 and MTemp [i][-j+1] == 0:
                    if k1 == 0 and MTemp [i-1][-j] != 0 and MTemp [i][-j] == 0 and MTemp [i+1][-j] == 0 and MTemp [i][-j-1] != 0 and MTemp [i+1][-j-1] != 0 and MTemp [i+2][-j-1] == 0:
                        PdCurvAux = [i , DimImg[1]-j]                   # Punto derecho auxiliar en la curvatura
                        k1 = 1
                                                
                if k0 == k1 == 1:
                    break
            if k0 == k1 == 1:
                break
        line(imagen , (PiCurvAux[1],PiCurvAux[0]) , (PdCurvAux[1],PdCurvAux[0]), (0,0,255) , 1)
        
        if verIMG == 1:
            visgraf ()
        
        AnilloInferior = PdCurvAux [1] - PiCurvAux [1]                                                                                      # Anillo inferior en pixeles
        DiametroInferior = 2595.9                     # plano novacero (Acero)                                                              # Diámetro mayor en la zona de barolado del plano en mm
        AlturaBisel = 2095                            # plano novacero (Linea de barolado a bisel superior, 2645-250-100-200)                                                                                              # Altura al bisel desde el diámetro mayor en la zona de barolado del plano en mm
        AlturaBase = 400                              # plano de refractarios RHI (434 + 40)                                                # Altura de la base en mm
        AlturaRefractario = 100                       # Respuesta novacero                                                                  # Altura del refractario en mm
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
        
        if verIMG == 1:
            visgraf ()
        
        for i in range (NumRef + 1):                                                                                                        # Bucle para graficar lineas horizontales de refractarios
            line(imagen , (int (I[i][1]) , int (I[i][0])) , (int (II[i][1]) , int (II[i][0])), (0,0,255) , 1)
            line(imagen , (int (II[i][1]) , int (II[i][0])) , (int (C[i][1]) , int (C[i][0])), (0,0,255) , 1)
            line(imagen , (int (C[i][1]) , int (C[i][0])) , (int (ID[i][1]) , int (ID[i][0])), (0,0,255) , 1)
            line(imagen , (int (ID[i][1]) , int (ID[i][0])) , (int (D[i][1]) , int (D[i][0])), (0,0,255) , 1)
        
        if verIMG == 1:
            visgraf ()
        
        for i in range (NumRef):                                                                                                            # Bucle para graficar lineas verticales de refractarios
            line(imagen , (int (I[i][1]) , int (I[i][0])) , (int (I[i + 1][1]) , int (I[i + 1][0])), (0,0,255) , 1)
            line(imagen , (int (II[i][1]) , int (II[i][0])) , (int (II[i + 1][1]) , int (II[i + 1][0])), (0,0,255) , 1)
            line(imagen , (int (C[i][1]) , int (C[i][0])) , (int (C[i + 1][1]) , int (C[i + 1][0])), (0,0,255) , 1)
            line(imagen , (int (ID[i][1]) , int (ID[i][0])) , (int (ID[i + 1][1]) , int (ID[i + 1][0])), (0,0,255) , 1)
            line(imagen , (int (D[i][1]) , int (D[i][0])) , (int (D[i + 1][1]) , int (D[i + 1][0])), (0,0,255) , 1)
        
        if verIMG == 1 or verIMG == 2:
            visgraf ()
        
    except IndexError and UnboundLocalError:                                                                                                                      # Si no logra mallar, indica que termografía tiene problema y el programa termina.
        if FoP == 'F':
            print (f'\n\nLa imagen perteneciente a la colada No. {ColF[img]} no se pudo procesar, tome una nueva termografía y repita el proceso.\n\n')
        elif FoP == 'P':
            print (f'\n\nLa imagen perteneciente a la colada No. {ColT[img]} no se pudo procesar, tome una nueva termografía y repita el proceso.\n\n')
        return 'ImagenNoValida'

############################################################################
################### Función para evaluar las temperaturas de cada refractario
def temperaturasMaximas ():

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
            PI.append (intermedios (array (([[int(I[i][0]) , int(I[i][1])] , [int (I[i + 1][0]) , int (I[i + 1][1])]]))))
            PII.append (intermedios (array (([[int(II[i][0]) , int(II[i][1])] , [int (II[i + 1][0]) , int (II[i + 1][1])]]))))
            PC.append (intermedios (array (([[int(C[i][0]) , int(C[i][1])] , [int (C[i + 1][0]) , int (C[i + 1][1])]]))))
            PID.append (intermedios (array (([[int(ID[i][0]) , int(ID[i][1])] , [int (ID[i + 1][0]) , int (ID[i + 1][1])]]))))
            PD.append (intermedios (array (([[int(D[i][0]) , int(D[i][1])] , [int (D[i + 1][0]) , int (D[i + 1][1])]]))))
        
        for i in range (NumRef):                                            # Bucle para igualado de dimensiones de coordenadas verticales intermedias
            while len (PII [i]) != len (PI [i]):
                PII[i] = delete(PII[i],7,0)
            while len (PC [i]) != len (PI [i]):
                PC[i] = delete(PC[i],7,0)
            while len (PID [i]) != len (PI [i]):
                PID[i] = delete(PID[i],7,0)
            while len (PD [i]) != len (PI [i]):
                PD[i] = delete(PD[i],7,0)
        
        for k in range (shape(PI)[0]):                                   # Bucle para guardado de coordenadas horizontales intermedias
            for l in range (shape(PI)[1]):
                I_II.append (intermedios (array(([PI[k][l][0] , PI[k][l][1]] , [PII[k][l][0] , PII[k][l][1]]))))
                II_C.append (intermedios (array(([PII[k][l][0] , PII[k][l][1]] , [PC[k][l][0] , PC[k][l][1]]))))
                C_ID.append (intermedios (array(([PC[k][l][0] , PC[k][l][1]] , [PID[k][l][0] , PID[k][l][1]]))))
                ID_D.append (intermedios (array(([PID[k][l][0] , PID[k][l][1]] , [PD[k][l][0] , PD[k][l][1]]))))
        
        Error2 = 0
    
    except IndexError:                                                      # Si aparece un error de indice en la foto, retorna pidiendo que se suba de nuevo una termografía nueva.
        if FoP == 'F':
            print (f'\n\nLa imagen perteneciente a la colada No. {ColF[img]} no se pudo procesar, tome una nueva termografía y repita el proceso.\n\n')
        elif FoP == 'P':
            print (f'\n\nLa imagen perteneciente a la colada No. {ColT[img]} no se pudo procesar, tome una nueva termografía y repita el proceso.\n\n')
        return 'ImagenNoValida'
    
    if QQ == '1':
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
            if k0 == shape(PI)[1] :
                k0 = 0
                TmaxRef.append (max(TempTemporal))
                TempTemporal = []
        
        k0 = 0
        for k in range (len(II_C)):                                         # Bucle para el lado intermedio izquierdo
            k0 = k0 + 1
            for l in range (len(II_C[k])):
                TempTemporal.append (MTemp[II_C[k][l][0]][II_C[k][l][1]])
            if k0 == shape(PI)[1] :
                k0 = 0
                TmaxRef.append (max(TempTemporal))
                TempTemporal = []
        
        k0 = 0
        for k in range (len(C_ID)):                                         # Bucle para el lado intermedio derecho
            k0 = k0 + 1
            for l in range (len(C_ID[k])):
                TempTemporal.append (MTemp[C_ID[k][l][0]][C_ID[k][l][1]])
            if k0 == shape(PI)[1] :
                k0 = 0
                TmaxRef.append (max(TempTemporal))
                TempTemporal = []
        
        k0 = 0
        for k in range (len(ID_D)):                                         # Bucle para el lado derecho
            k0 = k0 + 1
            for l in range (len(ID_D[k])):
                TempTemporal.append (MTemp[ID_D[k][l][0]][ID_D[k][l][1]])
            if k0 == shape(PI)[1] :
                k0 = 0
                TmaxRef.append (max(TempTemporal))
                TempTemporal = []
        
        if FoP == 'F':                                                      # Verificador de imagenes frontales
            for k in range (NumRef * 4):                                    # Bucle para almacenaje de temperaturas máximas de cada refractario en la matriz de historicos
                HTmaxRefF [k][img] = TmaxRef [k]
        
        elif FoP == 'T':                                                    # Verificador de imagenes posteriores
            for k in range (NumRef * 4):                                    # Bucle para almacenaje de temperaturas máximas de cada refractario en la matriz de historicos
                HTmaxRefT [k][img] = TmaxRef [k]
        

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

        TmaxZonas = zeros ((3,1))                                        # Vector que guarda la temperatura máxima de cada zona
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

        if FoP == 'F':                                                      # Verificador de imagenes frontales
            for k in range (3):                                             # Bucle para almacenaje de temperaturas máximas de cada zona en la matriz de historicos
                HTmaxZonasF [k][img] = TmaxZonas [k][0]
        
        elif FoP == 'T':                                                    # Verificador de imagenes posteriores
            for k in range (3):                                             # Bucle para almacenaje de temperaturas máximas de cada zona en la matriz de historicos
                HTmaxZonasT [k][img] = TmaxZonas [k][0]

        ####################################################
        ################### Temperatura máxima de la cuchara
        ####################################################
        TmaxCuchara = max(TmaxRef)

        if FoP == 'F':                                                      # Verificador de imagenes frontales
            HTmaxCucharaF [0][img] = TmaxCuchara                            # Almacenaje de temperaturas máximas de la cuchara en la matriz de historicos
        elif FoP == 'T':                                                    # Verificador de imagenes posteriores
            HTmaxCucharaT [0][img] = TmaxCuchara                            # Almacenaje de temperaturas máximas de la cuchara en la matriz de historicos
    
    elif  QQ == '2':
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
            if k0 == shape(PI)[1] :
                k0 = 0
                TmaxRef.append (max(TempTemporal))
                TempTemporal = []
        
        k0 = 0
        for k in range (len(II_C)):                                         # Bucle para el lado intermedio izquierdo
            k0 = k0 + 1
            for l in range (len(II_C[k])):
                TempTemporal.append (MTemp[II_C[k][l][0]][II_C[k][l][1]])
            if k0 == shape(PI)[1] :
                k0 = 0
                TmaxRef.append (max(TempTemporal))
                TempTemporal = []
        
        k0 = 0
        for k in range (len(C_ID)):                                         # Bucle para el lado intermedio derecho
            k0 = k0 + 1
            for l in range (len(C_ID[k])):
                TempTemporal.append (MTemp[C_ID[k][l][0]][C_ID[k][l][1]])
            if k0 == shape(PI)[1] :
                k0 = 0
                TmaxRef.append (max(TempTemporal))
                TempTemporal = []
        
        k0 = 0
        for k in range (len(ID_D)):                                         # Bucle para el lado derecho
            k0 = k0 + 1
            for l in range (len(ID_D[k])):
                TempTemporal.append (MTemp[ID_D[k][l][0]][ID_D[k][l][1]])
            if k0 == shape(PI)[1] :
                k0 = 0
                TmaxRef.append (max(TempTemporal))
                TempTemporal = []
        
        if FoP == 'F':                                                      # Verificador de imagenes frontales
            for k in range (NumRef * 4):                                    # Bucle para almacenaje de temperaturas máximas de cada refractario en la matriz de historicos
                HTmaxRefF [k][-1] = TmaxRef [k]
        
        elif FoP == 'T':                                                    # Verificador de imagenes posteriores
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

        TmaxZonas = zeros ((3,1))                                        # Vector que guarda la temperatura máxima de cada zona
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

        if FoP == 'F':                                                      # Verificador de imagenes frontales
            for k in range (3):                                             # Bucle para almacenaje de temperaturas máximas de cada zona en la matriz de historicos
                HTmaxZonasF [k][-1] = TmaxZonas [k][0]
        
        elif FoP == 'T':                                                    # Verificador de imagenes posteriores
            for k in range (3):                                             # Bucle para almacenaje de temperaturas máximas de cada zona en la matriz de historicos
                HTmaxZonasT [k][-1] = TmaxZonas [k][0]
        
        ####################################################
        ################### Temperatura máxima de la cuchara
        ####################################################
        TmaxCuchara = max (MTemp[50:-50 , 50:-50])
        
        if FoP == 'F': 
            HTmaxCucharaF [0][-1] = TmaxCuchara                            # Almacenaje de temperaturas máximas de la cuchara en la matriz de historicos
        
        elif FoP == 'T':                                                    # Verificador de imagenes posteriores
            HTmaxCucharaT [0][-1] = TmaxCuchara                            # Almacenaje de temperaturas máximas de la cuchara en la matriz de historicos
         
############################################################################
################### Función para hallar las coordenadas sobre la línea que conecta 2 nodos
def intermedios (extremos):
            
    d0, d1 = abs(diff(extremos, axis=0))[0]
    if d0 > d1: 
        return c_[linspace(extremos[0, 0], extremos[1, 0], d0+1, dtype=int32), round(linspace(extremos[0, 1], extremos[1, 1], d0+1)).astype(int32)]
    else:
        return c_[round(linspace(extremos[0, 0], extremos[1, 0], d1+1)).astype(int32) , linspace(extremos[0, 1], extremos[1, 1], d1+1, dtype=int32)]

############################################################################
################### Función para saber que desea observar el usuario
def preguntasRespuesta ():

    global OPC1, OPC2 , OPC3 , Q2 , FoT , zona , refractario

    OPC1 = 'no'                                                                                                         # Opcion de ver temperatura maxima de la cuchara
    OPC2 = 'no'                                                                                                         # Opcion de ver temperatura maxima de las zonas de la cuchara 
    OPC3 = 'no'                                                                                                         # Opcion de ver temperatura maxima de los refractarios de la cuchara

    print ('Menú de opciones:\n\n')

    verif = 'no'
    while verif == 'no':                                                                                                # Verificacion del it del usuario de la pregunta de las 3 opciones
        Q = input ('\n\nQué gráfica desea observar? (Seleccione 1, 2 o 3.) \n1) Temperatura máxima de la cuchara vs No. de coladas. \n2) Temperatura máxima de las zonas de la cuchara vs No. de coladas. \n3) Temperatura máxima de cada refractario de la cuchara vs No. de coladas.\n            ')
        if Q == '1' or Q == '2' or Q == '3':
            verif = 'si'

    verif = 'no'
    while verif == 'no':    
        if Q == '1':                                                                                                    # Pregunta de temperatura máxima en la cuchara
            Q1 = input ('\nSeleccione 1 o 2. \n1) Frontal de la cuchara. \n2) Posterior de la cuchara.\n            ')  # Pregunta frontal o posterior
            if Q1 == '1' or Q1 == '2':
                if Q1 == '1':
                    FoT = 'F'
                elif Q1 == '2':
                    FoT = 'T'
                OPC1 = 'si'
                OPC2 = OPC3 = 'no'
                verif = 'si'
                
        elif Q == '2':                                                                                                  # Pregunta de temperatura máxima en las zonas de la cuchara
            Q1 = input ('\nSeleccione 1 o 2. \n1) Frontal de la cuchara. \n2) Posterior de la cuchara.\n            ')  # Pregunta frontal o posterior
            if Q1 == '1' or Q1 == '2':
                if Q1 == '1':
                    FoT = 'F'
                elif Q1 == '2':
                    FoT = 'T'
                Q2 = input ('Seleccione 1, 2 o 3. \n1) Zona 1. \n2) Zona 2. \n3) Zona 3. \n            ')               # Pregunta de la zona que se desea observar
                if Q2 == '1' or Q2 == '2' or Q2 == '3':
                    zona = int (Q2)
                    OPC2 = 'si'
                    OPC1 = OPC3 = 'no'
                    verif = 'si'
                    
        elif Q == '3':                                                                                                  # Pregunta de temperatura máxima en los refractarios de la cuchara
            Q1 = input ('\nSeleccione 1 o 2. \n1) Frontal de la cuchara. \n2) Posterior de la cuchara.\n            ')  # Pregunta frontal o posterior
            if Q1 == '1' or Q1 == '2':
                if Q1 == '1':
                    FoT = 'F'
                elif Q1 == '2':
                    FoT = 'T'
                Q2 = input ('Digite el número de refractario. \n            ')                                          # Pregunta del refractario que se desea observar
                if int(Q2) > 0:
                    refractario = int (Q2)
                    OPC3 = 'si'
                    OPC1 = OPC2 = 'no'
                    verif = 'si'
    
    if QQ == '1':
        analisis1 ()

    elif QQ == '2':
        analisis2 ()

############################################################################
################### Función para realizar el análisis de imágenes
def analisis1 ():

    global coladasFiltradas , temperaturasFiltradas , colOrd , tempOrd , graficas , coladas
    
    if OPC1 == 'si' and OPC2 == 'no' and OPC3 == 'no':                                              # Opcion ver temperatura máxima de la cuchara
        if FoT == 'F':                                                                              # Frontal
            coladasFiltradas = []                                                                   # Vector para guardar las coladas cuyas tempearaturas siempre crezcan
            temperaturasFiltradas = []                                                              # Vector para guardar las temperaturas que siempre crecen
            coladas = []                                                                            # Vector que guarda todas las coladas disponibles en termografías

            for i in range (len(ColF)):
                coladas.append(int(ColF[i]))                                                        # Definición de coladas en la carpeta
                
            colOrd = sorted(coladas)                                                                # Coladas ordenadas 
            orden = []                                                                              # Vector que guarda el orden de las coladas de menor a mayor
            for i in range (len (coladas)):
                orden.append (colOrd.index(coladas[i]))                                             # Vector que guarda el orden de las coladas de menor a mayor
                
            tempOrd = [i for _, i in sorted(zip(orden, HTmaxCucharaF[0]))]                          # Temperaturas conforme el orden de las coladas
            
            k0 = 0
            maxT = tempOrd [0]                                                                      # Vector que guarda un primer valor de temperatura máxima inicial
            for i in range (len (colOrd)):
                if i == 0 and tempOrd[i] != 0:
                    coladasFiltradas.append (colOrd[i])                                             # Coladas filtradas cuya temperatura siempre crece
                    temperaturasFiltradas.append (tempOrd[i])                                       # Temperaturas filtradas siempre crecientes
                if colOrd [i] >= ColadaCLE and k0 == 0:
                    maxT = tempOrd [i]
                    k0 = 1
                if i != 0 and tempOrd[i] != 0: 
                    if tempOrd [i] >= maxT:
                        maxT = tempOrd [i]                                                          # Se actualiza la temperatura máxima si la siguiente es mayor a todas las anteriores
                        coladasFiltradas.append (colOrd[i])                                         # Se guarda en el vector de coladas filtradas ordenadas
                        temperaturasFiltradas.append (tempOrd[i])                                   # Se guarda en el vector de temperaturas filtradas ordenadas
                        
            if ColadaACT != 0 and ColadaACT != coladasFiltradas [-1] and NT == 'si' and RT == 'no': # Si existe colada actual y su temperatura es menor a la del ultimo dato
                extrapolacion ()
            
            elif ColadaACT == 0 and colOrd [-1] != coladasFiltradas [-1]  and NT == 'no' and RT == 'si' :  # Si no existe colada actual y la temperatura de la ultima colada es menor a la anterior colada 
                extrapolacion ()    

            else:
                if ColadaCLE > 0:                                                                   # Si existió cambio de línea de escoria
                    graficas = 3
                    print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    extrapolacion ()
                    
                else:                                                                               # Si no existió cambio de línea de escoria
                    graficas = 2
                    print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    graficarTempColada ()

        elif FoT == 'T':                                                                            # Posterior

            coladasFiltradas = []
            temperaturasFiltradas = []

            coladas = []
            for i in range (len(ColT)):
                coladas.append(int(ColT[i]))                                                        # Definición de coladas en la carpeta

            colOrd = sorted(coladas)                                                                # Coladas ordenadas 
            orden = []  
            for i in range (len (coladas)):
                orden.append (colOrd.index(coladas[i]))                                             # Orden de las coladas
                
            tempOrd = [i for _, i in sorted(zip(orden, HTmaxCucharaT[0]))]                          # Temperaturas ordenadas conforme las coladas
            
            k0 = 0
            maxT = tempOrd [0]
            for i in range (len (colOrd)):
                if i == 0 and tempOrd[i] != 0:
                    coladasFiltradas.append (colOrd[i])                                             # Coladas filtradas cuya temperatura siempre crece
                    temperaturasFiltradas.append (tempOrd[i])                                       # Temperaturas filtradas cuya siempre crecientes
                if colOrd [i] >= ColadaCLE and k0 == 0:
                    maxT = tempOrd [i]
                    k0 = 1
                if i != 0 and tempOrd[i] != 0: 
                    if tempOrd [i] >= maxT:
                        maxT = tempOrd [i]
                        coladasFiltradas.append (colOrd[i])
                        temperaturasFiltradas.append (tempOrd[i])
                
            if ColadaACT != 0 and ColadaACT != coladasFiltradas [-1] and NT == 'si' and RT == 'no': 
                extrapolacion ()
            
            elif ColadaACT == 0 and colOrd [-1] != coladasFiltradas [-1]  and NT == 'no' and RT == 'si' : 
                extrapolacion ()    

            else:
                if ColadaCLE > 0:                                                                   # Si existió cambio de línea de escoria
                    graficas = 3
                    print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    extrapolacion ()
                    
                else:                                                                               # Si no existió cambio de línea de escoria
                    graficas = 2
                    print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    graficarTempColada ()

        verif = 'no'
        while verif == 'no':                                                                                                # Verificacion del input del usuario para regresar a las preguntas anteriores
            Q3 = input ('Desea regresar al menú de  opciones? (Seleccione 1 o 2.) \n1) Si. \n2) No. \n            ')
            if Q3 == '1':
                verif = 'si'
                preguntasRespuesta ()
            elif Q3 == '2':
                verif = 'si'
            
    elif OPC2 == 'si' and OPC1 == 'no' and OPC3 == 'no':                                            # Opcion ver temperatura máxima de las zonas de la cuchara
        if FoT == 'F':                                                                              # Frontal

            coladasFiltradas = []
            temperaturasFiltradas = []

            coladas = []
            for i in range (len(ColF)):
                coladas.append(int(ColF[i]))                                                        # Definición de coladas en la carpeta

            colOrd = sorted(coladas)                                                                # Coladas ordenadas 
            orden = []  
            for i in range (len (coladas)):
                orden.append (colOrd.index(coladas[i]))                                             # Orden de las coladas
                
            tempOrd = [i for _, i in sorted(zip(orden, HTmaxZonasF[zona - 1]))]                     # Temperaturas ordenadas conforme las coladas
            
            k0 = 0
            maxT = tempOrd [0]
            for i in range (len (tempOrd)):
                if i == 0 and tempOrd[i] != 0:
                    coladasFiltradas.append (colOrd[i])                                             # Coladas filtradas cuya temperatura siempre crece
                    temperaturasFiltradas.append (tempOrd[i])                                       # Temperaturas filtradas cuya siempre crecientes
                if colOrd [i] >= ColadaCLE and k0 == 0:
                    maxT = tempOrd [i]
                    k0 = 1
                if i != 0 and tempOrd[i] != 0: 
                    if tempOrd [i] >= maxT:
                        maxT = tempOrd [i]
                        coladasFiltradas.append (colOrd[i])
                        temperaturasFiltradas.append (tempOrd[i])
                        
            if ColadaACT != 0 and ColadaACT != coladasFiltradas [-1] and NT == 'si' and RT == 'no': 
                extrapolacion ()
            
            elif ColadaACT == 0 and colOrd [-1] != coladasFiltradas [-1]  and NT == 'no' and RT == 'si' : 
                extrapolacion ()    

            else:
                if ColadaCLE > 0:                                                                   # Si existió cambio de línea de escoria
                    graficas = 3
                    print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    extrapolacion ()
                    
                else:                                                                               # Si no existió cambio de línea de escoria
                    graficas = 2
                    print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    graficarTempColada ()

        elif FoT == 'T':                                                                            # Posterior

            coladasFiltradas = []
            temperaturasFiltradas = []

            coladas = []
            for i in range (len(ColT)):
                coladas.append(int(ColT[i]))                                                        # Definición de coladas en la carpeta

            colOrd = sorted(coladas)                                                                # Coladas ordenadas 
            orden = []  
            for i in range (len (coladas)):
                orden.append (colOrd.index(coladas[i]))                                             # Orden de las coladas
                
            tempOrd = [i for _, i in sorted(zip(orden, HTmaxZonasT[zona - 1]))]                          # Temperaturas ordenadas conforme las coladas
            
            k0 = 0
            maxT = tempOrd [0]
            for i in range (len (tempOrd)):
                if i == 0 and tempOrd[i] != 0:
                    coladasFiltradas.append (colOrd[i])                                             # Coladas filtradas cuya temperatura siempre crece
                    temperaturasFiltradas.append (tempOrd[i])                                       # Temperaturas filtradas cuya siempre crecientes
                if colOrd [i] >= ColadaCLE and k0 == 0:
                    maxT = tempOrd [i]
                    k0 = 1
                if i != 0 and tempOrd[i] != 0: 
                    if tempOrd [i] >= maxT:
                        maxT = tempOrd [i]
                        coladasFiltradas.append (colOrd[i])
                        temperaturasFiltradas.append (tempOrd[i])
                        
            if ColadaACT != 0 and ColadaACT != coladasFiltradas [-1] and NT == 'si' and RT == 'no': 
                extrapolacion ()
            
            elif ColadaACT == 0 and colOrd [-1] != coladasFiltradas [-1]  and NT == 'no' and RT == 'si' : 
                extrapolacion ()    

            else:
                if ColadaCLE > 0:                                                                   # Si existió cambio de línea de escoria
                    graficas = 3
                    print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    extrapolacion ()
                    
                else:                                                                               # Si no existió cambio de línea de escoria
                    graficas = 2
                    print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    graficarTempColada ()

        verif = 'no'
        while verif == 'no':                                                                                                # Verificacion del input del usuario para regresar a las preguntas anteriores
            Q3 = input ('Desea regresar al menú de  opciones? (Seleccione 1 o 2.) \n1) Si. \n2) No. \n            ')
            if Q3 == '1':
                verif = 'si'
                preguntasRespuesta ()
            elif Q3 == '2':
                verif = 'si'

    elif OPC3 == 'si' and OPC1 == 'no' and OPC2 == 'no':                                            # Opcion ver temperatura máxima de los refractarios de la cuchara
        if FoT == 'F':                                                                              # Frontal
            
            coladasFiltradas = []
            temperaturasFiltradas = []

            coladas = []
            for i in range (len(ColF)):
                coladas.append(int(ColF[i]))                                                        # Definición de coladas en la carpeta

            colOrd = sorted(coladas)                                                                # Coladas ordenadas 
            orden = []  
            for i in range (len (coladas)):
                orden.append (colOrd.index(coladas[i]))                                             # Orden de las coladas
                
            tempOrd = [i for _, i in sorted(zip(orden, HTmaxRefF[refractario - 1]))]                # Temperaturas ordenadas conforme las coladas
            
            k0 = 0
            maxT = tempOrd [0]
            for i in range (len (tempOrd)):
                if i == 0 and tempOrd[i] != 0:
                    coladasFiltradas.append (colOrd[i])                                             # Coladas filtradas cuya temperatura siempre crece
                    temperaturasFiltradas.append (tempOrd[i])                                       # Temperaturas filtradas siempre crecientes
                if colOrd [i] >= ColadaCLE and k0 == 0:
                    maxT = tempOrd [i]
                    k0 = 1
                if i != 0 and tempOrd[i] != 0: 
                    if tempOrd [i] >= maxT:
                        maxT = tempOrd [i]
                        coladasFiltradas.append (colOrd[i])                                         
                        temperaturasFiltradas.append (tempOrd[i])
            
            if ColadaACT != 0 and ColadaACT != coladasFiltradas [-1] and NT == 'si' and RT == 'no': 
                extrapolacion ()
                
            elif ColadaACT == 0 and colOrd [-1] != coladasFiltradas [-1]  and NT == 'no' and RT == 'si' : 
                extrapolacion ()    
                
            else:
                if ColadaCLE > 0:                                                                   # Si existió cambio de línea de escoria
                    graficas = 3
                    print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    extrapolacion ()
                    
                else:                                                                               # Si no existió cambio de línea de escoria
                    graficas = 2
                    print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    graficarTempColada ()
                
        elif FoT == 'T':                                                                            # Posterior

            coladasFiltradas = []
            temperaturasFiltradas = []

            coladas = []
            for i in range (len(ColT)):
                coladas.append(int(ColT[i]))                                                        # Definición de coladas en la carpeta

            colOrd = sorted(coladas)                                                                # Coladas ordenadas 
            orden = []  
            for i in range (len (coladas)):
                orden.append (colOrd.index(coladas[i]))                                             # Orden de las coladas
                
            tempOrd = [i for _, i in sorted(zip(orden, HTmaxRefT[refractario - 1]))]                # Temperaturas ordenadas conforme las coladas
            
            k0 = 0
            maxT = tempOrd [0]
            for i in range (len (tempOrd)):
                if i == 0 and tempOrd[i] != 0:
                    coladasFiltradas.append (colOrd[i])                                             # Coladas filtradas cuya temperatura siempre crece
                    temperaturasFiltradas.append (tempOrd[i])                                       # Temperaturas filtradas cuya siempre crecientes
                if colOrd [i] >= ColadaCLE and k0 == 0:
                    maxT = tempOrd [i]
                    k0 = 1
                if i != 0 and tempOrd[i] != 0: 
                    if tempOrd [i] >= maxT:
                        maxT = tempOrd [i]
                        coladasFiltradas.append (colOrd[i])
                        temperaturasFiltradas.append (tempOrd[i])
            
            if ColadaACT != 0 and ColadaACT != coladasFiltradas [-1] and NT == 'si' and RT == 'no': 
                extrapolacion ()
            
            elif ColadaACT == 0 and colOrd [-1] != coladasFiltradas [-1]  and NT == 'no' and RT == 'si' : 
                extrapolacion ()    

            else:
                if ColadaCLE > 0:                                                                   # Si existió cambio de línea de escoria
                    graficas = 3
                    print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    extrapolacion ()
                    
                else:                                                                               # Si no existió cambio de línea de escoria
                    graficas = 2
                    print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    graficarTempColada ()

        verif = 'no'
        while verif == 'no':                                                                                                # Verificacion del input del usuario para regresar a las preguntas anteriores
            Q3 = input ('Desea regresar al menú de  opciones? (Seleccione 1 o 2.) \n1) Si. \n2) No. \n            ')
            if Q3 == '1':
                verif = 'si'
                preguntasRespuesta ()

            elif Q3 == '2':
                verif = 'si'

############################################################################
################### Función para realizar el análisis de imágenes
def analisis2 (opc1, opc2, opc3, fop):

    global coladasFiltradas , temperaturasFiltradas , colOrd , tempOrd , graficas , coladas, OPC1, OPC2, OPC3, FoT
    OPC1 = opc1
    OPC2 = opc2
    OPC3 = opc3
    FoT = fop
    if OPC1 == 'si' and OPC2 == 'no' and OPC3 == 'no':                                              # Opcion ver temperatura máxima de la cuchara
        if FoT == 'F':                                                                              # Frontal
            coladasFiltradas = []                                                                   # Vector para guardar las coladas cuyas tempearaturas siempre crezcan
            temperaturasFiltradas = []                                                              # Vector para guardar las temperaturas que siempre crecen
            coladas = []                                                                            # Vector que guarda todas las coladas disponibles en termografías

            for i in range (len(ColF[0])):
                coladas.append(int(ColF[0][i]))                                                     # Definición de coladas en la carpeta

            colOrd = sorted(coladas)                                                                # Coladas ordenadas 
            orden = []                                                                              # Vector que guarda el orden de las coladas de menor a mayor
            for i in range (len (coladas)):
                orden.append (colOrd.index(coladas[i]))                                             # Vector que guarda el orden de las coladas de menor a mayor

            tempOrd = [i for _, i in sorted(zip(orden, HTmaxCucharaF[0]))]                          # Temperaturas conforme el orden de las coladas
            
            k0 = 0
            maxT = tempOrd [0]                                                                      # Vector que guarda un primer valor de temperatura máxima inicial
            for i in range (len (tempOrd)):
                if i == 0 and tempOrd[i] != 0:
                    coladasFiltradas.append (colOrd[i])                                             # Coladas filtradas cuya temperatura siempre crece
                    temperaturasFiltradas.append (tempOrd[i])                                       # Temperaturas filtradas cuya siempre crecientes
                if colOrd [i] >= ColadaCLE and k0 == 0:
                    maxT = tempOrd [i]
                    k0 = 1
                if i != 0 and tempOrd[i] != 0: 
                    if tempOrd [i] >= maxT:
                        maxT = tempOrd [i]                                                          # Se actualiza la temperatura máxima si la siguiente es mayor a todas las anteriores
                        coladasFiltradas.append (colOrd[i])                                         # Se guarda en el vector de coladas filtradas ordenadas
                        temperaturasFiltradas.append (tempOrd[i])
            
            if ColadaACT != 0 and ColadaACT != coladasFiltradas [-1]:                               # Si existe colada actual y su temperatura es menor a la del ultimo dato
                extrapolacion ()
                
            elif ColadaACT == 0 and colOrd [-1] != coladasFiltradas [-1]:                           # Si no existe colada actual y la temperatura de la ultima colada es menor a la anterior colada 
                extrapolacion ()    
            else:
                if ColadaCLE > 0:                                                                   # Si existió cambio de línea de escoria
                    graficas = 3
                    #print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    extrapolacion ()
                    
                else:                                                                               # Si no existió cambio de línea de escoria
                    graficas = 2
                    #print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    #graficarTempColada ()
                    
        elif FoT == 'T':                                                                            # Posterior

            coladasFiltradas = []
            temperaturasFiltradas = []
            coladas = []
            
            for i in range (len(ColT[0])):
                coladas.append(int(ColT[0][i]))                                                        # Definición de coladas en la carpeta

            colOrd = sorted(coladas)                                                                # Coladas ordenadas 
            orden = []  
            for i in range (len (coladas)):
                orden.append (colOrd.index(coladas[i]))                                             # Orden de las coladas
                
            tempOrd = [i for _, i in sorted(zip(orden, HTmaxCucharaT[0]))]                          # Temperaturas ordenadas conforme las coladas

            k0 = 0
            maxT = tempOrd [0]                                                                      # Vector que guarda un primer valor de temperatura máxima inicial
            for i in range (len (tempOrd)):
                if i == 0 and tempOrd[i] != 0:
                    coladasFiltradas.append (colOrd[i])                                             # Coladas filtradas cuya temperatura siempre crece
                    temperaturasFiltradas.append (tempOrd[i])                                       # Temperaturas filtradas cuya siempre crecientes
                if colOrd [i] >= ColadaCLE and k0 == 0:
                    maxT = tempOrd [i]
                    k0 = 1
                if i != 0 and tempOrd[i] != 0: 
                    if tempOrd [i] >= maxT:
                        maxT = tempOrd [i]                                                          # Se actualiza la temperatura máxima si la siguiente es mayor a todas las anteriores
                        coladasFiltradas.append (colOrd[i])                                         # Se guarda en el vector de coladas filtradas ordenadas
                        temperaturasFiltradas.append (tempOrd[i])
                    
            
            if ColadaACT != 0 and ColadaACT != coladasFiltradas [-1] and NT == 'si' and RT == 'no': 
                extrapolacion ()
            
            elif ColadaACT == 0 and colOrd [-1] != coladasFiltradas [-1]  and NT == 'no' and RT == 'si' : 
                extrapolacion ()    

            else:
                if ColadaCLE > 0:                                                                   # Si existió cambio de línea de escoria
                    graficas = 3
                    #print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    extrapolacion ()
                    
                else:                                                                               # Si no existió cambio de línea de escoria
                    graficas = 2
                    #print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    #graficarTempColada ()

        verif = 'no'
        while verif == 'no':                                                                        # Verificacion del input del usuario para regresar a las preguntas anteriores
            Q3 = '2'#Q3 = input ('Desea regresar al menú de  opciones? (Seleccione 1 o 2.) \n1) Si. \n2) No. \n            ')
            if Q3 == '1':
                verif = 'si'
                #preguntasRespuesta ()
            elif Q3 == '2':
                verif = 'si'
            
    elif OPC2 == 'si' and OPC1 == 'no' and OPC3 == 'no':                                            # Opcion ver temperatura máxima de las zonas de la cuchara
        if FoT == 'F':                                                                              # Frontal

            coladasFiltradas = []
            temperaturasFiltradas = []
            coladas = []
            
            for i in range (len(ColF[0])):
                coladas.append(int(ColF[0][i]))                                                        # Definición de coladas en la carpeta
            
            colOrd = sorted(coladas)                                                                # Coladas ordenadas 
            orden = []  
            for i in range (len (coladas)):
                orden.append (colOrd.index(coladas[i]))                                             # Orden de las coladas
            
            tempOrd = [i for _, i in sorted(zip(orden, HTmaxZonasF[zona - 1]))]                     # Temperaturas ordenadas conforme las coladas
            
            k0 = 0
            maxT = tempOrd [0]                                                                      # Vector que guarda un primer valor de temperatura máxima inicial
            for i in range (len (tempOrd)):
                if i == 0 and tempOrd[i] != 0:
                    coladasFiltradas.append (colOrd[i])                                             # Coladas filtradas cuya temperatura siempre crece
                    temperaturasFiltradas.append (tempOrd[i])                                       # Temperaturas filtradas cuya siempre crecientes
                if colOrd [i] >= ColadaCLE and k0 == 0:
                    maxT = tempOrd [i]
                    k0 = 1
                if i != 0 and tempOrd[i] != 0: 
                    if tempOrd [i] >= maxT:
                        maxT = tempOrd [i]                                                          # Se actualiza la temperatura máxima si la siguiente es mayor a todas las anteriores
                        coladasFiltradas.append (colOrd[i])                                         # Se guarda en el vector de coladas filtradas ordenadas
                        temperaturasFiltradas.append (tempOrd[i])
                    
            
            if ColadaACT != 0 and ColadaACT != coladasFiltradas [-1]: 
                extrapolacion ()
                
            elif ColadaACT == 0 and colOrd [-1] != coladasFiltradas [-1]: 
                extrapolacion ()    
                
            else:
                if ColadaCLE > 0:                                                                   # Si existió cambio de línea de escoria
                    graficas = 3
                    #print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    extrapolacion ()
                    
                else:                                                                               # Si no existió cambio de línea de escoria
                    graficas = 2
                    #print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    #graficarTempColada ()
                    
        elif FoT == 'T':                                                                            # Posterior

            coladasFiltradas = []
            temperaturasFiltradas = []
            coladas = []
            
            for i in range (len(ColF[0])):
                coladas.append(int(ColF[0][i]))                                                        # Definición de coladas en la carpeta
            
            colOrd = sorted(coladas)                                                                # Coladas ordenadas 
            orden = []  
            for i in range (len (coladas)):
                orden.append (colOrd.index(coladas[i]))                                             # Orden de las coladas
            
            tempOrd = [i for _, i in sorted(zip(orden, HTmaxZonasT[zona - 1]))]                     # Temperaturas ordenadas conforme las coladas
            
            k0 = 0
            maxT = tempOrd [0]                                                                      # Vector que guarda un primer valor de temperatura máxima inicial
            for i in range (len (tempOrd)):
                if i == 0 and tempOrd[i] != 0:
                    coladasFiltradas.append (colOrd[i])                                             # Coladas filtradas cuya temperatura siempre crece
                    temperaturasFiltradas.append (tempOrd[i])                                       # Temperaturas filtradas cuya siempre crecientes
                if colOrd [i] >= ColadaCLE and k0 == 0:
                    maxT = tempOrd [i]
                    k0 = 1
                if i != 0 and tempOrd[i] != 0: 
                    if tempOrd [i] >= maxT:
                        maxT = tempOrd [i]                                                          # Se actualiza la temperatura máxima si la siguiente es mayor a todas las anteriores
                        coladasFiltradas.append (colOrd[i])                                         # Se guarda en el vector de coladas filtradas ordenadas
                        temperaturasFiltradas.append (tempOrd[i])
                    
            
            if ColadaACT != 0 and ColadaACT != coladasFiltradas [-1]: 
                extrapolacion ()
                
            elif ColadaACT == 0 and colOrd [-1] != coladasFiltradas [-1]: 
                extrapolacion ()    
                
            else:
                if ColadaCLE > 0:                                                                   # Si existió cambio de línea de escoria
                    graficas = 3
                    #print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    extrapolacion ()
                    
                else:                                                                               # Si no existió cambio de línea de escoria
                    graficas = 2
                    #print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    #graficarTempColada ()

        verif = 'no'
        while verif == 'no':                                                                        # Verificacion del input del usuario para regresar a las preguntas anteriores
            Q3='2' #Q3 = input ('Desea regresar al menú de  opciones? (Seleccione 1 o 2.) \n1) Si. \n2) No. \n            ')
            if Q3 == '1':
                verif = 'si'
                #preguntasRespuesta ()
            elif Q3 == '2':
                verif = 'si'

    elif OPC3 == 'si' and OPC1 == 'no' and OPC2 == 'no':                                            # Opcion ver temperatura máxima de los refractarios de la cuchara
        if FoT == 'F':                                                                              # Frontal

            coladasFiltradas = []
            temperaturasFiltradas = []

            coladas = []
            for i in range (len(ColF[0])):
                coladas.append(int(ColF[0][i]))                                                        # Definición de coladas en la carpeta

            colOrd = sorted(coladas)                                                                # Coladas ordenadas 
            orden = []  
            for i in range (len (coladas)):
                orden.append (colOrd.index(coladas[i]))                                             # Orden de las coladas
                
            tempOrd = [i for _, i in sorted(zip(orden, HTmaxRefF[refractario - 1]))]                # Temperaturas ordenadas conforme las coladas

            k0 = 0
            maxT = tempOrd [0]                                                                      # Vector que guarda un primer valor de temperatura máxima inicial
            for i in range (len (tempOrd)):
                if i == 0 and tempOrd[i] != 0:
                    coladasFiltradas.append (colOrd[i])                                             # Coladas filtradas cuya temperatura siempre crece
                    temperaturasFiltradas.append (tempOrd[i])                                       # Temperaturas filtradas cuya siempre crecientes
                if colOrd [i] >= ColadaCLE and k0 == 0:
                    maxT = tempOrd [i]
                    k0 = 1
                if i != 0 and tempOrd[i] != 0: 
                    if tempOrd [i] >= maxT:
                        maxT = tempOrd [i]                                                          # Se actualiza la temperatura máxima si la siguiente es mayor a todas las anteriores
                        coladasFiltradas.append (colOrd[i])                                         # Se guarda en el vector de coladas filtradas ordenadas
                        temperaturasFiltradas.append (tempOrd[i])
                    
            
            if ColadaACT != 0 and ColadaACT != coladasFiltradas [-1]: 
                extrapolacion ()
            
            elif ColadaACT == 0 and colOrd [-1] != coladasFiltradas [-1]: 
                extrapolacion ()    

            else:
                if ColadaCLE > 0:                                                                   # Si existió cambio de línea de escoria
                    graficas = 3
                    #print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    extrapolacion ()
                    
                else:                                                                               # Si no existió cambio de línea de escoria
                    graficas = 2
                    #print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    #graficarTempColada ()

        elif FoT == 'T':                                                                            # Posterior

            coladasFiltradas = []
            temperaturasFiltradas = []

            coladas = []
            for i in range (len(ColT[0])):
                coladas.append(int(ColT[0][i]))                                                        # Definición de coladas en la carpeta

            colOrd = sorted(coladas)                                                                # Coladas ordenadas 
            orden = []  
            for i in range (len (coladas)):
                orden.append (colOrd.index(coladas[i]))                                             # Orden de las coladas
                
            tempOrd = [i for _, i in sorted(zip(orden, HTmaxRefT[refractario - 1]))]                # Temperaturas ordenadas conforme las coladas

            k0 = 0
            maxT = tempOrd [0]                                                                      # Vector que guarda un primer valor de temperatura máxima inicial
            for i in range (len (tempOrd)):
                if i == 0 and tempOrd[i] != 0:
                    coladasFiltradas.append (colOrd[i])                                             # Coladas filtradas cuya temperatura siempre crece
                    temperaturasFiltradas.append (tempOrd[i])                                       # Temperaturas filtradas cuya siempre crecientes
                if colOrd [i] >= ColadaCLE and k0 == 0:
                    maxT = tempOrd [i]
                    k0 = 1
                if i != 0 and tempOrd[i] != 0: 
                    if tempOrd [i] >= maxT:
                        maxT = tempOrd [i]                                                          # Se actualiza la temperatura máxima si la siguiente es mayor a todas las anteriores
                        coladasFiltradas.append (colOrd[i])                                         # Se guarda en el vector de coladas filtradas ordenadas
                        temperaturasFiltradas.append (tempOrd[i])
                    
            
            if ColadaACT != 0 and ColadaACT != coladasFiltradas [-1] and NT == 'si' and RT == 'no': 
                extrapolacion ()
            
            elif ColadaACT == 0 and colOrd [-1] != coladasFiltradas [-1]  and NT == 'no' and RT == 'si' : 
                extrapolacion ()    

            else:
                if ColadaCLE > 0:                                                                   # Si existió cambio de línea de escoria
                    graficas = 3
                    #print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    extrapolacion ()
                    
                else:                                                                               # Si no existió cambio de línea de escoria
                    graficas = 2
                    #print ('\n\nValor de temperatura mayor al de las coladas anteriores.')
                    #graficarTempColada ()

        verif = 'no'
        while verif == 'no':                                                                        # Verificacion del input del usuario para regresar a las preguntas anteriores
            Q3 = '2' #Q3 = input ('Desea regresar al menú de  opciones? (Seleccione 1 o 2.) \n1) Si. \n2) No. \n            ')
            if Q3 == '1':
                verif = 'si'
                #preguntasRespuesta ()

            elif Q3 == '2':
                verif = 'si'

############################################################################
################### Función diseñada para realizar extrapolacion de datos
def extrapolacion ():

    global coladasFiltradas , temperaturasFiltradas , graficas , coladasSup , coladasInf , temperaturasSup , temperaturasInf , ColadaACT
    
    if ColadaCLE == 0:                                                                                                                                      # Ingresa sí no hay cambio de línea de escoria
        
        graficas = 2
        
        if ColadaACT != 0:                                                                                                                                  # Ingresa si la colada acutal es menor a la colada 120 y diferente de 0
            if len (temperaturasFiltradas) == 1:                                                                                                            # Ingresa sí solo existe una temperatura y una colada para graficar
                coladasFiltradas.append(ColadaACT)
                temperaturasFiltradas.append(temperaturasFiltradas[-1] + 0.1)
                print ('\n\nValor de temperatura igual al anterior debido a que no hay datos para extrapolar.')                                                 # Se guarda el valor de la colada actual y se lo coteja con la temperatura anterior ya que no hay datos para extrapolar
            
            elif len (temperaturasFiltradas) == 2:                                                                                                          # Ingresa sí existen 2 valores de temperatura para hacer la curva
                m = (temperaturasFiltradas[-1] - temperaturasFiltradas[-2]) / (coladasFiltradas[-1] - coladasFiltradas[-2])                                 # Pendiente de la recta
                
                coladasFiltradas.append(ColadaACT)
                temperaturasFiltradas.append((temperaturasFiltradas[-1] + (m * (ColadaACT - coladasFiltradas[-2]) + temperaturasFiltradas[-1]))/2)
                print ('\n\nValor calculado con el promedio entre la extrapolación de la unica recta previamente existente y el valor anterior.')               # Se guarda el valor de la colada actual y se lo coteja con el promedio entre la temperatura extrapolada de la linea existente y el valor anterior

            elif len (temperaturasFiltradas) >= 3:                                                                                                          # Ingresa sí existen 3 o más valores de temperatura para hacer la curva
                m = ((temperaturasFiltradas[-1] - temperaturasFiltradas[-2]) /                                                                              
                    (coladasFiltradas[-1] - coladasFiltradas[-2]) + 
                    (temperaturasFiltradas[-2] - temperaturasFiltradas[-3]) / 
                    (coladasFiltradas[-2] - coladasFiltradas[-3])) / 2                                                                                      # Pendiente promedio entre las 2 anteriores existentes
                
                coladasFiltradas.append(ColadaACT)
                temperaturasFiltradas.append(m * (ColadaACT - coladasFiltradas[-2]) + temperaturasFiltradas[-1])
                print ('\n\nValor calculado con el promedio de las pendientes de las 2 rectas previamente existentes.')                                         # Se guarda el valor de la colada actual y se lo coteja con la temperatura extrapolada de la linea existente
        
        elif ColadaACT == 0 and coladasFiltradas [-1] != max (coladas):                                                                                     # Ingresa si no se va a ingresar una colada actual y el valor de temperatura de la ultima colada es menor al anterior
            if len (temperaturasFiltradas) == 1:                                                                                                            # Ingresa sí solo existe una temperatura y una colada para graficar
                coladasFiltradas.append(max (coladas))
                temperaturasFiltradas.append(temperaturasFiltradas[-1] + 0.1)
                print ('\n\nValor de temperatura igual al anterior debido a que no hay datos para extrapolar.')                                                 # Se guarda el valor de la colada actual y se lo coteja con la temperatura anterior ya que no hay datos para extrapolar
            
            elif len (temperaturasFiltradas) == 2:                                                                                                          # Ingresa sí existen 2 valores de temperatura para hacer la curva
                m = (temperaturasFiltradas[-1] - temperaturasFiltradas[-2]) / (coladasFiltradas[-1] - coladasFiltradas[-2])                                 # Pendiente de la única línea disponible
                
                coladasFiltradas.append(max (coladas))
                temperaturasFiltradas.append((temperaturasFiltradas[-1] + (m * (max (coladas) - coladasFiltradas[-2]) + temperaturasFiltradas[-1]))/2)
                print ('\n\nValor calculado con el promedio entre la extrapolación de la unica recta previamente existente y el valor anterior.')               # Se guarda el valor de la colada actual y se lo coteja con el promedio entre la temperatura extrapolada de la linea existente y el valor anterior

            elif len (temperaturasFiltradas) >= 3:                                                                                                          # Ingresa sí existen 3 o más valores de temperatura para hacer la curva
                m = ((temperaturasFiltradas[-1] - temperaturasFiltradas[-2]) / 
                    (coladasFiltradas[-1] - coladasFiltradas[-2]) + 
                    (temperaturasFiltradas[-2] - temperaturasFiltradas[-3]) / 
                    (coladasFiltradas[-2] - coladasFiltradas[-3])) / 2                                                                                      # Pendiente promedio entre las 2 anteriores existentes
                
                coladasFiltradas.append(max (coladas))
                temperaturasFiltradas.append(m * (max (coladas) - coladasFiltradas[-2]) + temperaturasFiltradas[-1])
                print ('\n\nValor calculado con el promedio de las pendientes de las 2 rectas previamente existentes.')                                         # Se guarda el valor de la colada actual y se lo coteja con la temperatura extrapolada de la linea existente

    elif ColadaCLE != 0:                                                                                                                                    # Ingresa sí hay cambio de línea de escoria
        graficas = 3
        
        coladasInf = []                                                                                                                                     # Vector para guardar las coladas inferiores a la colada en la que se realizo el cambio de línea de escoria
        coladasSup = []                                                                                                                                     # Vector para guardar las coladas superiores a la colada en la que se realizo el cambio de línea de escoria
        temperaturasInf = []                                                                                                                                # Vector para guardar las temperaturas de las coladas inferiores a la colada en la que se realizo el cambio de línea de escoria
        temperaturasSup = []                                                                                                                                # Vector para guardar las temperaturas de las coladas superiores a la colada en la que se realizo el cambio de línea de escoria

        for col in range (len (coladasFiltradas)):
            if coladasFiltradas [col] < ColadaCLE:
                coladasInf.append (coladasFiltradas [col])
                temperaturasInf.append (temperaturasFiltradas [col])
            elif coladasFiltradas [col] > ColadaCLE:
                coladasSup.append (coladasFiltradas [col])
                temperaturasSup.append (temperaturasFiltradas [col])
        
        if ColadaACT != 0:
            if len (temperaturasSup) == 1:                                                                                                            
                coladasSup.append(ColadaACT)
                temperaturasSup.append(temperaturasSup[-1] + 0.1)
                print ('\n\nValor de temperatura igual al anterior debido a que no hay datos para extrapolar.')
            
            elif len (temperaturasSup) == 2:                                                                                                          
                m = (temperaturasSup[-1] - temperaturasSup[-2]) / (coladasSup[-1] - coladasSup[-2]) 
                
                coladasSup.append(ColadaACT)
                temperaturasSup.append((temperaturasSup[-1] + (m * (ColadaACT - coladasSup[-2]) + temperaturasSup[-1]))/2)
                print ('\n\nValor calculado con el promedio entre la extrapolación de la unica recta previamente existente y el valor anterior.')
            
            elif len (temperaturasSup) >= 3:                                                                                                          
                m = ((temperaturasSup[-1] - temperaturasSup[-2]) / 
                    (coladasSup[-1] - coladasSup[-2]) + 
                    (temperaturasSup[-2] - temperaturasSup[-3]) / 
                    (coladasSup[-2] - coladasSup[-3])) / 2
                
                coladasSup.append(ColadaACT)
                temperaturasSup.append(m * (ColadaACT - coladasSup[-2]) + temperaturasSup[-1])
                print ('\n\nValor calculado con el promedio de las pendientes de las 2 rectas previamente existentes.')
        
        elif ColadaACT == 0 and coladasFiltradas [-1] != max (coladas):
            if len (temperaturasSup) == 1:                                                                                                            
                coladasSup.append(max (coladas))
                temperaturasSup.append(temperaturasSup[-1] + 0.1)
                print ('\n\nValor de temperatura igual al anterior debido a que no hay datos para extrapolar.')
            
            elif len (temperaturasSup) == 2:                                                                                                          
                m = (temperaturasSup[-1] - temperaturasSup[-2]) / (coladasSup[-1] - coladasSup[-2]) 
                
                coladasSup.append(max (coladas))
                temperaturasSup.append((temperaturasSup[-1] + (m * (max (coladas) - coladasSup[-2]) + temperaturasSup[-1]))/2)
                print ('\n\nValor calculado con el promedio entre la extrapolación de la unica recta previamente existente y el valor anterior.')
            
            elif len (temperaturasSup) >= 3:                                                                                                          
                m = ((temperaturasSup[-1] - temperaturasSup[-2]) / 
                    (coladasSup[-1] - coladasSup[-2]) + 
                    (temperaturasSup[-2] - temperaturasSup[-3]) / 
                    (coladasSup[-2] - coladasSup[-3])) / 2
                
                coladasSup.append(max (coladas))
                temperaturasSup.append(m * (max (coladas) - coladasSup[-2]) + temperaturasSup[-1])
                print ('\n\nValor calculado con el promedio de las pendientes de las 2 rectas previamente existentes.')

    #graficarTempColada ()

############################################################################
################### Función para realizar las gráficas
def graficarTempColada ():

    if graficas == 2:

        print ('\nColadas Filtradas: ' , coladasFiltradas)                    # Coladas que tienen valor de temperatura siempre creciente
        print ('Temperaturas Filtradas: ' , temperaturasFiltradas)          # Valores de temperatura de las coladas que tienen valor de temperatura siempre creciente
        print ('Coladas Ordenadas: ' , colOrd)                              # Todas las coladas disponibles
        print ('Temperaturas Ordenadas: ' , tempOrd , '\n')                        # Valores de temperatura de todas las coladas disponibles
        
        plt.plot (colOrd,tempOrd,'r-')                                      # Grafica todas las coladas
        plt.plot (coladasFiltradas,temperaturasFiltradas,'k-')              # Grafica las coladas filtradas
        if ColadaCLE > 0:
            plt.vlines (ColadaCLE, 100, 500, colors='b', linestyles='dashed', label='')

        plt.xlabel ('Número de coladas. [No.]')
        plt.ylabel ('Temperatura. [ºC]')
        plt.xlim (0 , 160)
        plt.ylim (250 , 400)
        
        if OPC1 == 'si' and OPC2 == 'no' and OPC3 == 'no':
            if FoT == 'F':
                plt.title ('Frontal de la cuchara.')
                #plt.savefig ('D:/JDGB/Novacero/23-003-01/Mallador-de-cuchara/Documentos/C_F.jpg')
            elif FoT == 'T':
                plt.title ('Posterior de la cuchara.')
                #plt.savefig ('D:/JDGB/Novacero/23-003-01/Mallador-de-cuchara/Documentos/C_P.jpg')
        elif OPC2 == 'si' and OPC1 == 'no' and OPC3 == 'no':
            if FoT == 'F':
                plt.title (f'Zona {zona}, frontal.')
                #plt.savefig (f'D:/JDGB/Novacero/23-003-01/Mallador-de-cuchara/Documentos/Z_{zona}_F.jpg')
            elif FoT == 'T':
                plt.title (f'Zona {zona}, posterior.')
                #plt.savefig (f'D:/JDGB/Novacero/23-003-01/Mallador-de-cuchara/Documentos/Z_{zona}_P.jpg')
        elif OPC3 == 'si' and OPC1 == 'no' and OPC2 == 'no':
            if FoT == 'F':
                plt.title (f'Refractario {refractario}, frontal.')
                #plt.savefig (f'D:/JDGB/Novacero/23-003-01/Mallador-de-cuchara/Documentos/R_{refractario}_F.jpg')
            elif FoT == 'T':
                plt.title (f'Refractario {refractario}, posterior.')
                #plt.savefig (f'D:/JDGB/Novacero/23-003-01/Mallador-de-cuchara/Documentos/R_{refractario}_P.jpg')
        plt.show ()
    
    elif graficas == 3:
    
        print ('\nColadas superiores Filtradas: ' , coladasSup)               # Coladas superiores a la colada en la que se realizo cambio de línea de escoria
        print ('Temperaturas superiores Filtradas: ' , temperaturasSup)     # Valores de temperatura de las coladas superiores a la colada en la que se realizó cambio de línea de escoria
        print ('Coladas inferiores Filtradas: ' , coladasInf)               # Coladas inferiores a la colada en la que se realizo cambio de línea de escoria
        print ('Temperaturas inferiores Filtradas: ' , temperaturasInf)     # Valores de temperatura de las coladas inferiores a la colada en la que se realizó cambio de línea de escoria
        print ('Coladas Ordenadas: ' , colOrd)                              # Todas las coladas disponibles
        print ('Temperaturas Ordenadas: ' , tempOrd , '\n')                        # Valores de temperatura de todas las coladas disponibles

        plt.plot (colOrd,tempOrd,'r-')                                      # Grafica todas las coladas
        plt.plot (coladasSup,temperaturasSup,'k-')                          # Grafica de las coladas superiores a la colada en la que se realizó cambio de línea de escoria
        plt.plot (coladasInf,temperaturasInf,'k-')                          # Grafica de las coladas inferiores a la colada en la que se realizó cambio de línea de escoria
        if ColadaCLE > 0:
            plt.vlines (ColadaCLE, 100, 500, colors='b', linestyles='dashed', label='')

        plt.xlabel ('Número de coladas. [No.]')
        plt.ylabel ('Temperatura. [ºC]')
        plt.xlim (0 , 160)
        plt.ylim (250 , 400)
        
        if OPC1 == 'si' and OPC2 == 'no' and OPC3 == 'no':
            if FoT == 'F':
                plt.title ('Frontal de la cuchara.')
                #plt.savefig ('D:/JDGB/Novacero/23-003-01/Mallador-de-cuchara/Documentos/C_F.jpg')
            elif FoT == 'T':
                plt.title ('Posterior de la cuchara.')
                #plt.savefig ('D:/JDGB/Novacero/23-003-01/Mallador-de-cuchara/Documentos/C_P.jpg')
        elif OPC2 == 'si' and OPC1 == 'no' and OPC3 == 'no':
            if FoT == 'F':
                plt.title (f'Zona {zona}, frontal.')
                #plt.savefig (f'D:/JDGB/Novacero/23-003-01/Mallador-de-cuchara/Documentos/Z_{zona}_F.jpg')
            elif FoT == 'T':
                plt.title (f'Zona {zona}, posterior.')
                #plt.savefig (f'D:/JDGB/Novacero/23-003-01/Mallador-de-cuchara/Documentos/Z_{zona}_P.jpg')
        elif OPC3 == 'si' and OPC1 == 'no' and OPC2 == 'no':
            if FoT == 'F':
                plt.title (f'Refractario {refractario}, frontal.')
                #plt.savefig (f'D:/JDGB/Novacero/23-003-01/Mallador-de-cuchara/Documentos/R_{refractario}_F.jpg')
            elif FoT == 'T':
                plt.title (f'Refractario {refractario}, posterior.')
                #plt.savefig (f'D:/JDGB/Novacero/23-003-01/Mallador-de-cuchara/Documentos/R_{refractario}_P.jpg')
        plt.show ()

############################################################################
################### Función para ver la imagen de la termografía
def visgraf ():
    '''if QQ == '1':
        if FoP == 'T':
            imwrite (f'T_{ColT[img]}_Mallada.png',imagen)
        if FoP == 'F':
            imwrite (f'F_{ColF[img]}_Mallada.png',imagen)
    imshow("Imagen", imagen)
    waitKey(0) 
    destroyAllWindows()'''

############################################################################
################### Llamado de función principal
def getValues(numNuevaColada:int, escoria:str, numColadaEscoria:int, cantidadColadas:int, colF:int, colT:int, htmaxcucharaF:float, htmaxcucharaT:float, htmaxzonasF:float, htmaxzonasT:float, htmaxrefF:float, htmaxrefT:float, commonpath:str)-> float:
    try:
        colF[0].append(numNuevaColada)
        colT[0].append(numNuevaColada)
        htmaxcucharaF[0].append(0)
        htmaxcucharaT[0].append(0)
        for i in range(3):
            htmaxzonasF[i].append(0)
            htmaxzonasT[i].append(0)
        for i in range(72):
            htmaxrefF[i].append(0)
            htmaxrefT[i].append(0)
    except:
        colF = zeros ((1 , cantidadColadas + 1))
        colT = zeros ((1 , cantidadColadas + 1))
        append(colF[0], numNuevaColada)
        append(colT[0], numNuevaColada)
        htmaxrefF = zeros ((18 * 4 , 2))                                         # Matriz que almacena historico de datos máximos de temperatura de cada refractaio en imagenes frontales
        htmaxrefT = zeros ((18 * 4 , 2))

        htmaxzonasF  = zeros((3, 2))
        htmaxzonasT  = zeros((3, 2))

        htmaxcucharaF  = zeros ((1, 1))
        htmaxcucharaT  = zeros ((1, 1))
        
        
    [datosF, datosT] = main (numNuevaColada, escoria, numColadaEscoria, cantidadColadas, colF, colT, htmaxcucharaF, htmaxcucharaT, htmaxzonasF, htmaxzonasT, htmaxrefF, htmaxrefT, commonpath)
    return [datosF, datosT]

if __name__ == "__main__":
    numNuevaColada = 33
    escoria = '2' # 1 Si ; 2 No
    numColadaEscoria = 0
    cantidadColadas = 1
    '''colF = []
    colT = []
    htmaxcucharaF=[]
    htmaxcucharaT=[]
    htmaxzonasF = []
    htmaxzonasT = []
    htmaxrefF = []
    htmaxrefT = []'''
    colF = [[20]]
    colT = [[20]]
    htmaxcucharaF=[[200]]
    htmaxcucharaT=[[200]]
    htmaxzonasF = [[180], [180], [180]]
    htmaxzonasT = [[180], [180], [180]]
    htmaxrefF = [[180], [180], [180], [180], [180], [180], [180], [180], [180], [180], 
                [180], [180], [180], [180], [180], [180], [180], [180], [180], [180], 
                [180], [180], [180], [180], [180], [180], [180], [180], [180], [180], 
                [180], [180], [180], [180], [180], [180], [180], [180], [180], [180], 
                [180], [180], [180], [180], [180], [180], [180], [180], [180], [180], 
                [180], [180], [180], [180], [180], [180], [180], [180], [180], [180], 
                [180], [180], [180], [180], [180], [180], [180], [180], [180], [180], 
                [180], [180]]
    htmaxrefT = [[180], [180], [180], [180], [180], [180], [180], [180], [180], [180], 
                [180], [180], [180], [180], [180], [180], [180], [180], [180], [180], 
                [180], [180], [180], [180], [180], [180], [180], [180], [180], [180], 
                [180], [180], [180], [180], [180], [180], [180], [180], [180], [180], 
                [180], [180], [180], [180], [180], [180], [180], [180], [180], [180], 
                [180], [180], [180], [180], [180], [180], [180], [180], [180], [180], 
                [180], [180], [180], [180], [180], [180], [180], [180], [180], [180], 
                [180], [180]]
    
    commonpath = "C:/Users/Diego/OneDrive - UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE/Diego/Proyectos/GUI Abaxfem/Archivos Fuente/Fotografias y archivos de termografias/157"
    [datosF, datosT] = getValues(numNuevaColada, escoria, numColadaEscoria, cantidadColadas, colF, colT, htmaxcucharaF, htmaxcucharaT, htmaxzonasF, htmaxzonasT, htmaxrefF, htmaxrefT, commonpath)
    print(datosF)
    print(datosT)