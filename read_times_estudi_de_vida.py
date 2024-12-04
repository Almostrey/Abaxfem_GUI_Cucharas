import pandas as pd
import numpy as np    
import tkinter as tk
from tkinter import filedialog

def read_times_estudi_de_vida():
    root=tk.Tk()
    root.withdraw()
    root.lift()
    root.attributes("-topmost", True)
    root.focus_force()
    Estudio_de_Vida_Path=filedialog.askopenfilename(title="Estudio_de_Vida.xlsx",initialfile="Estudio de Vida")             
    #validarVariablesExcel(Estudio_de_Vida_Path)
    Estudio_de_Vida=pd.read_excel(Estudio_de_Vida_Path,sheet_name="BASE DE DATOS")
    Estudio_de_Vida=Estudio_de_Vida.fillna(0)                                                                                   #todos las celdas que sean NAN se las remplaza por 0 
    tPrecalentamiento_diesel=Estudio_de_Vida.iloc[12:,8].to_numpy()                                                             #tPrecalentamiento_diesel se encuentra en la posicion [12:,8] del arvhico Estudio de vida
    tPrecalentamiento_oxigon=Estudio_de_Vida.iloc[12:,9].to_numpy()                                                             #tPrecalentamiento_oxigon se encuentra en la posicion [12:,9] del arvhico Estudio de vida
    tLF=Estudio_de_Vida.iloc[12:,10].to_numpy()                                                                                 #tLF se encuentra en la posicion[12:,10] del arvhico Estudio de vida
    tMCC_permanencia=Estudio_de_Vida.iloc[12:,11].to_numpy()                                                                    #tMCC_permanencia se encuentra en la posicion [12:,11]del arvhico Estudio de vida                                                             
    tMCC_colado=Estudio_de_Vida.iloc[12:,12].to_numpy()                                                                         #tMCC_colado se encuentra en la posicion [12:,12]del arvhico Estudio de vida        
    tMTTO=Estudio_de_Vida.iloc[12:,13].to_numpy()                                                                               #tMTTOse encuentra en la posicion [12:,13]del arvhico Estudio de vida  
    t_Parada_Noc=Estudio_de_Vida.iloc[12:,14].to_numpy()                                                                        #t_Parada se encuentra en la posicion [12:,14]del arvhico Estudio de vida         
    t=np.column_stack((tPrecalentamiento_diesel,tPrecalentamiento_oxigon,tLF,tMCC_permanencia,tMCC_colado,tMTTO,t_Parada_Noc))  #se crea una sola matriz t en la cual se ubican todos los tiempos del proceso, esta matriz sigue el mismo orden que el archivo Estudio de Vida
    t=np.where(t!="_", t, 0)                                                                                                    #se hace 0 los valores que sean _ o NAN                                                              
    t=np.where(t!=np.nan, t, 0)                                                                                                                                                                  
    
    return t
def validarVariablesExcel(Path: str):
    # Columnas D, G, H, J, K, L, M, N, O
    # Desde la fila 14 hasta abajo
    
    pass
# t=read_times_estudi_de_vida()
if __name__ == "__main__":
    read_times_estudi_de_vida()