# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VideoLogoWindow.ui'
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
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QWidget)
import resources_rc

class Ui_Video_Logo_Window(object):
    def setupUi(self, Video_Logo_Window):
        if not Video_Logo_Window.objectName():
            Video_Logo_Window.setObjectName(u"Video_Logo_Window")
        Video_Logo_Window.resize(400, 292)
        icon = QIcon()
        icon.addFile(u":/Images/ResourcesFolder/Imagenes/Logo_Lineas.png", QSize(), QIcon.Normal, QIcon.Off)
        Video_Logo_Window.setWindowIcon(icon)
        Video_Logo_Window.setStyleSheet(u"border-radius:30;")
        self.centralwidget = QWidget(Video_Logo_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:30;\n"
"")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 400, 300))
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:30;")
        self.VideoPlace = QVideoWidget(self.widget)
        self.VideoPlace.setObjectName(u"VideoPlace")
        self.VideoPlace.setGeometry(QRect(0, -3, 400, 301))
        self.VideoPlace.setStyleSheet(u"border: 0px solid #00007f;\n"
"border-radius:30;")
        Video_Logo_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Video_Logo_Window)

        QMetaObject.connectSlotsByName(Video_Logo_Window)
    # setupUi

    def retranslateUi(self, Video_Logo_Window):
        Video_Logo_Window.setWindowTitle(QCoreApplication.translate("Video_Logo_Window", u"Abaxfem", None))
    # retranslateUi

