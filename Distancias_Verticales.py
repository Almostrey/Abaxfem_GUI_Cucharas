import numpy as np
import pandas as pd

def distancias_verticales(x):
    if not isinstance(x, np.ndarray):
       x = x.to_numpy()
    Dim_x=np.shape(x)
    
    
    
    
    dist_vert=np.zeros((1,int(Dim_x[0]/2)),dtype=int)
    for i in range (int(Dim_x[0]/2)):
        dist_vert[0,i]=int(-x[i,1]+x[Dim_x[0]-(i+1),1])
    return dist_vert
