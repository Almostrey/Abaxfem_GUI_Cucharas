import numpy as np
def Max_value_matrix(Matr_Div_1_mod_Temp,Matr_Div_2_mod_Temp,Matr_Div_3_mod_Temp,Matr_Div_4_mod_Temp,PY):
    def find_MaxValue(Matr_Div_n_mod_Temp,PY,n):
        Max_temp_refrac=np.zeros((np.shape(PY)[0]-1,np.shape(PY)[1]-1))
        
        for k in range (np.shape(PY)[0]-1):
            Values=np.zeros((np.shape(Matr_Div_n_mod_Temp)[0],np.shape(Matr_Div_n_mod_Temp)[1]))
            for i in range (PY[k,n],PY[k+1,n]):
                for j in range (np.shape(Matr_Div_n_mod_Temp)[1]):
                    Values[i,j]=Matr_Div_n_mod_Temp[i,j]
            Max_temp_refrac[k,n]=Values.max()
        return Max_temp_refrac
    
    
    Max_temp_refrac_1=find_MaxValue(Matr_Div_1_mod_Temp,PY,0)
    Max_temp_refrac_2=find_MaxValue(Matr_Div_2_mod_Temp,PY,1)
    Max_temp_refrac_3=find_MaxValue(Matr_Div_3_mod_Temp,PY,2)
    Max_temp_refrac_4=find_MaxValue(Matr_Div_4_mod_Temp,PY,3)
    Max_temp_refrac_Matrix=Max_temp_refrac_1+Max_temp_refrac_2+Max_temp_refrac_3+Max_temp_refrac_4
    Values=np.zeros((np.shape(Max_temp_refrac_Matrix)[0],np.shape(Max_temp_refrac_Matrix)[1]))
    Max_temp_Zone_Matrix=np.zeros((3,1))
    for i in range (0,6):
        for j in range (np.shape(Max_temp_refrac_Matrix)[1]):
            Values[i,j]=Max_temp_refrac_Matrix[i,j]
            Max_temp_Zone_Matrix[0,0]=Values.max()
    for i in range (6,11):
        for j in range (np.shape(Max_temp_refrac_Matrix)[1]):
            Values[i,j]=Max_temp_refrac_Matrix[i,j]
            Max_temp_Zone_Matrix[1,0]=Values.max()
    for i in range (11,18):
        for j in range (np.shape(Max_temp_refrac_Matrix)[1]):
            Values[i,j]=Max_temp_refrac_Matrix[i,j]
            Max_temp_Zone_Matrix[2,0]=Values.max()
    Max_temp_general=Max_temp_refrac_Matrix.max ()      
        
    
    return Max_temp_refrac_Matrix, Max_temp_Zone_Matrix,Max_temp_general
    
        
    