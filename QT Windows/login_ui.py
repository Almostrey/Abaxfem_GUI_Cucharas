# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QWidget)
import resources_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.setWindowModality(Qt.NonModal)
        LoginWindow.resize(650, 400)
        LoginWindow.setMinimumSize(QSize(650, 400))
        LoginWindow.setMaximumSize(QSize(650, 400))
        font = QFont()
        font.setFamilies([u"Adobe Devanagari"])
        LoginWindow.setFont(font)
        LoginWindow.setMouseTracking(False)
        LoginWindow.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/Images/ResourcesFolder/Imagenes/Logo_Lineas.png", QSize(), QIcon.Normal, QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setWindowOpacity(1.000000000000000)
        LoginWindow.setAutoFillBackground(True)
        LoginWindow.setStyleSheet(u"")
        LoginWindow.setInputMethodHints(Qt.ImhNone)
        LoginWindow.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        LoginWindow.setAnimated(True)
        LoginWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"\n"
"background-color : rgba(255, 255, 255, 240);\n"
"border-radius:30;\n"
"border:1px solid gray;\n"
"\n"
"}")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(62, 80, 200, 200))
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: rgba(180, 180, 180, 255);\n"
"border-radius:100;\n"
"	image: url(:/Images/ResourcesFolder/Imagenes/Logo_Lineas.png);\n"
"border:0px;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(367, 60, 241, 31))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(23)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setKerning(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border:0px;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)
        self.txt_username = QLineEdit(self.centralwidget)
        self.txt_username.setObjectName(u"txt_username")
        self.txt_username.setGeometry(QRect(410, 130, 191, 41))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(16)
        font2.setBold(False)
        self.txt_username.setFont(font2)
        self.txt_username.setStyleSheet(u"border-radius:15px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(190, 190, 190);\n"
"border:0px;")
        self.txt_username.setMaxLength(16)
        self.txt_username.setCursorPosition(0)
        self.txt_username.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txt_username.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(386, 140, 21, 21))
        self.label_2.setStyleSheet(u"image: url(:/Icons/ResourcesFolder/featherIcons/user.svg);\n"
"background-color: rgb(190, 190, 190);\n"
"border-radius: 10px;\n"
"border:0px;")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(380, 130, 221, 41))
        self.frame_2.setStyleSheet(u"border-radius:15px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(190, 190, 190);\n"
"border:0px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(380, 200, 221, 41))
        self.frame_3.setStyleSheet(u"border-radius:15px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(190, 190, 190);\n"
"border:0px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.txt_password = QLineEdit(self.centralwidget)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setGeometry(QRect(410, 200, 191, 41))
        self.txt_password.setFont(font2)
        self.txt_password.setStyleSheet(u"border-radius:15px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(190, 190, 190);\n"
"border:0px;")
        self.txt_password.setMaxLength(16)
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setCursorPosition(0)
        self.txt_password.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txt_password.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(386, 210, 21, 21))
        self.label_3.setStyleSheet(u"image: url(:/Icons/ResourcesFolder/featherIcons/lock.svg);\n"
"background-color: rgb(190, 190, 190);\n"
"border-radius: 10px;\n"
"border:0px;")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(37, 240, 251, 71))
        self.frame_4.setStyleSheet(u"image: url(:/Images/ResourcesFolder/Imagenes/Logo_Letras.png);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pb_acceder = QPushButton(self.centralwidget)
        self.pb_acceder.setObjectName(u"pb_acceder")
        self.pb_acceder.setGeometry(QRect(380, 270, 221, 41))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.pb_acceder.setFont(font3)
        self.pb_acceder.setStyleSheet(u"QPushButton{\n"
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
        self.label_4.setGeometry(QRect(350, 350, 251, 20))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(11)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_webpage = QLabel(self.centralwidget)
        self.lbl_webpage.setObjectName(u"lbl_webpage")
        self.lbl_webpage.setGeometry(QRect(459, 370, 141, 20))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(11)
        font5.setUnderline(True)
        self.lbl_webpage.setFont(font5)
        self.lbl_webpage.setStyleSheet(u"color: rgb(35, 170, 242);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.lbl_webpage.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_webpage.setOpenExternalLinks(True)
        self.pb_exit = QPushButton(self.centralwidget)
        self.pb_exit.setObjectName(u"pb_exit")
        self.pb_exit.setGeometry(QRect(610, 13, 21, 21))
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
        self.pb_minimized = QPushButton(self.centralwidget)
        self.pb_minimized.setObjectName(u"pb_minimized")
        self.pb_minimized.setGeometry(QRect(580, 13, 21, 21))
        self.pb_minimized.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"image: url(:/Icons/ResourcesFolder/featherIcons/divide-square.svg);\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(200, 200, 200, 120);\n"
"	border-radius: 6px\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(180, 180, 180, 150);\n"
"	border-radius: 6px\n"
"}")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.frame_2.raise_()
        self.label.raise_()
        self.txt_username.raise_()
        self.label_2.raise_()
        self.frame_3.raise_()
        self.txt_password.raise_()
        self.label_3.raise_()
        self.frame.raise_()
        self.frame_4.raise_()
        self.pb_acceder.raise_()
        self.label_4.raise_()
        self.pb_exit.raise_()
        self.pb_minimized.raise_()
        self.lbl_webpage.raise_()

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Iniciar Sesi\u00f3n - Abaxfem", None))
#if QT_CONFIG(tooltip)
        LoginWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        LoginWindow.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.frame.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("LoginWindow", u"Inicio de Sesi\u00f3n", None))
        self.txt_username.setText("")
        self.txt_username.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Usuario", None))
        self.label_2.setText("")
        self.txt_password.setText("")
        self.txt_password.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Contrase\u00f1a", None))
        self.label_3.setText("")
        self.pb_acceder.setText(QCoreApplication.translate("LoginWindow", u"Acceder", None))
        self.label_4.setText(QCoreApplication.translate("LoginWindow", u"Abaxfem Simulaci\u00f3n e Ingenier\u00eda S.A.", None))
        self.lbl_webpage.setText(QCoreApplication.translate("LoginWindow", u"<a href=\"http://www.abaxfem.com\">www.abaxfem.com</a>", None))
        self.pb_exit.setText("")
        self.pb_minimized.setText("")
    # retranslateUi

