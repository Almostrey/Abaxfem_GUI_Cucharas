# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PopUpDeleteColada.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_PopUpDeleteColada(object):
    def setupUi(self, PopUpDeleteColada):
        if not PopUpDeleteColada.objectName():
            PopUpDeleteColada.setObjectName(u"PopUpDeleteColada")
        PopUpDeleteColada.resize(515, 289)
        PopUpDeleteColada.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/Images/ResourcesFolder/Imagenes/Logo_Lineas.png", QSize(), QIcon.Normal, QIcon.Off)
        PopUpDeleteColada.setWindowIcon(icon)
        self.centralwidget = QWidget(PopUpDeleteColada)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"background-color : rgba(255, 255, 255, 240);\n"
"border-radius:30;\n"
"border:1px solid gray;\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(117, 20, 281, 41))
        font = QFont()
        font.setFamilies([u"Bell MT"])
        font.setPointSize(22)
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
        self.label_4.setGeometry(QRect(50, 70, 260, 20))
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(14)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"border:0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.pb_exit = QPushButton(self.centralwidget)
        self.pb_exit.setObjectName(u"pb_exit")
        self.pb_exit.setGeometry(QRect(470, 10, 21, 21))
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
        self.pb_aceptar = QPushButton(self.centralwidget)
        self.pb_aceptar.setObjectName(u"pb_aceptar")
        self.pb_aceptar.setGeometry(QRect(157, 220, 200, 41))
        font2 = QFont()
        font2.setFamilies([u"Bell MT"])
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.pb_aceptar.setFont(font2)
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
        self.cbCuchara = QComboBox(self.centralwidget)
        self.cbCuchara.setObjectName(u"cbCuchara")
        self.cbCuchara.setGeometry(QRect(70, 101, 221, 31))
        font3 = QFont()
        font3.setFamilies([u"Bell MT"])
        font3.setPointSize(18)
        self.cbCuchara.setFont(font3)
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
        self.label_5.setGeometry(QRect(127, 140, 260, 20))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"border:0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(363, 70, 101, 20))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.txtCampana = QLineEdit(self.centralwidget)
        self.txtCampana.setObjectName(u"txtCampana")
        self.txtCampana.setEnabled(False)
        self.txtCampana.setGeometry(QRect(360, 100, 100, 30))
        font4 = QFont()
        font4.setFamilies([u"Rockwell"])
        font4.setPointSize(18)
        font4.setItalic(False)
        self.txtCampana.setFont(font4)
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
        self.cbColada = QComboBox(self.centralwidget)
        self.cbColada.setObjectName(u"cbColada")
        self.cbColada.setGeometry(QRect(147, 170, 220, 31))
        self.cbColada.setFont(font3)
        self.cbColada.setStyleSheet(u"QComboBox {\n"
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
        PopUpDeleteColada.setCentralWidget(self.centralwidget)

        self.retranslateUi(PopUpDeleteColada)

        QMetaObject.connectSlotsByName(PopUpDeleteColada)
    # setupUi

    def retranslateUi(self, PopUpDeleteColada):
        PopUpDeleteColada.setWindowTitle(QCoreApplication.translate("PopUpDeleteColada", u"Eliminar Colada - Abaxfem", None))
        self.label.setText(QCoreApplication.translate("PopUpDeleteColada", u"Eliminar Colada", None))
        self.label_4.setText(QCoreApplication.translate("PopUpDeleteColada", u"Escoja la cuchara", None))
        self.pb_exit.setText("")
        self.pb_aceptar.setText(QCoreApplication.translate("PopUpDeleteColada", u"Eliminar Colada", None))
        self.label_5.setText(QCoreApplication.translate("PopUpDeleteColada", u"\u00bfQue colada desea eliminar?", None))
        self.label_6.setText(QCoreApplication.translate("PopUpDeleteColada", u"Campa\u00f1a:", None))
        self.txtCampana.setText("")
    # retranslateUi

