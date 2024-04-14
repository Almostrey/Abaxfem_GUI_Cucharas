# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'errorSaveUserWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import resources_rc

class Ui_errorSaveUserWindow(object):
    def setupUi(self, errorSaveUserWindow):
        if not errorSaveUserWindow.objectName():
            errorSaveUserWindow.setObjectName(u"errorSaveUserWindow")
        errorSaveUserWindow.resize(340, 180)
        icon = QIcon()
        icon.addFile(u":/Images/ResourcesFolder/Imagenes/Logo_Lineas.png", QSize(), QIcon.Normal, QIcon.Off)
        errorSaveUserWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(errorSaveUserWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"background-color : rgba(255, 255, 255, 240);\n"
"border-radius:30;\n"
"border:1px solid gray;\n"
"}")
        self.pb_aceptar = QPushButton(self.centralwidget)
        self.pb_aceptar.setObjectName(u"pb_aceptar")
        self.pb_aceptar.setGeometry(QRect(72, 120, 201, 41))
        font = QFont()
        font.setFamilies([u"Bell MT"])
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pb_aceptar.setFont(font)
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
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(31, 70, 281, 20))
        font1 = QFont()
        font1.setFamilies([u"Bell MT"])
        font1.setPointSize(11)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"border:0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.pb_exit = QPushButton(self.centralwidget)
        self.pb_exit.setObjectName(u"pb_exit")
        self.pb_exit.setGeometry(QRect(301, 10, 21, 21))
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
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 281, 41))
        font2 = QFont()
        font2.setFamilies([u"Bell MT"])
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setKerning(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border:0px;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(31, 90, 281, 20))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"border:0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_5.setAlignment(Qt.AlignCenter)
        errorSaveUserWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(errorSaveUserWindow)

        QMetaObject.connectSlotsByName(errorSaveUserWindow)
    # setupUi

    def retranslateUi(self, errorSaveUserWindow):
        errorSaveUserWindow.setWindowTitle(QCoreApplication.translate("errorSaveUserWindow", u"Error al Guardar - Abaxfem", None))
        self.pb_aceptar.setText(QCoreApplication.translate("errorSaveUserWindow", u"Aceptar", None))
        self.label_4.setText(QCoreApplication.translate("errorSaveUserWindow", u"Debe llenar todas las celdas para guardar", None))
        self.pb_exit.setText("")
        self.label.setText(QCoreApplication.translate("errorSaveUserWindow", u"Error al Guardar", None))
        self.label_5.setText(QCoreApplication.translate("errorSaveUserWindow", u"un nuevo usuario", None))
    # retranslateUi

