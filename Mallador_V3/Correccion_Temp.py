#Librer√≠as
import pandas as pd                     # Para leer datos de excel
import numpy as np                      # Para trabajar matrices
import cv2                              # Para graficar sobre la termograf√≠a
import math  
import pickle
from multiprocessing import Process, Queue                       


def Corrector_Temp(Temp_file, Position_Matrix):
    def recorte_imagen(Temp_file,Position_Matrix):
    
    
        if not isinstance(Position_Matrix, np.ndarray):
            Position_Matrix =Position_Matrix.to_numpy()                          #Convetir la position Matrix a numpy
        DimTemp_file=np.shape(Temp_file)                                         #Obtener las dimensiones de la imagen (Alto, Largo ) 
        
        def creacion_limites_separacion():                                       #Se crea función para delimitar la matriz, con base en los puntos 
            
        
                                                                                 #Se crean matrices de zeros en las cuales se guardaran los valores de los límites que se usan para dividir la imagen en 4 secciones           
            Lim_Pix_I = np.zeros((DimTemp_file[0],2),dtype=int)                  #Matriz de zeros del limite inicio
            Lim_Pix_1_L=np.zeros((DimTemp_file[0],2),dtype=int)                  #Matriz de zeros del limite 1 
            Lim_Pix_2_L=np.zeros((DimTemp_file[0],2),dtype=int)                  #Matriz de zeros del limite 2 
            Lim_Pix_3_L=np.zeros((DimTemp_file[0],2),dtype=int)                  #Matriz de zeros del limite 3 
            Lim_Pix_F = np.zeros((DimTemp_file[0],2),dtype=int)                  #Matriz de zeros del limite Final
            
            
            for i in range (DimTemp_file[0]): 
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
        
        def Divisiones():                                                           #Funcion para dividir la Matriz de Temperaturas
            Matr_Div_1=np.zeros((DimTemp_file[0],DimTemp_file[1]))                  #Se crean matrices en zero para guardar los valores qu se encuentran dentro de los limites previamente establecidos
            Matr_Div_2=np.zeros((DimTemp_file[0],DimTemp_file[1]))
            Matr_Div_3=np.zeros((DimTemp_file[0],DimTemp_file[1]))
            Matr_Div_4=np.zeros((DimTemp_file[0],DimTemp_file[1]))  
            
            
            # def Recortes(Lim_Pix_1,Lim_Pix_2,Temp_file,result_queue):
            #     Matr_Div_n=np.zeros((DimTemp_file[0],DimTemp_file[1])) 
            #     for j in range(DimTemp_file[0]):
            #         for i in range(Lim_Pix_1[j,0],Lim_Pix_2[j,0]):
            #             Matr_Div_n[j,i]=Temp_file[j,i]
            #     Matr_Div_n = pickle.dumps(Matr_Div_n)
            #     result_queue.put(Matr_Div_n)
            # results_queue_1=Queue()
            # results_queue_2=Queue()
            # results_queue_3=Queue()
            # results_queue_4=Queue()
            # p1 = Process(target=Recortes, args=(Lim_Pix_I,Lim_Pix_1_L, results_queue_1))
            # p2 = Process(target=Recortes, args=(Lim_Pix_1_L,Lim_Pix_2_L, results_queue_2))
            # p3 = Process(target=Recortes, args=(Lim_Pix_2_L,Lim_Pix_3_L, results_queue_3))
            # p4 = Process(target=Recortes, args=(Lim_Pix_3_L,Lim_Pix_F, results_queue_4))
            # p1.start()
            # p2.start()
            # p3.start()
            # p4.start()
            # p1.join()
            # p2.join()
            # p3.join()
            # p4.join() 
            # Matr_Div_1 = pickle.loads(results_queue_1.get())
            # Matr_Div_2 = pickle.loads(results_queue_2.get())
            # Matr_Div_3 = pickle.loads(results_queue_3.get())
            # Matr_Div_4 = pickle.loads(results_queue_4.get())           
            
           
            #Recorte 1
            for j in range (DimTemp_file[0]):                                       #El recorte 1 incluye todos los elementos que se encuentran entre las coordenadas de  Lim_Pix_I y Lim_Pix_1_L-1
                for i in range (Lim_Pix_I[j,0],Lim_Pix_1_L[j,0]):                   
                    Matr_Div_1[j,i]=Temp_file[j,i]
                    
            #Recorte 2        
            for j in range (DimTemp_file[0]):                                       #El recorte 2 incluye todos los elementos que se encuentran entre las coordenadas de  Lim_Pix_1_L y Lim_Pix_2_L-1
                for i in range (Lim_Pix_1_L[j,0],Lim_Pix_2_L[j,0]):
                    Matr_Div_2[j,i]=Temp_file[j,i]
            
            #Recorte 3        
            for j in range (DimTemp_file[0]):                                       #El recorte 3 incluye todos los elementos que se encuentran entre las coordenadas de  Lim_Pix_2_L y Lim_Pix_3_L-1
                for i in range (Lim_Pix_2_L[j,0],Lim_Pix_3_L[j,0]):
                    Matr_Div_3[j,i]=Temp_file[j,i]
                    
            #Recorte 4        
            for j in range (DimTemp_file[0]):                                       #El recorte 4 incluye todos los elementos que se encuentran entre las coordenadas de  Lim_Pix_4_L y Lim_Pix_F-1
                for i in range (Lim_Pix_3_L[j,0],Lim_Pix_F[j,0]):
                    Matr_Div_4[j,i]=Temp_file[j,i]
            return Matr_Div_1,Matr_Div_2,Matr_Div_3,Matr_Div_4 
        
        
    
                
        #Codigo en el cual llamo a las funciones
        Lim_Pix_I, Lim_Pix_1_L,Lim_Pix_2_L,Lim_Pix_3_L,Lim_Pix_F=creacion_limites_separacion()                              #Se llama a funcion para determinar los limites de separacion
        Matr_Div_1,Matr_Div_2,Matr_Div_3,Matr_Div_4 =Divisiones()                                                           #Se llama a funcion para determinar las divisones y recortes realizados
    
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
        
    def ajuste_imagen (img,src,dst):
        H, _ = cv2.findHomography(src, dst)
        img_warp = cv2.warpPerspective(img, H, (img.shape[1], img.shape[0]))
        return img_warp
    # def ajuste_imagen_MP (img,src,dst,results_queue):
    #     H, _ = cv2.findHomography(src, dst)
    #     img_warp = cv2.warpPerspective(img, H, (img.shape[1], img.shape[0]))
    #     img_warp=pickle.dumps(img_warp)
    #     results_queue.put(img_warp)
        
    def visgraf(img):
        cv2.imshow("Imagen", img)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()
    
    
    
    
    
    Lim_Pix_I, Lim_Pix_1_L,Lim_Pix_2_L,Lim_Pix_3_L,Lim_Pix_F,Matr_Div_1,Matr_Div_2,Matr_Div_3,Matr_Div_4=recorte_imagen(Temp_file,Position_Matrix )
    Position_Matrix_Trans=Position_Transformation(Position_Matrix)
    src1,dst1,src2,dst2,src3,dst3,src4,dst4=src_dst(Position_Matrix)
    
    # results_queue_1_f=Queue()
    # results_queue_2_f=Queue()
    # results_queue_3_f=Queue()
    # results_queue_4_f=Queue()
    # p1f = Process(target=ajuste_imagen_MP, args=(Matr_Div_1,src1,dst1, results_queue_1_f))
    # p2f = Process(target=ajuste_imagen_MP, args=(Matr_Div_2,src2,dst2, results_queue_2_f))
    # p3f = Process(target=ajuste_imagen_MP, args=(Matr_Div_3,src3,dst3, results_queue_3_f))
    # p4f = Process(target=ajuste_imagen_MP, args=(Matr_Div_4,src4,dst4, results_queue_4_f))
    # p1f.start()
    # p2f.start()
    # p3f.start()
    # p4f.start()
    # p1f.join()
    # p2f.join()
    # p3f.join()
    # p4f.join() 
    # Matr_Div_1_mod = pickle.loads(results_queue_1_f.get())
    # Matr_Div_2_mod = pickle.loads(results_queue_2_f.get())
    # Matr_Div_3_mod = pickle.loads(results_queue_3_f.get())
    # Matr_Div_4_mod = pickle.loads(results_queue_4_f.get()) 
    
    Matr_Div_1_mod=ajuste_imagen (Matr_Div_1,src1,dst1)
    Matr_Div_2_mod=ajuste_imagen (Matr_Div_2,src2,dst2)
    Matr_Div_3_mod=ajuste_imagen (Matr_Div_3,src3,dst3)
    Matr_Div_4_mod=ajuste_imagen (Matr_Div_4,src4,dst4)
    
    Temp_Corregida=Matr_Div_4_mod+Matr_Div_3_mod+Matr_Div_2_mod+Matr_Div_1_mod
    return Temp_Corregida,Position_Matrix_Trans,Matr_Div_1_mod,Matr_Div_2_mod,Matr_Div_3_mod,Matr_Div_4_mod








