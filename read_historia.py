import pandas as pd  
import tkinter as tk
from tkinter import filedialog

def read_historia(path):
    #root=tk.Tk()
    #root.withdraw()
    
    #Historia_Path=filedialog.askopenfilename(title="Historia.xlsx",initialfile="Historia")   
    Historia=pd.read_excel(path,header=None)
    
    Historia=Historia.to_numpy()
    
    return Historia