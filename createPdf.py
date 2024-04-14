from xhtml2pdf import pisa
import jinja2
import subprocess
from datetime import datetime
import dataManager
import databaseLoginManage as dbLManager
from time import sleep
from os import getcwd

def getMaxInformation(nameCuchara:str, nameCampana:str):
    [col, maxF, maxT, escoria] = dataManager.getMaxHistory(nameCuchara, nameCampana)
    #Frontal
    HTmaxCucharaF = str(max(maxF))
    colMaxTempF = str(col[maxF.index(max(maxF))])
    HTminCucharaF = str(min(maxF))
    colMinTempF = str(col[maxF.index(min(maxF))])
    HTmeanCucharaF = str(sum(maxF)/len(maxF))
    pathImgFrontal = "Historial/CUCHARA_"+nameCuchara+"/CUCHARA_"+nameCuchara+"_CAMPANA_"+nameCampana+"/AnalisisTemperaturasFrontal.png"
    # Trasera
    HTmaxCucharaT = str(max(maxT))
    colMaxTempT = str(col[maxT.index(max(maxT))])
    HTminCucharaT = str(min(maxT))
    colMinTempT = str(col[maxT.index(min(maxT))])
    HTmeanCucharaT = str(sum(maxF)/len(maxF))
    pathImgTrasera = "Historial/CUCHARA_"+nameCuchara+"/CUCHARA_"+nameCuchara+"_CAMPANA_"+nameCampana+"/AnalisisTemperaturasTrasero.png"
    return [HTmaxCucharaF, colMaxTempF, HTminCucharaF, colMinTempF, HTmeanCucharaF, pathImgFrontal, 
            HTmaxCucharaT, colMaxTempT, HTminCucharaT, colMinTempT, HTmeanCucharaT, pathImgTrasera]

def getGeneralInformation(nameCuchara:str, nameCampana:str):
    date = datetime.strftime(datetime.now(), '%d/%m/%Y')
    time = datetime.strftime(datetime.now(), '%H:%M:%S')
    briefHistory = dbLManager.getBriefHistory(5)
    Username = briefHistory[len(briefHistory)-1][2]
    function = briefHistory[len(briefHistory)-1][1]
    ultimaColada = dataManager.getNameColadas(nameCuchara, nameCampana)[-1]
    coladaEscoria = str(dataManager.getEscoria(nameCuchara))
    dateInicio = dataManager.getCreationDateCampana(nameCuchara, nameCampana)
    dateFin = date
    return [date, time, Username, function, ultimaColada, coladaEscoria, dateInicio, dateFin]

def createPDF(nameCuchara:str, nameCampana:str, tipoGeneracion:str):
    [date, time, Username, function, ultimaColada, coladaEscoria, dateInicio, dateFin] = getGeneralInformation(nameCuchara, nameCampana)
    [HTmaxCucharaF, colMaxTempF, HTminCucharaF, colMinTempF, HTmeanCucharaF, pathImgFrontal,
     HTmaxCucharaT, colMaxTempT, HTminCucharaT, colMinTempT, HTmeanCucharaT, pathImgTrasera] = getMaxInformation(nameCuchara, nameCampana)
    loader = jinja2.FileSystemLoader("./")
    env = jinja2.Environment(loader = loader)
    htmlTemplate = "Template"
    template = env.get_template(htmlTemplate)
    if tipoGeneracion=="auto":
        tipoGeneracion = "Generaci&oacute;n autom&aacute;tica por fin de campa&ntilde;a."
    else:
        if tipoGeneracion=="manual":
            tipoGeneracion = "Generaci&oacute;n manual por parte del usuario."
        else:
            tipoGeneracion="Alguien ha alterado los archivos del programa."
    context = {'date' : date,
           'time' : time,
           'Username' : Username,
           'function' : function,
           'nameCuchara' : nameCuchara,
           'nameCampana' : nameCampana,
           'ultimaColada' : ultimaColada,
           'coladaEscoria' : coladaEscoria,
           'dateInicio' : dateInicio,
           'dateFin' : dateFin,
           'tipoGeneracion': tipoGeneracion,
            # Fronta;
           'HTmaxCucharaF' : HTmaxCucharaF,
           'colMaxTempF' : colMaxTempF,
           'HTminCucharaF' : HTminCucharaF,
           'colMinTempF' : colMinTempF,
           'HTmeanCucharaF' : HTmeanCucharaF,
           'pathImgFrontal' : pathImgFrontal,
            # Trasera
           'HTmaxCucharaT' : HTmaxCucharaT,
           'colMaxTempT' : colMaxTempT,
           'HTminCucharaT' : HTminCucharaT,
           'colMinTempT' : colMinTempT,
           'HTmeanCucharaT' : HTmeanCucharaT,
           'pathImgTrasera' : pathImgTrasera
           }
    result_file = open("Historial/CUCHARA_"+nameCuchara+"/CUCHARA_"+nameCuchara+"_CAMPANA_"+nameCampana+"/Reporte Cuchara "+nameCuchara+" - Campana "+str(nameCampana)+".pdf", "w+b")
    output_text = template.render(context)
    pdf = pisa.CreatePDF(output_text, dest=result_file)
    result_file.close()
    subprocess.Popen("Historial/CUCHARA_"+nameCuchara+"/CUCHARA_"+nameCuchara+"_CAMPANA_"+nameCampana+"/Reporte Cuchara "+nameCuchara+" - Campana "+str(nameCampana)+".pdf",shell=True)
    
'''# Generales
date = "20/12/2023"
time = "22:07:10"
Username = "Diego"
function = "ADMINISTRADOR"
nameCuchara = "1"
nameCampana = "11"
ultimaColada = "111"
coladaEscoria = "12"
dateInicio = "01/12/2023"
dateFin = "20/12/2023"
tipoGeneracion = "auto"
# Frontal
HTmaxCucharaF = "350"
colMaxTempF = "111"
HTminCucharaF = "200"
colMinTempF = "11"
HTmeanCucharaF = "300"
pathImgFrontal = "Historial/CUCHARA_Cucha45/CUCHARA_Cucha45_CAMPANA_1/AnalisisTemperaturasFrontal.png"
# Trasera
HTmaxCucharaT = "500"
colMaxTempT = "501"
HTminCucharaT = "100"
colMinTempT = "1"
HTmeanCucharaT = "350"
pathImgTrasera = "Historial/CUCHARA_Cucha45/CUCHARA_Cucha45_CAMPANA_1/AnalisisTemperaturasTrasero.png"
# Frontal - Zona 1
HTmaxZonasF1 = "500"
colMaxZonasF1 = "501"
HTminZonasF1 = "100"
colMinZonasF1 = "1"
HTmeanZonasF1 = "350"
pathImgZona1F = "Historial/CUCHARA_Cucha45/CUCHARA_Cucha45_CAMPANA_1/AnalisisTemperaturasTrasero.png"
# Frontal - Zona 2
HTmaxZonasF2 = "500"
colMaxZonasF2 = "501"
HTminZonasF2 = "100"
colMinZonasF2 = "1"
HTmeanZonasF2 = "350"
pathImgZona2F = "Historial/CUCHARA_Cucha45/CUCHARA_Cucha45_CAMPANA_1/AnalisisTemperaturasTrasero.png"
# Frontal - Zona 3
HTmaxZonasF3 = "500"
colMaxZonasF3 = "501"
HTminZonasF3 = "100"
colMinZonasF3 = "1"
HTmeanZonasF3 = "350"
pathImgZona3F = "Historial/CUCHARA_Cucha45/CUCHARA_Cucha45_CAMPANA_1/AnalisisTemperaturasTrasero.png"
# Trasera - Zona 1
HTmaxZonasT1 = "500"
colMaxZonasT1 = "501"
HTminZonasT1 = "100"
colMinZonasT1 = "1"
HTmeanZonasT1 = "350"
pathImgZona1T = "Historial/CUCHARA_Cucha45/CUCHARA_Cucha45_CAMPANA_1/AnalisisTemperaturasTrasero.png"
# Trasera - Zona 2
HTmaxZonasT2 = "500"
colMaxZonasT2 = "501"
HTminZonasT2 = "100"
colMinZonasT2 = "1"
HTmeanZonasT2 = "350"
pathImgZona2T = "Historial/CUCHARA_Cucha45/CUCHARA_Cucha45_CAMPANA_1/AnalisisTemperaturasTrasero.png"
# Trasera - Zona 3
HTmaxZonasT3 = "500"
colMaxZonasT3 = "501"
HTminZonasT3 = "100"
colMinZonasT3 = "1"
HTmeanZonasT3 = "350"
pathImgZona3T = "Historial/CUCHARA_Cucha45/CUCHARA_Cucha45_CAMPANA_1/AnalisisTemperaturasTrasero.png"
'''

if __name__ == "__main__":
    nameCuchara = "Cucha45"
    nameCampana = "101"
    tipoGeneracion="auto"
    createPDF(nameCuchara, nameCampana, tipoGeneracion)