import numpy as np
import cv2

def mallado_horizontal(Image_file, PX,PY):
    color=(255,0,0)                                                                                                                           #Se define el color de las l√≠neas de la malla                    
    thickness=1  
    if not isinstance(PX, np.ndarray):
       PX = PX.to_numpy()
    if not isinstance(PY, np.ndarray):
       PY = PY.to_numpy()   
    Dim_PX=np.shape(PX)
    for j in range (Dim_PX[1]-1):
        for i in range (Dim_PX[0]):
            Image_mallado_Horizontal=cv2.line(Image_file, (PX[i,j],PY[i,j]), (PX[i,j+1],PY[i,j+1]), color, thickness)
        
    return Image_mallado_Horizontal