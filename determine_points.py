import numpy as np
def determine_points(size_refrac,Matrix):                                       #funcion para crear puntos que permitan crear el mallado    
    
    if not isinstance(size_refrac, np.ndarray):             
       size_refrac = size_refrac.to_numpy()
    if not isinstance(Matrix, np.ndarray):
       Matrix = Matrix.to_numpy()
    
    PX=np.zeros((19,5),dtype=int)                                               #Matriz de las coordenadas en X de los puntos creados para el mallado 
    PY=np.zeros((19,5),dtype=int)                                               #Matriz de las coordenadas en Y de los puntos creados para el mallado 
    for j in range(5):
        for i in range(19):     
            PY[i,j]=i*size_refrac[j]+Matrix[j,1]
    
    
    for j in range (5):
        for i in range (19):
            delta_x=0
            delta_x_t=(Matrix[j,0]-Matrix[-(1+j),0])                           #se utiliza la formula deltaY1/deltaX1=deltaY/deltaX     
            delta_y_t=abs(Matrix[j,1]-Matrix[-(1+j),1])
            if Matrix[j,0]==Matrix[-j,0]:
                delta_x=0
            else:                 
                m=delta_x_t/delta_y_t
                delta_y=i*size_refrac[j]
                delta_x=m*delta_y          
                
                
            PX[i,j]=+Matrix[j,0]-delta_x
                
            

            
    return PX,PY

