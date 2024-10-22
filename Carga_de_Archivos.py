import pandas as pd                     # Para leer datos de excel
import numpy as np                      # Para trabajar matrices
import cv2  
import sys
def Carga_de_Archivos(Path_to_file_xlsx,Path_to_file_jpg,Position_Matrix):                                                                                             #Funci√≥n para cargar los archivos excel e im√°genes
    Temp_file = pd.read_excel(Path_to_file_xlsx)                                                                     #Abrir y leer archivo de Excel
    Temp_file = Temp_file.to_numpy()                                                                                 #Cambiar la mattriz a numpy para facilitar el llamado de datos  
    Temp_file = Temp_file[9:,1:]                                                                                     #Rango de datos en Excel
    
    Image_file = cv2.imread(Path_to_file_jpg, 1)                                                                     #Abrir y leer archivo de Excel
    
    DimTemp_file = np.shape(Temp_file)                                                                               #Dimensi√≥n de matriz de temperaturas
    DimImg_file = np.shape(Image_file)    
    if (DimImg_file[0],DimImg_file[1]) !=DimTemp_file or (DimImg_file[0],DimImg_file[1])!=(348,464):
        print("Dimensiones inconsistentes")
        sys.exit()
        
    # if DimImg_file!=DimTemp_file:
    #     Image_file= cv2.resize(Image_file,(DimTemp_file[1],DimTemp_file[0]),interpolation=cv2.INTER_CUBIC)                                                                            #Dimensi√≥n de la imagen 
    #     DimImg_file = np.shape(Image_file)
    # if DimImg_file!=(348,464,3):
    #     for i in range(len(Position_Matrix)):
    #         Position_Matrix.iloc[i,0]=int(DimImg_file[1]-(464-Position_Matrix.iloc[i,0])*DimImg_file[1]/464)
    #         Position_Matrix.iloc[i,1]=int(DimImg_file[0]-(348-Position_Matrix.iloc[i,1])*DimImg_file[0]/348)
        
    #     print("no")
    return Temp_file,Image_file,DimTemp_file,DimImg_file,Position_Matrix


