from sys import argv
from PySide6.QtGui import QDragMoveEvent, QPaintEvent
from cropWindow_ui import Ui_cropWindow
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

D_Anillo= 0.1464
D_Inf= 0.1464
Middle = 1/2

class Limit(qtw.QPushButton):
    def __init__(self, x, y, parent):
        super().__init__("+", parent)
        font = qtg.QFont()
        font.setFamilies([u"Rockwell"])
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
        print(coordenadas)
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

def main():
    app = qtw.QApplication(argv)
    ex = cropWindow("Archivos Fuente/Fotografias y archivos de termografias/13F.jpg")
    #ex = cropWindow("13F.jpg")
    ex.show()
    app.exec()

if __name__ == '__main__':
    main()