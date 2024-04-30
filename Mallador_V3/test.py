from V1 import V1
import pandas as pd
import os
import numpy as np

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
[91,321]]))

result = V1("C:/Users/Diego/OneDrive - UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE/Diego/Proyectos/GUI Abaxfem/Archivos Fuente/Fotografias y archivos de termografias/13F.jpg", "C:/Users/Diego/OneDrive - UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE/Diego/Proyectos/GUI Abaxfem/Archivos Fuente/Fotografias y archivos de termografias/13F.xlsx", Position_Matrix)
[Image_file,            Imagen_Retorno,         Imagen_zonal,           Matrix_Temp_AV,                     mean_temp_refrac,   
 max_temp_refrac_AV,    min_temp_refrac_AV,     std_temp_refrac_AV,     Max_temp_general_AV,                Max_temp_Zone_Matrix_AV,
 Min_temp_general_AV,   Min_temp_Zone_Matrix_AV     ] = result

## Guardar
x = float(result[4][1])


print(type(x))