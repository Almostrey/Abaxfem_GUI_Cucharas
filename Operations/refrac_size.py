import numpy as np
import math 
def refrac_size(x, Matrix):
    if not isinstance(x, np.ndarray):
       x = x.to_numpy()
    if not isinstance(Matrix, np.ndarray):
       Matrix = Matrix.to_numpy()
    size_refrac=np.zeros(np.shape(x)[1],dtype=int)
    for i in range (np.shape(x)[1]):
        size_refrac[i]=math.ceil(x[0,i]*100/2099.25)            #regla de 3 2099.95 es la distancia segun el plano, 100 es el grosor del ladrillo, la distancia vertical es x 
    return size_refrac
