# Librerias

from propiedadesFisicas import propiedadesFisicas
from radiacion import radiacion
from matrizKGyCG_Med import matrizKGyCG
from matrizRG import matrizRG
from evaluacion import evaluacion

def Proceso_Elementos_Finitos(colada,NNod,N1,TInicial,N2,N3,N4,N5,calentado,carga,descarga,TinternaCarga,Tinterna,Tamb,Long1,NElemMaterial,NElemTotal,NMateriales,Conec,dt,Tacero):
    rho, Cp, hConvInt, hConvExt= propiedadesFisicas (colada,NNod,N1,TInicial,N2,N3,N4,N5,calentado,carga,descarga)                                                                   # Define los parámetros geométricos y propiedades físicas del modelo
    hRadInt, hRadExt = radiacion (TInicial,Tamb,calentado,carga,descarga,TinternaCarga,Tinterna)                                                                           # Calcula el coeficiente de radiación térmico
    KG, CG, dx1, dx2, dx3, dx4, dx5= matrizKGyCG (Long1,NElemMaterial,NNod,NElemTotal,NMateriales,TInicial,Cp,rho,Conec,hConvExt,hRadExt,hConvInt,hRadInt,calentado,carga,descarga)      # Cálculo de la matriz de conductividad y la de capacitancia
    RG= matrizRG (NNod,Tamb,hConvExt,hRadExt, calentado, carga, descarga, TinternaCarga,hConvInt,hRadInt,Tinterna)                                          # Definición de matriz de cargas globales
    TFinal, TInicial,check= evaluacion (CG,KG,dt,TInicial,RG,carga, Tacero)   
    return  rho, Cp, hConvInt, hConvExt,  hRadInt, hRadExt, KG, CG, dx1, dx2, dx3, dx4, dx5,RG,TFinal, TInicial,check           