import cv2
import numpy as np
def draw_points(x,PX,PY):
    if not isinstance(x, np.ndarray):
       
       x = x.to_numpy()
    
    for j in range (5):
       for i in range (19):
           Image_dotted = cv2.circle(x, (PX[i,j],PY[i,j]), radius=1, color=(0, 0, 255),thickness=-1)
    return Image_dotted