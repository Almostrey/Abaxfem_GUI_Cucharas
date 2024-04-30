import pandas as pd                     # Para leer datos de excel
from Correccion_Imagen import Corrector_Imagen
from Correccion_Temp import Corrector_Temp
from Graph_visualization import visgraf
from Carga_de_Archivos import Carga_de_Archivos
from mallado_vertical import mallado_vertical
from Distancias_Verticales import distancias_verticales
from refrac_size import refrac_size
from determine_points import determine_points
from draw_points import draw_points
from mallado_horizontal import mallado_horizontal
from retorno_imagen import retorno_imagen
from zonas import zonas
from find_MaxValue import Max_value_matrix
from Correccion_Puntos_Atipicos import Correccion_Puntos_Atipicos

def V1 (Path_to_file_jpg, Path_to_file_xlsx, Position_Matrix):
  

    
    Temp_file,Image_file,DimTemp_file,DimImg_file,Position_Matrix=Carga_de_Archivos(Path_to_file_xlsx,Path_to_file_jpg,Position_Matrix)
    #visgraf(Image_file)
    ###Corrección REAL
    Imagen_Corregida,Position_Matrix_Trans=Corrector_Imagen(Image_file, Position_Matrix)
    Temp_Corregida,Position_Matrix_Trans_Temp,Matr_Div_1_mod_Temp,Matr_Div_2_mod_Temp,Matr_Div_3_mod_Temp,Matr_Div_4_mod_Temp=Corrector_Temp(Temp_file, Position_Matrix)
    #visgraf(Imagen_Corregida)
    


    
    
    dist_vert= distancias_verticales(Position_Matrix_Trans)
    refrac_size_Mat=refrac_size(dist_vert,Position_Matrix_Trans)
    
    PX,PY=determine_points(refrac_size_Mat,Position_Matrix_Trans)
    
    Imagen_dotted=draw_points(Imagen_Corregida,PX,PY)
    
    Matrix_Temp_AV,mean_temp_refrac,max_temp_refrac_AV,min_temp_refrac_AV,std_temp_refrac_AV, Max_temp_general_AV,Max_temp_Zone_Matrix_AV,Min_temp_general_AV,Min_temp_Zone_Matrix_AV=Correccion_Puntos_Atipicos(Position_Matrix_Trans,Matr_Div_1_mod_Temp,Matr_Div_2_mod_Temp,Matr_Div_3_mod_Temp,Matr_Div_4_mod_Temp,PY)
    
    ####Correccion puntos atipicos
    ###Encontrar valores atipicos
    ###
    
#    Max_temp_refrac_Matrix, Max_temp_Zone_Matrix, Max_temp_general=Max_value_matrix(Matr_Div_1_mod_Temp,Matr_Div_2_mod_Temp,Matr_Div_3_mod_Temp,Matr_Div_4_mod_Temp,PY)

    #visgraf(Imagen_dotted)
    
    Image_mallado_Horizontal=mallado_horizontal(Imagen_dotted,PX,PY)
    #visgraf(Image_mallado_Horizontal)
    
    Image_mallado_Vertical=mallado_vertical(Image_mallado_Horizontal, PX,PY)
    #visgraf(Image_mallado_Vertical)
    
    Zone_Position_Limits,Imagen_zonal=zonas (Image_mallado_Vertical,PX,PY)
    #visgraf(Imagen_zonal)
    
    Imagen_Retorno=retorno_imagen(Imagen_zonal, Position_Matrix_Trans,Position_Matrix)
    #visgraf(Imagen_Retorno)
    return Image_file,Imagen_Retorno, Imagen_zonal, Matrix_Temp_AV,mean_temp_refrac,max_temp_refrac_AV,min_temp_refrac_AV,std_temp_refrac_AV, Max_temp_general_AV,Max_temp_Zone_Matrix_AV,Min_temp_general_AV,Min_temp_Zone_Matrix_AV
