import tkinter as tk

def Observacion_Colada():
    def Close():
        frame.destroy()
    
    def save_text():
        global text_content 
        text_content = inputtxt.get("1.0", "end-1c")
        # print("Text content:", text_content)
        Close()
    
    frame = tk.Tk()
    frame.title("Observaciones Termografía")
    frame.geometry('600x150')
    
    # TextBox Creation
    inputtxt = tk.Text(frame, height=5, width=60)
    inputtxt.pack()
    
    # Button Creation
    printButton = tk.Button(frame, text="Guardar", command=save_text)
    printButton.pack()
    
    frame.mainloop()
    
    return text_content

# text_Content=Observacion_Colada()
# text_Content=Observacion_Colada()