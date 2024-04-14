from sys import argv
from os.path import isfile, isdir
from os import getcwd
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6 import QtMultimedia
from login_ui import Ui_LoginWindow
from VideoLogoWindow_ui import Ui_Video_Logo_Window
from PopUpLogin_ui import Ui_PopUpLogin
from PopUpAddCuchara_ui import Ui_PopUpAddCuchara
from PopUpAddCampana_ui import Ui_PopUpAddCampana
from PopUpAddColada_ui import Ui_PopUpAddColada
from AdministratorWindow_ui import Ui_AdministratorWindow
import databaseLoginManage as dbLManager
import dataManager as dataManager
from historialWindow_ui import Ui_historialWindow
from editUsers_ui import Ui_editUsersWindow
from errorDeleteUserWindow_ui import Ui_errorDeleteUserWindow
from LowerTempWindow_ui import Ui_LowerTempWindow
from HigherTempWindow_ui import Ui_HigherTempWindow
from deleteUserWindow_ui import Ui_deleteUserWindow
from errorSaveUserWindow_ui import Ui_errorSaveUserWindow
from saveUserWindow_ui import Ui_saveUserWindow
from PopUpDeleteColada_ui import Ui_PopUpDeleteColada
from PopUpApiKey_ui import Ui_PopUpApiKey
import mallador2
import createPdf
from time import sleep
from threading import Timer
from shutil import copy2
from subprocess import Popen
from PySide6 import QtSvg

umbralMinimo = 200
umbralMaximo = 400
ApiKey = "AbaxfemGuiCucharas2023"

class Video_Logo_Window(qtw.QMainWindow, Ui_Video_Logo_Window):
    def __init__(self):
        super(Video_Logo_Window, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(qtc.Qt.FramelessWindowHint)
        #self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setSource("ResourcesFolder/Start_Video/LogoVideo.mp4")
        self.player.setVideoOutput(self.VideoPlace)
        self.VideoPlace.show()
        self.player.play()
        self.player.playbackStateChanged.connect(self.paroVideo)
    def paroVideo(self):
        if self.player.isPlaying():
            pass
        else:
            self.close()
            self.w = LoginWindow()
            self.w.show()
        
class LoginWindow(qtw.QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(qtc.Qt.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.pb_exit.clicked.connect(self.close)
        self.pb_acceder.clicked.connect(self.login)
        self.pb_minimized.clicked.connect(self.showMinimized)
    def login(self):
        if dbLManager.login(self.txt_username.text(), self.txt_password.text()) == "ADMINISTRADOR" or dbLManager.login(self.txt_username.text(), self.txt_password.text()) == "OPERADOR":
            dbLManager.addHistory(self.txt_username.text())
            self.close()
            self.w = AdministratorWindow()
            self.w.show()
        else:
            self.close()
            self.w = PopUpLogin()
            self.w.show()
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPosition().toPoint()
    def mouseMoveEvent(self, event):
        delta = qtc.QPoint(event.globalPosition().toPoint() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPosition().toPoint()
    def keyPressEvent(self, event):
        if event.key() == qtc.Qt.Key_Return or event.key() == qtc.Qt.Key_Enter:
            if (self.txt_username.text() != "" and self.txt_password.text() != ""):
                self.login()

class PopUpLogin(qtw.QMainWindow, Ui_PopUpLogin):
    def __init__(self):
        super(PopUpLogin, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(qtc.Qt.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.pb_exit.clicked.connect(self.exitPopUp)
        self.pb_aceptar.clicked.connect(self.exitPopUp)
        self.activateWindow()
    def exitPopUp(self):
        self.close()
        self.w = LoginWindow()
        self.w.show()

class PopUpAddCuchara(qtw.QMainWindow, Ui_PopUpAddCuchara):
    def __init__(self):
        super(PopUpAddCuchara, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(qtc.Qt.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.pb_exit.clicked.connect(self.exitPopUp)
        self.pb_aceptar.clicked.connect(self.addCuchara)
        regex = qtc.QRegularExpression("[0-9-a-z-A-Z_]+")
        validator = qtg.QRegularExpressionValidator(regex)
        self.txtCuchara.setValidator(validator)
    def exitPopUp(self):
        self.close()
        self.w = AdministratorWindow()
        self.w.show()
    def addCuchara(self):
        nameNewCuchara = self.txtCuchara.text()
        nameNewCuchara = nameNewCuchara.replace(" ", "")
        nameNewCuchara = nameNewCuchara.replace("-", "")
        nameNewCuchara = nameNewCuchara.replace("_", "")
        if nameNewCuchara.upper()[0:7]=="CUCHARA":
            nameNewCuchara=nameNewCuchara[7:len(nameNewCuchara)]
            dataManager.addCuchara(nameNewCuchara)
            self.exitPopUp()
        elif nameNewCuchara=="":
            pass
        else:
            dataManager.addCuchara(nameNewCuchara)
            self.exitPopUp()

class PopUpApiKey(qtw.QMainWindow, Ui_PopUpApiKey):
    def __init__(self):
        super(PopUpApiKey, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(qtc.Qt.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.pb_exit.clicked.connect(self.close)
        self.pb_aceptar.clicked.connect(self.addLicense)
    def addLicense(self):
        if self.txtApiKey.text() != ApiKey:
            self.pb_aceptar.setText("API-KEY Incorrecta")
            Timer(5, self.setPbTxt).start()
        else:
            self.close()
            if dataManager.getWorkingDirectory() == False:
                dataManager.setWorkingDirectory(getcwd())
                dbLManager.createTable("LoginTable", "User text, Password text, Function text, Name text, Date text")
                dbLManager.createTable("HistoryLoginTable", "User text, Function text, Name text, Date text, Time Text")
                dbLManager.restore()
                dataManager.resetDatabase()
            else:
                dataManager.changeWorkingDirectory(getcwd())
                if isfile("dataL.db") and isfile("data.db") and isdir("Historial"):
                    dbLManager.createTable("LoginTable", "User text, Password text, Function text, Name text, Date text")
                    dbLManager.createTable("HistoryLoginTable", "User text, Function text, Name text, Date text, Time Text")
                    dbLManager.restore()
                    dataManager.resetDatabase()
            if isfile("ResourcesFolder/Start_Video/LogoVideo.mp4"):
                self.w = Video_Logo_Window()
            else:
                self.w = LoginWindow()
            self.w.show()
    def setPbTxt(self):
        self.pb_aceptar.setText("Ingresar")
                
class PopUpAddCampana(qtw.QMainWindow, Ui_PopUpAddCampana):
    def __init__(self):
        super(PopUpAddCampana, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(qtc.Qt.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        #self.spinBox.setMinimum(dataManager.getNameCampanas("")[0])
        self.pb_exit.clicked.connect(self.exitPopUp)
        self.pb_aceptar.clicked.connect(self.addCampana)
        self.loadData()
        self.comboBox.currentIndexChanged.connect(self.loadMinimum)
    def exitPopUp(self):
        self.close()
        self.w = AdministratorWindow()
        self.w.show()
    def addCampana(self):
        nameCuchara = self.comboBox.currentText()[8:len(self.comboBox.currentText())]
        newCampana = self.spinBox.value()
        if len(dataManager.getNameCampanas(nameCuchara)) == 0:
            pass
        else:
            try:
                createPdf.createPDF(nameCuchara, str(dataManager.getNameCampanas(nameCuchara)[-1]), "auto")
            except:
                pass
        dataManager.addCampana(nameCuchara, newCampana)
        self.close()
        self.w = AdministratorWindow()
        self.w.show()
    def loadData(self):
        cucharas = dataManager.getNameCucharas()
        for i in range(dataManager.countCucharas()):
            self.comboBox.addItem(qtg.QIcon("ResourcesFolder/featherIcons/briefcase.svg"), "Cuchara "+cucharas[i])
        try:
            self.spinBox.setMinimum(dataManager.getNameCampanas(self.comboBox.currentText()[8:len(self.comboBox.currentText())])[-1]+1)
            self.spinBox.setValue(dataManager.getNameCampanas(self.comboBox.currentText()[8:len(self.comboBox.currentText())])[-1]+1)
        except:
            self.spinBox.setMinimum(1)
            self.spinBox.setValue(1)
    def loadMinimum(self):
        try:
            self.spinBox.setMinimum(dataManager.getNameCampanas(self.comboBox.currentText()[8:len(self.comboBox.currentText())])[-1]+1)
            self.spinBox.setValue(dataManager.getNameCampanas(self.comboBox.currentText()[8:len(self.comboBox.currentText())])[-1]+1)
        except:
            self.spinBox.setMinimum(1)
            self.spinBox.setValue(1)

class PopUpAddColada(qtw.QMainWindow, Ui_PopUpAddColada):
    def __init__(self):
        super(PopUpAddColada, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(qtc.Qt.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        geo = self.frameGeometry()
        CenterPoint = qtg.QGuiApplication.primaryScreen().availableGeometry().center()
        geo.moveCenter(CenterPoint)
        self.move(geo.topLeft())
        #self.spinBox.setMinimum(dataManager.getNameCampanas("")[0])
        self.pb_exit.clicked.connect(self.exitPopUp)
        self.pb_aceptar.clicked.connect(lambda: self.addColada())
        self.cbCuchara.currentIndexChanged.connect(self.loadFirstData)
        self.pbFileDialog1.clicked.connect(self.fileDialogWindow)
        self.pbFileDialog2.clicked.connect(self.fileDialogWindow)
        self.pbFileDialog3.clicked.connect(self.fileDialogWindow)
        self.pbFileDialog4.clicked.connect(self.fileDialogWindow)
        self.startupData()
        self.loadEscoria()
        self.loadFirstEscoria()
        self.pbSiEscoria.clicked.connect(self.siNoEscoria)
        self.pbNoEscoria.clicked.connect(self.siNoEscoria)
        self.progressBar.hide()
    def loadFirstEscoria(self):
        self.pbSiEscoria.setEnabled(True)
        self.pbNoEscoria.setEnabled(False)
        self.sbEscoria.setEnabled(False)
    def siNoEscoria(self):
        if self.pbSiEscoria.isEnabled() and self.pbNoEscoria.isEnabled():
            self.pbNoEscoria.setEnabled(False)
            self.sbEscoria.setEnabled(False)
        else:
            try:
                nameCuchara = self.cbCuchara.currentText()[8:len(self.cbCuchara.currentText())]
                if dataManager.getEscoria(nameCuchara) == 0:
                    self.changeEnablePb()
                else:
                    self.pbNoEscoria.setEnabled(False)                   
                    self.pbSiEscoria.setEnabled(False)
                    self.sbEscoria.setEnabled(False)
            except:
                self.pbSiEscoria.setEnabled(False)
                self.pbNoEscoria.setEnabled(False)
                self.sbEscoria.setEnabled(False)
    def changeEnablePb(self):
        if self.pbSiEscoria.isEnabled(): 
            self.pbSiEscoria.setEnabled(False)
            self.pbNoEscoria.setEnabled(True)
            self.sbEscoria.setEnabled(True)
        else:
            self.pbNoEscoria.setEnabled(False)
            self.pbSiEscoria.setEnabled(True)
            self.sbEscoria.setEnabled(False)
    def loadEscoria(self):
        try:
            nameCuchara = self.cbCuchara.currentText()[8:len(self.cbCuchara.currentText())]
            numEscoria = dataManager.getEscoria(nameCuchara)
            if numEscoria>0:
                self.sbEscoria.setValue(numEscoria)
                self.sbEscoria.setEnabled(False)
            else:
                self.sbEscoria.setValue(0)
                self.sbEscoria.setEnabled(True)
        except:
            self.sbEscoria.setValue(0)
            self.sbEscoria.setEnabled(False)
    def fileDialogWindow(self):
        fileName, _ = qtw.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Imagen (*.jpg);; Excel (*.xlsx);; Imagen o Excel (*.jpg *.xlsx)")
        if ".jpg" in fileName:
            commonPath = fileName[0:-5]
        else:
            commonPath = fileName[0:-6]
        try:
            if isfile(commonPath+"F.jpg") and isfile(commonPath+"F.xlsx") and isfile(commonPath+"T.jpg") and isfile(commonPath+"T.xlsx") and int(self.txtUltimaColada.text()) < int(commonPath.split("/")[-1]):
                self.txtPathTermografiaF.setText(commonPath+"F.jpg")
                self.txtPathTermografiaT.setText(commonPath+"T.jpg")
                self.txtPathExcelF.setText(commonPath+"F.xlsx")
                self.txtPathExcelT.setText(commonPath+"T.xlsx")
                self.txtNewColada.setText(commonPath.split("/")[-1])
            else:
                self.txtPathTermografiaF.setText("Error en el nombre")
                self.txtPathTermografiaT.setText("Error en el nombre")
                self.txtPathExcelF.setText("o archivos faltantes")
                self.txtPathExcelT.setText("o archivos faltantes")
                self.txtNewColada.setText("")
        except:
            self.txtPathTermografiaF.setText("Error en el nombre")
            self.txtPathTermografiaT.setText("Error en el nombre")
            self.txtPathExcelF.setText("o archivos faltantes")
            self.txtPathExcelT.setText("o archivos faltantes")
            self.txtNewColada.setText("")
    def loadFirstData(self):
        try:
            self.loadEscoria()
            self.loadFirstEscoria()
            self.txtCampana.setText(str(dataManager.getNameCampanas(self.cbCuchara.currentText()[8:len(self.cbCuchara.currentText())])[-1]))
            self.txtPathTermografiaF.setText("Error en el nombre")
            self.txtPathTermografiaT.setText("Error en el nombre")
            self.txtPathExcelF.setText("o archivos faltantes")
            self.txtPathExcelT.setText("o archivos faltantes")
            self.txtNewColada.setText("")
            self.txtUltimaColada.setText(str(dataManager.getNameColadas(self.cbCuchara.currentText()[8:len(self.cbCuchara.currentText())], self.txtCampana.text())[-1]))
        except:
            self.txtCampana.setText("")
            self.txtPathTermografiaF.setText("Error en el nombre")
            self.txtPathTermografiaT.setText("Error en el nombre")
            self.txtPathExcelF.setText("o archivos faltantes")
            self.txtPathExcelT.setText("o archivos faltantes")
            self.txtNewColada.setText("")
            self.txtUltimaColada.setText("")
    def addColada(self):
        try:
            self.pb_aceptar.hide()
            self.progressBar.show()
            sleep(0.1)
            self.progressBar.setValue(0)
            escoria = "2"
            numEscoria = 0
            numUltimaColada = int(self.txtUltimaColada.text())
            numColada = int(self.txtNewColada.text())
            if not self.pbSiEscoria.isEnabled(): 
                if int(self.sbEscoria.text()) == 0:
                    pass
                else:
                    numEscoria = int(self.sbEscoria.text())
                    escoria = "1"
            else:
                pass
            if numColada>=numEscoria and numUltimaColada<numColada:
                nameCuchara = self.cbCuchara.currentText()[8:len(self.cbCuchara.currentText())]
                nameCampana = int(self.txtCampana.text())
                fileName = self.txtPathExcelF.text()
                if ".jpg" in fileName:
                    commonPath = fileName[0:-5]
                else:
                    commonPath = fileName[0:-6]
                cantidadColadas = len(dataManager.getNameColadas(nameCuchara, str(nameCampana)))
                sleep(0.1)
                self.progressBar.setValue(25)
                [colF, colT, HTmaxCucharaF, HTmaxCucharaT, HTmaxZonasF, HTmaxZonasT, HTmaxRefF, HTmaxRefT] = dataManager.getHistoricosCampanaFT(nameCuchara, nameCampana)
                sleep(0.1)
                self.progressBar.setValue(50)
                [datosF, datosT] = mallador2.getValues(numColada, escoria, numEscoria, cantidadColadas,[colF], [colT], [HTmaxCucharaF], [HTmaxCucharaT], [HTmaxZonasF], [HTmaxZonasT], [HTmaxRefF], [HTmaxRefT], commonPath)
                sleep(0.2)
                self.progressBar.setValue(75)
                dataManager.add_Colada(nameCuchara, nameCampana, numColada, datosF[2], datosT[2], datosF[1], datosT[1], datosF[0], datosT[0])
                sleep(0.2)
                self.progressBar.setValue(100)
                sleep(1)
                if dataManager.getEscoria(nameCuchara)==0:
                    dataManager.modifyEscoria(nameCuchara, str(nameCampana), numEscoria)
                else:
                    pass
                dataManager.updatePlot(str(nameCuchara), str(nameCampana))
                copy2(commonPath+"F.jpg", "Historial/CUCHARA_"+nameCuchara+"/CUCHARA_"+nameCuchara+"_CAMPANA_"+str(nameCampana)+"/")
                copy2(commonPath+"T.jpg", "Historial/CUCHARA_"+nameCuchara+"/CUCHARA_"+nameCuchara+"_CAMPANA_"+str(nameCampana)+"/")
                [col, maxF, maxT, escoria] = dataManager.getMaxHistory(nameCuchara, nameCampana)
                try:
                    if max(maxF) >= umbralMaximo*0.9 or max(maxT) >= umbralMaximo*0.9:
                        self.close()
                        self.w = higherTempWindow()
                        self.w.show()
                    elif maxF[-2] >= maxF[-1] or maxT [-2] >= maxT[-1]:
                        self.close()
                        self.w = lowerTempWindow()
                        self.w.show()
                    else:
                        self.exitPopUp()
                except:
                    self.exitPopUp()
            else:
                self.progressBar.hide()
                self.pb_aceptar.show()
                if numColada<numEscoria:
                    self.pb_aceptar.setText("# Escoria >= # Colada")
                    Timer(5, self.setPbAceptarName).start()
                else:
                    if numUltimaColada>=numColada:
                        self.pb_aceptar.setText("# Colada >= # Ultima Colada")
                        Timer(5, self.setPbAceptarName).start()
                    else:
                        pass
        except:
            if self.progressBar.value() == 50:
                self.pb_aceptar.setText("Imágenes ingresadas incorrectas!")
            else:
                self.pb_aceptar.setText("Ingrese los datos faltantes")
            Timer(5, self.setPbAceptarName).start()
            self.pb_aceptar.show()
            self.progressBar.hide()
    def setPbAceptarName(self):
        self.pb_aceptar.setText("Añadir Colada")
    def exitPopUp(self):
        self.close()
        self.w = AdministratorWindow()
        self.w.show()
    def startupData(self):
        cucharas = dataManager.getNameCucharas()
        for i in range(dataManager.countCucharas()):
            self.cbCuchara.addItem(qtg.QIcon("ResourcesFolder/featherIcons/briefcase.svg"), "Cuchara "+cucharas[i])

class PopUpDeleteColada(qtw.QMainWindow, Ui_PopUpDeleteColada):
    def __init__(self):
        super(PopUpDeleteColada, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(qtc.Qt.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.pb_exit.clicked.connect(self.exitPopUp)
        self.loadCucharas()
        self.loadCampanaColadas()
        self.cbCuchara.currentIndexChanged.connect(self.loadCampanaColadas)
        self.pb_aceptar.clicked.connect(self.deleteColada)
    def deleteColada(self):
        try:
            nameCampana = self.txtCampana.text()
            nameCuchara = self.cbCuchara.currentText()
            nameColada = self.cbColada.currentText()
            dataManager.deleteColada(nameCuchara[8:len(nameCuchara)], str(nameCampana), int(nameColada))
            self.exitPopUp()
        except:
            pass
    def loadCampanaColadas(self):
        try:
            self.txtCampana.setText(str(dataManager.getNameCampanas(self.cbCuchara.currentText()[8:len(self.cbCuchara.currentText())])[-1]))
            nameCampana = self.txtCampana.text()
            nameCuchara = self.cbCuchara.currentText()
            colada = dataManager.getNameColadas(nameCuchara[8:len(nameCuchara)], nameCampana)
            self.cbColada.clear()
            if colada == [0, 0]:
                pass
            else:
                for i in range(len(colada)):
                    self.cbColada.addItem(qtg.QIcon("ResourcesFolder/featherIcons/file.svg"), str(colada[i]))
        except:
            self.cbColada.clear()
    def loadCucharas(self):
        cucharas = dataManager.getNameCucharas()
        for i in range(dataManager.countCucharas()):
            self.cbCuchara.addItem(qtg.QIcon("ResourcesFolder/featherIcons/briefcase.svg"), "Cuchara "+cucharas[i])
    def exitPopUp(self):
        self.close()
        self.w = AdministratorWindow()
        self.w.show()

class AdministratorWindow(qtw.QMainWindow, Ui_AdministratorWindow):
    def __init__(self):
        super(AdministratorWindow, self).__init__()
        self.setupUi(self)
        self.showMaximized()
        #self.setWindowFlag(qtc.Qt.FramelessWindowHint)
        #self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        #self.loadRefracTemps()
        self.printTree()
        self.printHistory()
        self.checkHighTemperature()
        self.pbHistorial.clicked.connect(self.historialWindow)
        self.pbPerfiles.clicked.connect(self.editUsers)
        self.treeMenu.itemClicked.connect(self.onItemClicked)
        self.pbAddCuchara.clicked.connect(self.addCuchara)
        self.pbDeleteCuchara.clicked.connect(self.deleteCuchara)
        self.pbAddCampana.clicked.connect(self.addCampana)
        self.pbDeleteCampana.clicked.connect(self.deleteCampana)
        self.pbAddColada.clicked.connect(self.addColada)
        self.pbHistorialZonasF.clicked.connect(self.changeImageF)
        self.pbHistorialZonasT.clicked.connect(self.changeImageT)
        self.pbVerArchivos.clicked.connect(self.verArchivos)
        self.pbDeleteColada.clicked.connect(self.deleteColada)
        self.pbReporte.clicked.connect(self.generarReporte)
    def checkHighTemperature(self):
        pass
    def generarReporte(self):
        try:
            nameCampana = self.treeMenu.currentItem().text(0)
            nameCuchara = self.treeMenu.currentItem().parent().text(0)
            nameCuchara = nameCuchara[8:len(nameCuchara)]
            nameCampana = nameCampana[8:len(nameCampana)]
            createPdf.createPDF(nameCuchara, str(nameCampana), "manual")
        except:
            pass
    def verArchivos(self):
        try:
            nameCampana = self.treeMenu.currentItem().text(0)
            nameCuchara = self.treeMenu.currentItem().parent().text(0)
            nameCuchara = nameCuchara[8:len(nameCuchara)]
            nameCampana = nameCampana[8:len(nameCampana)]
            pathDir = "Historial\CUCHARA_"+nameCuchara+"\CUCHARA_"+nameCuchara+"_CAMPANA_"+nameCampana
            Popen(f"explorer \"{pathDir}\"")
        except:
            try:
                nameCuchara = self.treeMenu.currentItem().text(0)
                nameCuchara = nameCuchara[8:len(nameCuchara)]
                pathDir = "Historial\CUCHARA_"+nameCuchara
                Popen(f"explorer \"{pathDir}\"")
            except:
                pathDir = "Historial"
                Popen(f"explorer \"{pathDir}\"")
    def deleteColada(self):
        self.close()
        self.w = PopUpDeleteColada()
        self.w.show()
    def changeImageF(self):
        if self.pbHistorialZonasF.text() == "Historial":
            self.label_30.hide()
            self.label_29.hide()
            self.label_31.hide()
            self.frame_31.hide()
            self.frame_32.hide()
            self.frame_74.hide()
            self.frame_79.hide()
            self.frame_80.hide()
            self.frame_81.hide()
            self.frame_82.hide()
            self.frame_86.hide()
            self.txtZona1F.hide()
            self.txtZona2F.hide()
            self.txtZona3F.hide()
            try:
                nameCampana = self.treeMenu.currentItem().text(0)
                nameCuchara = self.treeMenu.currentItem().parent().text(0)
                self.frame_17.setStyleSheet("border-image: url('Historial/CUCHARA_"+nameCuchara[8:len(nameCuchara)]+"/CUCHARA_"+nameCuchara[8:len(nameCuchara)]+"_CAMPANA_"+nameCampana[8:len(nameCampana)]+"/AnalisisTemperaturasFrontal.png');")
                self.frame_78.setStyleSheet("border-image: url('');\n background-color:rgba(0, 0, 0, 0);")
            except:
                self.frame_17.setStyleSheet("border-image: url('');")
                self.frame_78.setStyleSheet("border-image: url('');\n background-color:rgba(0, 0, 0, 0);")
            self.pbHistorialZonasF.setText("Zonas")
        else:
            self.label_30.show()
            self.label_29.show()
            self.label_31.show()
            self.frame_31.show()
            self.frame_32.show()
            self.frame_74.show()
            self.frame_78.show()
            self.frame_82.show()
            self.frame_79.show()
            self.frame_80.show()
            self.frame_81.show()
            self.frame_86.show()
            self.txtZona1F.show()
            self.txtZona2F.show()
            self.txtZona3F.show()
            self.frame_17.setStyleSheet("background-color: rgb(134, 154, 175);")
            self.pbHistorialZonasF.setText("Historial")
    def changeImageT(self):
        if self.pbHistorialZonasT.text() == "Historial":
            self.label_23.hide()
            self.label_24.hide()
            self.label_25.hide()
            self.frame_26.hide()
            self.frame_27.hide()
            self.frame_28.hide()
            self.frame_29.hide()
            self.frame_30.hide()
            self.frame_50.hide()
            self.frame_51.hide()
            self.frame_52.hide()
            self.txtZona1T.hide()
            self.txtZona2T.hide()
            self.txtZona3T.hide()
            try:
                nameCampana = self.treeMenu.currentItem().text(0)
                nameCuchara = self.treeMenu.currentItem().parent().text(0)
                self.frame_18.setStyleSheet("border-image: url('Historial/CUCHARA_"+nameCuchara[8:len(nameCuchara)]+"/CUCHARA_"+nameCuchara[8:len(nameCuchara)]+"_CAMPANA_"+nameCampana[8:len(nameCampana)]+"/AnalisisTemperaturasTrasero.png');")
                self.frame_34.setStyleSheet("border-image: url('');\n background-color:rgba(0, 0, 0, 0);")
            except:
                self.frame_18.setStyleSheet("border-image: url('');")
                self.frame_34.setStyleSheet("border-image: url('');\n background-color:rgba(0, 0, 0, 0);")
            self.pbHistorialZonasT.setText("Zonas")
        else:
            self.label_23.show()
            self.label_24.show()
            self.label_25.show()
            self.frame_26.show()
            self.frame_27.show()
            self.frame_28.show()
            self.frame_29.show()
            self.frame_30.show()
            self.frame_50.show()
            self.frame_51.show()
            self.frame_52.show()
            self.txtZona1T.show()
            self.txtZona2T.show()
            self.txtZona3T.show()
            self.frame_18.setStyleSheet("background-color: rgb(134, 154, 175);")
            self.pbHistorialZonasT.setText("Historial")
    def updateImage(self):
        if self.pbHistorialZonasT.text() == "Historial":
            pass
        else:
            try:
                nameCampana = self.treeMenu.currentItem().text(0)
                nameCuchara = self.treeMenu.currentItem().parent().text(0)
                self.frame_18.setStyleSheet("border-image: url('Historial/CUCHARA_"+nameCuchara[8:len(nameCuchara)]+"/CUCHARA_"+nameCuchara[8:len(nameCuchara)]+"_CAMPANA_"+nameCampana[8:len(nameCampana)]+"/AnalisisTemperaturasTrasero.png');")
            except:
                self.frame_18.setStyleSheet("border-image: url('');")
        if self.pbHistorialZonasF.text() == "Historial":
            pass
        else:
            try:
                nameCampana = self.treeMenu.currentItem().text(0)
                nameCuchara = self.treeMenu.currentItem().parent().text(0)
                self.frame_17.setStyleSheet("border-image: url('Historial/CUCHARA_"+nameCuchara[8:len(nameCuchara)]+"/CUCHARA_"+nameCuchara[8:len(nameCuchara)]+"_CAMPANA_"+nameCampana[8:len(nameCampana)]+"/AnalisisTemperaturasFrontal.png');")
            except:
                self.frame_17.setSty7leSheet("border-image: url('');")
    def addColada(self):
        self.close()
        self.w = PopUpAddColada()
        self.w.show()
    def addCuchara(self):
        self.close()
        self.w = PopUpAddCuchara()
        self.w.show()
    def deleteCuchara(self):
        try:
            nameCuchara = self.treeMenu.currentItem().text(0)
            nameCuchara = nameCuchara[8:len(nameCuchara)]
            if dataManager.deleteCuchara(nameCuchara):
                self.treeMenu.clear()
                self.printTree()
            else:
                pass
        except:
            pass
    def addCampana(self):
        self.close()
        self.w = PopUpAddCampana()
        self.w.show()
    def deleteCampana(self):
        try:
            nameCampana = self.treeMenu.currentItem().text(0)
            nameCuchara = self.treeMenu.currentItem().parent().text(0)
            nameCampana = nameCampana[8:len(nameCampana)]
            nameCuchara = nameCuchara[8:len(nameCuchara)]
            dataManager.deleteCampana(nameCuchara, int(nameCampana))
            self.treeMenu.clear()
            self.printTree()
        except:
            pass
    def printHistory(self):
        briefHistory = dbLManager.getBriefHistory(5)
        historyCount = len(briefHistory)
        self.labelUsername.setText(briefHistory[len(briefHistory)-1][2] + " - " + briefHistory[len(briefHistory)-1][1])
        if briefHistory[len(briefHistory)-1][1] == "ADMINISTRADOR":
            pass
        else:
            self.pbPerfiles.hide()
            self.pbVerArchivos.hide()
            self.pbDeleteColada.hide()
            self.pbDeleteCampana.hide()
            self.pbDeleteCuchara.hide()
        if historyCount != 5:
            for i in range(5-historyCount):
                briefHistory.append(['-', '-', '-', '-', '-'])
        self.nameHistory0.setText(briefHistory[4][2])
        self.dateHistory0.setText(briefHistory[4][3])
        self.nameHistory1.setText(briefHistory[3][2])
        self.dateHistory1.setText(briefHistory[3][3])
        self.nameHistory2.setText(briefHistory[2][2])
        self.dateHistory2.setText(briefHistory[2][3])
        self.nameHistory3.setText(briefHistory[1][2])
        self.dateHistory3.setText(briefHistory[1][3])
        self.nameHistory4.setText(briefHistory[0][2])
        self.dateHistory4.setText(briefHistory[0][3])
    def onItemClicked(self):
        try:
            campana = self.treeMenu.currentItem().text(0)
            cuchara = self.treeMenu.currentItem().parent().text(0)
            coladas = dataManager.getNameColadas(cuchara[8:], campana[8:])
            print("Coladas: "+str(coladas)[1:-1])
            self.labelColadas.setText("Coladas: "+str(coladas)[1:-1])
            self.loadZonas()
            self.updateImage()
        except:
            self.txtZona1F.setText("")
            self.txtZona2F.setText("")
            self.txtZona3F.setText("")
            self.txtZona1T.setText("")
            self.txtZona2T.setText("")
            self.txtZona3T.setText("")
            self.setZonesColor(0, 0, 0)
    def loadZonas(self):
        nameCampana = self.treeMenu.currentItem().text(0)
        nameCuchara = self.treeMenu.currentItem().parent().text(0)
        [maxZonasF, maxZonasT] = dataManager.getZonas(nameCuchara[8:], nameCampana[8:])
        [percentageZonasF, percentageZonasT] = self.getPercentage(maxZonasF, maxZonasT, umbralMinimo, umbralMaximo)
        self.txtZona1F.setText(str(percentageZonasF[0])[0:5]+" %")
        self.txtZona2F.setText(str(percentageZonasF[1])[0:5]+" %")
        self.txtZona3F.setText(str(percentageZonasF[2])[0:5]+" %")
        self.txtZona1T.setText(str(percentageZonasT[0])[0:5]+" %")
        self.txtZona2T.setText(str(percentageZonasT[1])[0:5]+" %")
        self.txtZona3T.setText(str(percentageZonasT[2])[0:5]+" %")
        self.setZonesColor(percentageZonasF, percentageZonasT, umbralMinimo)
    def setZonesColor(self, percentageZonasF, percentageZonasT, umbral):
        # Siendo 0% Riesgo : rgb(154, 171, 188)
        # Siendo 100% Riesgo : rgb(255, 0, 0)
        if percentageZonasF==0:
            rgbTxt = f"rgba(0, 255, 255, 50)"
            self.colorZone1F.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 "+rgbTxt+", stop: 0.48 rgb(198, 197, 195), stop: 0.52 rgb(198, 197, 195), stop: 1.0  "+rgbTxt+");\n border-radius:0px;\nborder:1px solid rgb(167, 167, 164);")
            self.colorZone2F.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 "+rgbTxt+", stop: 0.48 rgb(198, 197, 195), stop: 0.52 rgb(198, 197, 195), stop: 1.0  "+rgbTxt+");\n border-radius:0px;\nborder:1px solid rgb(167, 167, 164);")
            self.colorZone3F.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 "+rgbTxt+", stop: 0.48 rgb(198, 197, 195), stop: 0.52 rgb(198, 197, 195), stop: 1.0  "+rgbTxt+");\n border-radius:0px;\nborder:1px solid rgb(167, 167, 164);")
            self.colorZone1T.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 "+rgbTxt+", stop: 0.48 rgb(198, 197, 195), stop: 0.52 rgb(198, 197, 195), stop: 1.0  "+rgbTxt+");\n border-radius:0px;\nborder:1px solid rgb(167, 167, 164);")
            self.colorZone2T.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 "+rgbTxt+", stop: 0.48 rgb(198, 197, 195), stop: 0.52 rgb(198, 197, 195), stop: 1.0  "+rgbTxt+");\n border-radius:0px;\nborder:1px solid rgb(167, 167, 164);")
            self.colorZone3T.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 "+rgbTxt+", stop: 0.48 rgb(198, 197, 195), stop: 0.52 rgb(198, 197, 195), stop: 1.0  "+rgbTxt+");\n border-radius:0px;\nborder:1px solid rgb(167, 167, 164);")
        else:
            minRed = 0
            minGreen = 255
            minBlue = 255
            minA = 50
            maxRed = 255
            maxGreen = 0
            maxBlue = 0
            maxA = 255
            rgbTxt = f"rgba({int(self.map_range(percentageZonasF[0], 0, 100, minRed, maxRed))}, {int(self.map_range(percentageZonasF[0], 0, 100, minGreen, maxGreen))}, {int(self.map_range(percentageZonasF[0], 0, 100, minBlue, maxBlue))}, {int(self.map_range(percentageZonasF[0], 0, 100, minA, maxA))})"
            self.colorZone1F.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 "+rgbTxt+", stop: 0.48 rgb(198, 197, 195), stop: 0.52 rgb(198, 197, 195), stop: 1.0  "+rgbTxt+");\n border-radius:0px;\nborder:1px solid rgb(167, 167, 164);")
            rgbTxt = f"rgba({int(self.map_range(percentageZonasF[1], 0, 100, minRed, maxRed))}, {int(self.map_range(percentageZonasF[1], 0, 100, minGreen, maxGreen))}, {int(self.map_range(percentageZonasF[1], 0, 100, minBlue, maxBlue))}, {int(self.map_range(percentageZonasF[1], 0, 100, minA, maxA))})"
            self.colorZone2F.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 "+rgbTxt+", stop: 0.48 rgb(198, 197, 195), stop: 0.52 rgb(198, 197, 195), stop: 1.0  "+rgbTxt+");\n border-radius:0px;\nborder:1px solid rgb(167, 167, 164);")
            rgbTxt = f"rgba({int(self.map_range(percentageZonasF[2], 0, 100, minRed, maxRed))}, {int(self.map_range(percentageZonasF[2], 0, 100, minGreen, maxGreen))}, {int(self.map_range(percentageZonasF[2], 0, 100, minBlue, maxBlue))}, {int(self.map_range(percentageZonasF[2], 0, 100, minA, maxA))})"
            self.colorZone3F.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 "+rgbTxt+", stop: 0.48 rgb(198, 197, 195), stop: 0.52 rgb(198, 197, 195), stop: 1.0  "+rgbTxt+");\n border-radius:0px;\nborder:1px solid rgb(167, 167, 164);")
            rgbTxt = f"rgba({int(self.map_range(percentageZonasT[0], 0, 100, minRed, maxRed))}, {int(self.map_range(percentageZonasT[0], 0, 100, minGreen, maxGreen))}, {int(self.map_range(percentageZonasT[0], 0, 100, minBlue, maxBlue))}, {int(self.map_range(percentageZonasT[0], 0, 100, minA, maxA))})"
            self.colorZone1T.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 "+rgbTxt+", stop: 0.48 rgb(198, 197, 195), stop: 0.52 rgb(198, 197, 195), stop: 1.0  "+rgbTxt+");\n border-radius:0px;\nborder:1px solid rgb(167, 167, 164);")
            rgbTxt = f"rgba({int(self.map_range(percentageZonasT[1], 0, 100, minRed, maxRed))}, {int(self.map_range(percentageZonasT[1], 0, 100, minGreen, maxGreen))}, {int(self.map_range(percentageZonasT[1], 0, 100, minBlue, maxBlue))}, {int(self.map_range(percentageZonasT[1], 0, 100, minA, maxA))})"
            self.colorZone2T.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 "+rgbTxt+", stop: 0.48 rgb(198, 197, 195), stop: 0.52 rgb(198, 197, 195), stop: 1.0  "+rgbTxt+");\n border-radius:0px;\nborder:1px solid rgb(167, 167, 164);")
            rgbTxt = f"rgba({int(self.map_range(percentageZonasT[2], 0, 100, minRed, maxRed))}, {int(self.map_range(percentageZonasT[2], 0, 100, minGreen, maxGreen))}, {int(self.map_range(percentageZonasT[2], 0, 100, minBlue, maxBlue))}, {int(self.map_range(percentageZonasT[2], 0, 100, minA, maxA))})"
            self.colorZone3T.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 "+rgbTxt+", stop: 0.48 rgb(198, 197, 195), stop: 0.52 rgb(198, 197, 195), stop: 1.0  "+rgbTxt+");\n border-radius:0px;\nborder:1px solid rgb(167, 167, 164);")
    def map_range(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
    def getPercentage(self, maxZonasF:float, maxZonasT:float, umbralMinimo:float, umbralMaximo:float):
        percentageZonasF = []
        percentageZonasT = []
        for i in range(len(maxZonasF)):
            percentageZonasF.append(self.map_range(maxZonasF[i], umbralMinimo, umbralMaximo, 0, 100))
            percentageZonasT.append(self.map_range(maxZonasT[i], umbralMinimo, umbralMaximo, 0, 100))
        return [percentageZonasF, percentageZonasT]
    def printTree(self):
        self.treeMenu.setColumnCount(1)
        for i in range(dataManager.countCucharas()):
            a = qtw.QTreeWidgetItem(["Cuchara "+dataManager.getNameCucharas()[i]])
            self.treeMenu.addTopLevelItem(a)
            for j in range(dataManager.countCampanas(dataManager.getNameCucharas()[i])):
                branch = qtw.QTreeWidgetItem(["Campaña "+str(dataManager.getNameCampanas(dataManager.getNameCucharas()[i])[j])])
                a.addChild(branch)
                font = branch.font(0)
                font.setItalic(True)
                branch.setFont(0, font)
                icon = branch.icon(0)
                branch.setIcon(0, qtg.QIcon("ResourcesFolder/featherIcons/file-text.svg"))
                a.setIcon(0, qtg.QIcon("ResourcesFolder/featherIcons/briefcase.svg"))
    def historialWindow(self):
        self.close()
        self.w = historialWindow()
        self.w.show()
    def editUsers(self):
        self.close()
        self.w = editUsers()
        self.w.show()

class historialWindow(qtw.QMainWindow, Ui_historialWindow):
    def __init__(self):
        super(historialWindow, self).__init__()
        self.setupUi(self)
        self.loadHistoryData()
        #self.setWindowFlag(qtc.Qt.FramelessWindowHint)
        #self.setAttribute(qtc.Qt.WA_TranslucentBackground)
    def closeEvent(self, event):
        self.close()
        self.w = AdministratorWindow()
        self.w.show()
    def loadHistoryData(self):
        self.tableWidget.setColumnWidth(0, 124)
        self.tableWidget.setColumnWidth(1, 124)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)
        row = 0
        people = dbLManager.readRows("HistoryLoginTable")
        self.tableWidget.setRowCount(len(people))
        for person in people:
            self.tableWidget.setItem(row, 0, qtw.QTableWidgetItem(person[0]))
            self.tableWidget.setItem(row, 1, qtw.QTableWidgetItem(person[1]))
            self.tableWidget.setItem(row, 2, qtw.QTableWidgetItem(person[2]))
            self.tableWidget.setItem(row, 3, qtw.QTableWidgetItem(person[3]))
            self.tableWidget.setItem(row, 4, qtw.QTableWidgetItem(person[4]))
            for i in range(5):
                item = self.tableWidget.item(row, i)
                item.setTextAlignment(qtc.Qt.AlignCenter)
                if i%2 == 0:
                    item.setBackground(qtg.QColor(217, 225, 243))
            row += 1

class editUsers(qtw.QMainWindow, Ui_editUsersWindow):
    def __init__(self):
        super(editUsers, self).__init__()
        self.setupUi(self)
        self.pbAddUser.clicked.connect(self.addUser)
        self.pbSaveAndExit.clicked.connect(self.saveAndExit)
        self.pbDeleteRow.clicked.connect(self.deleteRow)
        self.loadLoginData()
    def addUser(self):
        people = dbLManager.readRows("LoginTable")
        self.tableWidget.setRowCount(len(people)+1)
    def saveAndExit(self):
        if self.emptycell() == True:
            self.close()
            self.w = errorSaveUserWindow()
            self.w.show()
        else:
            self.saveInfo()
            self.close()
            self.w = saveUserWindow()
            self.w.show()
        if self.tableWidget.rowCount() == 0:
            dbLManager.restore()
    def emptycell(self):
        for i in range(self.tableWidget.rowCount()):
            for j in range(4):
                try:
                    item = self.tableWidget.item(i, j)
                    if item.text() == "":
                        return True
                    else:
                        pass
                except:
                    return True
        return False
    def closeEvent(self, event):
        self.close()
        self.w = AdministratorWindow()
        self.w.show()
    def keyPressEvent(self, event):
        if (event.key() == qtc.Qt.Key_Return or event.key() == qtc.Qt.Key_Enter) and self.emptycell() == False:
            self.saveInfo()
    def saveInfo(self):
        if len(dbLManager.readRows("LoginTable")) < self.tableWidget.rowCount():
            dbLManager.insertLoginRow("LoginTable", 'a', 'b', 'c', 'd')
        people = dbLManager.readRows("LoginTable")
        for i in range(self.tableWidget.rowCount()):
            userref = people[i][0]
            user = self.tableWidget.item(i, 0)
            if dbLManager.isDuplicated("LoginTable", "User", user.text()) == True:
                user = people[i][0]
            else:
                user = user.text()
            item = self.tableWidget.item(i, 1)
            if item.text()=="*******":
                password = people[i][1]
            else:
                password = self.tableWidget.item(i, 1).text()
            function = self.tableWidget.item(i, 2)
            if function.text().upper() == "ADMINISTRADOR":
                function = "ADMINISTRADOR"
            else:
                function = "OPERADOR"
            name = self.tableWidget.item(i, 3)
            if user != people[i][0] or password != people[i][1] or function !=people[i][2] or name.text() != people[i][3]:
                dbLManager.updateFields("LoginTable", "User", f"'{userref}'", 'Password', f"'{password}'")
                dbLManager.updateFields("LoginTable", "User", f"'{userref}'", 'Function', f"'{function}'")
                dbLManager.updateFields("LoginTable", "User", f"'{userref}'", 'Name', f"'{name.text()}'")
                dbLManager.updateFields("LoginTable", "User", f"'{userref}'", 'User', f"'{user}'")
                self.loadLoginData()
            else:
                pass
    def loadLoginData(self):
        self.tableWidget.setColumnWidth(0, 110)
        self.tableWidget.setColumnWidth(1, 124)
        self.tableWidget.setColumnWidth(2, 125)
        self.tableWidget.setColumnWidth(3, 125)
        self.tableWidget.setColumnWidth(4, 114)
        row = 0
        people = dbLManager.readRows("LoginTable")
        self.tableWidget.setRowCount(len(people))
        for person in people:
            self.tableWidget.setItem(row, 0, qtw.QTableWidgetItem(person[0]))
            self.tableWidget.setItem(row, 1, qtw.QTableWidgetItem("*******"))
            self.tableWidget.setItem(row, 2, qtw.QTableWidgetItem(person[2]))
            self.tableWidget.setItem(row, 3, qtw.QTableWidgetItem(person[3]))
            self.tableWidget.setItem(row, 4, qtw.QTableWidgetItem(person[4]))
            for i in range(5):
                item = self.tableWidget.item(row, i)
                item.setTextAlignment(qtc.Qt.AlignCenter)
                if i%2 == 0:
                    item.setBackground(qtg.QColor(217, 225, 243))
            row += 1
    def deleteRow(self):
        if dbLManager.searchDB("LoginTable", "User", f"'{self.tableWidget.currentItem().text()}'") == []:
            self.close()
            self.w = errorDeleteUserWindow()
            self.w.show()
        else:
            dbLManager.deleteRow("LoginTable", "User", f"'{self.tableWidget.currentItem().text()}'")
            self.close()
            self.w = deleteUserWindow()
            self.w.show()

class deleteUserWindow(qtw.QMainWindow, Ui_deleteUserWindow):
    def __init__(self):
        super(deleteUserWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(qtc.Qt.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.pb_exit.clicked.connect(self.closeWindow)
        self.pb_aceptar.clicked.connect(self.closeWindow)
    def closeWindow(self):
        self.close()
        self.w = editUsers()
        self.w.show()

class errorDeleteUserWindow(qtw.QMainWindow, Ui_errorDeleteUserWindow):
    def __init__(self):
        super(errorDeleteUserWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(qtc.Qt.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.pb_aceptar.setGraphicsEffect(qtw.QGraphicsDropShadowEffect(blurRadius = 25, xOffset = 3, yOffset = 0))
        self.pb_exit.clicked.connect(self.closeWindow)
        self.pb_aceptar.clicked.connect(self.closeWindow)
    def closeWindow(self):
        self.close()
        self.w = editUsers()
        self.w.show()

class lowerTempWindow(qtw.QMainWindow, Ui_LowerTempWindow):
    def __init__(self):
        super(lowerTempWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(qtc.Qt.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.pb_aceptar.setGraphicsEffect(qtw.QGraphicsDropShadowEffect(blurRadius = 25, xOffset = 3, yOffset = 0))
        self.pb_exit.clicked.connect(self.closeWindow)
        self.pb_aceptar.clicked.connect(self.closeWindow)
    def closeWindow(self):
        self.close()
        self.w = AdministratorWindow()
        self.w.show()

class higherTempWindow(qtw.QMainWindow, Ui_HigherTempWindow):
    def __init__(self):
        super(higherTempWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(qtc.Qt.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.pb_aceptar.setGraphicsEffect(qtw.QGraphicsDropShadowEffect(blurRadius = 25, xOffset = 3, yOffset = 0))
        self.pb_exit.clicked.connect(self.closeWindow)
        self.pb_aceptar.clicked.connect(self.closeWindow)
    def closeWindow(self):
        self.close()
        self.w = AdministratorWindow()
        self.w.show()

class errorSaveUserWindow(qtw.QMainWindow, Ui_errorSaveUserWindow):
    def __init__(self):
        super(errorSaveUserWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(qtc.Qt.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.pb_exit.clicked.connect(self.closeWindow)
        self.pb_aceptar.clicked.connect(self.closeWindow)
    def closeWindow(self):
        self.close()
        self.w = editUsers()
        self.w.show()

class saveUserWindow(qtw.QMainWindow, Ui_saveUserWindow):
    def __init__(self):
        super(saveUserWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(qtc.Qt.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.pb_exit.clicked.connect(self.closeWindow)
        self.pb_aceptar.clicked.connect(self.closeWindow)
    def closeWindow(self):
        self.close()
        self.w = AdministratorWindow()
        self.w.show()

if __name__ == "__main__":
    app = qtw.QApplication(argv)

    if dataManager.getWorkingDirectory() == getcwd():
        if isfile("dataL.db"):
            pass
        else:
            dbLManager.createDB()
            dbLManager.createTable("LoginTable", "User text, Password text, Function text, Name text, Date text")
            dbLManager.createTable("HistoryLoginTable", "User text, Function text, Name text, Date text, Time Text")
            dbLManager.restore()
        if dataManager.dataIsCorrupted():
            print("Datos Corruptos, correo enviado")
        else:
            pass
        if isfile("ResourcesFolder/Start_Video/LogoVideo.mp4"):
            window = Video_Logo_Window()
        else:
            window = LoginWindow()
    else:
        dataManager.dataIsCorrupted()
        window = PopUpApiKey()
    
    window.show()
    app.exec()