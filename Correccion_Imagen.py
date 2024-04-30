#Librer√≠as
import pandas as pd                     # Para leer datos de excel
import numpy as np                      # Para trabajar matrices
import cv2                              # Para graficar sobre la termograf√≠a
import math                         


def Corrector_Imagen(img1, Position_Matrix):
    def recorte_imagen(img1,Position_Matrix):
        #Load the image
    
    
        if not isinstance(Position_Matrix, np.ndarray):
            Position_Matrix =Position_Matrix.to_numpy()                        #Convetir la position Matrix a numpy
        DimImg_file=np.shape(img1)                                         #Obtener las dimensiones de la imagen (Alto, Largo, ) 
        
        def creacion_limites_separacion():                                 #Se crea función para delimitar, con base en los puntos 
            
        
            
            Lim_Pix_I=np.zeros((DimImg_file[0],2),dtype=int)               #Se crean matrices de zeros en las cuales se guardaran los valores de los límites 
            Lim_Pix_1_L=np.zeros((DimImg_file[0],2),dtype=int)
            Lim_Pix_2_L=np.zeros((DimImg_file[0],2),dtype=int)
            Lim_Pix_3_L=np.zeros((DimImg_file[0],2),dtype=int)
            Lim_Pix_F=np.zeros((DimImg_file[0],2),dtype=int)
            
            #Inicio
            for i in range (DimImg_file[0]):                                                                        #Se determinan los pixeles que seran los limites izquierdos de la imagen recortada
                #Inicio                                                                                             #Se determinan los pixeles que seran los limites izquierdos de la imagen recortada
                if Position_Matrix[0,0]==Position_Matrix[9,0]:                                                      #En caso de que los puntos 1 y 10 no tengan variacion en x, sin pendiente
                    Lim_Pix_I[i,0]=int(Position_Matrix[0,0])                                                        #El pixel limite es la coordenada x del punto 1 Para toda la altura de la matriz de temperatura
                    Lim_Pix_I[i,1]=int(i)                                                   
                else:                                                                                               #En caso de que los puntos 1 y 10 tengan variacion en x    
                    mI=(Position_Matrix[0,1]-Position_Matrix[9,1])/(Position_Matrix[0,0]-Position_Matrix[9,0])      #Se calcula la pendiente de la recta que une ambos puntos
                    bI=(-mI*Position_Matrix[0,0]+Position_Matrix[0,1])                                              #Se calcula el valor de la constante b de la recta que une los puntos 
                    Lim_Pix_I[i,0]=int(math.ceil((i-bI)/mI))                                                        #x=(i-b)/m donde i es la coordenada en y
                    Lim_Pix_I[i,1]=int(i)                                                                           #i es la coordenada en y 
                
                
                #Division 1                                                                                         #Se determinan los pixeles que seran los limites centrales izquierdos de la imagen recortada
                if Position_Matrix[1,0]==Position_Matrix[8,0]:                                                      #En caso de que los puntos 2 y 9 no tengan variacion en x, sin pendiente
                    Lim_Pix_1_L[i,0]=int(Position_Matrix[1,0])                                                      #El pixel limite izquierdo de esta division es la coordenada x del punto 2 Para toda la altura de la matriz de temperatura            
                    Lim_Pix_1_L[i,1]=int(i)
                else:                                                                                               #En caso de que los puntos 2 y 9 tengan variacion en x  
                    m1=(Position_Matrix[1,1]-Position_Matrix[8,1])/(Position_Matrix[1,0]-Position_Matrix[8,0])      #Se calcula la pendiente de la recta que une ambos puntos
                    b1=(-m1*Position_Matrix[1,0]+Position_Matrix[1,1])                                              #Se calcula el valor de la constante b de la recta que une los puntos 
                    Lim_Pix_1_L[i,0]=int(math.floor((i-b1)/m1))                                                     #la coordenada en x izquierda de esta division es x=(i-b)/m donde i es la coordenada en y
                    Lim_Pix_1_L[i,1]=int(i)                                                                         #i es la coordenada en y 

                
                
                #Division 2                                                                                         #Se determinan los pixeles que seran los limites centrales de la imagen recortada
                if Position_Matrix[2,0]==Position_Matrix[7,0]:
                    Lim_Pix_2_L[i,0]=int(Position_Matrix[2,0])
                    Lim_Pix_2_L[i,1]=int(i)

            
                else:
                    m2=(Position_Matrix[2,1]-Position_Matrix[7,1])/(Position_Matrix[2,0]-Position_Matrix[7,0])
                    b2=(-m2*Position_Matrix[2,0]+Position_Matrix[2,1])
                    
                    Lim_Pix_2_L[i,0]=int(math.floor((i-b2)/m2))
                    Lim_Pix_2_L[i,1]=int(i)

               
                
               
                #Division 3                                                                                              #Se determinan los pixeles que seran los limites centrales derechos de la imagen recortada
                if Position_Matrix[3,0]==Position_Matrix[6,0]:
                    Lim_Pix_3_L[i,0]=int(Position_Matrix[3,0])
                    Lim_Pix_3_L[i,1]=int(i)
       
                else:
                    m3=(Position_Matrix[3,1]-Position_Matrix[6,1])/(Position_Matrix[3,0]-Position_Matrix[6,0])
                    b3=(-m3*Position_Matrix[3,0]+Position_Matrix[3,1])
                    Lim_Pix_3_L[i,1]=int(i)
                    Lim_Pix_3_L[i,0]=int(math.floor((i-b3)/m3))

                
                #Final                                                                                                   #Se determinan los pixeles que seran los limites derechos de la imagen recortada
                if Position_Matrix[4,0]==Position_Matrix[5,0]:
                    Lim_Pix_F[i,0]=int(Position_Matrix[4,0])
                    Lim_Pix_F[i,1]=int(i)   
                else:
                    mF=(Position_Matrix[4,1]-Position_Matrix[5,1])/(Position_Matrix[4,0]-Position_Matrix[5,0])
                    bF=(-mF*Position_Matrix[4,0]+Position_Matrix[4,1])
                    Lim_Pix_F[i,0]=int(math.floor((i-bF)/mF))
                    Lim_Pix_F[i,1]=int(i)
            return Lim_Pix_I, Lim_Pix_1_L,Lim_Pix_2_L,Lim_Pix_3_L,Lim_Pix_F
        
        def Divisiones():
            Matr_Div_1=np.zeros((DimImg_file[0],DimImg_file[1], DimImg_file[2]),dtype=np.uint8)                         #Se crean matrices en las cuales se guardaran las imagenes correspondientes
            Matr_Div_2=np.zeros((DimImg_file[0],DimImg_file[1], DimImg_file[2]),dtype=np.uint8)
            Matr_Div_3=np.zeros((DimImg_file[0],DimImg_file[1], DimImg_file[2]),dtype=np.uint8)
            Matr_Div_4=np.zeros((DimImg_file[0],DimImg_file[1], DimImg_file[2]),dtype=np.uint8)    
            #Division 1
            for j in range (DimImg_file[0]):
                for i in range (Lim_Pix_I[j,0],Lim_Pix_1_L[j,0]):                                                        #El recorte 1 incluye todos los elementos que se encuentran entre las coordenadas de  Lim_Pix_I y Lim_Pix_1_L-1
                    Matr_Div_1[j,i]=img1[j,i]
            #Division 2      
            for j in range (DimImg_file[0]):                                                                             #El recorte 2 incluye todos los elementos que se encuentran entre las coordenadas de  Lim_Pix_1_L y Lim_Pix_2_L-1
                for i in range (Lim_Pix_1_L[j,0],Lim_Pix_2_L[j,0]):
                    Matr_Div_2[j,i]=img1[j,i]
            #Division 3
            for j in range (DimImg_file[0]):                                                                             #El recorte 3 incluye todos los elementos que se encuentran entre las coordenadas de  Lim_Pix_2_L y Lim_Pix_3_L-1
                for i in range (Lim_Pix_2_L[j,0],Lim_Pix_3_L[j,0]):
                    Matr_Div_3[j,i]=img1[j,i]
            #Division 4        
            for j in range (DimImg_file[0]):
                for i in range (Lim_Pix_3_L[j,0],Lim_Pix_F[j,0]):                                                        #El recorte 4 incluye todos los elementos que se encuentran entre las coordenadas de  Lim_Pix_4_L y Lim_Pix_F-1
                    Matr_Div_4[j,i]=img1[j,i]
            return Matr_Div_1,Matr_Div_2,Matr_Div_3,Matr_Div_4 
        
        
    
                
        #Codigo en el cual llamo a las funciones
        Lim_Pix_I, Lim_Pix_1_L,Lim_Pix_2_L,Lim_Pix_3_L,Lim_Pix_F=creacion_limites_separacion()
        Matr_Div_1,Matr_Div_2,Matr_Div_3,Matr_Div_4 =Divisiones()
    
        return Lim_Pix_I, Lim_Pix_1_L,Lim_Pix_2_L,Lim_Pix_3_L,Lim_Pix_F,Matr_Div_1,Matr_Div_2,Matr_Div_3,Matr_Div_4
    
    
    def Position_Transformation(Position_Matrix):                                                                                     #funcion para determinar los puntos destino a los cuales se va a tranformar la matriz
        if not isinstance(Position_Matrix, np.ndarray):
            Position_Matrix =Position_Matrix.to_numpy()
        Position_Matrix_Trans=np.zeros((10,2),dtype=int)                                                                              #Se crea matriz de zeros que guardara los valores de las coordenadas de destino
        Y_sup=Position_Matrix[7,1]-0.809*(Position_Matrix[5,0]-Position_Matrix[9,0])                                                  #Considerando las las dimensiones de planos de la cuchara, se determina la posicion en x de destino
        
        Position_Matrix_Trans[0,0]=Position_Matrix[8,0]-(Position_Matrix[8,0]-Position_Matrix[9,0])*1.03                              #Considerando las dimensiones de planos de la cuchara, se determina la posicion en x de destino del punto 1 en funcion del punto 10 
        Position_Matrix_Trans[0,1]=Y_sup
        

        Position_Matrix_Trans[4,0]=Position_Matrix[7,0]+(Position_Matrix[5,0]-Position_Matrix[7,0])*1.03                              #Considerando las dimensiones de planos de la cuchara, se determina la posicion en x de destino del punto 5 en funcion del punto 6
        Position_Matrix_Trans[4,1]=Y_sup 
            
        Position_Matrix_Trans[1,0]=(Position_Matrix_Trans[4,0]-Position_Matrix_Trans[0,0])*0.1464+Position_Matrix_Trans[0,0]          #Considerando la perspectiva y las dimensiones de planos de la cuchara, se determina la posicion en x de destino del punto 2 
        Position_Matrix_Trans[1,1]=Y_sup
    
        Position_Matrix_Trans[2,0]=(Position_Matrix_Trans[4,0]-Position_Matrix_Trans[0,0])/2+Position_Matrix_Trans[0,0]               #Considerando la perspectiva y las dimensiones de planos de la cuchara, se determina la posicion en x de destino del punto 3
        Position_Matrix_Trans[2,1]=Y_sup

        
        Position_Matrix_Trans[3,0]=-(Position_Matrix_Trans[4,0]-Position_Matrix_Trans[0,0])*0.1464+Position_Matrix_Trans[4,0]         #Considerando la perspectiva y las dimensiones de planos de la cuchara, se determina la posicion en x de destino del punto 4
        Position_Matrix_Trans[3,1]=Y_sup


#Puntos Inferiores (La posicion en x no se modifica para ninguno de estos puntos. La posicion en Y se la ajusta para que sea igual a la del nodo mas bajo )
        Position_Matrix_Trans[5,0]=Position_Matrix[5,0]
        Position_Matrix_Trans[5,1]= Position_Matrix[7,1]   
        

        Position_Matrix_Trans[6,0]=Position_Matrix[6,0]
        Position_Matrix_Trans[6,1]=Position_Matrix[7,1]
        

        Position_Matrix_Trans[7,0]=Position_Matrix[7,0]
        Position_Matrix_Trans[7,1]= Position_Matrix[7,1] 
        

        Position_Matrix_Trans[8,0]=Position_Matrix[8,0]
        Position_Matrix_Trans[8,1]= Position_Matrix[7,1]
        

        Position_Matrix_Trans[9,0]=Position_Matrix[9,0]
        Position_Matrix_Trans[9,1]=Position_Matrix[7,1] 
        
        return Position_Matrix_Trans
    
    def src_dst(Position_Matrix):
        if not isinstance(Position_Matrix, np.ndarray):
            Position_Matrix =Position_Matrix.to_numpy()
            
        #Origen y Destino para la division o recorte 1 
        src1=np.array([Position_Matrix[0,0],Position_Matrix[0,1],Position_Matrix[1,0],Position_Matrix[1,1],Position_Matrix[8,0],Position_Matrix[8,1],Position_Matrix[9,0],Position_Matrix[9,1]]).reshape((4,1,2))
        dst1=np.array([Position_Matrix_Trans[0,0],Position_Matrix_Trans[0,1],Position_Matrix_Trans[1,0],Position_Matrix_Trans[1,1],Position_Matrix_Trans[8,0],Position_Matrix_Trans[8,1],Position_Matrix_Trans[9,0],Position_Matrix_Trans[9,1]]).reshape((4,1,2))
        
        #Origen y Destino para la division o recorte 2
        src2=np.array([Position_Matrix[1,0],Position_Matrix[1,1],Position_Matrix[2,0],Position_Matrix[2,1],Position_Matrix[7,0],Position_Matrix[7,1],Position_Matrix[8,0],Position_Matrix[8,1]]).reshape((4,1,2))
        dst2=np.array([Position_Matrix_Trans[1,0],Position_Matrix_Trans[1,1],Position_Matrix_Trans[2,0],Position_Matrix_Trans[2,1],Position_Matrix_Trans[7,0],Position_Matrix_Trans[7,1],Position_Matrix_Trans[8,0],Position_Matrix_Trans[8,1]]).reshape((4,1,2))
        
        #Origen y Destino para la division o recorte 3
        src3=np.array([Position_Matrix[2,0],Position_Matrix[2,1],Position_Matrix[3,0],Position_Matrix[3,1],Position_Matrix[6,0],Position_Matrix[6,1],Position_Matrix[7,0],Position_Matrix[7,1]]).reshape((4,1,2))
        dst3=np.array([Position_Matrix_Trans[2,0],Position_Matrix_Trans[2,1],Position_Matrix_Trans[3,0],Position_Matrix_Trans[3,1],Position_Matrix_Trans[6,0],Position_Matrix_Trans[6,1],Position_Matrix_Trans[7,0],Position_Matrix_Trans[7,1]]).reshape((4,1,2))
        
        #Origen y Destino para la division o recorte 4
        src4=np.array([Position_Matrix[3,0],Position_Matrix[3,1],Position_Matrix[4,0],Position_Matrix[4,1],Position_Matrix[5,0],Position_Matrix[5,1],Position_Matrix[6,0],Position_Matrix[6,1]]).reshape((4,1,2))
        dst4=np.array([Position_Matrix_Trans[3,0],Position_Matrix_Trans[3,1],Position_Matrix_Trans[4,0],Position_Matrix_Trans[4,1],Position_Matrix_Trans[5,0],Position_Matrix_Trans[5,1],Position_Matrix_Trans[6,0],Position_Matrix_Trans[6,1]]).reshape((4,1,2))
        return src1,dst1,src2,dst2,src3,dst3,src4,dst4  
    
    
    
    def ajuste_imagen (img,src,dst):                                                    #se utiliza la funcion Homography para cambiar la perspectiva. 
        H, _ = cv2.findHomography(src, dst)
        img_warp = cv2.warpPerspective(img, H, (img.shape[1], img.shape[0]))
        return img_warp
    
    def visgraf(img):
        cv2.imshow("Imagen", img)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()
    
    
    
    
    
    Lim_Pix_I, Lim_Pix_1_L,Lim_Pix_2_L,Lim_Pix_3_L,Lim_Pix_F,Matr_Div_1,Matr_Div_2,Matr_Div_3,Matr_Div_4=recorte_imagen(img1,Position_Matrix )
    Position_Matrix_Trans=Position_Transformation(Position_Matrix)
    src1,dst1,src2,dst2,src3,dst3,src4,dst4=src_dst(Position_Matrix)
    
    
    Matr_Div_1_mod=ajuste_imagen (Matr_Div_1,src1,dst1)
    Matr_Div_2_mod=ajuste_imagen (Matr_Div_2,src2,dst2)
    Matr_Div_3_mod=ajuste_imagen (Matr_Div_3,src3,dst3)
    Matr_Div_4_mod=ajuste_imagen (Matr_Div_4,src4,dst4)
    Imagen_Corregida=Matr_Div_4_mod+Matr_Div_3_mod+Matr_Div_2_mod+Matr_Div_1_mod
    return Imagen_Corregida,Position_Matrix_Trans








