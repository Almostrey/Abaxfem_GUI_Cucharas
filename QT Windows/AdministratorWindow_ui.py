# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdministratorWindow.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QToolButton,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_AdministratorWindow(object):
    def setupUi(self, AdministratorWindow):
        if not AdministratorWindow.objectName():
            AdministratorWindow.setObjectName(u"AdministratorWindow")
        AdministratorWindow.resize(1435, 771)
        AdministratorWindow.setMinimumSize(QSize(1366, 768))
        icon = QIcon()
        icon.addFile(u":/Images/ResourcesFolder/Imagenes/Logo_Lineas.png", QSize(), QIcon.Normal, QIcon.Off)
        AdministratorWindow.setWindowIcon(icon)
        AdministratorWindow.setStyleSheet(u"QToolTip{\n"
"	font: 10pt \"Century\";\n"
"}")
        self.centralwidget = QWidget(AdministratorWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(1200, 0))
        self.centralwidget.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.horizontalLayout_13 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_23 = QFrame(self.centralwidget)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_23)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameTop = QFrame(self.frame_23)
        self.frameTop.setObjectName(u"frameTop")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameTop.sizePolicy().hasHeightForWidth())
        self.frameTop.setSizePolicy(sizePolicy1)
        self.frameTop.setMaximumSize(QSize(16777215, 50))
        self.frameTop.setStyleSheet(u"")
        self.frameTop.setFrameShape(QFrame.StyledPanel)
        self.frameTop.setFrameShadow(QFrame.Raised)
        self.frameTop.setLineWidth(1)
        self.horizontalLayout_3 = QHBoxLayout(self.frameTop)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, 0)
        self.pbVerCucharas = QPushButton(self.frameTop)
        self.pbVerCucharas.setObjectName(u"pbVerCucharas")
        self.pbVerCucharas.setMinimumSize(QSize(300, 48))
        self.pbVerCucharas.setMaximumSize(QSize(300, 48))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.pbVerCucharas.setFont(font)
        self.pbVerCucharas.setStyleSheet(u"QPushButton{\n"
" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 140, 34, 240);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(235, 115, 9, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"ResourcesFolder/featherIcons/chevrons-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbVerCucharas.setIcon(icon1)
        self.pbVerCucharas.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.pbVerCucharas)

        self.frame_9 = QFrame(self.frameTop)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 48))
        self.frame_9.setMaximumSize(QSize(16777215, 48))
        self.frame_9.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 2, 4, 2)
        self.frame_6 = QFrame(self.frame_9)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(290, 40))
        self.frame_6.setMaximumSize(QSize(300, 16777215))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"border:0px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 0, -1, 0)
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(40, 0))
        self.label_3.setMaximumSize(QSize(20, 16777215))
        self.label_3.setStyleSheet(u"image: url(:/Icons/ResourcesFolder/featherIcons/user.svg);")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.labelUsername = QLabel(self.frame_6)
        self.labelUsername.setObjectName(u"labelUsername")
        self.labelUsername.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(11)
        self.labelUsername.setFont(font1)
        self.labelUsername.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.labelUsername)

        self.labelUsername.raise_()
        self.label_3.raise_()

        self.horizontalLayout_5.addWidget(self.frame_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.frame_8 = QFrame(self.frame_9)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(450, 0))
        self.frame_8.setMaximumSize(QSize(600, 16777215))
        self.frame_8.setStyleSheet(u"border:0px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pbVerArchivos = QPushButton(self.frame_8)
        self.pbVerArchivos.setObjectName(u"pbVerArchivos")
        self.pbVerArchivos.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.pbVerArchivos.setFont(font2)
        self.pbVerArchivos.setStyleSheet(u"QPushButton{\n"
"	border:1px solid gray;\n"
"	border-radius:10px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 140, 34, 240);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(235, 115, 9, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.pbVerArchivos)

        self.pbPerfiles = QPushButton(self.frame_8)
        self.pbPerfiles.setObjectName(u"pbPerfiles")
        self.pbPerfiles.setMinimumSize(QSize(0, 40))
        self.pbPerfiles.setFont(font2)
        self.pbPerfiles.setStyleSheet(u"QPushButton{\n"
"	border:1px solid gray;\n"
"	border-radius:10px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 140, 34, 240);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(235, 115, 9, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.pbPerfiles)

        self.pbHistorial = QPushButton(self.frame_8)
        self.pbHistorial.setObjectName(u"pbHistorial")
        self.pbHistorial.setMinimumSize(QSize(0, 40))
        self.pbHistorial.setFont(font2)
        self.pbHistorial.setStyleSheet(u"QPushButton{\n"
"	border:1px solid gray;\n"
"	border-radius:10px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 140, 34, 240);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(235, 115, 9, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.pbHistorial)

        self.pbReporte = QPushButton(self.frame_8)
        self.pbReporte.setObjectName(u"pbReporte")
        self.pbReporte.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        self.pbReporte.setFont(font3)
        self.pbReporte.setStyleSheet(u"QPushButton{\n"
"	border:1px solid gray;\n"
"	border-radius:10px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 140, 34, 240);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(235, 115, 9, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.pbReporte)


        self.horizontalLayout_5.addWidget(self.frame_8)


        self.horizontalLayout_3.addWidget(self.frame_9)

        self.frame_7 = QFrame(self.frameTop)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(200, 50))
        self.frame_7.setMaximumSize(QSize(200, 50))
        self.frame_7.setStyleSheet(u"background-color: rgba(170, 0, 0, 0);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 50))
        self.label.setMaximumSize(QSize(200, 50))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"image: url(:/Images/ResourcesFolder/Imagenes/Logo_Letras.png);\n"
"border-color: rgb(255, 255, 255);\n"
"padding: 0 0 3 0")

        self.verticalLayout_12.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frameTop)

        self.frameBottom = QFrame(self.frame_23)
        self.frameBottom.setObjectName(u"frameBottom")
        self.frameBottom.setMinimumSize(QSize(900, 0))
        self.frameBottom.setFrameShape(QFrame.StyledPanel)
        self.frameBottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameBottom)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameCucharas = QFrame(self.frameBottom)
        self.frameCucharas.setObjectName(u"frameCucharas")
        sizePolicy.setHeightForWidth(self.frameCucharas.sizePolicy().hasHeightForWidth())
        self.frameCucharas.setSizePolicy(sizePolicy)
        self.frameCucharas.setMinimumSize(QSize(98, 400))
        self.frameCucharas.setMaximumSize(QSize(300, 16777215))
        self.frameCucharas.setSizeIncrement(QSize(0, 0))
        self.frameCucharas.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"    min-width: 6em;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.verticalLayout_8 = QVBoxLayout(self.frameCucharas)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.treeMenu = QTreeWidget(self.frameCucharas)
        icon2 = QIcon()
        icon2.addFile(u":/Icons/ResourcesFolder/featherIcons/box.svg", QSize(), QIcon.Normal, QIcon.Off)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(16)
        font4.setBold(True)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        __qtreewidgetitem.setFont(0, font4);
        __qtreewidgetitem.setBackground(0, QColor(255, 255, 255));
        __qtreewidgetitem.setForeground(0, brush);
        __qtreewidgetitem.setIcon(0, icon2);
        self.treeMenu.setHeaderItem(__qtreewidgetitem)
        self.treeMenu.setObjectName(u"treeMenu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.treeMenu.sizePolicy().hasHeightForWidth())
        self.treeMenu.setSizePolicy(sizePolicy2)
        self.treeMenu.setMinimumSize(QSize(98, 0))
        self.treeMenu.setMaximumSize(QSize(400, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(16)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        self.treeMenu.setFont(font5)
        self.treeMenu.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"    min-width: 6em;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"background-color: rgb(255, 255, 255)")
        self.treeMenu.setAlternatingRowColors(True)
        self.treeMenu.setIndentation(30)
        self.treeMenu.setAnimated(True)
        self.treeMenu.setHeaderHidden(False)

        self.verticalLayout_8.addWidget(self.treeMenu)

        self.frame_14 = QFrame(self.frameCucharas)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setMinimumSize(QSize(96, 100))
        self.frame_14.setMaximumSize(QSize(280, 100))
        self.frame_14.setStyleSheet(u" border: 0px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"    min-width: 6em;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"background-color:rgba(255, 255, 255, 0);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_14)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pbAddCuchara = QPushButton(self.frame_14)
        self.pbAddCuchara.setObjectName(u"pbAddCuchara")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pbAddCuchara.sizePolicy().hasHeightForWidth())
        self.pbAddCuchara.setSizePolicy(sizePolicy3)
        self.pbAddCuchara.setMinimumSize(QSize(98, 40))
        self.pbAddCuchara.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(11)
        font6.setBold(True)
        self.pbAddCuchara.setFont(font6)
        self.pbAddCuchara.setStyleSheet(u"QPushButton{\n"
"	border:1px solid gray;\n"
"	border-radius:10px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 140, 34, 240);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(235, 115, 9, 255);\n"
"}")

        self.gridLayout.addWidget(self.pbAddCuchara, 0, 0, 1, 1)

        self.pbDeleteCuchara = QPushButton(self.frame_14)
        self.pbDeleteCuchara.setObjectName(u"pbDeleteCuchara")
        sizePolicy3.setHeightForWidth(self.pbDeleteCuchara.sizePolicy().hasHeightForWidth())
        self.pbDeleteCuchara.setSizePolicy(sizePolicy3)
        self.pbDeleteCuchara.setMinimumSize(QSize(98, 40))
        self.pbDeleteCuchara.setFont(font6)
        self.pbDeleteCuchara.setStyleSheet(u"QPushButton{\n"
"	border:1px solid gray;\n"
"	border-radius:10px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 140, 34, 240);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(235, 115, 9, 255);\n"
"}")

        self.gridLayout.addWidget(self.pbDeleteCuchara, 0, 1, 1, 1)

        self.pbAddCampana = QPushButton(self.frame_14)
        self.pbAddCampana.setObjectName(u"pbAddCampana")
        sizePolicy.setHeightForWidth(self.pbAddCampana.sizePolicy().hasHeightForWidth())
        self.pbAddCampana.setSizePolicy(sizePolicy)
        self.pbAddCampana.setMinimumSize(QSize(98, 40))
        self.pbAddCampana.setFont(font6)
        self.pbAddCampana.setStyleSheet(u"QPushButton{\n"
"	border:1px solid gray;\n"
"	border-radius:10px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 140, 34, 240);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(235, 115, 9, 255);\n"
"}")

        self.gridLayout.addWidget(self.pbAddCampana, 1, 0, 1, 1)

        self.pbDeleteCampana = QPushButton(self.frame_14)
        self.pbDeleteCampana.setObjectName(u"pbDeleteCampana")
        sizePolicy.setHeightForWidth(self.pbDeleteCampana.sizePolicy().hasHeightForWidth())
        self.pbDeleteCampana.setSizePolicy(sizePolicy)
        self.pbDeleteCampana.setMinimumSize(QSize(98, 40))
        self.pbDeleteCampana.setFont(font6)
        self.pbDeleteCampana.setStyleSheet(u"QPushButton{\n"
"	border:1px solid gray;\n"
"	border-radius:10px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 140, 34, 240);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(235, 115, 9, 255);\n"
"}")

        self.gridLayout.addWidget(self.pbDeleteCampana, 1, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_14)


        self.horizontalLayout.addWidget(self.frameCucharas)

        self.frame_2 = QFrame(self.frameBottom)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setMinimumSize(QSize(96, 0))
        self.frame_2.setStyleSheet(u" border: 0px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"    min-width: 6em;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"background-color:rgba(0, 255, 255, 0)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_2)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(150)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy4)
        self.frame_21.setMinimumSize(QSize(98, 0))
        self.frame_21.setMaximumSize(QSize(16777215, 16777215))
        self.frame_21.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"    min-width: 6em;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_21)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_4 = QFrame(self.frame_21)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(96, 100))
        self.frame_4.setMaximumSize(QSize(16777215, 150))
        self.frame_4.setStyleSheet(u" border: 0px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"    min-width: 6em;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(98, 91))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel{\n"
"image: url(:/Icons/ResourcesFolder/featherIcons/user.svg);\n"
"\n"
"border-radius: 10px;\n"
"border:0px;\n"
"}")

        self.verticalLayout_3.addWidget(self.label_2)

        self.nameHistory0 = QLabel(self.frame_3)
        self.nameHistory0.setObjectName(u"nameHistory0")
        self.nameHistory0.setFont(font3)
        self.nameHistory0.setStyleSheet(u"border:0px;\n"
"border-radius:0px;\n"
"border-bottom:1px solid;\n"
"border-top:1px solid;")
        self.nameHistory0.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.nameHistory0)

        self.dateHistory0 = QLabel(self.frame_3)
        self.dateHistory0.setObjectName(u"dateHistory0")
        self.dateHistory0.setFont(font3)
        self.dateHistory0.setStyleSheet(u"border:0px")
        self.dateHistory0.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.dateHistory0)


        self.horizontalLayout_6.addWidget(self.frame_3)

        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(98, 91))
        self.frame_10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"image: url(:/Icons/ResourcesFolder/featherIcons/user.svg);\n"
"\n"
"border-radius: 10px;\n"
"border:0px;")

        self.verticalLayout_4.addWidget(self.label_6)

        self.nameHistory1 = QLabel(self.frame_10)
        self.nameHistory1.setObjectName(u"nameHistory1")
        self.nameHistory1.setFont(font3)
        self.nameHistory1.setStyleSheet(u"border:0px;\n"
"border-radius:0px;\n"
"border-bottom:1px solid;\n"
"border-top:1px solid;")
        self.nameHistory1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.nameHistory1)

        self.dateHistory1 = QLabel(self.frame_10)
        self.dateHistory1.setObjectName(u"dateHistory1")
        self.dateHistory1.setFont(font3)
        self.dateHistory1.setStyleSheet(u"border:0px;")
        self.dateHistory1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.dateHistory1)


        self.horizontalLayout_6.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(98, 91))
        self.frame_11.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"image: url(:/Icons/ResourcesFolder/featherIcons/user.svg);\n"
"\n"
"border-radius: 10px;\n"
"border:0px;\n"
"")

        self.verticalLayout_5.addWidget(self.label_9)

        self.nameHistory2 = QLabel(self.frame_11)
        self.nameHistory2.setObjectName(u"nameHistory2")
        self.nameHistory2.setFont(font3)
        self.nameHistory2.setStyleSheet(u"border:0px;\n"
"border-radius:0px;\n"
"border-bottom:1px solid;\n"
"border-top:1px solid;")
        self.nameHistory2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.nameHistory2)

        self.dateHistory2 = QLabel(self.frame_11)
        self.dateHistory2.setObjectName(u"dateHistory2")
        self.dateHistory2.setFont(font3)
        self.dateHistory2.setStyleSheet(u"border:0px;")
        self.dateHistory2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.dateHistory2)


        self.horizontalLayout_6.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(98, 91))
        self.frame_12.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"image: url(:/Icons/ResourcesFolder/featherIcons/user.svg);\n"
"\n"
"border-radius: 10px;\n"
"border:0px;")

        self.verticalLayout_6.addWidget(self.label_12)

        self.nameHistory3 = QLabel(self.frame_12)
        self.nameHistory3.setObjectName(u"nameHistory3")
        self.nameHistory3.setFont(font3)
        self.nameHistory3.setStyleSheet(u"border:0px;\n"
"border-radius:0px;\n"
"border-bottom:1px solid;\n"
"border-top:1px solid;")
        self.nameHistory3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.nameHistory3)

        self.dateHistory3 = QLabel(self.frame_12)
        self.dateHistory3.setObjectName(u"dateHistory3")
        self.dateHistory3.setFont(font3)
        self.dateHistory3.setStyleSheet(u"border:0px;")
        self.dateHistory3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.dateHistory3)


        self.horizontalLayout_6.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(98, 91))
        self.frame_13.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"image: url(:/Icons/ResourcesFolder/featherIcons/user.svg);\n"
"\n"
"border-radius: 10px;\n"
"border:0px;")

        self.verticalLayout_7.addWidget(self.label_15)

        self.nameHistory4 = QLabel(self.frame_13)
        self.nameHistory4.setObjectName(u"nameHistory4")
        self.nameHistory4.setFont(font3)
        self.nameHistory4.setStyleSheet(u"border:0px;\n"
"border-radius:0px;\n"
"border-bottom:1px solid;\n"
"border-top:1px solid;")
        self.nameHistory4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.nameHistory4)

        self.dateHistory4 = QLabel(self.frame_13)
        self.dateHistory4.setObjectName(u"dateHistory4")
        self.dateHistory4.setFont(font3)
        self.dateHistory4.setStyleSheet(u"border:0px;")
        self.dateHistory4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.dateHistory4)


        self.horizontalLayout_6.addWidget(self.frame_13)


        self.verticalLayout_13.addWidget(self.frame_4)

        self.frame_15 = QFrame(self.frame_21)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setMinimumSize(QSize(96, 0))
        self.frame_15.setStyleSheet(u" border: 0px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"    min-width: 6em;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_15)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy5)
        self.frame_18.setMinimumSize(QSize(96, 0))
        self.frame_18.setMaximumSize(QSize(1000, 16777215))
        self.frame_18.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(134, 154, 175);\n"
"}")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_18)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(15, 15, 15, -1)
        self.frame_26 = QFrame(self.frame_18)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setMinimumSize(QSize(96, 50))
        self.frame_26.setMaximumSize(QSize(16777215, 84))
        self.frame_26.setStyleSheet(u"background-color: rgb(209, 209, 207);\n"
"border-radius:0px;")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.frame_35 = QFrame(self.frame_26)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(96, 0))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_26)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy3.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy3)
        self.frame_36.setMinimumSize(QSize(96, 0))
        self.frame_36.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                 stop: 0 rgb(157, 156, 153), stop: 0.4 rgb(209, 208, 206),\n"
"                                 stop: 0.6 rgb(209, 208, 206), stop: 1.0  rgb(157, 156, 153));")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_26)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(96, 0))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_37)


        self.verticalLayout_10.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_18)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(16777215, 30))
        self.frame_27.setStyleSheet(u"background-color: rgb(209, 209, 207);\n"
"border-radius:0px;")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.frame_27)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy)
        self.frame_40.setMinimumSize(QSize(96, 0))
        self.frame_40.setMaximumSize(QSize(20, 16777215))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_40)

        self.frame_39 = QFrame(self.frame_27)
        self.frame_39.setObjectName(u"frame_39")
        sizePolicy3.setHeightForWidth(self.frame_39.sizePolicy().hasHeightForWidth())
        self.frame_39.setSizePolicy(sizePolicy3)
        self.frame_39.setMinimumSize(QSize(96, 0))
        self.frame_39.setMaximumSize(QSize(16777215, 16777215))
        self.frame_39.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                 stop: 0 rgb(157, 156, 153), stop: 0.4 rgb(209, 208, 206),\n"
"                                 stop: 0.6 rgb(209, 208, 206), stop: 1.0  rgb(157, 156, 153));\n"
"border-radius:0px;")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_39)

        self.frame_38 = QFrame(self.frame_27)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy)
        self.frame_38.setMinimumSize(QSize(96, 0))
        self.frame_38.setMaximumSize(QSize(20, 16777215))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_38)


        self.verticalLayout_10.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_18)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(96, 80))
        self.frame_28.setMaximumSize(QSize(16777215, 130))
        self.frame_28.setStyleSheet(u"background-color: rgb(209, 209, 207);\n"
"border-radius:0px;")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.frame_43 = QFrame(self.frame_28)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(96, 0))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_43)

        self.colorZone1T = QFrame(self.frame_28)
        self.colorZone1T.setObjectName(u"colorZone1T")
        sizePolicy3.setHeightForWidth(self.colorZone1T.sizePolicy().hasHeightForWidth())
        self.colorZone1T.setSizePolicy(sizePolicy3)
        self.colorZone1T.setMinimumSize(QSize(98, 0))
        self.colorZone1T.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                 stop: 0 rgb(154, 171, 188), stop: 0.48 rgb(198, 197, 195),\n"
"                                 stop: 0.52 rgb(198, 197, 195), stop: 1.0  rgb(154, 171, 188));\n"
"\n"
"border-radius:0px;\n"
"border:1px solid rgb(167, 167, 164);\n"
"\n"
"")
        self.colorZone1T.setFrameShape(QFrame.StyledPanel)
        self.colorZone1T.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.colorZone1T)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_16 = QSpacerItem(110, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_16)

        self.label_23 = QLabel(self.colorZone1T)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(98, 20))
        self.label_23.setMaximumSize(QSize(140, 40))
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"border-radius:0px;\n"
"border-top: 1px solid;\n"
"border-bottom: 1px solid;\n"
"border-right: 1px solid;\n"
"background-color:rgba(0, 0, 0, 0);")

        self.horizontalLayout_21.addWidget(self.label_23)

        self.txtZona1T = QLabel(self.colorZone1T)
        self.txtZona1T.setObjectName(u"txtZona1T")
        self.txtZona1T.setMinimumSize(QSize(98, 20))
        self.txtZona1T.setMaximumSize(QSize(55, 40))
        self.txtZona1T.setFont(font1)
        self.txtZona1T.setStyleSheet(u"border-radius:0px;\n"
"border-top: 1px solid;\n"
"border-bottom: 1px solid;\n"
"border-left: 1px solid;\n"
"background-color:rgba(0, 0, 0, 0);")
        self.txtZona1T.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.txtZona1T)

        self.horizontalSpacer_17 = QSpacerItem(95, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_17)


        self.horizontalLayout_11.addWidget(self.colorZone1T)

        self.frame_41 = QFrame(self.frame_28)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(96, 0))
        self.frame_41.setStyleSheet(u"border-image: url(:/Images/ResourcesFolder/Imagenes/ZonasRefracSup.png);")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_41)


        self.verticalLayout_10.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_18)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(96, 70))
        self.frame_29.setMaximumSize(QSize(16777215, 100))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.frame_46 = QFrame(self.frame_29)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(96, 0))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.frame_46)

        self.colorZone2T = QFrame(self.frame_29)
        self.colorZone2T.setObjectName(u"colorZone2T")
        sizePolicy3.setHeightForWidth(self.colorZone2T.sizePolicy().hasHeightForWidth())
        self.colorZone2T.setSizePolicy(sizePolicy3)
        self.colorZone2T.setMinimumSize(QSize(98, 0))
        self.colorZone2T.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                 stop: 0 rgb(122, 124, 151), stop: 0.48 rgb(198, 197, 195),\n"
"                                 stop: 0.52 rgb(198, 197, 195), stop: 1.0  rgb(122, 124, 151));\n"
"border-radius:0px;\n"
"border:1px solid rgb(167, 167, 164);")
        self.colorZone2T.setFrameShape(QFrame.StyledPanel)
        self.colorZone2T.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.colorZone2T)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_18 = QSpacerItem(95, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_18)

        self.label_24 = QLabel(self.colorZone2T)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(98, 20))
        self.label_24.setMaximumSize(QSize(140, 40))
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"border-radius:0px;\n"
"border-top: 1px solid;\n"
"border-bottom: 1px solid;\n"
"border-right: 1px solid;\n"
"background-color:rgba(0, 0, 0, 0);")

        self.horizontalLayout_22.addWidget(self.label_24)

        self.txtZona2T = QLabel(self.colorZone2T)
        self.txtZona2T.setObjectName(u"txtZona2T")
        self.txtZona2T.setMinimumSize(QSize(98, 20))
        self.txtZona2T.setMaximumSize(QSize(55, 40))
        self.txtZona2T.setFont(font1)
        self.txtZona2T.setStyleSheet(u"border-radius:0px;\n"
"border-top: 1px solid;\n"
"border-bottom: 1px solid;\n"
"border-left: 1px solid;\n"
"background-color:rgba(0, 0, 0, 0);")
        self.txtZona2T.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.txtZona2T)

        self.horizontalSpacer_19 = QSpacerItem(95, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_19)


        self.horizontalLayout_12.addWidget(self.colorZone2T)

        self.frame_44 = QFrame(self.frame_29)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(96, 0))
        self.frame_44.setStyleSheet(u"border-image: url(:/Images/ResourcesFolder/Imagenes/ZonasRefracMed.png);")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.frame_44)


        self.verticalLayout_10.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_18)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(96, 90))
        self.frame_30.setMaximumSize(QSize(16777215, 150))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, 0, -1, 0)
        self.frame_49 = QFrame(self.frame_30)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(96, 0))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame_49)

        self.colorZone3T = QFrame(self.frame_30)
        self.colorZone3T.setObjectName(u"colorZone3T")
        sizePolicy3.setHeightForWidth(self.colorZone3T.sizePolicy().hasHeightForWidth())
        self.colorZone3T.setSizePolicy(sizePolicy3)
        self.colorZone3T.setMinimumSize(QSize(98, 0))
        self.colorZone3T.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                 stop: 0 rgb(47, 146, 178), stop: 0.48 rgb(190, 192, 194),\n"
"                                 stop: 0.52 rgb(190, 192, 194), stop: 1.0  rgb(47, 146, 178));\n"
"border-radius:0px;\n"
"border:1px solid rgb(167, 167, 164);\n"
"\n"
"")
        self.colorZone3T.setFrameShape(QFrame.StyledPanel)
        self.colorZone3T.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.colorZone3T)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_20 = QSpacerItem(95, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_20)

        self.label_25 = QLabel(self.colorZone3T)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(98, 20))
        self.label_25.setMaximumSize(QSize(140, 40))
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"border-radius:0px;\n"
"border-top: 1px solid;\n"
"border-bottom: 1px solid;\n"
"border-right: 1px solid;\n"
"background-color:rgba(0, 0, 0, 0);")

        self.horizontalLayout_23.addWidget(self.label_25)

        self.txtZona3T = QLabel(self.colorZone3T)
        self.txtZona3T.setObjectName(u"txtZona3T")
        self.txtZona3T.setMinimumSize(QSize(98, 20))
        self.txtZona3T.setMaximumSize(QSize(55, 40))
        self.txtZona3T.setFont(font1)
        self.txtZona3T.setStyleSheet(u"border-radius:0px;\n"
"border-top: 1px solid;\n"
"border-bottom: 1px solid;\n"
"border-left: 1px solid;\n"
"background-color:rgba(0, 0, 0, 0);")
        self.txtZona3T.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.txtZona3T)

        self.horizontalSpacer_21 = QSpacerItem(95, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_21)


        self.horizontalLayout_19.addWidget(self.colorZone3T)

        self.frame_47 = QFrame(self.frame_30)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(96, 0))
        self.frame_47.setStyleSheet(u"border-image: url(:/Images/ResourcesFolder/Imagenes/ZonasRefracInf.png);")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame_47)


        self.verticalLayout_10.addWidget(self.frame_30)

        self.frame_34 = QFrame(self.frame_18)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(96, 85))
        self.frame_34.setMaximumSize(QSize(16777215, 118))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.frame_52 = QFrame(self.frame_34)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(96, 0))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.frame_52)

        self.frame_51 = QFrame(self.frame_34)
        self.frame_51.setObjectName(u"frame_51")
        sizePolicy3.setHeightForWidth(self.frame_51.sizePolicy().hasHeightForWidth())
        self.frame_51.setSizePolicy(sizePolicy3)
        self.frame_51.setMinimumSize(QSize(98, 0))
        self.frame_51.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                 stop: 0 rgb(157, 156, 153), stop: 0.48 rgb(190, 189, 187),\n"
"                                 stop: 0.52 rgb(190, 189, 187), stop: 1.0  rgb(157, 156, 153));\n"
"border-radius:0px;\n"
"border:1px solid rgb(167, 167, 164);\n"
"border-bottom-right-radius:50px;\n"
"border-bottom-left-radius:50px;\n"
"\n"
"\n"
"")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.frame_51)

        self.frame_50 = QFrame(self.frame_34)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(96, 0))
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.frame_50)


        self.verticalLayout_10.addWidget(self.frame_34)


        self.gridLayout_2.addWidget(self.frame_18, 1, 1, 1, 1)

        self.frame_19 = QFrame(self.frame_15)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy6 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy6)
        self.frame_19.setMaximumSize(QSize(16777215, 40))
        self.frame_19.setStyleSheet(u"border:0px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_19)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(194, 30))
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(18)
        font7.setBold(True)
        self.label_4.setFont(font7)
        self.label_4.setStyleSheet(u"QLabel{\n"
"border-radius:0px;\n"
"border : 0px;\n"
"border-bottom:1px solid;\n"
"border-top:1px solid;\n"
"padding: 0 0 0 98;\n"
"}")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_4)

        self.pbHistorialZonasF = QPushButton(self.frame_19)
        self.pbHistorialZonasF.setObjectName(u"pbHistorialZonasF")
        self.pbHistorialZonasF.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.pbHistorialZonasF.sizePolicy().hasHeightForWidth())
        self.pbHistorialZonasF.setSizePolicy(sizePolicy5)
        self.pbHistorialZonasF.setMinimumSize(QSize(98, 0))
        self.pbHistorialZonasF.setMaximumSize(QSize(16777215, 16777215))
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(14)
        self.pbHistorialZonasF.setFont(font8)
        self.pbHistorialZonasF.setStyleSheet(u"QPushButton:enabled{\n"
"	background-color: rgb(214, 214, 214);\n"
"border: 1px solid gray;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 140, 34, 240);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(235, 115, 9, 255);\n"
"}")

        self.horizontalLayout_15.addWidget(self.pbHistorialZonasF)


        self.gridLayout_2.addWidget(self.frame_19, 0, 0, 1, 1)

        self.frame_20 = QFrame(self.frame_15)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 40))
        self.frame_20.setStyleSheet(u" border: 0px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.pbHistorialZonasT = QPushButton(self.frame_20)
        self.pbHistorialZonasT.setObjectName(u"pbHistorialZonasT")
        sizePolicy5.setHeightForWidth(self.pbHistorialZonasT.sizePolicy().hasHeightForWidth())
        self.pbHistorialZonasT.setSizePolicy(sizePolicy5)
        self.pbHistorialZonasT.setFont(font8)
        self.pbHistorialZonasT.setStyleSheet(u"QPushButton:enabled{\n"
"	background-color: rgb(214, 214, 214);\n"
"border: 1px solid gray;\n"
"border-top-left-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 140, 34, 240);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(235, 115, 9, 255);\n"
"}")

        self.horizontalLayout_17.addWidget(self.pbHistorialZonasT)

        self.label_5 = QLabel(self.frame_20)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font7)
        self.label_5.setStyleSheet(u"QLabel{\n"
"border-radius:0px;\n"
"border : 0px;\n"
"border-bottom:1px solid;\n"
"border-top:1px solid;\n"
"padding: 0 98 0 0;\n"
"}")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_5)


        self.gridLayout_2.addWidget(self.frame_20, 0, 1, 1, 1)

        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy5.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy5)
        self.frame_17.setMinimumSize(QSize(96, 0))
        self.frame_17.setMaximumSize(QSize(1000, 16777215))
        self.frame_17.setSizeIncrement(QSize(0, 0))
        self.frame_17.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(134, 154, 175);\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_17)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(15, 15, 15, -1)
        self.frame_74 = QFrame(self.frame_17)
        self.frame_74.setObjectName(u"frame_74")
        sizePolicy.setHeightForWidth(self.frame_74.sizePolicy().hasHeightForWidth())
        self.frame_74.setSizePolicy(sizePolicy)
        self.frame_74.setMinimumSize(QSize(96, 50))
        self.frame_74.setMaximumSize(QSize(16777215, 84))
        self.frame_74.setStyleSheet(u"background-color: rgb(209, 209, 207);\n"
"border-radius:0px;")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(-1, 0, -1, 0)
        self.frame_75 = QFrame(self.frame_74)
        self.frame_75.setObjectName(u"frame_75")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_75.sizePolicy().hasHeightForWidth())
        self.frame_75.setSizePolicy(sizePolicy7)
        self.frame_75.setMinimumSize(QSize(96, 0))
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_32.addWidget(self.frame_75)

        self.frame_76 = QFrame(self.frame_74)
        self.frame_76.setObjectName(u"frame_76")
        sizePolicy3.setHeightForWidth(self.frame_76.sizePolicy().hasHeightForWidth())
        self.frame_76.setSizePolicy(sizePolicy3)
        self.frame_76.setMinimumSize(QSize(96, 0))
        self.frame_76.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                 stop: 0 rgb(157, 156, 153), stop: 0.4 rgb(209, 208, 206),\n"
"                                 stop: 0.6 rgb(209, 208, 206), stop: 1.0  rgb(157, 156, 153));")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_32.addWidget(self.frame_76)

        self.frame_77 = QFrame(self.frame_74)
        self.frame_77.setObjectName(u"frame_77")
        sizePolicy7.setHeightForWidth(self.frame_77.sizePolicy().hasHeightForWidth())
        self.frame_77.setSizePolicy(sizePolicy7)
        self.frame_77.setMinimumSize(QSize(96, 0))
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_32.addWidget(self.frame_77)


        self.verticalLayout_11.addWidget(self.frame_74)

        self.frame_31 = QFrame(self.frame_17)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(16777215, 30))
        self.frame_31.setStyleSheet(u"background-color: rgb(209, 209, 207);\n"
"border-radius:0px;")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_59 = QFrame(self.frame_31)
        self.frame_59.setObjectName(u"frame_59")
        sizePolicy.setHeightForWidth(self.frame_59.sizePolicy().hasHeightForWidth())
        self.frame_59.setSizePolicy(sizePolicy)
        self.frame_59.setMinimumSize(QSize(96, 0))
        self.frame_59.setMaximumSize(QSize(20, 16777215))
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_29.addWidget(self.frame_59)

        self.frame_63 = QFrame(self.frame_31)
        self.frame_63.setObjectName(u"frame_63")
        sizePolicy3.setHeightForWidth(self.frame_63.sizePolicy().hasHeightForWidth())
        self.frame_63.setSizePolicy(sizePolicy3)
        self.frame_63.setMinimumSize(QSize(96, 0))
        self.frame_63.setMaximumSize(QSize(16777215, 16777215))
        self.frame_63.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                 stop: 0 rgb(157, 156, 153), stop: 0.4 rgb(209, 208, 206),\n"
"                                 stop: 0.6 rgb(209, 208, 206), stop: 1.0  rgb(157, 156, 153));\n"
"border-radius:0px;")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_29.addWidget(self.frame_63)

        self.frame_67 = QFrame(self.frame_31)
        self.frame_67.setObjectName(u"frame_67")
        sizePolicy.setHeightForWidth(self.frame_67.sizePolicy().hasHeightForWidth())
        self.frame_67.setSizePolicy(sizePolicy)
        self.frame_67.setMinimumSize(QSize(96, 0))
        self.frame_67.setMaximumSize(QSize(20, 16777215))
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_29.addWidget(self.frame_67)


        self.verticalLayout_11.addWidget(self.frame_31)

        self.frame_82 = QFrame(self.frame_17)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setMinimumSize(QSize(96, 80))
        self.frame_82.setMaximumSize(QSize(16777215, 130))
        self.frame_82.setStyleSheet(u"background-color: rgb(209, 209, 207);\n"
"border-radius:0px;")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(-1, 0, -1, 0)
        self.frame_83 = QFrame(self.frame_82)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMinimumSize(QSize(96, 0))
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_34.addWidget(self.frame_83)

        self.colorZone1F = QFrame(self.frame_82)
        self.colorZone1F.setObjectName(u"colorZone1F")
        sizePolicy3.setHeightForWidth(self.colorZone1F.sizePolicy().hasHeightForWidth())
        self.colorZone1F.setSizePolicy(sizePolicy3)
        self.colorZone1F.setMinimumSize(QSize(98, 0))
        self.colorZone1F.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                 stop: 0 rgb(154, 171, 188), stop: 0.48 rgb(198, 197, 195),\n"
"                                 stop: 0.52 rgb(198, 197, 195), stop: 1.0  rgb(154, 171, 188));\n"
"\n"
"border-radius:0px;\n"
"border:1px solid rgb(167, 167, 164);")
        self.colorZone1F.setFrameShape(QFrame.StyledPanel)
        self.colorZone1F.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.colorZone1F)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalSpacer_30 = QSpacerItem(110, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_30)

        self.label_30 = QLabel(self.colorZone1F)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(98, 20))
        self.label_30.setMaximumSize(QSize(140, 40))
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(u"border-radius:0px;\n"
"border-top: 1px solid;\n"
"border-bottom: 1px solid;\n"
"border-right: 1px solid;\n"
"background-color:rgba(0, 0, 0, 0);")

        self.horizontalLayout_35.addWidget(self.label_30)

        self.txtZona1F = QLabel(self.colorZone1F)
        self.txtZona1F.setObjectName(u"txtZona1F")
        self.txtZona1F.setMinimumSize(QSize(98, 20))
        self.txtZona1F.setMaximumSize(QSize(55, 40))
        self.txtZona1F.setFont(font1)
        self.txtZona1F.setStyleSheet(u"border-radius:0px;\n"
"border-top: 1px solid;\n"
"border-bottom: 1px solid;\n"
"border-left: 1px solid;\n"
"background-color:rgba(0, 0, 0, 0);")
        self.txtZona1F.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.txtZona1F)

        self.horizontalSpacer_31 = QSpacerItem(110, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_31)


        self.horizontalLayout_34.addWidget(self.colorZone1F)

        self.frame_85 = QFrame(self.frame_82)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMinimumSize(QSize(96, 0))
        self.frame_85.setStyleSheet(u"border-image: url(:/Images/ResourcesFolder/Imagenes/ZonasRefracSup.png);")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_34.addWidget(self.frame_85)


        self.verticalLayout_11.addWidget(self.frame_82)

        self.frame_32 = QFrame(self.frame_17)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(96, 70))
        self.frame_32.setMaximumSize(QSize(16777215, 100))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, 0, -1, 0)
        self.frame_71 = QFrame(self.frame_32)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMinimumSize(QSize(96, 0))
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_30.addWidget(self.frame_71)

        self.colorZone2F = QFrame(self.frame_32)
        self.colorZone2F.setObjectName(u"colorZone2F")
        sizePolicy3.setHeightForWidth(self.colorZone2F.sizePolicy().hasHeightForWidth())
        self.colorZone2F.setSizePolicy(sizePolicy3)
        self.colorZone2F.setMinimumSize(QSize(98, 0))
        self.colorZone2F.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                 stop: 0 rgb(122, 124, 151), stop: 0.48 rgb(198, 197, 195),\n"
"                                 stop: 0.52 rgb(198, 197, 195), stop: 1.0  rgb(122, 124, 151));\n"
"border-radius:0px;\n"
"border:1px solid rgb(167, 167, 164);")
        self.colorZone2F.setFrameShape(QFrame.StyledPanel)
        self.colorZone2F.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.colorZone2F)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalSpacer_28 = QSpacerItem(110, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_28)

        self.label_29 = QLabel(self.colorZone2F)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(98, 20))
        self.label_29.setMaximumSize(QSize(140, 40))
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(u"border-radius:0px;\n"
"border-top: 1px solid;\n"
"border-bottom: 1px solid;\n"
"border-right: 1px solid;\n"
"background-color:rgba(0, 0, 0, 0);")

        self.horizontalLayout_31.addWidget(self.label_29)

        self.txtZona2F = QLabel(self.colorZone2F)
        self.txtZona2F.setObjectName(u"txtZona2F")
        self.txtZona2F.setMinimumSize(QSize(98, 20))
        self.txtZona2F.setMaximumSize(QSize(55, 40))
        self.txtZona2F.setFont(font1)
        self.txtZona2F.setStyleSheet(u"border-radius:0px;\n"
"border-top: 1px solid;\n"
"border-bottom: 1px solid;\n"
"border-left: 1px solid;\n"
"background-color:rgba(0, 0, 0, 0);")
        self.txtZona2F.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.txtZona2F)

        self.horizontalSpacer_29 = QSpacerItem(110, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_29)


        self.horizontalLayout_30.addWidget(self.colorZone2F)

        self.frame_73 = QFrame(self.frame_32)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(96, 0))
        self.frame_73.setStyleSheet(u"border-image: url(:/Images/ResourcesFolder/Imagenes/ZonasRefracMed.png);")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_30.addWidget(self.frame_73)


        self.verticalLayout_11.addWidget(self.frame_32)

        self.frame_86 = QFrame(self.frame_17)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(96, 90))
        self.frame_86.setMaximumSize(QSize(16777215, 150))
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(-1, 0, -1, 0)
        self.frame_87 = QFrame(self.frame_86)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMinimumSize(QSize(96, 0))
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_36.addWidget(self.frame_87)

        self.colorZone3F = QFrame(self.frame_86)
        self.colorZone3F.setObjectName(u"colorZone3F")
        sizePolicy3.setHeightForWidth(self.colorZone3F.sizePolicy().hasHeightForWidth())
        self.colorZone3F.setSizePolicy(sizePolicy3)
        self.colorZone3F.setMinimumSize(QSize(98, 0))
        self.colorZone3F.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                 stop: 0 rgb(47, 146, 178), stop: 0.48 rgb(190, 192, 194),\n"
"                                 stop: 0.52 rgb(190, 192, 194), stop: 1.0  rgb(47, 146, 178));\n"
"border-radius:0px;\n"
"border:1px solid rgb(167, 167, 164);\n"
"\n"
"")
        self.colorZone3F.setFrameShape(QFrame.StyledPanel)
        self.colorZone3F.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.colorZone3F)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalSpacer_32 = QSpacerItem(110, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_32)

        self.label_31 = QLabel(self.colorZone3F)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(98, 20))
        self.label_31.setMaximumSize(QSize(140, 40))
        self.label_31.setFont(font)
        self.label_31.setStyleSheet(u"border-radius:0px;\n"
"border-top: 1px solid;\n"
"border-bottom: 1px solid;\n"
"border-right: 1px solid;\n"
"background-color:rgba(0, 0, 0, 0);")

        self.horizontalLayout_37.addWidget(self.label_31)

        self.txtZona3F = QLabel(self.colorZone3F)
        self.txtZona3F.setObjectName(u"txtZona3F")
        self.txtZona3F.setMinimumSize(QSize(98, 20))
        self.txtZona3F.setMaximumSize(QSize(55, 40))
        self.txtZona3F.setFont(font1)
        self.txtZona3F.setStyleSheet(u"border-radius:0px;\n"
"border-top: 1px solid;\n"
"border-bottom: 1px solid;\n"
"border-left: 1px solid;\n"
"background-color:rgba(0, 0, 0, 0);")
        self.txtZona3F.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.txtZona3F)

        self.horizontalSpacer_33 = QSpacerItem(110, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_33)


        self.horizontalLayout_36.addWidget(self.colorZone3F)

        self.frame_89 = QFrame(self.frame_86)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMinimumSize(QSize(96, 0))
        self.frame_89.setStyleSheet(u"border-image: url(:/Images/ResourcesFolder/Imagenes/ZonasRefracInf.png);")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_36.addWidget(self.frame_89)


        self.verticalLayout_11.addWidget(self.frame_86)

        self.frame_78 = QFrame(self.frame_17)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(96, 85))
        self.frame_78.setMaximumSize(QSize(16777215, 118))
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(-1, 0, -1, -1)
        self.frame_79 = QFrame(self.frame_78)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMinimumSize(QSize(96, 0))
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_33.addWidget(self.frame_79)

        self.frame_80 = QFrame(self.frame_78)
        self.frame_80.setObjectName(u"frame_80")
        sizePolicy3.setHeightForWidth(self.frame_80.sizePolicy().hasHeightForWidth())
        self.frame_80.setSizePolicy(sizePolicy3)
        self.frame_80.setMinimumSize(QSize(98, 0))
        self.frame_80.setStyleSheet(u"background: qlineargradient(spread:pad,x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                 stop: 0 rgb(157, 156, 153), stop: 0.48 rgb(190, 189, 187),\n"
"                                 stop: 0.52 rgb(190, 189, 187), stop: 1.0  rgb(157, 156, 153));\n"
"border-radius:0px;\n"
"border:1px solid rgb(167, 167, 164);\n"
"border-bottom-right-radius:50px;\n"
"border-bottom-left-radius:50px;\n"
"\n"
"\n"
"")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_33.addWidget(self.frame_80)

        self.frame_81 = QFrame(self.frame_78)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMinimumSize(QSize(96, 0))
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_33.addWidget(self.frame_81)


        self.verticalLayout_11.addWidget(self.frame_78)


        self.gridLayout_2.addWidget(self.frame_17, 1, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_15)

        self.verticalLayout_13.setStretch(0, 1)
        self.verticalLayout_13.setStretch(1, 2)

        self.verticalLayout_2.addWidget(self.frame_21)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(98, 50))
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"    min-width: 6em;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_5)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(96, 50))
        self.frame_16.setMaximumSize(QSize(16777215, 50))
        self.frame_16.setStyleSheet(u" border: 0px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"background-color:rgba(255, 255, 255, 0);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(9, 0, 9, 0)
        self.frame_22 = QFrame(self.frame_16)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"QFrame{\n"
"border:0px;\n"
"background-color:rgba(255, 255, 255, 0);\n"
"}")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.labelColadas = QLabel(self.frame_22)
        self.labelColadas.setObjectName(u"labelColadas")
        sizePolicy1.setHeightForWidth(self.labelColadas.sizePolicy().hasHeightForWidth())
        self.labelColadas.setSizePolicy(sizePolicy1)
        self.labelColadas.setMinimumSize(QSize(96, 0))
        self.labelColadas.setMaximumSize(QSize(16777215, 35))
        self.labelColadas.setFont(font8)
        self.labelColadas.setStyleSheet(u"QLabel{\n"
"border-radius:0px;\n"
"border:0px;\n"
"border-color: rgb(163, 163, 163);\n"
"border-top:1px solid;\n"
"border-bottom:1px solid;\n"
"}")

        self.horizontalLayout_8.addWidget(self.labelColadas)


        self.horizontalLayout_7.addWidget(self.frame_22)

        self.frame_33 = QFrame(self.frame_16)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.pbAddColada = QPushButton(self.frame_33)
        self.pbAddColada.setObjectName(u"pbAddColada")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.pbAddColada.sizePolicy().hasHeightForWidth())
        self.pbAddColada.setSizePolicy(sizePolicy8)
        self.pbAddColada.setMinimumSize(QSize(98, 35))
        self.pbAddColada.setMaximumSize(QSize(16777215, 35))
        font9 = QFont()
        font9.setFamilies([u"Arial"])
        font9.setPointSize(14)
        font9.setBold(False)
        self.pbAddColada.setFont(font9)
        self.pbAddColada.setStyleSheet(u"QPushButton{\n"
"	border:1px solid gray;\n"
"	border-radius:10px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 140, 34, 240);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(235, 115, 9, 255);\n"
"}")

        self.horizontalLayout_18.addWidget(self.pbAddColada)

        self.pbDeleteColada = QPushButton(self.frame_33)
        self.pbDeleteColada.setObjectName(u"pbDeleteColada")
        sizePolicy8.setHeightForWidth(self.pbDeleteColada.sizePolicy().hasHeightForWidth())
        self.pbDeleteColada.setSizePolicy(sizePolicy8)
        self.pbDeleteColada.setMinimumSize(QSize(98, 35))
        self.pbDeleteColada.setMaximumSize(QSize(16777215, 35))
        self.pbDeleteColada.setFont(font9)
        self.pbDeleteColada.setStyleSheet(u"QPushButton{\n"
"	border:1px solid gray;\n"
"	border-radius:10px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 140, 34, 240);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(235, 115, 9, 255);\n"
"}")

        self.horizontalLayout_18.addWidget(self.pbDeleteColada)


        self.horizontalLayout_7.addWidget(self.frame_33)


        self.verticalLayout_9.addWidget(self.frame_16)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frameAddColada = QFrame(self.frameBottom)
        self.frameAddColada.setObjectName(u"frameAddColada")
        sizePolicy.setHeightForWidth(self.frameAddColada.sizePolicy().hasHeightForWidth())
        self.frameAddColada.setSizePolicy(sizePolicy)
        self.frameAddColada.setMinimumSize(QSize(300, 0))
        self.frameAddColada.setMaximumSize(QSize(300, 16777215))
        self.frameAddColada.setContextMenuPolicy(Qt.NoContextMenu)
        self.frameAddColada.setStyleSheet(u"QFrame{\n"
" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}")
        self.frameAddColada.setFrameShape(QFrame.Box)
        self.frameAddColada.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frameAddColada)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frameAddColada)
        self.frame.setObjectName(u"frame")
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setStyleSheet(u"border: 0px solid gray;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        font10 = QFont()
        font10.setFamilies([u"Arial"])
        font10.setPointSize(20)
        font10.setBold(True)
        font10.setItalic(False)
        font10.setKerning(True)
        self.label_7.setFont(font10)
        self.label_7.setStyleSheet(u" border: 0px solid gray;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_7)


        self.verticalLayout_14.addWidget(self.frame)

        self.frame_48 = QFrame(self.frameAddColada)
        self.frame_48.setObjectName(u"frame_48")
        sizePolicy2.setHeightForWidth(self.frame_48.sizePolicy().hasHeightForWidth())
        self.frame_48.setSizePolicy(sizePolicy2)
        self.frame_48.setStyleSheet(u"border: 0px solid;")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_48)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_56 = QFrame(self.frame_48)
        self.frame_56.setObjectName(u"frame_56")
        sizePolicy2.setHeightForWidth(self.frame_56.sizePolicy().hasHeightForWidth())
        self.frame_56.setSizePolicy(sizePolicy2)
        self.frame_56.setStyleSheet(u"border-color: #DDDDDD;\n"
"border:0px;\n"
"background-color: #DDDDDD;")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_8 = QLabel(self.frame_56)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        font11 = QFont()
        font11.setFamilies([u"Arial"])
        font11.setPointSize(16)
        self.label_8.setFont(font11)
        self.label_8.setStyleSheet(u"border:0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_8)

        self.cbCuchara = QLineEdit(self.frame_56)
        self.cbCuchara.setObjectName(u"cbCuchara")
        self.cbCuchara.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.cbCuchara.sizePolicy().hasHeightForWidth())
        self.cbCuchara.setSizePolicy(sizePolicy2)
        self.cbCuchara.setMinimumSize(QSize(98, 0))
        self.cbCuchara.setMaximumSize(QSize(100, 16777215))
        font12 = QFont()
        font12.setFamilies([u"Arial"])
        font12.setPointSize(18)
        font12.setItalic(False)
        self.cbCuchara.setFont(font12)
        self.cbCuchara.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"    min-width: 6em;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.cbCuchara.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.cbCuchara)


        self.verticalLayout_16.addWidget(self.frame_56)

        self.frame_54 = QFrame(self.frame_48)
        self.frame_54.setObjectName(u"frame_54")
        sizePolicy2.setHeightForWidth(self.frame_54.sizePolicy().hasHeightForWidth())
        self.frame_54.setSizePolicy(sizePolicy2)
        self.frame_54.setStyleSheet(u"border-color: #DDDDDD;\n"
"border:0px;\n"
"background-color: #DDDDDD;")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_10 = QLabel(self.frame_54)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        font13 = QFont()
        font13.setFamilies([u"Arial"])
        font13.setPointSize(15)
        self.label_10.setFont(font13)
        self.label_10.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_10)

        self.txtCampana = QLineEdit(self.frame_54)
        self.txtCampana.setObjectName(u"txtCampana")
        self.txtCampana.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.txtCampana.sizePolicy().hasHeightForWidth())
        self.txtCampana.setSizePolicy(sizePolicy2)
        self.txtCampana.setMinimumSize(QSize(98, 0))
        self.txtCampana.setMaximumSize(QSize(100, 16777215))
        self.txtCampana.setFont(font12)
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

        self.horizontalLayout_25.addWidget(self.txtCampana)


        self.verticalLayout_16.addWidget(self.frame_54)

        self.frame_55 = QFrame(self.frame_48)
        self.frame_55.setObjectName(u"frame_55")
        sizePolicy2.setHeightForWidth(self.frame_55.sizePolicy().hasHeightForWidth())
        self.frame_55.setSizePolicy(sizePolicy2)
        self.frame_55.setStyleSheet(u"border-color: #DDDDDD;\n"
"border:0px;\n"
"background-color: #DDDDDD;")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_17 = QLabel(self.frame_55)
        self.label_17.setObjectName(u"label_17")
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)
        self.label_17.setFont(font13)
        self.label_17.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_17)

        self.txtUltimaColada = QLineEdit(self.frame_55)
        self.txtUltimaColada.setObjectName(u"txtUltimaColada")
        self.txtUltimaColada.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.txtUltimaColada.sizePolicy().hasHeightForWidth())
        self.txtUltimaColada.setSizePolicy(sizePolicy2)
        self.txtUltimaColada.setMinimumSize(QSize(98, 0))
        self.txtUltimaColada.setMaximumSize(QSize(100, 16777215))
        self.txtUltimaColada.setFont(font12)
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

        self.horizontalLayout_14.addWidget(self.txtUltimaColada)


        self.verticalLayout_16.addWidget(self.frame_55)


        self.verticalLayout_14.addWidget(self.frame_48)

        self.frame_24 = QFrame(self.frameAddColada)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy2.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy2)
        self.frame_24.setStyleSheet(u"border: 0px solid gray;")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_24)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_58 = QFrame(self.frame_24)
        self.frame_58.setObjectName(u"frame_58")
        sizePolicy2.setHeightForWidth(self.frame_58.sizePolicy().hasHeightForWidth())
        self.frame_58.setSizePolicy(sizePolicy2)
        self.frame_58.setStyleSheet(u"border-color: #D3D3D3;\n"
"border:0px;\n"
"background-color: #D3D3D3;\n"
"")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_58)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_11 = QLabel(self.frame_58)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font13)
        self.label_11.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_11)


        self.verticalLayout_23.addWidget(self.frame_58)

        self.frame_64 = QFrame(self.frame_24)
        self.frame_64.setObjectName(u"frame_64")
        sizePolicy2.setHeightForWidth(self.frame_64.sizePolicy().hasHeightForWidth())
        self.frame_64.setSizePolicy(sizePolicy2)
        self.frame_64.setStyleSheet(u"border-color: #D3D3D3;\n"
"border:0px;\n"
"background-color: #D3D3D3;\n"
"")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pbSiEscoria = QPushButton(self.frame_64)
        self.pbSiEscoria.setObjectName(u"pbSiEscoria")
        self.pbSiEscoria.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.pbSiEscoria.sizePolicy().hasHeightForWidth())
        self.pbSiEscoria.setSizePolicy(sizePolicy2)
        font14 = QFont()
        font14.setFamilies([u"Arial"])
        font14.setPointSize(13)
        self.pbSiEscoria.setFont(font14)
        self.pbSiEscoria.setStyleSheet(u"QPushButton:enabled{\n"
"	background-color: rgb(154, 174, 195);\n"
"border-radius:12px;\n"
"}\n"
"QPushButton:disabled{\n"
"color:rgb(255, 255, 255);\n"
"background-color: rgb(140, 140, 140);\n"
"border-radius:12px;\n"
"}")

        self.horizontalLayout_16.addWidget(self.pbSiEscoria)

        self.pbNoEscoria = QPushButton(self.frame_64)
        self.pbNoEscoria.setObjectName(u"pbNoEscoria")
        sizePolicy2.setHeightForWidth(self.pbNoEscoria.sizePolicy().hasHeightForWidth())
        self.pbNoEscoria.setSizePolicy(sizePolicy2)
        self.pbNoEscoria.setFont(font14)
        self.pbNoEscoria.setStyleSheet(u"QPushButton:enabled{\n"
"	background-color: rgb(154, 174, 195);\n"
"border-radius:12px;\n"
"}\n"
"QPushButton:disabled{\n"
"color:rgb(255, 255, 255);\n"
"background-color: rgb(140, 140, 140);\n"
"border-radius:12px;\n"
"}")

        self.horizontalLayout_16.addWidget(self.pbNoEscoria)

        self.sbEscoria = QSpinBox(self.frame_64)
        self.sbEscoria.setObjectName(u"sbEscoria")
        sizePolicy2.setHeightForWidth(self.sbEscoria.sizePolicy().hasHeightForWidth())
        self.sbEscoria.setSizePolicy(sizePolicy2)
        self.sbEscoria.setFont(font11)
        self.sbEscoria.setStyleSheet(u"QSpinBox{\n"
" border: 0px solid gray;\n"
"	background-color: rgb(255, 255, 255);\n"
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
        self.sbEscoria.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sbEscoria.setAccelerated(True)
        self.sbEscoria.setMaximum(1000)
        self.sbEscoria.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_16.addWidget(self.sbEscoria)


        self.verticalLayout_23.addWidget(self.frame_64)


        self.verticalLayout_14.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frameAddColada)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy2.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy2)
        self.frame_25.setStyleSheet(u"border: 0px solid gray;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_25)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_57 = QFrame(self.frame_25)
        self.frame_57.setObjectName(u"frame_57")
        sizePolicy2.setHeightForWidth(self.frame_57.sizePolicy().hasHeightForWidth())
        self.frame_57.setSizePolicy(sizePolicy2)
        self.frame_57.setStyleSheet(u"border-color: #DDDDDD;\n"
"border:0px;\n"
"background-color: #DDDDDD;")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_57)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_13 = QLabel(self.frame_57)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)
        self.label_13.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_13)


        self.verticalLayout_17.addWidget(self.frame_57)

        self.frame_60 = QFrame(self.frame_25)
        self.frame_60.setObjectName(u"frame_60")
        sizePolicy.setHeightForWidth(self.frame_60.sizePolicy().hasHeightForWidth())
        self.frame_60.setSizePolicy(sizePolicy)
        self.frame_60.setStyleSheet(u"border-color: #DDDDDD;\n"
"border:0px;\n"
"background-color: #DDDDDD;")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_60)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_14 = QLabel(self.frame_60)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setFont(font11)
        self.label_14.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)

        self.txtPathTermografiaF = QLineEdit(self.frame_60)
        self.txtPathTermografiaF.setObjectName(u"txtPathTermografiaF")
        self.txtPathTermografiaF.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.txtPathTermografiaF.sizePolicy().hasHeightForWidth())
        self.txtPathTermografiaF.setSizePolicy(sizePolicy8)
        font15 = QFont()
        font15.setFamilies([u"Arial"])
        font15.setPointSize(12)
        font15.setItalic(False)
        self.txtPathTermografiaF.setFont(font15)
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

        self.gridLayout_3.addWidget(self.txtPathTermografiaF, 0, 1, 1, 1)

        self.pbFileDialog1 = QToolButton(self.frame_60)
        self.pbFileDialog1.setObjectName(u"pbFileDialog1")
        sizePolicy8.setHeightForWidth(self.pbFileDialog1.sizePolicy().hasHeightForWidth())
        self.pbFileDialog1.setSizePolicy(sizePolicy8)
        self.pbFileDialog1.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(0, 0, 0);\n"
"    border: 1px solid gray;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")

        self.gridLayout_3.addWidget(self.pbFileDialog1, 0, 2, 1, 1)

        self.label_16 = QLabel(self.frame_60)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setFont(font11)
        self.label_16.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)

        self.txtPathExcelF = QLineEdit(self.frame_60)
        self.txtPathExcelF.setObjectName(u"txtPathExcelF")
        self.txtPathExcelF.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.txtPathExcelF.sizePolicy().hasHeightForWidth())
        self.txtPathExcelF.setSizePolicy(sizePolicy8)
        self.txtPathExcelF.setFont(font15)
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

        self.gridLayout_3.addWidget(self.txtPathExcelF, 1, 1, 1, 1)

        self.pbFileDialog2 = QToolButton(self.frame_60)
        self.pbFileDialog2.setObjectName(u"pbFileDialog2")
        sizePolicy8.setHeightForWidth(self.pbFileDialog2.sizePolicy().hasHeightForWidth())
        self.pbFileDialog2.setSizePolicy(sizePolicy8)
        self.pbFileDialog2.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(0, 0, 0);\n"
"    border: 1px solid gray;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")

        self.gridLayout_3.addWidget(self.pbFileDialog2, 1, 2, 1, 1)


        self.verticalLayout_17.addWidget(self.frame_60)


        self.verticalLayout_14.addWidget(self.frame_25)

        self.frame_42 = QFrame(self.frameAddColada)
        self.frame_42.setObjectName(u"frame_42")
        sizePolicy2.setHeightForWidth(self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy2)
        self.frame_42.setStyleSheet(u"border: 0px solid gray;")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_42)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_61 = QFrame(self.frame_42)
        self.frame_61.setObjectName(u"frame_61")
        sizePolicy.setHeightForWidth(self.frame_61.sizePolicy().hasHeightForWidth())
        self.frame_61.setSizePolicy(sizePolicy)
        self.frame_61.setStyleSheet(u"border-color: #D3D3D3;\n"
"border:0px;\n"
"background-color: #D3D3D3;\n"
"")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_61)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_18 = QLabel(self.frame_61)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setFont(font4)
        self.label_18.setToolTipDuration(-1)
        self.label_18.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_18)


        self.verticalLayout_20.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.frame_42)
        self.frame_62.setObjectName(u"frame_62")
        sizePolicy.setHeightForWidth(self.frame_62.sizePolicy().hasHeightForWidth())
        self.frame_62.setSizePolicy(sizePolicy)
        self.frame_62.setStyleSheet(u"border-color: #D3D3D3;\n"
"border:0px;\n"
"background-color: #D3D3D3;\n"
"")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_62)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_19 = QLabel(self.frame_62)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setFont(font11)
        self.label_19.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)

        self.txtPathTermografiaT = QLineEdit(self.frame_62)
        self.txtPathTermografiaT.setObjectName(u"txtPathTermografiaT")
        self.txtPathTermografiaT.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.txtPathTermografiaT.sizePolicy().hasHeightForWidth())
        self.txtPathTermografiaT.setSizePolicy(sizePolicy8)
        self.txtPathTermografiaT.setFont(font15)
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

        self.gridLayout_4.addWidget(self.txtPathTermografiaT, 0, 1, 1, 1)

        self.pbFileDialog3 = QToolButton(self.frame_62)
        self.pbFileDialog3.setObjectName(u"pbFileDialog3")
        sizePolicy8.setHeightForWidth(self.pbFileDialog3.sizePolicy().hasHeightForWidth())
        self.pbFileDialog3.setSizePolicy(sizePolicy8)
        self.pbFileDialog3.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(0, 0, 0);\n"
"    border: 1px solid gray;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")

        self.gridLayout_4.addWidget(self.pbFileDialog3, 0, 2, 1, 1)

        self.label_20 = QLabel(self.frame_62)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setFont(font11)
        self.label_20.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_20, 1, 0, 1, 1)

        self.txtPathExcelT = QLineEdit(self.frame_62)
        self.txtPathExcelT.setObjectName(u"txtPathExcelT")
        self.txtPathExcelT.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.txtPathExcelT.sizePolicy().hasHeightForWidth())
        self.txtPathExcelT.setSizePolicy(sizePolicy8)
        self.txtPathExcelT.setFont(font15)
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

        self.gridLayout_4.addWidget(self.txtPathExcelT, 1, 1, 1, 1)

        self.pbFileDialog4 = QToolButton(self.frame_62)
        self.pbFileDialog4.setObjectName(u"pbFileDialog4")
        sizePolicy8.setHeightForWidth(self.pbFileDialog4.sizePolicy().hasHeightForWidth())
        self.pbFileDialog4.setSizePolicy(sizePolicy8)
        self.pbFileDialog4.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(0, 0, 0);\n"
"    border: 1px solid gray;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")

        self.gridLayout_4.addWidget(self.pbFileDialog4, 1, 2, 1, 1)


        self.verticalLayout_20.addWidget(self.frame_62)


        self.verticalLayout_14.addWidget(self.frame_42)

        self.frame_45 = QFrame(self.frameAddColada)
        self.frame_45.setObjectName(u"frame_45")
        sizePolicy2.setHeightForWidth(self.frame_45.sizePolicy().hasHeightForWidth())
        self.frame_45.setSizePolicy(sizePolicy2)
        self.frame_45.setStyleSheet(u"border-color: #DDDDDD;\n"
"border:0px;\n"
"background-color: #DDDDDD;")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_45)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setVerticalSpacing(6)
        self.gridLayout_5.setContentsMargins(9, 0, 9, 0)
        self.label_21 = QLabel(self.frame_45)
        self.label_21.setObjectName(u"label_21")
        sizePolicy2.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy2)
        self.label_21.setFont(font8)
        self.label_21.setStyleSheet(u"border:0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_21, 0, 0, 1, 2)

        self.txtNewColada = QLineEdit(self.frame_45)
        self.txtNewColada.setObjectName(u"txtNewColada")
        self.txtNewColada.setEnabled(False)
        sizePolicy9 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.txtNewColada.sizePolicy().hasHeightForWidth())
        self.txtNewColada.setSizePolicy(sizePolicy9)
        self.txtNewColada.setMinimumSize(QSize(98, 0))
        self.txtNewColada.setMaximumSize(QSize(100, 16777215))
        font16 = QFont()
        font16.setFamilies([u"Arial"])
        font16.setPointSize(16)
        font16.setItalic(False)
        self.txtNewColada.setFont(font16)
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

        self.gridLayout_5.addWidget(self.txtNewColada, 0, 2, 1, 1)

        self.label_22 = QLabel(self.frame_45)
        self.label_22.setObjectName(u"label_22")
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)
        self.label_22.setFont(font8)
        self.label_22.setStyleSheet(u"border:0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_22, 1, 0, 1, 1)

        self.txtObservaciones = QLineEdit(self.frame_45)
        self.txtObservaciones.setObjectName(u"txtObservaciones")
        sizePolicy9.setHeightForWidth(self.txtObservaciones.sizePolicy().hasHeightForWidth())
        self.txtObservaciones.setSizePolicy(sizePolicy9)
        self.txtObservaciones.setMinimumSize(QSize(102, 0))
        self.txtObservaciones.setFont(font8)
        self.txtObservaciones.setFocusPolicy(Qt.StrongFocus)
        self.txtObservaciones.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 1px 1px 1px 3px;\n"
"    min-width: 6em;\n"
"\n"
"\n"
"	background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.txtObservaciones, 1, 1, 1, 2)


        self.verticalLayout_14.addWidget(self.frame_45)

        self.frame_53 = QFrame(self.frameAddColada)
        self.frame_53.setObjectName(u"frame_53")
        sizePolicy2.setHeightForWidth(self.frame_53.sizePolicy().hasHeightForWidth())
        self.frame_53.setSizePolicy(sizePolicy2)
        self.frame_53.setStyleSheet(u"border-color: #D3D3D3;\n"
"border:0px;\n"
"background-color: #D3D3D3;\n"
"")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_53)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_66 = QFrame(self.frame_53)
        self.frame_66.setObjectName(u"frame_66")
        sizePolicy2.setHeightForWidth(self.frame_66.sizePolicy().hasHeightForWidth())
        self.frame_66.setSizePolicy(sizePolicy2)
        self.frame_66.setStyleSheet(u"QFrame{\n"
"border-radius:15px;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"border:0px;\n"
"}")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.pb_recortar = QPushButton(self.frame_66)
        self.pb_recortar.setObjectName(u"pb_recortar")
        sizePolicy2.setHeightForWidth(self.pb_recortar.sizePolicy().hasHeightForWidth())
        self.pb_recortar.setSizePolicy(sizePolicy2)
        font17 = QFont()
        font17.setFamilies([u"Arial"])
        font17.setPointSize(13)
        font17.setBold(True)
        font17.setItalic(False)
        font17.setUnderline(False)
        font17.setStrikeOut(False)
        self.pb_recortar.setFont(font17)
        self.pb_recortar.setStyleSheet(u"QPushButton{\n"
"	border-radius:9px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(240, 120, 14, 210);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 135, 29, 230);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(255, 135, 29, 255);\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color: rgba(0, 0, 0, 100);\n"
"}")

        self.horizontalLayout_27.addWidget(self.pb_recortar)


        self.verticalLayout_21.addWidget(self.frame_66)

        self.frame_65 = QFrame(self.frame_53)
        self.frame_65.setObjectName(u"frame_65")
        sizePolicy2.setHeightForWidth(self.frame_65.sizePolicy().hasHeightForWidth())
        self.frame_65.setSizePolicy(sizePolicy2)
        self.frame_65.setStyleSheet(u"QFrame{\n"
"border-radius:15px;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"border:0px;\n"
"}")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.pb_aceptar = QPushButton(self.frame_65)
        self.pb_aceptar.setObjectName(u"pb_aceptar")
        self.pb_aceptar.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.pb_aceptar.sizePolicy().hasHeightForWidth())
        self.pb_aceptar.setSizePolicy(sizePolicy2)
        self.pb_aceptar.setFont(font17)
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
"}\n"
"QPushButton:disabled{\n"
"	background-color: rgba(0, 0, 0, 100);\n"
"}")

        self.horizontalLayout_26.addWidget(self.pb_aceptar)

        self.progressBar = QProgressBar(self.frame_65)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy2.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy2)
        font18 = QFont()
        font18.setFamilies([u"Arial"])
        font18.setPointSize(15)
        font18.setBold(True)
        self.progressBar.setFont(font18)
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

        self.horizontalLayout_26.addWidget(self.progressBar)


        self.verticalLayout_21.addWidget(self.frame_65)


        self.verticalLayout_14.addWidget(self.frame_53)


        self.horizontalLayout.addWidget(self.frameAddColada)


        self.verticalLayout.addWidget(self.frameBottom)


        self.horizontalLayout_13.addWidget(self.frame_23)

        AdministratorWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdministratorWindow)

        QMetaObject.connectSlotsByName(AdministratorWindow)
    # setupUi

    def retranslateUi(self, AdministratorWindow):
        AdministratorWindow.setWindowTitle(QCoreApplication.translate("AdministratorWindow", u"Pantalla Principal - Abaxfem", None))
        self.pbVerCucharas.setText(QCoreApplication.translate("AdministratorWindow", u"Men\u00fa", None))
        self.label_3.setText("")
        self.labelUsername.setText(QCoreApplication.translate("AdministratorWindow", u"-", None))
        self.pbVerArchivos.setText(QCoreApplication.translate("AdministratorWindow", u"Ver Archivos", None))
        self.pbPerfiles.setText(QCoreApplication.translate("AdministratorWindow", u"Editar Perfiles", None))
        self.pbHistorial.setText(QCoreApplication.translate("AdministratorWindow", u"Historial", None))
        self.pbReporte.setText(QCoreApplication.translate("AdministratorWindow", u"Reporte", None))
        self.label.setText("")
        ___qtreewidgetitem = self.treeMenu.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("AdministratorWindow", u"Cuchara/Campa\u00f1a", None));
        self.pbAddCuchara.setText(QCoreApplication.translate("AdministratorWindow", u"A\u00f1adir Cuchara", None))
        self.pbDeleteCuchara.setText(QCoreApplication.translate("AdministratorWindow", u"Eliminar Cuchara", None))
        self.pbAddCampana.setText(QCoreApplication.translate("AdministratorWindow", u"A\u00f1adir Campa\u00f1a", None))
        self.pbDeleteCampana.setText(QCoreApplication.translate("AdministratorWindow", u"Eliminar Campa\u00f1a", None))
        self.label_2.setText("")
        self.nameHistory0.setText(QCoreApplication.translate("AdministratorWindow", u"-", None))
        self.dateHistory0.setText(QCoreApplication.translate("AdministratorWindow", u"-", None))
        self.label_6.setText("")
        self.nameHistory1.setText(QCoreApplication.translate("AdministratorWindow", u"-", None))
        self.dateHistory1.setText(QCoreApplication.translate("AdministratorWindow", u"-", None))
        self.label_9.setText("")
        self.nameHistory2.setText(QCoreApplication.translate("AdministratorWindow", u"-", None))
        self.dateHistory2.setText(QCoreApplication.translate("AdministratorWindow", u"-", None))
        self.label_12.setText("")
        self.nameHistory3.setText(QCoreApplication.translate("AdministratorWindow", u"-", None))
        self.dateHistory3.setText(QCoreApplication.translate("AdministratorWindow", u"-", None))
        self.label_15.setText("")
        self.nameHistory4.setText(QCoreApplication.translate("AdministratorWindow", u"-", None))
        self.dateHistory4.setText(QCoreApplication.translate("AdministratorWindow", u"-", None))
        self.label_23.setText(QCoreApplication.translate("AdministratorWindow", u"Riesgo Zona 1: ", None))
        self.txtZona1T.setText(QCoreApplication.translate("AdministratorWindow", u"-", None))
        self.label_24.setText(QCoreApplication.translate("AdministratorWindow", u"Riesgo Zona 2: ", None))
        self.txtZona2T.setText(QCoreApplication.translate("AdministratorWindow", u"-", None))
        self.label_25.setText(QCoreApplication.translate("AdministratorWindow", u"Riesgo Zona 3: ", None))
        self.txtZona3T.setText(QCoreApplication.translate("AdministratorWindow", u"-", None))
        self.label_4.setText(QCoreApplication.translate("AdministratorWindow", u"Vista Frontal", None))
        self.pbHistorialZonasF.setText(QCoreApplication.translate("AdministratorWindow", u"Historial", None))
        self.pbHistorialZonasT.setText(QCoreApplication.translate("AdministratorWindow", u"Historial", None))
        self.label_5.setText(QCoreApplication.translate("AdministratorWindow", u"Vista Trasera", None))
        self.label_30.setText(QCoreApplication.translate("AdministratorWindow", u"Riesgo Zona 1: ", None))
        self.txtZona1F.setText(QCoreApplication.translate("AdministratorWindow", u"-", None))
        self.label_29.setText(QCoreApplication.translate("AdministratorWindow", u"Riesgo Zona 2: ", None))
        self.txtZona2F.setText(QCoreApplication.translate("AdministratorWindow", u"-", None))
        self.label_31.setText(QCoreApplication.translate("AdministratorWindow", u"Riesgo Zona 3: ", None))
        self.txtZona3F.setText(QCoreApplication.translate("AdministratorWindow", u"-", None))
        self.labelColadas.setText(QCoreApplication.translate("AdministratorWindow", u"Coladas:", None))
        self.pbAddColada.setText(QCoreApplication.translate("AdministratorWindow", u"A\u00f1adir Colada", None))
        self.pbDeleteColada.setText(QCoreApplication.translate("AdministratorWindow", u"Eliminar Colada", None))
        self.label_7.setText(QCoreApplication.translate("AdministratorWindow", u"A\u00f1adir Nueva Colada", None))
        self.label_8.setText(QCoreApplication.translate("AdministratorWindow", u"Cuchara:", None))
        self.cbCuchara.setText("")
        self.label_10.setText(QCoreApplication.translate("AdministratorWindow", u"Campa\u00f1a:", None))
        self.txtCampana.setText("")
        self.label_17.setText(QCoreApplication.translate("AdministratorWindow", u"\u00daltima Colada:", None))
        self.txtUltimaColada.setText("")
        self.label_11.setText(QCoreApplication.translate("AdministratorWindow", u"\u00bfCambio de Linea de Escoria?", None))
        self.pbSiEscoria.setText(QCoreApplication.translate("AdministratorWindow", u"SI", None))
        self.pbNoEscoria.setText(QCoreApplication.translate("AdministratorWindow", u"NO", None))
        self.label_13.setText(QCoreApplication.translate("AdministratorWindow", u"Cara Frontal", None))
        self.label_14.setText(QCoreApplication.translate("AdministratorWindow", u"Termograf\u00eda", None))
        self.txtPathTermografiaF.setText(QCoreApplication.translate("AdministratorWindow", u"C: ... /Docs/", None))
#if QT_CONFIG(tooltip)
        self.pbFileDialog1.setToolTip(QCoreApplication.translate("AdministratorWindow", u"Importante! Los archivos deben estar guardados en la misma carpeta de la siguiente manera: (151F. jpg/xlsx) (151T. jpg/xlsx). Donde 151 es el n\u00famero de la colada.", None))
#endif // QT_CONFIG(tooltip)
        self.pbFileDialog1.setText(QCoreApplication.translate("AdministratorWindow", u"...", None))
        self.label_16.setText(QCoreApplication.translate("AdministratorWindow", u"Excel", None))
        self.txtPathExcelF.setText(QCoreApplication.translate("AdministratorWindow", u"C: ... /Docs/", None))
#if QT_CONFIG(tooltip)
        self.pbFileDialog2.setToolTip(QCoreApplication.translate("AdministratorWindow", u"Importante! Los archivos deben estar guardados en la misma carpeta de la siguiente manera: (151F. jpg/xlsx) (151T. jpg/xlsx). Donde 151 es el n\u00famero de la colada.", None))
#endif // QT_CONFIG(tooltip)
        self.pbFileDialog2.setText(QCoreApplication.translate("AdministratorWindow", u"...", None))
        self.label_18.setText(QCoreApplication.translate("AdministratorWindow", u"Cara Trasera", None))
        self.label_19.setText(QCoreApplication.translate("AdministratorWindow", u"Termograf\u00eda", None))
        self.txtPathTermografiaT.setText(QCoreApplication.translate("AdministratorWindow", u"C: ... /Docs/", None))
#if QT_CONFIG(tooltip)
        self.pbFileDialog3.setToolTip(QCoreApplication.translate("AdministratorWindow", u"Importante! Los archivos deben estar guardados en la misma carpeta de la siguiente manera: (151F. jpg/xlsx) (151T. jpg/xlsx). Donde 151 es el n\u00famero de la colada.", None))
#endif // QT_CONFIG(tooltip)
        self.pbFileDialog3.setText(QCoreApplication.translate("AdministratorWindow", u"...", None))
        self.label_20.setText(QCoreApplication.translate("AdministratorWindow", u"Excel", None))
        self.txtPathExcelT.setText(QCoreApplication.translate("AdministratorWindow", u"C: ... /Docs/", None))
#if QT_CONFIG(tooltip)
        self.pbFileDialog4.setToolTip(QCoreApplication.translate("AdministratorWindow", u"Importante! Los archivos deben estar guardados en la misma carpeta de la siguiente manera: (151F. jpg/xlsx) (151T. jpg/xlsx). Donde 151 es el n\u00famero de la colada.", None))
#endif // QT_CONFIG(tooltip)
        self.pbFileDialog4.setText(QCoreApplication.translate("AdministratorWindow", u"...", None))
        self.label_21.setText(QCoreApplication.translate("AdministratorWindow", u"# Nueva Colada:", None))
        self.txtNewColada.setText("")
        self.label_22.setText(QCoreApplication.translate("AdministratorWindow", u"Obs:", None))
        self.txtObservaciones.setInputMask("")
        self.txtObservaciones.setText("")
        self.pb_recortar.setText(QCoreApplication.translate("AdministratorWindow", u"Recortar Imagen", None))
        self.pb_aceptar.setText(QCoreApplication.translate("AdministratorWindow", u"A\u00f1adir Colada", None))
    # retranslateUi

