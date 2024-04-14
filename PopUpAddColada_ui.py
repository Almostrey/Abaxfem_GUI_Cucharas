# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PopUpAddColada.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSpinBox,
    QToolButton, QWidget)
import resources_rc

class Ui_PopUpAddColada(object):
    def setupUi(self, PopUpAddColada):
        if not PopUpAddColada.objectName():
            PopUpAddColada.setObjectName(u"PopUpAddColada")
        PopUpAddColada.resize(510, 771)
        PopUpAddColada.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/Images/ResourcesFolder/Imagenes/Logo_Lineas.png", QSize(), QIcon.Normal, QIcon.Off)
        PopUpAddColada.setWindowIcon(icon)
        PopUpAddColada.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.centralwidget = QWidget(PopUpAddColada)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"background-color : rgba(255, 255, 255, 255);\n"
"border-radius:30;\n"
"border:1px solid gray;\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(115, 20, 280, 41))
        font = QFont()
        font.setFamilies([u"Bell MT"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border:0px;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 80, 350, 20))
        font1 = QFont()
        font1.setFamilies([u"Bell MT"])
        font1.setPointSize(16)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"border:0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.pb_exit = QPushButton(self.centralwidget)
        self.pb_exit.setObjectName(u"pb_exit")
        self.pb_exit.setGeometry(QRect(460, 20, 21, 21))
        self.pb_exit.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	image: url(:/Icons/ResourcesFolder/featherIcons/x-square.svg);\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(200, 200, 200, 120);\n"
"	border-radius: 6px\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(180, 180, 180, 150);\n"
"	border-radius: 6px\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 670, 21, 21))
        self.label_2.setStyleSheet(u"image: url(:/Icons/ResourcesFolder/featherIcons/file-plus.svg);\n"
"background-color: rgba(190, 190, 190, 0);\n"
"border-radius: 10px;\n"
"border:0px;")
        self.cbCuchara = QComboBox(self.centralwidget)
        self.cbCuchara.setObjectName(u"cbCuchara")
        self.cbCuchara.setGeometry(QRect(145, 120, 220, 35))
        font2 = QFont()
        font2.setFamilies([u"Bell MT"])
        font2.setPointSize(18)
        self.cbCuchara.setFont(font2)
        self.cbCuchara.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;"
                        "\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"\n"
"	image: url(:/Icons/ResourcesFolder/featherIcons/chevron-down.svg);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 170, 101, 30))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 660, 241, 40))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"border:0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.txtCampana = QLineEdit(self.centralwidget)
        self.txtCampana.setObjectName(u"txtCampana")
        self.txtCampana.setEnabled(False)
        self.txtCampana.setGeometry(QRect(120, 170, 100, 30))
        font3 = QFont()
        font3.setFamilies([u"Rockwell"])
        font3.setPointSize(18)
        font3.setItalic(False)
        self.txtCampana.setFont(font3)
        self.txtCampana.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"    min-width: 6em;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.txtCampana.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(105, 210, 300, 30))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.pbSiEscoria = QPushButton(self.centralwidget)
        self.pbSiEscoria.setObjectName(u"pbSiEscoria")
        self.pbSiEscoria.setEnabled(True)
        self.pbSiEscoria.setGeometry(QRect(104, 250, 40, 40))
        font4 = QFont()
        font4.setFamilies([u"Bell MT"])
        font4.setPointSize(14)
        self.pbSiEscoria.setFont(font4)
        self.pbSiEscoria.setStyleSheet(u"QPushButton:enabled{\n"
"background-color: rgb(215, 215, 215);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"QPushButton:disabled{\n"
"color:rgb(255, 255, 255);\n"
"	background-color: rgb(130, 130, 130);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}")
        self.pbNoEscoria = QPushButton(self.centralwidget)
        self.pbNoEscoria.setObjectName(u"pbNoEscoria")
        self.pbNoEscoria.setGeometry(QRect(144, 250, 40, 40))
        self.pbNoEscoria.setFont(font4)
        self.pbNoEscoria.setStyleSheet(u"QPushButton:enabled{\n"
"background-color: rgb(215, 215, 215);\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"}\n"
"QPushButton:disabled{\n"
"color:rgb(255, 255, 255);\n"
"	background-color: rgb(130, 130, 130);\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"}")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(204, 250, 220, 40))
        self.frame_3.setStyleSheet(u"border-radius:15px;\n"
"color: rgb(0, 0, 0);\n"
"    border: 1px solid gray;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.sbEscoria = QSpinBox(self.frame_3)
        self.sbEscoria.setObjectName(u"sbEscoria")
        self.sbEscoria.setGeometry(QRect(29, 1, 181, 38))
        font5 = QFont()
        font5.setFamilies([u"Rockwell"])
        font5.setPointSize(18)
        self.sbEscoria.setFont(font5)
        self.sbEscoria.setStyleSheet(u"QSpinBox{\n"
" border: 0px solid gray;\n"
"}\n"
"QSpinBox::up-button  {\n"
"	image: url(:/Icons/ResourcesFolder/featherIcons/arrow-up.svg);\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed  {\n"
"	background-color: rgb(180, 180, 180);\n"
"}\n"
"\n"
"QSpinBox::down-button  {\n"
"	image: url(:/Icons/ResourcesFolder/featherIcons/arrow-down.svg);\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed  {\n"
"	background-color: rgb(180, 180, 180);\n"
"}")
        self.sbEscoria.setAlignment(Qt.AlignCenter)
        self.sbEscoria.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.sbEscoria.setAccelerated(True)
        self.sbEscoria.setMaximum(1000)
        self.sbEscoria.setStepType(QAbstractSpinBox.DefaultStepType)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 260, 21, 21))
        self.label_3.setStyleSheet(u"image: url(:/Icons/ResourcesFolder/featherIcons/arrow-right-circle.svg);\n"
"background-color: rgba(190, 190, 190, 0);\n"
"border-radius: 10px;\n"
"border:0px;")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(135, 400, 240, 30))
        font6 = QFont()
        font6.setFamilies([u"Bell MT"])
        font6.setPointSize(16)
        font6.setBold(True)
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 440, 151, 31))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 480, 151, 31))
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.txtPathTermografiaF = QLineEdit(self.centralwidget)
        self.txtPathTermografiaF.setObjectName(u"txtPathTermografiaF")
        self.txtPathTermografiaF.setEnabled(False)
        self.txtPathTermografiaF.setGeometry(QRect(160, 440, 281, 31))
        font7 = QFont()
        font7.setFamilies([u"Rockwell"])
        font7.setPointSize(12)
        font7.setItalic(False)
        self.txtPathTermografiaF.setFont(font7)
        self.txtPathTermografiaF.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.txtPathTermografiaF.setAlignment(Qt.AlignCenter)
        self.pbFileDialog1 = QToolButton(self.centralwidget)
        self.pbFileDialog1.setObjectName(u"pbFileDialog1")
        self.pbFileDialog1.setGeometry(QRect(450, 440, 31, 31))
        self.pbFileDialog1.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(0, 0, 0);\n"
"    border: 1px solid gray;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.pbFileDialog2 = QToolButton(self.centralwidget)
        self.pbFileDialog2.setObjectName(u"pbFileDialog2")
        self.pbFileDialog2.setGeometry(QRect(450, 480, 31, 31))
        self.pbFileDialog2.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(0, 0, 0);\n"
"    border: 1px solid gray;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.txtPathExcelF = QLineEdit(self.centralwidget)
        self.txtPathExcelF.setObjectName(u"txtPathExcelF")
        self.txtPathExcelF.setEnabled(False)
        self.txtPathExcelF.setGeometry(QRect(160, 480, 281, 31))
        self.txtPathExcelF.setFont(font7)
        self.txtPathExcelF.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.txtPathExcelF.setAlignment(Qt.AlignCenter)
        self.pbFileDialog4 = QToolButton(self.centralwidget)
        self.pbFileDialog4.setObjectName(u"pbFileDialog4")
        self.pbFileDialog4.setGeometry(QRect(450, 610, 31, 31))
        self.pbFileDialog4.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(0, 0, 0);\n"
"    border: 1px solid gray;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.pbFileDialog3 = QToolButton(self.centralwidget)
        self.pbFileDialog3.setObjectName(u"pbFileDialog3")
        self.pbFileDialog3.setGeometry(QRect(450, 570, 31, 31))
        self.pbFileDialog3.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(0, 0, 0);\n"
"    border: 1px solid gray;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 570, 151, 31))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 610, 151, 31))
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(135, 530, 240, 30))
        self.label_13.setFont(font6)
        self.label_13.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.txtPathExcelT = QLineEdit(self.centralwidget)
        self.txtPathExcelT.setObjectName(u"txtPathExcelT")
        self.txtPathExcelT.setEnabled(False)
        self.txtPathExcelT.setGeometry(QRect(160, 610, 281, 31))
        self.txtPathExcelT.setFont(font7)
        self.txtPathExcelT.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.txtPathExcelT.setAlignment(Qt.AlignCenter)
        self.txtPathTermografiaT = QLineEdit(self.centralwidget)
        self.txtPathTermografiaT.setObjectName(u"txtPathTermografiaT")
        self.txtPathTermografiaT.setEnabled(False)
        self.txtPathTermografiaT.setGeometry(QRect(160, 570, 281, 31))
        self.txtPathTermografiaT.setFont(font7)
        self.txtPathTermografiaT.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.txtPathTermografiaT.setAlignment(Qt.AlignCenter)
        self.txtNewColada = QLineEdit(self.centralwidget)
        self.txtNewColada.setObjectName(u"txtNewColada")
        self.txtNewColada.setEnabled(False)
        self.txtNewColada.setGeometry(QRect(314, 660, 140, 40))
        self.txtNewColada.setFont(font3)
        self.txtNewColada.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"    min-width: 6em;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.txtNewColada.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(9, 310, 491, 30))
        font8 = QFont()
        font8.setFamilies([u"Bell MT"])
        font8.setPointSize(12)
        font8.setBold(True)
        self.label_14.setFont(font8)
        self.label_14.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(243, 144, 57);\n"
"border:0px;")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 340, 491, 30))
        self.label_15.setFont(font8)
        self.label_15.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(243, 144, 57);\n"
"border:0px;")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 370, 491, 30))
        self.label_16.setFont(font8)
        self.label_16.setStyleSheet(u"border:0px;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(243, 144, 57);")
        self.label_16.setAlignment(Qt.AlignCenter)
        self.txtUltimaColada = QLineEdit(self.centralwidget)
        self.txtUltimaColada.setObjectName(u"txtUltimaColada")
        self.txtUltimaColada.setEnabled(False)
        self.txtUltimaColada.setGeometry(QRect(380, 170, 100, 30))
        self.txtUltimaColada.setFont(font3)
        self.txtUltimaColada.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"    min-width: 6em;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.txtUltimaColada.setAlignment(Qt.AlignCenter)
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(241, 170, 131, 30))
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(80, 705, 350, 51))
        self.frame.setStyleSheet(u"QFrame{\n"
"border-radius:15px;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"border:0px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_aceptar = QPushButton(self.frame)
        self.pb_aceptar.setObjectName(u"pb_aceptar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_aceptar.sizePolicy().hasHeightForWidth())
        self.pb_aceptar.setSizePolicy(sizePolicy)
        font9 = QFont()
        font9.setFamilies([u"Bell MT"])
        font9.setPointSize(15)
        font9.setBold(True)
        font9.setItalic(False)
        font9.setUnderline(False)
        font9.setStrikeOut(False)
        self.pb_aceptar.setFont(font9)
        self.pb_aceptar.setStyleSheet(u"QPushButton{\n"
"	border-radius:15px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(240, 120, 14, 210);\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 135, 29, 230);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(255, 135, 29, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.pb_aceptar)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        font10 = QFont()
        font10.setFamilies([u"Bell MT"])
        font10.setPointSize(15)
        font10.setBold(True)
        self.progressBar.setFont(font10)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"border-radius:15px;\n"
"	color: rgb(0, 0, 0);\n"
"background-color:rgba(0, 0, 0, 0)\n"
"}\n"
"QProgressBar::chunk{\n"
"	background-color: rgb(243, 144, 57);\n"
"border-radius:15px;\n"
"}")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.progressBar)

        PopUpAddColada.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.label_4.raise_()
        self.pb_exit.raise_()
        self.cbCuchara.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.txtCampana.raise_()
        self.label_7.raise_()
        self.pbSiEscoria.raise_()
        self.pbNoEscoria.raise_()
        self.frame_3.raise_()
        self.label_3.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.txtPathTermografiaF.raise_()
        self.pbFileDialog1.raise_()
        self.pbFileDialog2.raise_()
        self.txtPathExcelF.raise_()
        self.pbFileDialog4.raise_()
        self.pbFileDialog3.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.txtPathExcelT.raise_()
        self.txtPathTermografiaT.raise_()
        self.txtNewColada.raise_()
        self.label_2.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.txtUltimaColada.raise_()
        self.label_17.raise_()
        self.frame.raise_()

        self.retranslateUi(PopUpAddColada)

        QMetaObject.connectSlotsByName(PopUpAddColada)
    # setupUi

    def retranslateUi(self, PopUpAddColada):
        PopUpAddColada.setWindowTitle(QCoreApplication.translate("PopUpAddColada", u"A\u00f1adir Nueva Colada - Abaxfem", None))
        self.label.setText(QCoreApplication.translate("PopUpAddColada", u"A\u00f1adir Nueva Colada", None))
        self.label_4.setText(QCoreApplication.translate("PopUpAddColada", u"Escoja en que cuchara se a\u00f1ade la colada", None))
        self.pb_exit.setText("")
        self.label_2.setText("")
        self.label_5.setText(QCoreApplication.translate("PopUpAddColada", u"Campa\u00f1a:", None))
        self.label_6.setText(QCoreApplication.translate("PopUpAddColada", u"N\u00famero de la nueva colada:", None))
        self.txtCampana.setText("")
        self.label_7.setText(QCoreApplication.translate("PopUpAddColada", u"\u00bfCambio de Linea de Escoria?", None))
        self.pbSiEscoria.setText(QCoreApplication.translate("PopUpAddColada", u"SI", None))
        self.pbNoEscoria.setText(QCoreApplication.translate("PopUpAddColada", u"NO", None))
        self.label_3.setText("")
        self.label_8.setText(QCoreApplication.translate("PopUpAddColada", u"Cara Frontal", None))
        self.label_9.setText(QCoreApplication.translate("PopUpAddColada", u"Termograf\u00eda", None))
        self.label_10.setText(QCoreApplication.translate("PopUpAddColada", u"Excel", None))
        self.txtPathTermografiaF.setText(QCoreApplication.translate("PopUpAddColada", u"C: ... /Usuario/Documentos/", None))
        self.pbFileDialog1.setText(QCoreApplication.translate("PopUpAddColada", u"...", None))
        self.pbFileDialog2.setText(QCoreApplication.translate("PopUpAddColada", u"...", None))
        self.txtPathExcelF.setText(QCoreApplication.translate("PopUpAddColada", u"C: ... /Usuario/Documentos/", None))
        self.pbFileDialog4.setText(QCoreApplication.translate("PopUpAddColada", u"...", None))
        self.pbFileDialog3.setText(QCoreApplication.translate("PopUpAddColada", u"...", None))
        self.label_11.setText(QCoreApplication.translate("PopUpAddColada", u"Termograf\u00eda", None))
        self.label_12.setText(QCoreApplication.translate("PopUpAddColada", u"Excel", None))
        self.label_13.setText(QCoreApplication.translate("PopUpAddColada", u"Cara Trasera", None))
        self.txtPathExcelT.setText(QCoreApplication.translate("PopUpAddColada", u"C: ... /Usuario/Documentos/", None))
        self.txtPathTermografiaT.setText(QCoreApplication.translate("PopUpAddColada", u"C: ... /Usuario/Documentos/", None))
        self.txtNewColada.setText(QCoreApplication.translate("PopUpAddColada", u"22", None))
        self.label_14.setText(QCoreApplication.translate("PopUpAddColada", u"Importante! Los archivos deben estar guardados en la misma carpeta", None))
        self.label_15.setText(QCoreApplication.translate("PopUpAddColada", u"de la siguiente manera: (151F. jpg/xlsx) (151T. jpg/xlsx)", None))
        self.label_16.setText(QCoreApplication.translate("PopUpAddColada", u"Donde 151 es el n\u00famero de la colada", None))
        self.txtUltimaColada.setText("")
        self.label_17.setText(QCoreApplication.translate("PopUpAddColada", u"\u00daltima Colada:", None))
        self.pb_aceptar.setText(QCoreApplication.translate("PopUpAddColada", u"A\u00f1adir Colada", None))
    # retranslateUi

