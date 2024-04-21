import pandas as pd
from V1 import V1
from V1 import visgraf
import time
import tkinter as tk
from tkinter import filedialog
import os
import numpy as np
# root=tk.Tk()
# root.withdraw()
# Path_to_file_jpg=filedialog.askopenfilename(title="FXX.jpg",initialfile="FXX.jpg")   
# Path_to_file_xlsx=Path_to_file_jpg.replace("jpg","xlsx")
# Path_to_file_jpg=Path_to_file_jpg.replace("/","\\")
# Path_to_file_xlsx=Path_to_file_xlsx.replace("/","\\")

os.chdir(r"S:\23-003-01 CalculoTermicoCucharas\FaseIII Validación\Información Procesada\Documentos\Temperaturas_Cuchara5_Campaña44\Termografías\Frontales_5_44")
start = time.time()




num=1


Position_Matrix= pd.DataFrame(
    
([[78,59],
[127,45],
[246,36],
[364,39],
[414,53],
[408,313],
[361,329],
[249,334],
[136,331],
[91,321]])





)











Path_to_file_xlsx = (f"F{num}.xlsx")                                                                                                            #Path al archivo de excel
Path_to_file_jpg =  Path_to_file_xlsx.replace(".xlsx",".jpg")
# Position_Matrix= pd.DataFrame([[81, 60],             #P1
                        # [126, 46],            #P2
                        # [237, 37],            #P3
                        # [348, 42],            #P4
                        # [395, 54],            #P5
                        # [397, 293],           #P6
                        # [351, 310],           #P7
                        # [243, 319],           #P8
                        # [135, 317],           #P9
                        # [91, 308]])           #P10




# os.chdir(r"C:\Users\ABAXFEM3\Downloads\13FModified")
Image_file,Imagen_Retorno, Imagen_zonal, Matrix_Temp_AV,mean_temp_refrac,max_temp_refrac_AV,min_temp_refrac_AV,std_temp_refrac_AV, Max_temp_general_AV,Max_temp_Zone_Matrix_AV,Min_temp_general_AV,Min_temp_Zone_Matrix_AV = V1 (Path_to_file_jpg, Path_to_file_xlsx, Position_Matrix)
# end = time.time()
# print(end - start) 
# max_=np.reshape(max_temp_refrac_AV,(1,72))
# min_=np.reshape(min_temp_refrac_AV,(1,72))
# std=np.reshape(std_temp_refrac_AV,(1,72))
# mean=np.reshape(mean_temp_refrac,(1,72))
# visgraf("Original",Image_file)
# visgraf("Zonal",Imagen_zonal)
# visgraf("Mallado",Imagen_Retorno)
# cv2.imwrite("13F.jpg",Imagen_Retorno)     
del num,Image_file,Imagen_Retorno,Imagen_zonal,Matrix_Temp_AV,Path_to_file_jpg,Path_to_file_xlsx,start,Position_Matrix
# del Max_temp_general_AV,min_temp_refrac_AV,Min_temp_Zone_Matrix_AV,Min_temp_general_AV,std_temp_refrac_AV, mean_temp_refrac