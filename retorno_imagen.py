#Librer√≠as
import pandas as pd                     # Para leer datos de excel
import numpy as np                      # Para trabajar matrices
import cv2                              # Para graficar sobre la termograf√≠a
import math                         


def retorno_imagen(img1, Position_Matrix,Position_Matrix_Trans):
    if not isinstance(Position_Matrix_Trans, np.ndarray):
        Position_Matrix_Trans = Position_Matrix_Trans.to_numpy()
    def recorte_imagen(img1,Position_Matrix):
        #Load the image
    
    
        if not isinstance(Position_Matrix, np.ndarray):
            Position_Matrix =Position_Matrix.to_numpy()                        #Convetir la position Matrix a numpy
        DimImg_file=np.shape(img1)                                         #Obtener las dimensiones de la imagen (Alto, Largo, ) 
        
        def creacion_limites_separacion():                                 #Se crea función para delimitar, con base en los puntos 
            
        
            
            Lim_Pix_I=np.zeros((DimImg_file[0],2),dtype=int)               #Se crean matrices de zeros en las cuales se guardaran los valores de los límites 
            Lim_Pix_1_L=np.zeros((DimImg_file[0],2),dtype=int)
            Lim_Pix_1_R=np.zeros((DimImg_file[0],2),dtype=int)
            Lim_Pix_2_L=np.zeros((DimImg_file[0],2),dtype=int)
            Lim_Pix_2_R=np.zeros((DimImg_file[0],2),dtype=int)
            Lim_Pix_3_L=np.zeros((DimImg_file[0],2),dtype=int)
            Lim_Pix_3_R=np.zeros((DimImg_file[0],2),dtype=int)
            Lim_Pix_F=np.zeros((DimImg_file[0],2),dtype=int)
            
            #Inicio
            for i in range (DimImg_file[0]):                                                                        #Se determinan los pixeles que seran los limites izquierdos de la imagen recortada
                if Position_Matrix[0,0]==Position_Matrix[9,0]:
                    Lim_Pix_I[i,0]=int(Position_Matrix[0,0])
                    Lim_Pix_I[i,1]=int(i)
                else:
                    mI=(Position_Matrix[0,1]-Position_Matrix[9,1])/(Position_Matrix[0,0]-Position_Matrix[9,0])
                    bI=(-mI*Position_Matrix[0,0]+Position_Matrix[0,1])
                    Lim_Pix_I[i,0]=int(math.ceil((i-bI)/mI))
                    Lim_Pix_I[i,1]=int(i)
                
                
                #Division 1                                                                                              #Se determinan los pixeles que seran los limites centrales izquierdos de la imagen recortada
                if Position_Matrix[1,0]==Position_Matrix[8,0]:
                    Lim_Pix_2_L[i,0]=int(Position_Matrix[1,0])
                    Lim_Pix_2_L[i,1]=int(i)
                else:
                    m1=(Position_Matrix[1,1]-Position_Matrix[8,1])/(Position_Matrix[1,0]-Position_Matrix[8,0])
                    b1=(-m1*Position_Matrix[1,0]+Position_Matrix[1,1])
                    Lim_Pix_1_L[i,0]=int(math.floor((i-b1)/m1))
                    Lim_Pix_1_L[i,1]=int(i)
                
                
                #Division 2                                                                                              #Se determinan los pixeles que seran los limites centrales de la imagen recortada
                if Position_Matrix[2,0]==Position_Matrix[7,0]:
                    Lim_Pix_2_L[i,0]=int(Position_Matrix[2,0])
                    Lim_Pix_2_L[i,1]=int(i)
            
                else:
                    m2=(Position_Matrix[2,1]-Position_Matrix[7,1])/(Position_Matrix[2,0]-Position_Matrix[7,0])
                    b2=(-m2*Position_Matrix[2,0]+Position_Matrix[2,1])
                    
                    Lim_Pix_2_L[i,0]=int(math.ceil((i-b2)/m2))
                    Lim_Pix_2_L[i,1]=int(i)
               
                
               
                #Division 3                                                                                              #Se determinan los pixeles que seran los limites centrales derechos de la imagen recortada
                if Position_Matrix[3,0]==Position_Matrix[6,0]:
                    Lim_Pix_3_L[i,0]=int(Position_Matrix[3,0])
                    Lim_Pix_3_L[i,1]=int(i)
                else:
                    m3=(Position_Matrix[3,1]-Position_Matrix[6,1])/(Position_Matrix[3,0]-Position_Matrix[6,0])
                    b3=(-m3*Position_Matrix[3,0]+Position_Matrix[3,1])
                    Lim_Pix_3_L[i,1]=int(i)
                    Lim_Pix_3_L[i,0]=int(math.ceil((i-b3)/m3))
                
                #Final                                                                                                   #Se determinan los pixeles que seran los limites derechos de la imagen recortada
                if Position_Matrix[4,0]==Position_Matrix[5,0]:
                    Lim_Pix_I[i,0]=int(Position_Matrix[4,0])
                    Lim_Pix_I[i,1]=int(i)   
                else:
                    mF=(Position_Matrix[4,1]-Position_Matrix[5,1])/(Position_Matrix[4,0]-Position_Matrix[5,0])
                    bF=(-mF*Position_Matrix[4,0]+Position_Matrix[4,1])
                    Lim_Pix_F[i,0]=int(math.ceil((i-bF)/mF))
                    Lim_Pix_F[i,1]=int(i)
            return Lim_Pix_I, Lim_Pix_1_L,Lim_Pix_2_L,Lim_Pix_3_L,Lim_Pix_F
        
        def Divisiones():
            Matr_Div_1=np.zeros((DimImg_file[0],DimImg_file[1], DimImg_file[2]),dtype=np.uint8)
            Matr_Div_2=np.zeros((DimImg_file[0],DimImg_file[1], DimImg_file[2]),dtype=np.uint8)
            Matr_Div_3=np.zeros((DimImg_file[0],DimImg_file[1], DimImg_file[2]),dtype=np.uint8)
            Matr_Div_4=np.zeros((DimImg_file[0],DimImg_file[1], DimImg_file[2]),dtype=np.uint8)    
            for j in range (DimImg_file[0]):
                for i in range (Lim_Pix_I[j,0],Lim_Pix_1_L[j,0]):
                    Matr_Div_1[j,i]=img1[j,i]
                    
            for j in range (DimImg_file[0]):
                for i in range (Lim_Pix_1_L[j,0],Lim_Pix_2_L[j,0]):
                    Matr_Div_2[j,i]=img1[j,i]
                    
            for j in range (DimImg_file[0]):
                for i in range (Lim_Pix_2_L[j,0],Lim_Pix_3_L[j,0]):
                    Matr_Div_3[j,i]=img1[j,i]
                    
            for j in range (DimImg_file[0]):
                for i in range (Lim_Pix_3_L[j,0],Lim_Pix_F[j,0]):
                    Matr_Div_4[j,i]=img1[j,i]
            return Matr_Div_1,Matr_Div_2,Matr_Div_3,Matr_Div_4 
        
        
    
                
        #Codigo en el cual llamo a las funciones
        Lim_Pix_I, Lim_Pix_1_L,Lim_Pix_2_L,Lim_Pix_3_L,Lim_Pix_F=creacion_limites_separacion()
        Matr_Div_1,Matr_Div_2,Matr_Div_3,Matr_Div_4 =Divisiones()
    
        return Lim_Pix_I, Lim_Pix_1_L,Lim_Pix_2_L,Lim_Pix_3_L,Lim_Pix_F,Matr_Div_1,Matr_Div_2,Matr_Div_3,Matr_Div_4
    
    
   
    def src_dst(Position_Matrix):
        if not isinstance(Position_Matrix, np.ndarray):
            Position_Matrix =Position_Matrix.to_numpy()

        src1=np.array([Position_Matrix[0,0],Position_Matrix[0,1],Position_Matrix[1,0],Position_Matrix[1,1],Position_Matrix[8,0],Position_Matrix[8,1],Position_Matrix[9,0],Position_Matrix[9,1]]).reshape((4,1,2))
        dst1=np.array([Position_Matrix_Trans[0,0],Position_Matrix_Trans[0,1],Position_Matrix_Trans[1,0],Position_Matrix_Trans[1,1],Position_Matrix_Trans[8,0],Position_Matrix_Trans[8,1],Position_Matrix_Trans[9,0],Position_Matrix_Trans[9,1]]).reshape((4,1,2))
        
        src2=np.array([Position_Matrix[1,0],Position_Matrix[1,1],Position_Matrix[2,0],Position_Matrix[2,1],Position_Matrix[7,0],Position_Matrix[7,1],Position_Matrix[8,0],Position_Matrix[8,1]]).reshape((4,1,2))
        dst2=np.array([Position_Matrix_Trans[1,0],Position_Matrix_Trans[1,1],Position_Matrix_Trans[2,0],Position_Matrix_Trans[2,1],Position_Matrix_Trans[7,0],Position_Matrix_Trans[7,1],Position_Matrix_Trans[8,0],Position_Matrix_Trans[8,1]]).reshape((4,1,2))
        
        src3=np.array([Position_Matrix[2,0],Position_Matrix[2,1],Position_Matrix[3,0],Position_Matrix[3,1],Position_Matrix[6,0],Position_Matrix[6,1],Position_Matrix[7,0],Position_Matrix[7,1]]).reshape((4,1,2))
        dst3=np.array([Position_Matrix_Trans[2,0],Position_Matrix_Trans[2,1],Position_Matrix_Trans[3,0],Position_Matrix_Trans[3,1],Position_Matrix_Trans[6,0],Position_Matrix_Trans[6,1],Position_Matrix_Trans[7,0],Position_Matrix_Trans[7,1]]).reshape((4,1,2))
        
        src4=np.array([Position_Matrix[3,0],Position_Matrix[3,1],Position_Matrix[4,0],Position_Matrix[4,1],Position_Matrix[5,0],Position_Matrix[5,1],Position_Matrix[6,0],Position_Matrix[6,1]]).reshape((4,1,2))
        dst4=np.array([Position_Matrix_Trans[3,0],Position_Matrix_Trans[3,1],Position_Matrix_Trans[4,0],Position_Matrix_Trans[4,1],Position_Matrix_Trans[5,0],Position_Matrix_Trans[5,1],Position_Matrix_Trans[6,0],Position_Matrix_Trans[6,1]]).reshape((4,1,2))
        return src1,dst1,src2,dst2,src3,dst3,src4,dst4  
        
    def ajuste_imagen (img,src,dst):
        H, _ = cv2.findHomography(src, dst)
        img_warp = cv2.warpPerspective(img, H, (img.shape[1], img.shape[0]))
        return img_warp
    
    def visgraf(img):
        cv2.imshow("Imagen", img)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()
    
    
    
    
    
    Lim_Pix_I, Lim_Pix_1_L,Lim_Pix_2_L,Lim_Pix_3_L,Lim_Pix_F,Matr_Div_1,Matr_Div_2,Matr_Div_3,Matr_Div_4=recorte_imagen(img1,Position_Matrix )
    src1,dst1,src2,dst2,src3,dst3,src4,dst4=src_dst(Position_Matrix)
    
    
    Matr_Div_1_mod=ajuste_imagen (Matr_Div_1,src1,dst1)
    Matr_Div_2_mod=ajuste_imagen (Matr_Div_2,src2,dst2)
    Matr_Div_3_mod=ajuste_imagen (Matr_Div_3,src3,dst3)
    Matr_Div_4_mod=ajuste_imagen (Matr_Div_4,src4,dst4)
    Imagen_Corregida=Matr_Div_4_mod+Matr_Div_3_mod+Matr_Div_2_mod+Matr_Div_1_mod
    return Imagen_Corregida










