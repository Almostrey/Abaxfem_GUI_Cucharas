import numpy as np
import cv2
import math
def Correccion_Puntos_Atipicos(Position_Matrix_Trans,Matr_Div_1_mod_Temp,Matr_Div_2_mod_Temp,Matr_Div_3_mod_Temp,Matr_Div_4_mod_Temp,PY):
    def Position_Matrix_Trans_Atipicos(Position_Matrix_Trans):        #Definicion de la nueva posicion para que las Matr_Div_n_mod sean rectangulares
        Position_Matrix_Trans_AV=np.zeros((10,2),dtype=int)
        Y_sup=int(Position_Matrix_Trans[7,1]-0.809*(Position_Matrix_Trans[5,0]-Position_Matrix_Trans[9,0])) #Se calcula en funcion de los puntos inferiores
        
        #Punto 1
        Position_Matrix_Trans_AV[0,0]=Position_Matrix_Trans[0,0]
        Position_Matrix_Trans_AV[0,1]=Y_sup
        
        #Punto 5
        Position_Matrix_Trans_AV[4,0]=Position_Matrix_Trans[4,0]
        Position_Matrix_Trans_AV[4,1]=Y_sup  
            
        #Punto 2
        Position_Matrix_Trans_AV[1,0]=Position_Matrix_Trans[1,0]
        Position_Matrix_Trans_AV[1,1]=Y_sup
    
        #Punto 3
        Position_Matrix_Trans_AV[2,0]=Position_Matrix_Trans[2,0]
        Position_Matrix_Trans_AV[2,1]=Y_sup
        
        #Punto 4
        Position_Matrix_Trans_AV[3,0]=Position_Matrix_Trans[3,0]
        Position_Matrix_Trans_AV[3,1]=Y_sup
        
        Y_inf=Position_Matrix_Trans[7,1]
        #Punto 6
        Position_Matrix_Trans_AV[5,0]=Position_Matrix_Trans[4,0]
        Position_Matrix_Trans_AV[5,1]=Y_inf 

        #Punto 7
        Position_Matrix_Trans_AV[6,0]=Position_Matrix_Trans[3,0]
        Position_Matrix_Trans_AV[6,1]=Y_inf  


        #Punto 8
        Position_Matrix_Trans_AV[7,0]=Position_Matrix_Trans[2,0]
        Position_Matrix_Trans_AV[7,1]=Y_inf  
        
        #Punto 9
        Position_Matrix_Trans_AV[8,0]=Position_Matrix_Trans[1,0]
        Position_Matrix_Trans_AV[8,1]= Y_inf 
        
        #Punto 10
        Position_Matrix_Trans_AV[9,0]=Position_Matrix_Trans[0,0]
        Position_Matrix_Trans_AV[9,1]=Y_inf 
        return Position_Matrix_Trans_AV,Y_sup,Y_inf
    def src_dst(Position_Matrix_Trans,Position_Matrix_Trans_AV):
        if not isinstance(Position_Matrix_Trans, np.ndarray):
            Position_Matrix_Trans=Position_Matrix_Trans.to_numpy()
            
        #Origen y Destino para la division o recorte 1 
        src1=np.array([Position_Matrix_Trans[0,0],Position_Matrix_Trans[0,1],Position_Matrix_Trans[1,0],Position_Matrix_Trans[1,1],Position_Matrix_Trans[8,0],Position_Matrix_Trans[8,1],Position_Matrix_Trans[9,0],Position_Matrix_Trans[9,1]]).reshape((4,1,2))
        dst1=np.array([Position_Matrix_Trans_AV[0,0],Position_Matrix_Trans_AV[0,1],Position_Matrix_Trans_AV[1,0],Position_Matrix_Trans_AV[1,1],Position_Matrix_Trans_AV[8,0],Position_Matrix_Trans_AV[8,1],Position_Matrix_Trans_AV[9,0],Position_Matrix_Trans_AV[9,1]]).reshape((4,1,2))
        
        #Origen y Destino para la division o recorte 2
        src2=np.array([Position_Matrix_Trans[1,0],Position_Matrix_Trans[1,1],Position_Matrix_Trans[2,0],Position_Matrix_Trans[2,1],Position_Matrix_Trans[7,0],Position_Matrix_Trans[7,1],Position_Matrix_Trans[8,0],Position_Matrix_Trans[8,1]]).reshape((4,1,2))
        dst2=np.array([Position_Matrix_Trans_AV[1,0],Position_Matrix_Trans_AV[1,1],Position_Matrix_Trans_AV[2,0],Position_Matrix_Trans_AV[2,1],Position_Matrix_Trans_AV[7,0],Position_Matrix_Trans_AV[7,1],Position_Matrix_Trans_AV[8,0],Position_Matrix_Trans_AV[8,1]]).reshape((4,1,2))
        
        #Origen y Destino para la division o recorte 3
        src3=np.array([Position_Matrix_Trans[2,0],Position_Matrix_Trans[2,1],Position_Matrix_Trans[3,0],Position_Matrix_Trans[3,1],Position_Matrix_Trans[6,0],Position_Matrix_Trans[6,1],Position_Matrix_Trans[7,0],Position_Matrix_Trans[7,1]]).reshape((4,1,2))
        dst3=np.array([Position_Matrix_Trans_AV[2,0],Position_Matrix_Trans_AV[2,1],Position_Matrix_Trans_AV[3,0],Position_Matrix_Trans_AV[3,1],Position_Matrix_Trans_AV[6,0],Position_Matrix_Trans_AV[6,1],Position_Matrix_Trans_AV[7,0],Position_Matrix_Trans_AV[7,1]]).reshape((4,1,2))
        
        #Origen y Destino para la division o recorte 4
        src4=np.array([Position_Matrix_Trans[3,0],Position_Matrix_Trans[3,1],Position_Matrix_Trans[4,0],Position_Matrix_Trans[4,1],Position_Matrix_Trans[5,0],Position_Matrix_Trans[5,1],Position_Matrix_Trans[6,0],Position_Matrix_Trans[6,1]]).reshape((4,1,2))
        dst4=np.array([Position_Matrix_Trans_AV[3,0],Position_Matrix_Trans_AV[3,1],Position_Matrix_Trans_AV[4,0],Position_Matrix_Trans_AV[4,1],Position_Matrix_Trans_AV[5,0],Position_Matrix_Trans_AV[5,1],Position_Matrix_Trans_AV[6,0],Position_Matrix_Trans_AV[6,1]]).reshape((4,1,2))
        return src1,dst1,src2,dst2,src3,dst3,src4,dst4  
    def Homography (Matrix,src,dst):
        H, _ = cv2.findHomography(src, dst)
        Matrix_warp = cv2.warpPerspective(Matrix, H, (Matrix.shape[1], Matrix.shape[0]))
        return Matrix_warp
   
    
    
    
    Position_Matrix_Trans_AV,Y_sup,Y_inf=Position_Matrix_Trans_Atipicos(Position_Matrix_Trans)
    src1,dst1,src2,dst2,src3,dst3,src4,dst4=src_dst(Position_Matrix_Trans,Position_Matrix_Trans_AV)
    
    
    
    Matr_Div_1_mod_AV=Homography (Matr_Div_1_mod_Temp,src1,dst1)
    Matr_Div_2_mod_AV=Homography (Matr_Div_2_mod_Temp,src2,dst2)
    Matr_Div_3_mod_AV=Homography (Matr_Div_3_mod_Temp,src3,dst3)
    Matr_Div_4_mod_AV=Homography (Matr_Div_4_mod_Temp,src4,dst4)
    
    #Eliminacion de datos para posterior append
    Matr_Div_1_mod_AV=Matr_Div_1_mod_AV[Y_sup:Y_inf,Position_Matrix_Trans_AV[0,0]:Position_Matrix_Trans_AV[1,0]]
    Matr_Div_2_mod_AV=Matr_Div_2_mod_AV[Y_sup:Y_inf,Position_Matrix_Trans_AV[1,0]:Position_Matrix_Trans_AV[2,0]]
    Matr_Div_3_mod_AV=Matr_Div_3_mod_AV[Y_sup:Y_inf,Position_Matrix_Trans_AV[2,0]:Position_Matrix_Trans_AV[3,0]]
    Matr_Div_4_mod_AV=Matr_Div_4_mod_AV[Y_sup:Y_inf,Position_Matrix_Trans_AV[3,0]:Position_Matrix_Trans_AV[4,0]]
    #Append
    

    
    
    
    #Posicion en Y de las divisiones.  
    PYD_AV=np.zeros((np.shape(PY)[0],1),dtype=int)
    Size_Refrac=((Position_Matrix_Trans_AV[-1,1]-Position_Matrix_Trans_AV[0,1])/(np.shape(PY)[0]-1))
    for i in range (1,np.shape(PY)[0]):
        PYD_AV[i,0]=int(Size_Refrac*i)
    PYD_AV[np.shape(PY)[0]-1,0] = Position_Matrix_Trans_AV[-1,1]- Position_Matrix_Trans_AV[0,1]   
    
    
    mean_temp_refrac=np.zeros((len(PY)-1,4))
    max_temp_refrac_AV=np.zeros((len(PY)-1,4))
    min_temp_refrac_AV=np.zeros((len(PY)-1,4))
    std_temp_refrac_AV=np.zeros((len(PY)-1,4))
    
    Matr_Apoyo=[None]*(len(PY)-1)
    for i in range (len(PY)-1):
        Matr_refrac=np.copy(Matr_Div_1_mod_AV[PYD_AV[i,0]:PYD_AV[i+1,0],:])
        std=np.std(Matr_refrac)
        mean=np.mean(Matr_refrac)
        mask=(Matr_refrac<=(mean-2*std)) | (Matr_refrac>=(mean+2*std))
        Matr_refrac[mask] = mean
        Matr_Apoyo[i]=np.copy(Matr_refrac)
        mean_temp_refrac[i,0]=mean
        max_temp_refrac_AV[i,0]=Matr_refrac.max()
        min_temp_refrac_AV[i,0]=Matr_refrac.min()
        std_temp_refrac_AV[i,0]=std
        
    Matr_Div_1_mod_AV =np.vstack(Matr_Apoyo)
    
    Matr_Apoyo=[None]*(len(PY)-1)
    for i in range (len(PY)-1):
        Matr_refrac=np.copy(Matr_Div_2_mod_AV[PYD_AV[i,0]:PYD_AV[i+1,0],:])
        std=np.std(Matr_refrac)
        mean=np.mean(Matr_refrac)
        mask=(Matr_refrac<=(mean-2*std)) | (Matr_refrac>=(mean+2*std))
        Matr_refrac[mask] = mean
        Matr_Apoyo[i]=np.copy(Matr_refrac)
        mean_temp_refrac[i,1]=mean
        max_temp_refrac_AV[i,1]=Matr_refrac.max()
        min_temp_refrac_AV[i,1]=Matr_refrac.min()
        std_temp_refrac_AV[i,1]=std
    Matr_Div_2_mod_AV =np.vstack(Matr_Apoyo)
    
    Matr_Apoyo=[None]*(len(PY)-1)
    for i in range (len(PY)-1):
        Matr_refrac=np.copy(Matr_Div_3_mod_AV[PYD_AV[i,0]:PYD_AV[i+1,0],:])
        std=np.std(Matr_refrac)
        mean=np.mean(Matr_refrac)
        mask=(Matr_refrac<=(mean-2*std)) | (Matr_refrac>=(mean+2*std))
        Matr_refrac[mask] = mean
        Matr_Apoyo[i]=np.copy(Matr_refrac)
        mean_temp_refrac[i,2]=mean
        max_temp_refrac_AV[i,2]=Matr_refrac.max()
        min_temp_refrac_AV[i,2]=Matr_refrac.min()
        std_temp_refrac_AV[i,2]=std
    Matr_Div_3_mod_AV =np.vstack(Matr_Apoyo)
    
    Matr_Apoyo=[None]*(len(PY)-1)
    for i in range (len(PY)-1):
        Matr_refrac=np.copy(Matr_Div_4_mod_AV[PYD_AV[i,0]:PYD_AV[i+1,0],:])
        std=np.std(Matr_refrac)
        mean=np.mean(Matr_refrac)
        mask=(Matr_refrac<=(mean-2*std)) | (Matr_refrac>=(mean+2*std))
        Matr_refrac[mask] = mean
        Matr_Apoyo[i]=np.copy(Matr_refrac)
        mean_temp_refrac[i,3]=mean
        max_temp_refrac_AV[i,3]=Matr_refrac.max()
        min_temp_refrac_AV[i,3]=Matr_refrac.min()
        std_temp_refrac_AV[i,3]=std
    Matr_Div_4_mod_AV =np.vstack(Matr_Apoyo)
    
    Max_temp_Zone_Matrix_AV=np.array(([max_temp_refrac_AV[0:6,:].max()],
                                      [max_temp_refrac_AV[6:11,:].max()],
                                      [max_temp_refrac_AV[11:18,:].max()]))
    Max_temp_general_AV=Max_temp_Zone_Matrix_AV.max()
    
    Min_temp_Zone_Matrix_AV=np.array(([min_temp_refrac_AV[0:6,:].min()],
                                      [min_temp_refrac_AV[6:11,:].min()],
                                      [min_temp_refrac_AV[11:18,:].min()]))
    Min_temp_general_AV=Min_temp_Zone_Matrix_AV.min()
    
    
    Matrix_Temp_AV = np.hstack((Matr_Div_1_mod_AV,Matr_Div_2_mod_AV,Matr_Div_3_mod_AV,Matr_Div_4_mod_AV))
    return Matrix_Temp_AV,mean_temp_refrac,max_temp_refrac_AV,min_temp_refrac_AV,std_temp_refrac_AV, Max_temp_general_AV,Max_temp_Zone_Matrix_AV,Min_temp_general_AV,Min_temp_Zone_Matrix_AV
    
