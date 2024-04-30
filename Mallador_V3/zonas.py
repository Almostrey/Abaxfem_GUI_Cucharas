import numpy as np
import cv2

def zonas (Image,PX,PY):
    if not isinstance(PX, np.ndarray):
       PX = PX.to_numpy()
    if not isinstance(PY, np.ndarray):
       PY = PY.to_numpy()
    Zone_Position_Limits= np.zeros((8,2),dtype=int)

    Zone_Position_Limits[0,0]=PX[0,0]
    Zone_Position_Limits[0,1]=PY[0,0]
    Zone_Position_Limits[1,0]=PX[0,4]
    Zone_Position_Limits[1,1]=PY[0,4]
    
    
    Zone_Position_Limits[2,0]=PX[6,0]
    Zone_Position_Limits[2,1]=PY[6,0]
    Zone_Position_Limits[3,0]=PX[6,4]
    Zone_Position_Limits[3,1]=PY[6,4]
    
    Zone_Position_Limits[4,0]=PX[11,0]
    Zone_Position_Limits[4,1]=PY[11,0]
    Zone_Position_Limits[5,0]=PX[11,4]
    Zone_Position_Limits[5,1]=PY[11,4]
    
    Zone_Position_Limits[6,0]=PX[18,0]
    Zone_Position_Limits[6,1]=PY[18,0]
    Zone_Position_Limits[7,0]=PX[18,4]
    Zone_Position_Limits[7,1]=PY[18,4]
    color=(0,255,0)
    thickness=1
    for i in range (0,8,2):
        Image_zonas=cv2.line(Image, (Zone_Position_Limits[i,0],Zone_Position_Limits[i,1]), (Zone_Position_Limits[i+1,0],Zone_Position_Limits[i+1,1]), color, thickness) 
    
    return Zone_Position_Limits,Image_zonas
