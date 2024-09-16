# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cropWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_cropWindow(object):
    def setupUi(self, cropWindow):
        if not cropWindow.objectName():
            cropWindow.setObjectName(u"cropWindow")
        cropWindow.resize(1880, 826)
        cropWindow.setMinimumSize(QSize(1880, 826))
        cropWindow.setMaximumSize(QSize(1880, 826))
        self.centralwidget = QWidget(cropWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame_3)

        self.frameCropImage2 = QFrame(self.centralwidget)
        self.frameCropImage2.setObjectName(u"frameCropImage2")
        self.frameCropImage2.setMinimumSize(QSize(928, 696))
        self.frameCropImage2.setMaximumSize(QSize(1920, 1080))
        self.frameCropImage2.setAcceptDrops(False)
        self.frameCropImage2.setStyleSheet(u"background-color:rgba(200, 200, 200, 0);")
        self.frameCropImage2.setFrameShape(QFrame.StyledPanel)
        self.frameCropImage2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameCropImage2)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameCropImage = QFrame(self.frameCropImage2)
        self.frameCropImage.setObjectName(u"frameCropImage")
        self.frameCropImage.setMinimumSize(QSize(928, 696))
        self.frameCropImage.setFrameShape(QFrame.StyledPanel)
        self.frameCropImage.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frameCropImage)

        self.label = QLabel(self.frameCropImage2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(928, 696))
        self.label.setMaximumSize(QSize(928, 696))
        self.label.setStyleSheet(u"border-image: url(:/Images/ResourcesFolder/Imagenes/Cuchara_Ejemplo_Recorte.JPG);")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frameCropImage2)

        self.pbAceptar = QFrame(self.centralwidget)
        self.pbAceptar.setObjectName(u"pbAceptar")
        self.pbAceptar.setMinimumSize(QSize(0, 50))
        self.pbAceptar.setMaximumSize(QSize(16777215, 50))
        self.pbAceptar.setStyleSheet(u"")
        self.pbAceptar.setFrameShape(QFrame.StyledPanel)
        self.pbAceptar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.pbAceptar)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 5)
        self.pushButton = QPushButton(self.pbAceptar)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_3.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.pbAceptar)

        cropWindow.setCentralWidget(self.centralwidget)
        self.frameCropImage2.raise_()
        self.frame_3.raise_()
        self.pbAceptar.raise_()

        self.retranslateUi(cropWindow)

        QMetaObject.connectSlotsByName(cropWindow)
    # setupUi

    def retranslateUi(self, cropWindow):
        cropWindow.setWindowTitle(QCoreApplication.translate("cropWindow", u"Recorte de Imagen", None))
        self.label_2.setText(QCoreApplication.translate("cropWindow", u"Por favor, recorte unicamente la cuchara de toda la imagen mostrada", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("cropWindow", u"Aceptar", None))
    # retranslateUi

