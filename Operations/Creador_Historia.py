import numpy as np 

def Creador_Historia(Historia,NNod,colada,Long1,TFinal,tasaDesgaste):
    Historia_Apoyo=np.zeros((1,NNod+3))
    Historia_Apoyo[0,0]=colada
    Historia_Apoyo[0,1]=Long1[0]
    for i in range (np.shape(TFinal)[0]):
        Historia_Apoyo[0,i+2]=TFinal[i]
    Historia_Apoyo[0,-1]=tasaDesgaste
    Historia=np.append(Historia, Historia_Apoyo, axis=0)
    return Historia