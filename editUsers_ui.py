# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editUsers.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)
import resources_rc

class Ui_editUsersWindow(object):
    def setupUi(self, editUsersWindow):
        if not editUsersWindow.objectName():
            editUsersWindow.setObjectName(u"editUsersWindow")
        editUsersWindow.resize(600, 350)
        icon = QIcon()
        icon.addFile(u":/Images/ResourcesFolder/Imagenes/Logo_Lineas.png", QSize(), QIcon.Normal, QIcon.Off)
        editUsersWindow.setWindowIcon(icon)
        editUsersWindow.setStyleSheet(u"background-color: rgba(255, 255, 255, 255)")
        self.centralwidget = QWidget(editUsersWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        icon1 = QIcon()
        icon1.addFile(u":/Icons/ResourcesFolder/featherIcons/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font = QFont()
        font.setFamilies([u"Rockwell"])
        font.setPointSize(12)
        font.setWeight(QFont.Medium)
        font.setStyleStrategy(QFont.PreferDefault)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setBackground(QColor(217, 225, 243));
        __qtablewidgetitem.setForeground(brush);
        __qtablewidgetitem.setIcon(icon1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        icon2 = QIcon()
        icon2.addFile(u":/Icons/ResourcesFolder/featherIcons/unlock.svg", QSize(), QIcon.Normal, QIcon.Off)
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(12)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        __qtablewidgetitem1.setBackground(QColor(217, 225, 243));
        __qtablewidgetitem1.setIcon(icon2);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        icon3 = QIcon()
        icon3.addFile(u":/Icons/ResourcesFolder/featherIcons/briefcase.svg", QSize(), QIcon.Normal, QIcon.Off)
        font2 = QFont()
        font2.setFamilies([u"Rockwell"])
        font2.setPointSize(12)
        font2.setBold(False)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        __qtablewidgetitem2.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem2.setIcon(icon3);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        icon4 = QIcon()
        icon4.addFile(u":/Icons/ResourcesFolder/featherIcons/at-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        __qtablewidgetitem3.setBackground(QColor(217, 225, 243));
        __qtablewidgetitem3.setForeground(brush);
        __qtablewidgetitem3.setIcon(icon4);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        icon5 = QIcon()
        icon5.addFile(u":/Icons/ResourcesFolder/featherIcons/calendar.svg", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        __qtablewidgetitem4.setIcon(icon5);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 600, 280))
        font3 = QFont()
        font3.setFamilies([u"Rockwell"])
        font3.setPointSize(10)
        font3.setWeight(QFont.Medium)
        self.tableWidget.setFont(font3)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet(u"QHeaderView:section\n"
"{\n"
"background-color: rgb(237, 245, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setLineWidth(2)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.pbAddUser = QPushButton(self.centralwidget)
        self.pbAddUser.setObjectName(u"pbAddUser")
        self.pbAddUser.setGeometry(QRect(70, 297, 120, 30))
        font4 = QFont()
        font4.setFamilies([u"Rockwell"])
        font4.setPointSize(11)
        self.pbAddUser.setFont(font4)
        self.pbAddUser.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(230, 110, 4, 220);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 140, 34, 240);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(235, 115, 9, 255);\n"
"}")
        self.pbSaveAndExit = QPushButton(self.centralwidget)
        self.pbSaveAndExit.setObjectName(u"pbSaveAndExit")
        self.pbSaveAndExit.setGeometry(QRect(410, 297, 120, 30))
        self.pbSaveAndExit.setFont(font4)
        self.pbSaveAndExit.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(230, 110, 4, 220);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 140, 34, 240);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(235, 115, 9, 255);\n"
"}")
        self.pbDeleteRow = QPushButton(self.centralwidget)
        self.pbDeleteRow.setObjectName(u"pbDeleteRow")
        self.pbDeleteRow.setGeometry(QRect(240, 297, 120, 30))
        self.pbDeleteRow.setFont(font4)
        self.pbDeleteRow.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(230, 110, 4, 220);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 140, 34, 240);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(235, 115, 9, 255);\n"
"}")
        editUsersWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(editUsersWindow)

        QMetaObject.connectSlotsByName(editUsersWindow)
    # setupUi

    def retranslateUi(self, editUsersWindow):
        editUsersWindow.setWindowTitle(QCoreApplication.translate("editUsersWindow", u"Editar Cuentas de Usuario - Abaxfem", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("editUsersWindow", u"Usuario", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("editUsersWindow", u"Contrase\u00f1a", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("editUsersWindow", u"Funci\u00f3n", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("editUsersWindow", u"Nombre", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("editUsersWindow", u"Creado el", None));
        self.pbAddUser.setText(QCoreApplication.translate("editUsersWindow", u"A\u00f1adir Usuario", None))
        self.pbSaveAndExit.setText(QCoreApplication.translate("editUsersWindow", u"Guardar y Salir", None))
        self.pbDeleteRow.setText(QCoreApplication.translate("editUsersWindow", u"Eliminar Usuario", None))
    # retranslateUi

