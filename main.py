from sys import argv, exit, path
from os.path import isfile, isdir
from os import getcwd
path.append(getcwd()+'/QT Windows')
path.append(getcwd()+'/Operations')
import os
from PySide6 import QtCore as qtc
from PySide6.QtCore import QProcess
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtGui import QDragMoveEvent, QPaintEvent
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
from cropWindow_ui import Ui_cropWindow
import mallador2
import createPdf
from time import sleep
from threading import Timer
from shutil import copy2
from subprocess import Popen
from PySide6 import QtSvg
import pandas as pd
import V1
import main_MP_sup
import main_MP_Inf
import main_MP_Med
from numpy import array, reshape
import PySide6.QtConcurrent
from PySide6.QtCore import QRunnable
from multiprocessing import freeze_support
from read_historia import read_historia
from  Observacion_Colada import  Observacion_Colada
from grafico_espesores import grafico_espesores
from grafico_espesores import grafico_espesores




umbralMinimo = 0
umbralMaximo = 500
ApiKey = "AbaxfemGuiCucharas2023"
D_Anillo= 0.1464
D_Inf= 0.1464
Middle = 1/2
num_process=3
os.environ["OMP_NUM_THREADS"]="1"
global Position_MatrixT, Position_MatrixF

class Limit(qtw.QPushButton):
    def __init__(self, x, y, parent):
        super().__init__("+", parent)
        font = qtg.QFont()
        #font.setFamilies([u"Rockwell"])
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
        font.setBold(False)
        self.setFont(font)
        self.setGeometry(x, y, 25, 25)
        self.setStyleSheet("""
        QPushButton{
            border-image:url("");
            color: rgba(0, 0, 255, 100);
            padding: 0 0 0 0;
            border-radius:8px;
            border:3px solid rgba(0, 0, 255, 255);
        }
        QPushButton:hover{
            background-color: rgba(100, 100, 100, 180);
        }
        QPushButton:pressed{
            background-color: rgba(100, 100, 100, 180);}""")
    def mouseMoveEvent(self, e):
        if e.buttons() != qtc.Qt.LeftButton: return
        else: pass
        mimeData = qtc.QMimeData()
        drag = qtg.QDrag(self)
        drag.setMimeData(mimeData)
        position = e.globalPosition().toPoint()
        drag.setHotSpot(position)
        pm = qtg.QPixmap(32,32)
        pm.fill(qtc.Qt.transparent) 
        drag.setDragCursor(pm, qtc.Qt.MoveAction)
        dropAction = drag.exec(qtc.Qt.MoveAction)

class cropWindow(qtw.QMainWindow, Ui_cropWindow):
    def __init__(self, pathImage):
        super(cropWindow, self).__init__()
        self.pathImage = pathImage
        self.setupUi(self)
        CenterPoint = qtg.QGuiApplication.primaryScreen().availableGeometry().center()
        geo = self.frameGeometry()
        geo.moveCenter(CenterPoint)
        self.move(geo.topLeft())
        self.select = "TopLeft"
        self.setFocusPolicy(qtc.Qt.StrongFocus)
        self.setAcceptDrops(True)
        self.pbTopLeft = Limit(100, 50, self.frameCropImage)
        self.pbTopLeftMiddle = Limit(215, 10, self.frameCropImage)
        self.pbTopMiddle = Limit(450, 10, self.frameCropImage)
        self.pbTopRightMiddle = Limit(685, 10, self.frameCropImage)
        self.pbTopRight = Limit(800, 50, self.frameCropImage)
        self.pbBottomLeft = Limit(100, 650, self.frameCropImage)
        self.pbBottomLeftMiddle = Limit(215, 680, self.frameCropImage)
        self.pbBottomMiddle = Limit(450, 680, self.frameCropImage)
        self.pbBottomRightMiddle = Limit(685, 680, self.frameCropImage)
        self.pbBottomRight = Limit(800, 650, self.frameCropImage)
        self.pbTopLeft.pressed.connect(self.pbTopLeftAction)
        self.pbTopRight.pressed.connect(self.pbTopRightAction)
        self.pbTopLeftMiddle.pressed.connect(self.pbTopLeftMiddleAction)
        self.pbTopMiddle.pressed.connect(self.pbTopMiddleAction)
        self.pbTopRightMiddle.pressed.connect(self.pbTopRightMiddleAction)
        self.pbBottomLeft.pressed.connect(self.pbBottomLeftAction)
        self.pbBottomRight.pressed.connect(self.pbBottomRightAction)
        self.pbBottomLeftMiddle.pressed.connect(self.pbBottomLeftMiddleAction)
        self.pbBottomMiddle.pressed.connect(self.pbBottomMiddleAction)
        self.pbBottomRightMiddle.pressed.connect(self.pbBottomRightMiddleAction)
        self.pushButton.clicked.connect(self.cropImage)
    def cropImage(self):
        global windowColada, PositionMatrixF, PositionMatrixT
        """print("-----------------------------------------------------")
        print("1. [" + str(int((self.pbTopLeft.pos().x() + int(self.pbTopLeft.width()/2))/2)) + ", " + str(int((self.pbTopLeft.pos().y() + int(self.pbTopLeft.height()/2))/2)) +"]")
        print("2. [" + str(int((self.pbTopLeftMiddle.pos().x() + int(self.pbTopLeftMiddle.width()/2))/2)) + ", " + str(int((self.pbTopLeftMiddle.pos().y() + int(self.pbTopLeftMiddle.height()/2))/2)) +"]")
        print("3. [" + str(int((self.pbTopRightMiddle.pos().x() + int(self.pbTopRightMiddle.width()/2))/2)) + ", " + str(int((self.pbTopRightMiddle.pos().y() + int(self.pbTopRightMiddle.height()/2))/2)) +"]")
        print("4. [" + str(int((self.pbTopRight.pos().x() + int(self.pbTopRight.width()/2))/2)) + ", " + str(int((self.pbTopRight.pos().y() + int(self.pbTopRight.height()/2))/2)) +"]")
        print("5. [" + str(int((self.pbBottomRight.pos().x() + int(self.pbBottomRight.width()/2))/2)) + ", " + str(int((self.pbBottomRight.pos().y() + int(self.pbBottomRight.height()/2))/2)) +"]")
        print("6. [" + str(int((self.pbBottomRightMiddle.pos().x() + int(self.pbBottomRightMiddle.width()/2))/2)) + ", " + str(int((self.pbBottomRightMiddle.pos().y() + int(self.pbBottomRightMiddle.height()/2))/2)) +"]")
        print("7. [" + str(int((self.pbBottomLeftMiddle.pos().x() + int(self.pbBottomLeftMiddle.width()/2))/2)) + ", " + str(int((self.pbBottomLeftMiddle.pos().y() + int(self.pbBottomLeftMiddle.height()/2))/2)) +"]")
        print("8. [" + str(int((self.pbBottomLeft.pos().x() + int(self.pbBottomLeft.width()/2))/2)) + ", " + str(int((self.pbBottomLeft.pos().y() + int(self.pbBottomLeft.height()/2))/2)) +"]")"""
        coordenadas = [[int((self.pbTopLeft.pos().x() + int(self.pbTopLeft.width()/2))/2), int((self.pbTopLeft.pos().y() + int(self.pbTopLeft.height()/2))/2)], 
                       [int((self.pbTopLeftMiddle.pos().x() + int(self.pbTopLeftMiddle.width()/2))/2) , int((self.pbTopLeftMiddle.pos().y() + int(self.pbTopLeftMiddle.height()/2))/2)], 
                       [int((self.pbTopMiddle.pos().x() + int(self.pbTopMiddle.width()/2))/2) , int((self.pbTopMiddle.pos().y() + int(self.pbTopMiddle.height()/2))/2)], 
                       [int((self.pbTopRightMiddle.pos().x() + int(self.pbTopRightMiddle.width()/2))/2) , int((self.pbTopRightMiddle.pos().y() + int(self.pbTopRightMiddle.height()/2))/2)], 
                       [int((self.pbTopRight.pos().x() + int(self.pbTopRight.width()/2))/2) , int((self.pbTopRight.pos().y() + int(self.pbTopRight.height()/2))/2)], 
                       [int((self.pbBottomRight.pos().x() + int(self.pbBottomRight.width()/2))/2) , int((self.pbBottomRight.pos().y() + int(self.pbBottomRight.height()/2))/2)], 
                       [int((self.pbBottomRightMiddle.pos().x() + int(self.pbBottomRightMiddle.width()/2))/2) , int((self.pbBottomRightMiddle.pos().y() + int(self.pbBottomRightMiddle.height()/2))/2)], 
                       [int((self.pbBottomMiddle.pos().x() + int(self.pbBottomMiddle.width()/2))/2) , int((self.pbBottomMiddle.pos().y() + int(self.pbBottomMiddle.height()/2))/2)], 
                       [int((self.pbBottomLeftMiddle.pos().x() + int(self.pbBottomLeftMiddle.width()/2))/2) , int((self.pbBottomLeftMiddle.pos().y() + int(self.pbBottomLeftMiddle.height()/2))/2)], 
                       [int((self.pbBottomLeft.pos().x() + int(self.pbBottomLeft.width()/2))/2) , int((self.pbBottomLeft.pos().y() + int(self.pbBottomLeft.height()/2))/2)]]
        #print(coordenadas)
        #print(self.pathImage)
        if self.pathImage[-5] == "F":
            PositionMatrixF = coordenadas
            window = self.window()
            window.close()
            aux = self.pathImage[0:-5]
            aux = aux+"T.jpg"
            self.window = cropWindow(aux)
            self.window.show()
        else:
            PositionMatrixT = coordenadas
            self.close()
            windowColada.show()
    def pbTopLeftAction(self): self.select = "TopLeft"
    def pbTopRightAction(self): self.select = "TopRight"
    def pbTopLeftMiddleAction(self): self.select = "TopLeftMiddle"
    def pbTopMiddleAction(self): self.select = "TopMiddle"
    def pbTopRightMiddleAction(self): self.select = "TopRightMiddle"
    def pbBottomLeftAction(self): self.select = "BottomLeft"
    def pbBottomRightAction(self): self.select = "BottomRight"
    def pbBottomLeftMiddleAction(self): self.select = "BottomLeftMiddle"
    def pbBottomMiddleAction(self): self.select = "BottomMiddle"
    def pbBottomRightMiddleAction(self): self.select = "BottomRightMiddle"
    def dragEnterEvent(self, e): e.accept()
    def keyPressEvent(self, event: qtg.QKeyEvent):
        if event.key() == qtc.Qt.Key_Left:
            if self.select == "TopLeft":
                position = self.pbTopLeft.pos()+self.frameCropImage.pos()
                position.setX(position.x()-1)
                self.pbTopLeft.move(position-self.frameCropImage.pos())
                # Middle Right
                position.setX(self.pbTopRight.pos().x()-((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo))
                position.setY(self.pbTopRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopRightMiddle.move(position-self.frameCropImage.pos())
                # Middle
                position.setX(self.pbTopLeft.pos().x()+((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*Middle))
                position.setY(self.pbTopMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopMiddle.move(position-self.frameCropImage.pos())
                # Middle Left
                position.setX(((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo)+self.pbTopLeft.pos().x())
                position.setY(self.pbTopLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopLeftMiddle.move(position-self.frameCropImage.pos())
            elif self.select == "TopRight":
                position = self.pbTopRight.pos()+self.frameCropImage.pos()
                position.setX(position.x()-1)
                self.pbTopRight.move(position-self.frameCropImage.pos())
                # Middle Right
                position.setX(self.pbTopRight.pos().x()-((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo))
                position.setY(self.pbTopRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopRightMiddle.move(position-self.frameCropImage.pos())
                # Middle
                position.setX(self.pbTopLeft.pos().x()+((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*Middle))
                position.setY(self.pbTopMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopMiddle.move(position-self.frameCropImage.pos())
                # Middle Left
                position.setX(((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo)+self.pbTopLeft.pos().x())
                position.setY(self.pbTopLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopLeftMiddle.move(position-self.frameCropImage.pos())
            elif self.select == "BottomRight":
                position = self.pbBottomRight.pos()+self.frameCropImage.pos()
                position.setX(position.x()-1)
                self.pbBottomRight.move(position-self.frameCropImage.pos())
                # Middle Right
                position.setX(self.pbBottomRight.pos().x()-((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf))
                position.setY(self.pbBottomRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomRightMiddle.move(position-self.frameCropImage.pos())
                # Middle
                position.setX(self.pbBottomLeft.pos().x()+((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*Middle))
                position.setY(self.pbBottomMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomMiddle.move(position-self.frameCropImage.pos())
                # Middle Left
                position.setX(((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf)+self.pbBottomLeft.pos().x())
                position.setY(self.pbBottomLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomLeftMiddle.move(position-self.frameCropImage.pos())
            elif self.select == "BottomLeft":
                position = self.pbBottomLeft.pos()+self.frameCropImage.pos()
                position.setX(position.x()-1)
                self.pbBottomLeft.move(position-self.frameCropImage.pos())
                # Middle Right
                position.setX(self.pbBottomRight.pos().x()-((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf))
                position.setY(self.pbBottomRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomRightMiddle.move(position-self.frameCropImage.pos())
                # Middle
                position.setX(self.pbBottomLeft.pos().x()+((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*Middle))
                position.setY(self.pbBottomMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomMiddle.move(position-self.frameCropImage.pos())
                # Middle Left
                position.setX(((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf)+self.pbBottomLeft.pos().x())
                position.setY(self.pbBottomLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomLeftMiddle.move(position-self.frameCropImage.pos())
            else: pass
        elif event.key() == qtc.Qt.Key_Right:
            if self.select == "TopLeft":
                position = self.pbTopLeft.pos()+self.frameCropImage.pos()
                position.setX(position.x()+1)
                self.pbTopLeft.move(position-self.frameCropImage.pos())
                # Middle Right
                position.setX(self.pbTopRight.pos().x()-((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo))
                position.setY(self.pbTopRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopRightMiddle.move(position-self.frameCropImage.pos())
                # Middle
                position.setX(self.pbTopLeft.pos().x()+((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*Middle))
                position.setY(self.pbTopMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopMiddle.move(position-self.frameCropImage.pos())
                # Middle Left
                position.setX(((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo)+self.pbTopLeft.pos().x())
                position.setY(self.pbTopLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopLeftMiddle.move(position-self.frameCropImage.pos())
            elif self.select == "TopRight":
                position = self.pbTopRight.pos()+self.frameCropImage.pos()
                position.setX(position.x()+1)
                self.pbTopRight.move(position-self.frameCropImage.pos())
                # Middle Right
                position.setX(self.pbTopRight.pos().x()-((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo))
                position.setY(self.pbTopRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopRightMiddle.move(position-self.frameCropImage.pos())
                # Middle
                position.setX(self.pbTopLeft.pos().x()+((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*Middle))
                position.setY(self.pbTopMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopMiddle.move(position-self.frameCropImage.pos())
                # Middle Left
                position.setX(((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo)+self.pbTopLeft.pos().x())
                position.setY(self.pbTopLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopLeftMiddle.move(position-self.frameCropImage.pos())
            elif self.select == "BottomRight":
                position = self.pbBottomRight.pos()+self.frameCropImage.pos()
                position.setX(position.x()+1)
                self.pbBottomRight.move(position-self.frameCropImage.pos())
                # Middle Right
                position.setX(self.pbBottomRight.pos().x()-((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf))
                position.setY(self.pbBottomRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomRightMiddle.move(position-self.frameCropImage.pos())
                # Middle
                position.setX(self.pbBottomLeft.pos().x()+((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*Middle))
                position.setY(self.pbBottomMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomMiddle.move(position-self.frameCropImage.pos())
                # Middle Left
                position.setX(((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf)+self.pbBottomLeft.pos().x())
                position.setY(self.pbBottomLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomLeftMiddle.move(position-self.frameCropImage.pos())
            elif self.select == "BottomLeft":
                position = self.pbBottomLeft.pos()+self.frameCropImage.pos()
                position.setX(position.x()+1)
                self.pbBottomLeft.move(position-self.frameCropImage.pos())
                # Middle Right
                position.setX(self.pbBottomRight.pos().x()-((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf))
                position.setY(self.pbBottomRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomRightMiddle.move(position-self.frameCropImage.pos())
                # Middle
                position.setX(self.pbBottomLeft.pos().x()+((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*Middle))
                position.setY(self.pbBottomMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomMiddle.move(position-self.frameCropImage.pos())
                # Middle Left
                position.setX(((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf)+self.pbBottomLeft.pos().x())
                position.setY(self.pbBottomLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomLeftMiddle.move(position-self.frameCropImage.pos())
            else: pass
        elif event.key() == qtc.Qt.Key_Up:
            if self.select == "TopLeft":
                position = self.pbTopLeft.pos()+self.frameCropImage.pos()
                position.setY(position.y()-1)
                self.pbTopLeft.move(position-self.frameCropImage.pos())
            elif self.select == "TopRight":
                position = self.pbTopRight.pos()+self.frameCropImage.pos()
                position.setY(position.y()-1)
                self.pbTopRight.move(position-self.frameCropImage.pos())
            elif self.select == "TopLeftMiddle":
                position = self.pbTopLeftMiddle.pos()+self.frameCropImage.pos()
                position.setY(position.y()-1)
                self.pbTopLeftMiddle.move(position-self.frameCropImage.pos())
            elif self.select == "TopMiddle":
                position = self.pbTopMiddle.pos()+self.frameCropImage.pos()
                position.setY(position.y()-1)
                self.pbTopMiddle.move(position-self.frameCropImage.pos())
            elif self.select == "TopRightMiddle":
                position = self.pbTopRightMiddle.pos()+self.frameCropImage.pos()
                position.setY(position.y()-1)
                self.pbTopRightMiddle.move(position-self.frameCropImage.pos())
            elif self.select == "BottomRight":
                position = self.pbBottomRight.pos()+self.frameCropImage.pos()
                position.setY(position.y()-1)
                self.pbBottomRight.move(position-self.frameCropImage.pos())
            elif self.select == "BottomLeft":
                position = self.pbBottomLeft.pos()+self.frameCropImage.pos()
                position.setY(position.y()-1)
                self.pbBottomLeft.move(position-self.frameCropImage.pos())
            elif self.select == "BottomLeftMiddle":
                position = self.pbBottomLeftMiddle.pos()+self.frameCropImage.pos()
                position.setY(position.y()-1)
                self.pbBottomLeftMiddle.move(position-self.frameCropImage.pos())
            elif self.select == "BottomMiddle":
                position = self.pbBottomMiddle.pos()+self.frameCropImage.pos()
                position.setY(position.y()-1)
                self.pbBottomMiddle.move(position-self.frameCropImage.pos())
            elif self.select == "BottomRightMiddle":
                position = self.pbBottomRightMiddle.pos()+self.frameCropImage.pos()
                position.setY(position.y()-1)
                self.pbBottomRightMiddle.move(position-self.frameCropImage.pos())
            else: pass
        elif event.key() == qtc.Qt.Key_Down:
            if self.select == "TopLeft":
                position = self.pbTopLeft.pos()+self.frameCropImage.pos()
                position.setY(position.y()+1)
                self.pbTopLeft.move(position-self.frameCropImage.pos())
            elif self.select == "TopRight":
                position = self.pbTopRight.pos()+self.frameCropImage.pos()
                position.setY(position.y()+1)
                self.pbTopRight.move(position-self.frameCropImage.pos())
            elif self.select == "TopLeftMiddle":
                position = self.pbTopLeftMiddle.pos()+self.frameCropImage.pos()
                position.setY(position.y()+1)
                self.pbTopLeftMiddle.move(position-self.frameCropImage.pos())
            elif self.select == "TopMiddle":
                position = self.pbTopMiddle.pos()+self.frameCropImage.pos()
                position.setY(position.y()+1)
                self.pbTopMiddle.move(position-self.frameCropImage.pos())
            elif self.select == "TopRightMiddle":
                position = self.pbTopRightMiddle.pos()+self.frameCropImage.pos()
                position.setY(position.y()+1)
                self.pbTopRightMiddle.move(position-self.frameCropImage.pos())
            elif self.select == "BottomRight":
                position = self.pbBottomRight.pos()+self.frameCropImage.pos()
                position.setY(position.y()+1)
                self.pbBottomRight.move(position-self.frameCropImage.pos())
            elif self.select == "BottomLeft":
                position = self.pbBottomLeft.pos()+self.frameCropImage.pos()
                position.setY(position.y()+1)
                self.pbBottomLeft.move(position-self.frameCropImage.pos())
            elif self.select == "BottomLeftMiddle":
                position = self.pbBottomLeftMiddle.pos()+self.frameCropImage.pos()
                position.setY(position.y()+1)
                self.pbBottomLeftMiddle.move(position-self.frameCropImage.pos())
            elif self.select == "BottomMiddle":
                position = self.pbBottomMiddle.pos()+self.frameCropImage.pos()
                position.setY(position.y()+1)
                self.pbBottomMiddle.move(position-self.frameCropImage.pos())
            elif self.select == "BottomRightMiddle":
                position = self.pbBottomRightMiddle.pos()+self.frameCropImage.pos()
                position.setY(position.y()+1)
                self.pbBottomRightMiddle.move(position-self.frameCropImage.pos())
            else: pass
        else: pass
        self.update()
    def dragMoveEvent(self, e) -> None:
        position = e.position().toPoint()
        if self.select == "TopLeft":
            self.pbTopLeft.show()
            if position.x()>=self.frameCropImage2.pos().x() and position.x()<=self.frameCropImage2.width()/2:
                position.setX(position.x()-self.pbTopLeft.width()/2-self.frameCropImage2.pos().x())
            else:
                if position.x()<self.frameCropImage2.pos().x():
                    position.setX(0)
                else:
                    position.setX(self.frameCropImage2.width()/2-20)
            if position.y()>=self.frameCropImage2.pos().y() and position.y()<=self.frameCropImage2.height()+self.frameCropImage2.pos().y():
                position.setY(position.y()-self.pbTopLeft.height()/2-self.frameCropImage2.pos().y())
            else:
                if position.y()<self.frameCropImage2.pos().y():
                    position.setY(0)
                else:
                    position.setY(self.frameCropImage2.height()-20)
            self.pbTopLeft.move(position)
            # Middle Right
            position.setX(self.pbTopRight.pos().x()-((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo))
            position.setY(self.pbTopRightMiddle.pos().y()+self.frameCropImage.pos().y())
            self.pbTopRightMiddle.move(position-self.frameCropImage.pos())
            # Middle
            position.setX(self.pbTopLeft.pos().x()+((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*Middle))
            position.setY(self.pbTopMiddle.pos().y()+self.frameCropImage.pos().y())
            self.pbTopMiddle.move(position-self.frameCropImage.pos())
            # Middle Left
            position.setX(((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo)+self.pbTopLeft.pos().x())
            position.setY(self.pbTopLeftMiddle.pos().y()+self.frameCropImage.pos().y())
            self.pbTopLeftMiddle.move(position-self.frameCropImage.pos())
        elif self.select == "TopRight":
            self.pbTopRight.show()
            if position.x()>=self.frameCropImage2.pos().x() and position.x()<=self.frameCropImage2.width()/2:
                position.setX(position.x()-self.pbTopRight.width()/2-self.frameCropImage2.pos().x())
            else:
                if position.x()<self.frameCropImage2.pos().x():
                    position.setX(0)
                else:
                    position.setX(self.frameCropImage2.width()/2-20)
            if position.y()>=self.frameCropImage2.pos().y() and position.y()<=self.frameCropImage2.height()+self.frameCropImage2.pos().y():
                position.setY(position.y()-self.pbTopRight.height()/2-self.frameCropImage2.pos().y())
            else:
                if position.y()<self.frameCropImage2.pos().y():
                    position.setY(0)
                else:
                    position.setY(self.frameCropImage2.height()-20)
            self.pbTopRight.move(position-self.frameCropImage.pos())
            # Middle Right
            position.setX(self.pbTopRight.pos().x()-((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo))
            position.setY(self.pbTopRightMiddle.pos().y()+self.frameCropImage.pos().y())
            self.pbTopRightMiddle.move(position-self.frameCropImage.pos())
            # Middle
            position.setX(self.pbTopLeft.pos().x()+((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*Middle))
            position.setY(self.pbTopMiddle.pos().y()+self.frameCropImage.pos().y())
            self.pbTopMiddle.move(position-self.frameCropImage.pos())
            # Middle Left
            position.setX(((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo)+self.pbTopLeft.pos().x())
            position.setY(self.pbTopLeftMiddle.pos().y()+self.frameCropImage.pos().y())
            self.pbTopLeftMiddle.move(position-self.frameCropImage.pos())
        elif self.select == "TopLeftMiddle":
            self.pbTopLeftMiddle.show()
            #position.setX(position.x()-self.pbTopLeftMiddle.width()/2)
            position.setX(((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo)+self.pbTopLeft.pos().x())
            if position.y()>=self.frameCropImage2.pos().y() and position.y()<=self.frameCropImage2.height()+self.frameCropImage2.pos().y():
                position.setY(position.y()-self.pbTopLeftMiddle.height()/2-self.frameCropImage2.pos().y())
            else:
                if position.y()<self.frameCropImage2.pos().y():
                    position.setY(0)
                else:
                    position.setY(self.frameCropImage2.height()-20)
            self.pbTopLeftMiddle.move(position-self.frameCropImage.pos())
        elif self.select == "TopMiddle":
            self.pbTopMiddle.show()
            #position.setX(position.x()-self.pbTopMiddle.width()/2)
            position.setX(((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*Middle)+self.pbTopLeft.pos().x())
            if position.y()>=self.frameCropImage2.pos().y() and position.y()<=self.frameCropImage2.height()+self.frameCropImage2.pos().y():
                position.setY(position.y()-self.pbTopMiddle.height()/2-self.frameCropImage2.pos().y())
            else:
                if position.y()<self.frameCropImage2.pos().y():
                    position.setY(0)
                else:
                    position.setY(self.frameCropImage2.height()-20)
            self.pbTopMiddle.move(position-self.frameCropImage.pos())
        elif self.select == "TopRightMiddle":
            self.pbTopRightMiddle.show()
            #position.setX(position.x()-self.pbTopRightMiddle.width()/2)
            position.setX(self.pbTopRight.pos().x()-((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo))
            if position.y()>=self.frameCropImage2.pos().y() and position.y()<=self.frameCropImage2.height()+self.frameCropImage2.pos().y():
                position.setY(position.y()-self.pbTopRightMiddle.height()/2-self.frameCropImage2.pos().y())
            else:
                if position.y()<self.frameCropImage2.pos().y():
                    position.setY(0)
                else:
                    position.setY(self.frameCropImage2.height()-20)
            self.pbTopRightMiddle.move(position-self.frameCropImage.pos())
        elif self.select == "BottomRight":
            self.pbBottomRight.show()
            if position.x()>=self.frameCropImage2.pos().x() and position.x()<=self.frameCropImage2.width()/2:
                position.setX(position.x()-self.pbBottomRight.width()/2-self.frameCropImage2.pos().x())
            else:
                if position.x()<self.frameCropImage2.pos().x():
                    position.setX(0)
                else:
                    position.setX(self.frameCropImage2.width()/2-20)
            if position.y()>=self.frameCropImage2.pos().y() and position.y()<=self.frameCropImage2.height()+self.frameCropImage2.pos().y():
                position.setY(position.y()-self.pbBottomRight.height()/2-self.frameCropImage2.pos().y())
            else:
                if position.y()<self.frameCropImage2.pos().y():
                    position.setY(0)
                else:
                    position.setY(self.frameCropImage2.height()-20)
            self.pbBottomRight.move(position-self.frameCropImage.pos())
            # Middle Right
            position.setX(self.pbBottomRight.pos().x()-((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf))
            position.setY(self.pbBottomRightMiddle.pos().y()+self.frameCropImage.pos().y())
            self.pbBottomRightMiddle.move(position-self.frameCropImage.pos())
            # Middle
            position.setX(self.pbBottomLeft.pos().x()+((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*Middle))
            position.setY(self.pbBottomMiddle.pos().y()+self.frameCropImage.pos().y())
            self.pbBottomMiddle.move(position-self.frameCropImage.pos())
            # Middle Left
            position.setX(((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf)+self.pbBottomLeft.pos().x())
            position.setY(self.pbBottomLeftMiddle.pos().y()+self.frameCropImage.pos().y())
            self.pbBottomLeftMiddle.move(position-self.frameCropImage.pos())
        elif self.select == "BottomLeft":
            self.pbBottomLeft.show()
            if position.x()>=self.frameCropImage2.pos().x() and position.x()<=self.frameCropImage2.width()/2:
                position.setX(position.x()-self.pbBottomRight.width()/2-self.frameCropImage2.pos().x())
            else:
                if position.x()<self.frameCropImage2.pos().x():
                    position.setX(0)
                else:
                    position.setX(self.frameCropImage2.width()/2-20)
            if position.y()>=self.frameCropImage2.pos().y() and position.y()<=self.frameCropImage2.height()+self.frameCropImage2.pos().y():
                position.setY(position.y()-self.pbBottomRight.height()/2-self.frameCropImage2.pos().y())
            else:
                if position.y()<self.frameCropImage2.pos().y():
                    position.setY(0)
                else:
                    position.setY(self.frameCropImage2.height()-20)
            self.pbBottomLeft.move(position-self.frameCropImage.pos())
            # Middle Right
            position.setX(self.pbBottomRight.pos().x()-((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf))
            position.setY(self.pbBottomRightMiddle.pos().y()+self.frameCropImage.pos().y())
            self.pbBottomRightMiddle.move(position-self.frameCropImage.pos())
            # Middle
            position.setX(self.pbBottomLeft.pos().x()+((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*Middle))
            position.setY(self.pbBottomMiddle.pos().y()+self.frameCropImage.pos().y())
            self.pbBottomMiddle.move(position-self.frameCropImage.pos())
            # Middle Left
            position.setX(((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf)+self.pbBottomLeft.pos().x())
            position.setY(self.pbBottomLeftMiddle.pos().y()+self.frameCropImage.pos().y())
            self.pbBottomLeftMiddle.move(position-self.frameCropImage.pos())
        elif self.select == "BottomLeftMiddle":
            self.pbBottomLeftMiddle.show()
            #position.setX(position.x()-self.pbBottomLeftMiddle.width()/2)
            position.setX(((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf)+self.pbBottomLeft.pos().x())
            if position.y()>=self.frameCropImage2.pos().y() and position.y()<=self.frameCropImage2.height()+self.frameCropImage2.pos().y():
                position.setY(position.y()-self.pbBottomLeftMiddle.height()/2-self.frameCropImage2.pos().y())
            else:
                if position.y()<self.frameCropImage2.pos().y():
                    position.setY(0)
                else:
                    position.setY(self.frameCropImage2.height()-20)
            self.pbBottomLeftMiddle.move(position-self.frameCropImage.pos())
        elif self.select == "BottomMiddle":
            self.pbBottomMiddle.show()
            #position.setX(position.x()-self.pbBottomMiddle.width()/2)
            position.setX(((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*Middle)+self.pbBottomLeft.pos().x())
            if position.y()>=self.frameCropImage2.pos().y() and position.y()<=self.frameCropImage2.height()+self.frameCropImage2.pos().y():
                position.setY(position.y()-self.pbBottomMiddle.height()/2-self.frameCropImage2.pos().y())
            else:
                if position.y()<self.frameCropImage2.pos().y():
                    position.setY(0)
                else:
                    position.setY(self.frameCropImage2.height()-20)
            self.pbBottomMiddle.move(position-self.frameCropImage.pos())
        elif self.select == "BottomRightMiddle":
            self.pbBottomRightMiddle.show()
            #position.setX(position.x()-self.pbBottomRightMiddle.width()/2)
            position.setX(self.pbBottomRight.pos().x()-((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf))
            if position.y()>=self.frameCropImage2.pos().y() and position.y()<=self.frameCropImage2.height()+self.frameCropImage2.pos().y():
                position.setY(position.y()-self.pbTopRightMiddle.height()/2-self.frameCropImage2.pos().y())
            else:
                if position.y()<self.frameCropImage2.pos().y():
                    position.setY(0)
                else:
                    position.setY(self.frameCropImage2.height()-20)
            self.pbBottomRightMiddle.move(position-self.frameCropImage.pos())
        else: pass
        e.setDropAction(qtc.Qt.MoveAction)
        self.update()
        e.accept()
    def dropEvent(self, e):
        position = e.position().toPoint()
        if self.select == "TopLeft":
            if self.pbTopLeft.pos().x()+self.pbTopLeft.height()/2 >= self.frameCropImage.width():
                position.setX(self.frameCropImage.width()-self.pbTopLeft.width()/2+self.frameCropImage.pos().x())
                position.setY(self.pbTopLeft.pos().y()+self.frameCropImage.pos().y())
                self.pbTopLeft.move(position-self.frameCropImage.pos())
                # Middle Right
                position.setX(self.pbTopRight.pos().x()-((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo))
                position.setY(self.pbTopRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopRightMiddle.move(position-self.frameCropImage.pos())
                # Middle Left
                position.setX(((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo)+self.pbTopLeft.pos().x())
                position.setY(self.pbTopLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopLeftMiddle.move(position-self.frameCropImage.pos())
            if self.pbTopLeft.pos().x()+self.pbTopLeft.height()/2 <= 0:
                position.setX(self.frameCropImage.pos().x()-self.pbTopLeft.height()/2)
                position.setY(self.pbTopLeft.pos().y()+self.frameCropImage.pos().y())
                self.pbTopLeft.move(position-self.frameCropImage.pos())
                # Middle Right
                position.setX(self.pbTopRight.pos().x()-((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo))
                position.setY(self.pbTopRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopRightMiddle.move(position-self.frameCropImage.pos())
                # Middle Left
                position.setX(((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo)+self.pbTopLeft.pos().x())
                position.setY(self.pbTopLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopLeftMiddle.move(position-self.frameCropImage.pos())
            if self.pbTopLeft.pos().y()+self.pbTopLeft.height()/2 <= 0:
                position.setX(self.pbTopLeft.pos().x()+self.pbTopLeft.width()/2-9)
                position.setY(self.frameCropImage.pos().y()-self.pbTopLeft.height()/2)
                self.pbTopLeft.move(position-self.frameCropImage.pos())
            if self.pbTopLeft.pos().y()+self.pbTopLeft.height()/2 >= self.frameCropImage.height():
                position.setX(self.pbTopLeft.pos().x()+self.pbTopLeft.width()/2-9)
                position.setY(self.frameCropImage.height()-self.pbTopLeft.height()/2+self.frameCropImage.pos().y())
                self.pbTopLeft.move(position-self.frameCropImage.pos())
        if self.select == "TopLeftMiddle":
            if self.pbTopLeftMiddle.pos().x()+self.pbTopLeftMiddle.height()/2 >= self.frameCropImage.width():
                position.setX(self.frameCropImage.width()-self.pbTopLeftMiddle.width()/2+self.frameCropImage.pos().x())
                position.setY(self.pbTopLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopLeftMiddle.move(position-self.frameCropImage.pos())
            if self.pbTopLeftMiddle.pos().x()+self.pbTopLeftMiddle.height()/2 <= 0:
                position.setX(self.frameCropImage.pos().x()-self.pbTopLeftMiddle.height()/2)
                position.setY(self.pbTopLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopLeftMiddle.move(position-self.frameCropImage.pos())
            if self.pbTopLeftMiddle.pos().y()+self.pbTopLeftMiddle.height()/2 <= 0:
                position.setX(self.pbTopLeftMiddle.pos().x()+self.pbTopLeftMiddle.width()/2-9)
                position.setY(self.frameCropImage.pos().y()-self.pbTopLeftMiddle.height()/2)
                self.pbTopLeftMiddle.move(position-self.frameCropImage.pos())
            if self.pbTopLeftMiddle.pos().y()+self.pbTopLeftMiddle.height()/2 >= self.frameCropImage.height():
                position.setX(self.pbTopLeftMiddle.pos().x()+self.pbTopLeftMiddle.width()/2-9)
                position.setY(self.frameCropImage.height()-self.pbTopLeftMiddle.height()/2+self.frameCropImage.pos().y())
                self.pbTopLeftMiddle.move(position-self.frameCropImage.pos())
        if self.select == "TopRightMiddle":
            if self.pbTopRightMiddle.pos().x()+self.pbTopRightMiddle.height()/2 >= self.frameCropImage.width():
                position.setX(self.frameCropImage.width()-self.pbTopRightMiddle.width()/2+self.frameCropImage.pos().x())
                position.setY(self.pbTopRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopRightMiddle.move(position-self.frameCropImage.pos())
            if self.pbTopRightMiddle.pos().x()+self.pbTopRightMiddle.height()/2 <= 0:
                position.setX(self.frameCropImage.pos().x()-self.pbTopRightMiddle.height()/2)
                position.setY(self.pbTopRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopRightMiddle.move(position-self.frameCropImage.pos())
            if self.pbTopRightMiddle.pos().y()+self.pbTopRightMiddle.height()/2 <= 0:
                position.setX(self.pbTopRightMiddle.pos().x()+self.pbTopRightMiddle.width()/2-9)
                position.setY(self.frameCropImage.pos().y()-self.pbTopRightMiddle.height()/2)
                self.pbTopRightMiddle.move(position-self.frameCropImage.pos())
            if self.pbTopRightMiddle.pos().y()+self.pbTopRightMiddle.height()/2 >= self.frameCropImage.height():
                position.setX(self.pbTopRightMiddle.pos().x()+self.pbTopRightMiddle.width()/2-9)
                position.setY(self.frameCropImage.height()-self.pbTopRightMiddle.height()/2+self.frameCropImage.pos().y())
                self.pbTopRightMiddle.move(position-self.frameCropImage.pos())
        if self.select == "TopRight":
            if self.pbTopRight.pos().x()+self.pbTopRight.height()/2 >= self.frameCropImage.width():
                position.setX(self.frameCropImage.width()-self.pbTopRight.width()/2+self.frameCropImage.pos().x())
                position.setY(self.pbTopRight.pos().y()+self.frameCropImage.pos().y())
                self.pbTopRight.move(position-self.frameCropImage.pos())
                # Middle Right
                position.setX(self.pbTopRight.pos().x()-((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo))
                position.setY(self.pbTopRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopRightMiddle.move(position-self.frameCropImage.pos())
                # Middle Left
                position.setX(((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo)+self.pbTopLeft.pos().x())
                position.setY(self.pbTopLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopLeftMiddle.move(position-self.frameCropImage.pos())
            if self.pbTopRight.pos().x()+self.pbTopRight.height()/2 <= 0:
                position.setX(self.frameCropImage.pos().x()-self.pbTopRight.height()/2)
                position.setY(self.pbTopRight.pos().y()+self.frameCropImage.pos().y())
                self.pbTopRight.move(position-self.frameCropImage.pos())
                # Middle Right
                position.setX(self.pbTopRight.pos().x()-((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo))
                position.setY(self.pbTopRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopRightMiddle.move(position-self.frameCropImage.pos())
                # Middle Left
                position.setX(((self.pbTopRight.pos().x()-self.pbTopLeft.pos().x())*D_Anillo)+self.pbTopLeft.pos().x())
                position.setY(self.pbTopLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbTopLeftMiddle.move(position-self.frameCropImage.pos())
            if self.pbTopRight.pos().y()+self.pbTopRight.height()/2 <= 0:
                position.setX(self.pbTopRight.pos().x()+self.pbTopRight.width()/2-9)
                position.setY(self.frameCropImage.pos().y()-self.pbTopRight.height()/2)
                self.pbTopRight.move(position-self.frameCropImage.pos())
            if self.pbTopRight.pos().y()+self.pbTopRight.height()/2 >= self.frameCropImage.height():
                position.setX(self.pbTopRight.pos().x()+self.pbTopRight.width()/2-9)
                position.setY(self.frameCropImage.height()-self.pbTopRight.height()/2+self.frameCropImage.pos().y())
                self.pbTopRight.move(position-self.frameCropImage.pos())     
        if self.select == "BottomRight":
            if self.pbBottomRight.pos().x()+self.pbBottomRight.height()/2 >= self.frameCropImage.width():
                position.setX(self.frameCropImage.width()-self.pbBottomRight.width()/2+self.frameCropImage.pos().x())
                position.setY(self.pbBottomRight.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomRight.move(position-self.frameCropImage.pos())
                # Middle Right
                position.setX(self.pbBottomRight.pos().x()-((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf))
                position.setY(self.pbBottomRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomRightMiddle.move(position-self.frameCropImage.pos())
                # Middle Left
                position.setX(((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf)+self.pbBottomLeft.pos().x())
                position.setY(self.pbBottomLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomLeftMiddle.move(position-self.frameCropImage.pos())
            if self.pbBottomRight.pos().x()+self.pbBottomRight.height()/2 <= 0:
                position.setX(self.frameCropImage.pos().x()-self.pbBottomRight.height()/2)
                position.setY(self.pbBottomRight.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomRight.move(position-self.frameCropImage.pos())
                # Middle Right
                position.setX(self.pbBottomRight.pos().x()-((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf))
                position.setY(self.pbBottomRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomRightMiddle.move(position-self.frameCropImage.pos())
                # Middle Left
                position.setX(((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf)+self.pbBottomLeft.pos().x())
                position.setY(self.pbBottomLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomLeftMiddle.move(position-self.frameCropImage.pos())
            if self.pbBottomRight.pos().y()+self.pbBottomRight.height()/2 <= 0:
                position.setX(self.pbBottomRight.pos().x()+self.pbBottomRight.width()/2-9)
                position.setY(self.frameCropImage.pos().y()-self.pbBottomRight.height()/2)
                self.pbBottomRight.move(position-self.frameCropImage.pos())
            if self.pbBottomRight.pos().y()+self.pbBottomRight.height()/2 >= self.frameCropImage.height():
                position.setX(self.pbBottomRight.pos().x()+self.pbBottomRight.width()/2-9)
                position.setY(self.frameCropImage.height()-self.pbBottomRight.height()/2+self.frameCropImage.pos().y())
                self.pbBottomRight.move(position-self.frameCropImage.pos())
        if self.select == "BottomLeft":
            if self.pbBottomLeft.pos().x()+self.pbBottomLeft.height()/2 >= self.frameCropImage.width():
                position.setX(self.frameCropImage.width()-self.pbBottomLeft.width()/2+self.frameCropImage.pos().x())
                position.setY(self.pbBottomLeft.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomLeft.move(position-self.frameCropImage.pos())
                # Middle Right
                position.setX(self.pbBottomRight.pos().x()-((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf))
                position.setY(self.pbBottomRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomRightMiddle.move(position-self.frameCropImage.pos())
                # Middle Left
                position.setX(((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf)+self.pbBottomLeft.pos().x())
                position.setY(self.pbBottomLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomLeftMiddle.move(position-self.frameCropImage.pos())
            if self.pbBottomLeft.pos().x()+self.pbBottomLeft.height()/2 <= 0:
                position.setX(self.frameCropImage.pos().x()-self.pbBottomLeft.height()/2)
                position.setY(self.pbBottomLeft.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomLeft.move(position-self.frameCropImage.pos())
                # Middle Right
                position.setX(self.pbBottomRight.pos().x()-((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf))
                position.setY(self.pbBottomRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomRightMiddle.move(position-self.frameCropImage.pos())
                # Middle Left
                position.setX(((self.pbBottomRight.pos().x()-self.pbBottomLeft.pos().x())*D_Inf)+self.pbBottomLeft.pos().x())
                position.setY(self.pbBottomLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomLeftMiddle.move(position-self.frameCropImage.pos())
            if self.pbBottomLeft.pos().y()+self.pbBottomLeft.height()/2 <= 0:
                position.setX(self.pbBottomLeft.pos().x()+self.pbBottomLeft.width()/2-9)
                position.setY(self.frameCropImage.pos().y()-self.pbBottomLeft.height()/2)
                self.pbBottomLeft.move(position-self.frameCropImage.pos())
            if self.pbBottomLeft.pos().y()+self.pbBottomLeft.height()/2 >= self.frameCropImage.height():
                position.setX(self.pbBottomLeft.pos().x()+self.pbBottomLeft.width()/2-9)
                position.setY(self.frameCropImage.height()-self.pbBottomLeft.height()/2+self.frameCropImage.pos().y())
                self.pbBottomLeft.move(position-self.frameCropImage.pos())
        if self.select == "BottomLeftMiddle":
            if self.pbBottomLeftMiddle.pos().x()+self.pbBottomLeftMiddle.height()/2 >= self.frameCropImage.width():
                position.setX(self.frameCropImage.width()-self.pbBottomLeftMiddle.width()/2+self.frameCropImage.pos().x())
                position.setY(self.pbBottomLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomLeftMiddle.move(position-self.frameCropImage.pos())
            if self.pbBottomLeftMiddle.pos().x()+self.pbBottomLeftMiddle.height()/2 <= 0:
                position.setX(self.frameCropImage.pos().x()-self.pbBottomLeftMiddle.height()/2)
                position.setY(self.pbBottomLeftMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomLeftMiddle.move(position-self.frameCropImage.pos())
            if self.pbBottomLeftMiddle.pos().y()+self.pbBottomLeftMiddle.height()/2 <= 0:
                position.setX(self.pbBottomLeftMiddle.pos().x()+self.pbBottomLeftMiddle.width()/2-9)
                position.setY(self.frameCropImage.pos().y()-self.pbBottomLeftMiddle.height()/2)
                self.pbBottomLeftMiddle.move(position-self.frameCropImage.pos())
            if self.pbBottomLeftMiddle.pos().y()+self.pbBottomLeftMiddle.height()/2 >= self.frameCropImage.height():
                position.setX(self.pbBottomLeftMiddle.pos().x()+self.pbBottomLeftMiddle.width()/2-9)
                position.setY(self.frameCropImage.height()-self.pbBottomLeftMiddle.height()/2+self.frameCropImage.pos().y())
                self.pbBottomLeftMiddle.move(position-self.frameCropImage.pos())
        if self.select == "BottomRightMiddle":
            if self.pbBottomRightMiddle.pos().x()+self.pbBottomRightMiddle.height()/2 >= self.frameCropImage.width():
                position.setX(self.frameCropImage.width()-self.pbBottomRightMiddle.width()/2+self.frameCropImage.pos().x())
                position.setY(self.pbBottomRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomRightMiddle.move(position-self.frameCropImage.pos())
            if self.pbBottomRightMiddle.pos().x()+self.pbBottomRightMiddle.height()/2 <= 0:
                position.setX(self.frameCropImage.pos().x()-self.pbBottomRightMiddle.height()/2)
                position.setY(self.pbBottomRightMiddle.pos().y()+self.frameCropImage.pos().y())
                self.pbBottomRightMiddle.move(position-self.frameCropImage.pos())
            if self.pbBottomRightMiddle.pos().y()+self.pbBottomRightMiddle.height()/2 <= 0:
                position.setX(self.pbBottomRightMiddle.pos().x()+self.pbBottomRightMiddle.width()/2-9)
                position.setY(self.frameCropImage.pos().y()-self.pbBottomRightMiddle.height()/2)
                self.pbBottomRightMiddle.move(position-self.frameCropImage.pos())
            if self.pbBottomRightMiddle.pos().y()+self.pbBottomRightMiddle.height()/2 >= self.frameCropImage.height():
                position.setX(self.pbBottomRightMiddle.pos().x()+self.pbBottomRightMiddle.width()/2-9)
                position.setY(self.frameCropImage.height()-self.pbBottomRightMiddle.height()/2+self.frameCropImage.pos().y())
                self.pbBottomRightMiddle.move(position-self.frameCropImage.pos())
        self.update()
    def paintEvent(self, event: QPaintEvent) -> None:
        painter = qtg.QPainter(self)
        pixmap = qtg.QPixmap(self.pathImage)
        painter.drawPixmap(9, 64, 928, 696 , pixmap)
        #painter.begin(self)
        painter.setRenderHint(qtg.QPainter.Antialiasing)
        painter.setPen(qtg.QPen(qtg.QColor(0, 0, 255, 60), 4, qtc.Qt.DotLine))
        brush = qtg.QBrush(qtg.QColor(0, 0, 255, 60))
        painter.setBrush(brush)
        points = [
            qtc.QPoint(self.pbTopLeft.pos().x()+self.pbTopLeft.width()/2+self.frameCropImage.pos().x()+self.frameCropImage2.pos().x(), self.pbTopLeft.geometry().y()+self.pbTopLeft.height()/2+self.frameCropImage.pos().y()+self.frameCropImage2.pos().y()),
            qtc.QPoint(self.pbTopLeftMiddle.geometry().x()+self.pbTopLeftMiddle.width()/2+self.frameCropImage.geometry().x()+self.frameCropImage2.pos().x(), self.pbTopLeftMiddle.geometry().y()+self.pbTopLeftMiddle.height()/2+self.frameCropImage.geometry().y()+self.frameCropImage2.pos().y()),
            qtc.QPoint(self.pbTopMiddle.geometry().x()+self.pbTopMiddle.width()/2+self.frameCropImage.geometry().x()+self.frameCropImage2.pos().x(), self.pbTopMiddle.geometry().y()+self.pbTopMiddle.height()/2+self.frameCropImage.geometry().y()+self.frameCropImage2.pos().y()),
            qtc.QPoint(self.pbTopRightMiddle.geometry().x()+self.pbTopRightMiddle.width()/2+self.frameCropImage.geometry().x()+self.frameCropImage2.pos().x(), self.pbTopRightMiddle.geometry().y()+self.pbTopRightMiddle.height()/2+self.frameCropImage.geometry().y()+self.frameCropImage2.pos().y()),
            qtc.QPoint(self.pbTopRight.geometry().x()+self.pbTopRight.width()/2+self.frameCropImage.geometry().x()+self.frameCropImage2.pos().x(), self.pbTopRight.geometry().y()+self.pbTopRight.height()/2+self.frameCropImage.geometry().y()+self.frameCropImage2.pos().y()),
            qtc.QPoint(self.pbBottomRight.geometry().x()+self.pbBottomRight.width()/2+self.frameCropImage.geometry().x()+self.frameCropImage2.pos().x(), self.pbBottomRight.geometry().y()+self.pbBottomRight.height()/2+self.frameCropImage.geometry().y()+self.frameCropImage2.pos().y()),
            qtc.QPoint(self.pbBottomRightMiddle.geometry().x()+self.pbBottomRightMiddle.width()/2+self.frameCropImage.geometry().x()+self.frameCropImage2.pos().x(), self.pbBottomRightMiddle.geometry().y()+self.pbBottomRightMiddle.height()/2+self.frameCropImage.geometry().y()+self.frameCropImage2.pos().y()),
            qtc.QPoint(self.pbBottomMiddle.geometry().x()+self.pbBottomMiddle.width()/2+self.frameCropImage.geometry().x()+self.frameCropImage2.pos().x(), self.pbBottomMiddle.geometry().y()+self.pbBottomMiddle.height()/2+self.frameCropImage.geometry().y()+self.frameCropImage2.pos().y()),
            qtc.QPoint(self.pbBottomLeftMiddle.geometry().x()+self.pbBottomLeftMiddle.width()/2+self.frameCropImage.geometry().x()+self.frameCropImage2.pos().x(), self.pbBottomLeftMiddle.geometry().y()+self.pbBottomLeftMiddle.height()/2+self.frameCropImage.geometry().y()+self.frameCropImage2.pos().y()),
            qtc.QPoint(self.pbBottomLeft.geometry().x()+self.pbBottomLeft.width()/2+self.frameCropImage.geometry().x()+self.frameCropImage2.pos().x(), self.pbBottomLeft.geometry().y()+self.pbBottomLeft.height()/2+self.frameCropImage.geometry().y()+self.frameCropImage2.pos().y())
        ]
        painter.drawPolygon(points)

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
        try:
            lastCampana = str(dataManager.getNameCampanas(nameCuchara)[-1])
            pathPdfFile = "Historial/CUCHARA_"+str(nameCuchara)+"/CUCHARA_"+str(nameCuchara)+"_CAMPANA_"+lastCampana+"/Reporte Cuchara "+str(nameCuchara)+" - Campana "+str(lastCampana)+".pdf"
            pathTotal = dataManager.getWorkingDirectory()+"/"+pathPdfFile
            if isfile(pathTotal):
                nameFile = "Reporte Cuchara "+str(nameCuchara)+" - Campana "+str(lastCampana)+".pdf"
                body = "Ha finalizado la Campaña #"+str(lastCampana)+" de la Cuchara "+str(nameCuchara)+". \nEl reporte de la campaña #"+str(lastCampana)+" ha sido generado y enviado a su correo electrónico. \n\n\nSi el archivo adjunto está corrupto, se puede obtener el reporte en la siguiente dirección del ordenador que tiene instalado la interfaz gráfica: "+str(pathTotal)
                dataManager.sendEmail(body, "Interfaz Gráfica Cucharas - ABAXFEM. Fin de la Campaña #"+ str(lastCampana)+" de la Cuchara "+str(nameCuchara), pathPdfFile, nameFile)
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

class PopUpAddColada(qtw.QMainWindow, Ui_PopUpAddColada, QRunnable):
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
        self.pb_recortar.clicked.connect(self.recortarImg)
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
        self.pb_aceptar.setEnabled(0)
        self.pb_recortar.setEnabled(1)
        regex = qtc.QRegularExpression("[0-9-a-z-A-Z_ .,/\!@$%^&*()=+:;?+-ñáéíóú]+")
        validator = qtg.QRegularExpressionValidator(regex)
        self.txtObservaciones.setValidator(validator)
    def recortarImg(self):
        global windowColada
        if self.txtNewColada.text() != "":
            windowColada = self.window()
            windowColada.hide()
            self.cropWindow = cropWindow(self.txtPathTermografiaF.text())
            self.cropWindow.show()
            self.pb_recortar.setEnabled(0)
            self.pb_aceptar.setEnabled(1)
            self.pb_recortar.setText("Recorte Realizado")
        else:
            pass
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
                self.pb_aceptar.setEnabled(0)
                self.pb_recortar.setEnabled(1)
                self.pb_recortar.setText("Recortar Imagen")
            else:
                self.txtPathTermografiaF.setText("Error en el nombre")
                self.txtPathTermografiaT.setText("Error en el nombre")
                self.txtPathExcelF.setText("o archivos faltantes")
                self.txtPathExcelT.setText("o archivos faltantes")
                self.txtNewColada.setText("")
                self.pb_aceptar.setEnabled(0)
                self.pb_recortar.setEnabled(1)
                self.pb_recortar.setText("Recortar Imagen")
        except:
            self.txtPathTermografiaF.setText("Error en el nombre")
            self.txtPathTermografiaT.setText("Error en el nombre")
            self.txtPathExcelF.setText("o archivos faltantes")
            self.txtPathExcelT.setText("o archivos faltantes")
            self.txtNewColada.setText("")
            self.pb_aceptar.setEnabled(0)
            self.pb_recortar.setEnabled(1)
            self.pb_recortar.setText("Recortar Imagen")
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
            self.pb_aceptar.setEnabled(0)
            self.pb_recortar.setEnabled(1)
            self.pb_recortar.setText("Recortar Imagen")
            self.txtUltimaColada.setText(str(dataManager.getNameColadas(self.cbCuchara.currentText()[8:len(self.cbCuchara.currentText())], self.txtCampana.text())[-1]))
        except:
            self.txtCampana.setText("")
            self.txtPathTermografiaF.setText("Error en el nombre")
            self.txtPathTermografiaT.setText("Error en el nombre")
            self.txtPathExcelF.setText("o archivos faltantes")
            self.txtPathExcelT.setText("o archivos faltantes")
            self.txtNewColada.setText("")
            self.txtUltimaColada.setText("")
            self.pb_aceptar.setEnabled(0)
            self.pb_recortar.setEnabled(1)
            self.pb_recortar.setText("Recortar Imagen")
    def addColada(self):
        global PositionMatrixF, PositionMatrixT
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
                PositionMatrixF = pd.DataFrame(PositionMatrixF)
                PositionMatrixT = pd.DataFrame(PositionMatrixT)
                #-------------------------BOTON PARA TEXTO DE OBSERVACIONES-------------------------------------------
                # texto_Observacion=Observacion_Colada()
                # print(texto_Observacion)
                #-------------------------BOTON PARA TEXTO DE OBSERVACIONES-------------------------------------------
                infoF = V1.V1(self.txtPathTermografiaF.text(), self.txtPathExcelF.text(), PositionMatrixF)
                infoT = V1.V1(self.txtPathTermografiaT.text(), self.txtPathExcelT.text(), PositionMatrixT)
                sleep(0.2)
                self.progressBar.setValue(75)
                if int(dataManager.getNameColadas(nameCuchara, str(nameCampana))[-1]) == 0:
                # if True:
                    # Nuevo
                    Historia = 0
                    Nuevo1Viejo2 = 1
                    HistoriaF = 0
                    HistoriaT = 0
                    pathDirectory = dataManager.getWorkingDirectory()+"/Historial/CUCHARA_"+str(nameCuchara)+"/CUCHARA_"+str(nameCuchara)+"_CAMPANA_"+str(nameCampana)+"/"
                    qtw.QApplication.processEvents()
                    [RiesgoF, RiesgoT, observacionF, observacionT] = main_MP_sup.getRiesgo(numColada, numColada, self.numpy2float(reshape(infoF[9], 3)), self.numpy2float(reshape(infoT[9], 3)), Nuevo1Viejo2, pathDirectory, int(self.sbEscoria.text()))
                    
                else:
                    # Viejo
                    #[HistoriaPreviaF, HistoriaPreviaT] = dataManager.getHistoriaEF(nameCuchara, nameCampana)
                    Nuevo1Viejo2 = 2
                    HistoriaF = 0
                    HistoriaT = 0
                    pathDirectory = dataManager.getWorkingDirectory()+"/Historial/CUCHARA_"+str(nameCuchara)+"/CUCHARA_"+str(nameCuchara)+"_CAMPANA_"+str(nameCampana)+"/"
                    qtw.QApplication.processEvents()
                    zonasSup = dataManager.getZonasEF(str(nameCuchara), str(nameCampana))[0]
                    zonasSup.append(self.numpy2float(reshape(infoF[9], 3)))
                    zonasInf = dataManager.getZonasEF(str(nameCuchara), str(nameCampana))[1]
                    zonasInf.append(self.numpy2float(reshape(infoT[9], 3)))
                    #print(zonasSup)
                    #print(zonasInf)
                    coladasHistoria = dataManager.getNameColadas(str(nameCuchara), str(nameCampana))
                    coladasHistoria.append(numColada)
                    #print(coladasHistoria)
                    print("paso1")
                    [RiesgoF, RiesgoT, observacionF, observacionT] = main_MP_sup.getRiesgo(numColada, coladasHistoria, zonasSup, zonasInf, Nuevo1Viejo2, pathDirectory, int(self.sbEscoria.text()))
                # print(pathDirectory)
                # grafico_espesores(pathDirectory)    
                sleep(0.2)
                self.progressBar.setValue(85)
                
                txtObservaciones = str(self.txtObservaciones.text())
                dataManager.add_Colada(nameCuchara, nameCampana, numColada, float(infoF[8]), float(infoT[8]), self.numpy2float(reshape(infoF[9], 3)), 
                                       self.numpy2float(reshape(infoT[9], 3)), self.numpy2float(reshape(infoF[5], 72)), self.numpy2float(reshape(infoT[5], 72)), 
                                       str(HistoriaF), str(HistoriaT), str(RiesgoF), str(RiesgoT), 
                                       str(observacionF), txtObservaciones)
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
    def numpy2float(self, numnumpy):
        aux = []
        for i in numnumpy:
            aux.append(float(i))
        return aux
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
            #print("Coladas: "+str(coladas)[1:-1])
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
        #[percentageZonasF, percentageZonasT] = self.getPercentage(maxZonasF, maxZonasT, umbralMinimo, umbralMaximo)
        [RiesgoF, RiesgoT] = dataManager.getRiesgoEF(str(nameCuchara[8:]), str(nameCampana[8:]))
        self.txtZona1F.setText(str(RiesgoF[0])[0:5]+" %")
        self.txtZona2F.setText(str(RiesgoF[1])[0:5]+" %")
        self.txtZona3F.setText(str(RiesgoF[2])[0:5]+" %")
        self.txtZona1T.setText(str(RiesgoT[0])[0:5]+" %")
        self.txtZona2T.setText(str(RiesgoT[1])[0:5]+" %")
        self.txtZona3T.setText(str(RiesgoT[2])[0:5]+" %")
        self.setZonesColor(RiesgoF, RiesgoT, umbralMinimo)
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
    freeze_support()
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
            #window = LoginWindow()
        else:
            window = LoginWindow()
    else:
        dataManager.dataIsCorrupted()
        window = PopUpApiKey()
    
    window.show()
    exit(app.exec())