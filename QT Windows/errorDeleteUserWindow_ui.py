# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'errorDeleteUserWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_errorDeleteUserWindow(object):
    def setupUi(self, errorDeleteUserWindow):
        if not errorDeleteUserWindow.objectName():
            errorDeleteUserWindow.setObjectName(u"errorDeleteUserWindow")
        errorDeleteUserWindow.resize(340, 180)
        icon = QIcon()
        icon.addFile(u":/Images/ResourcesFolder/Imagenes/Logo_Lineas.png", QSize(), QIcon.Normal, QIcon.Off)
        errorDeleteUserWindow.setWindowIcon(icon)
        errorDeleteUserWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(errorDeleteUserWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"background-color : rgba(255, 255, 255, 240);\n"
"border-radius:30;\n"
"border:1px solid gray;\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(29, 30, 281, 41))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border:0;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(25, 80, 291, 20))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(11)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0;\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.pb_aceptar = QPushButton(self.centralwidget)
        self.pb_aceptar.setObjectName(u"pb_aceptar")
        self.pb_aceptar.setGeometry(QRect(71, 110, 201, 41))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
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
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 340, 180))
        self.frame.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        errorDeleteUserWindow.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.pb_aceptar.raise_()
        self.pb_exit.raise_()

        self.retranslateUi(errorDeleteUserWindow)

        QMetaObject.connectSlotsByName(errorDeleteUserWindow)
    # setupUi

    def retranslateUi(self, errorDeleteUserWindow):
        errorDeleteUserWindow.setWindowTitle(QCoreApplication.translate("errorDeleteUserWindow", u"Error de Selecci\u00f3n - Abaxfem", None))
        self.label.setText(QCoreApplication.translate("errorDeleteUserWindow", u"Error de Selecci\u00f3n", None))
        self.label_4.setText(QCoreApplication.translate("errorDeleteUserWindow", u"Seleccione al USUARIO que desea eliminar", None))
        self.pb_aceptar.setText(QCoreApplication.translate("errorDeleteUserWindow", u"Aceptar", None))
        self.pb_exit.setText("")
    # retranslateUi

