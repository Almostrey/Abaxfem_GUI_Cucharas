import pandas as pd
import numpy as np    
import tkinter as tk
from tkinter import filedialog

def read_temps_medidas():
    root=tk.Tk()
    root.withdraw()
    Temps_medidas_Path=filedialog.askopenfilename(title="Temps_medidas.xlsx",initialfile="Temps_medidas")   
    Temps_medidas=pd.read_excel(Temps_medidas_Path)
    colada=Temps_medidas.iloc[0:,0].to_numpy()
    temp=Temps_medidas.iloc[0:,1].to_numpy()
    temp_medidas=np.column_stack((colada,temp))
    temp_medidas=np.where(temp_medidas!="_", temp_medidas, 0)
    temp_medidas[np.isnan(temp_medidas)] = 0
    
    return temp_medidas