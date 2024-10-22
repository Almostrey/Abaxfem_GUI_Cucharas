# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PopUpApiKey.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_PopUpApiKey(object):
    def setupUi(self, PopUpApiKey):
        if not PopUpApiKey.objectName():
            PopUpApiKey.setObjectName(u"PopUpApiKey")
        PopUpApiKey.resize(340, 220)
        PopUpApiKey.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/Images/ResourcesFolder/Imagenes/Logo_Lineas.png", QSize(), QIcon.Normal, QIcon.Off)
        PopUpApiKey.setWindowIcon(icon)
        self.centralwidget = QWidget(PopUpApiKey)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"background-color : rgba(255, 255, 255, 240);\n"
"border-radius:30;\n"
"border:1px solid gray;\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(29, 20, 281, 41))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
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
        self.label_4.setGeometry(QRect(40, 60, 260, 20))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(11)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"border:0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.pb_exit = QPushButton(self.centralwidget)
        self.pb_exit.setObjectName(u"pb_exit")
        self.pb_exit.setGeometry(QRect(300, 10, 21, 21))
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
        self.pb_aceptar.setGeometry(QRect(70, 160, 201, 41))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
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
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(60, 110, 221, 41))
        self.frame_2.setStyleSheet(u"border-radius:15px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(190, 190, 190);\n"
"border:0px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.txtApiKey = QLineEdit(self.centralwidget)
        self.txtApiKey.setObjectName(u"txtApiKey")
        self.txtApiKey.setGeometry(QRect(90, 110, 191, 41))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(16)
        font3.setBold(False)
        self.txtApiKey.setFont(font3)
        self.txtApiKey.setStyleSheet(u"border-radius:15px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(190, 190, 190);\n"
"border:0px;")
        self.txtApiKey.setMaxLength(22)
        self.txtApiKey.setEchoMode(QLineEdit.Password)
        self.txtApiKey.setCursorPosition(0)
        self.txtApiKey.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txtApiKey.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(66, 120, 21, 21))
        self.label_2.setStyleSheet(u"image: url(:/Icons/ResourcesFolder/featherIcons/alert-circle.svg);\n"
"background-color: rgb(190, 190, 190);\n"
"border-radius: 10px;\n"
"border:0px;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 80, 260, 20))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"border:0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_5.setAlignment(Qt.AlignCenter)
        PopUpApiKey.setCentralWidget(self.centralwidget)

        self.retranslateUi(PopUpApiKey)

        QMetaObject.connectSlotsByName(PopUpApiKey)
    # setupUi

    def retranslateUi(self, PopUpApiKey):
        PopUpApiKey.setWindowTitle(QCoreApplication.translate("PopUpApiKey", u"API-KEY - Abaxfem", None))
        self.label.setText(QCoreApplication.translate("PopUpApiKey", u"Ingrese API-KEY", None))
        self.label_4.setText(QCoreApplication.translate("PopUpApiKey", u"Ingrese la licencia de la aplicacion", None))
        self.pb_exit.setText("")
        self.pb_aceptar.setText(QCoreApplication.translate("PopUpApiKey", u"Ingresar", None))
        self.txtApiKey.setText("")
        self.txtApiKey.setPlaceholderText(QCoreApplication.translate("PopUpApiKey", u"API-KEY", None))
        self.label_2.setText("")
        self.label_5.setText(QCoreApplication.translate("PopUpApiKey", u"para que esta funcione", None))
    # retranslateUi

