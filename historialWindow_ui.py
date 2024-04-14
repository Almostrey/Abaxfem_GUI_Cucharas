# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'historialWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QMainWindow,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)
import resources_rc

class Ui_historialWindow(object):
    def setupUi(self, historialWindow):
        if not historialWindow.objectName():
            historialWindow.setObjectName(u"historialWindow")
        historialWindow.resize(600, 350)
        historialWindow.setMinimumSize(QSize(600, 350))
        historialWindow.setMaximumSize(QSize(600, 350))
        icon = QIcon()
        icon.addFile(u":/Images/ResourcesFolder/Imagenes/Logo_Lineas.png", QSize(), QIcon.Normal, QIcon.Off)
        historialWindow.setWindowIcon(icon)
        historialWindow.setStyleSheet(u"")
        historialWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(historialWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(600, 350))
        self.centralwidget.setMaximumSize(QSize(600, 350))
        self.centralwidget.setStyleSheet(u"")
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
        icon2.addFile(u":/Icons/ResourcesFolder/featherIcons/briefcase.svg", QSize(), QIcon.Normal, QIcon.Off)
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(12)
        font1.setBold(False)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        __qtablewidgetitem1.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem1.setIcon(icon2);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        icon3 = QIcon()
        icon3.addFile(u":/Icons/ResourcesFolder/featherIcons/at-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        __qtablewidgetitem2.setBackground(QColor(217, 225, 243));
        __qtablewidgetitem2.setForeground(brush);
        __qtablewidgetitem2.setIcon(icon3);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        icon4 = QIcon()
        icon4.addFile(u":/Icons/ResourcesFolder/featherIcons/calendar.svg", QSize(), QIcon.Normal, QIcon.Off)
        font2 = QFont()
        font2.setFamilies([u"Rockwell"])
        font2.setPointSize(12)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        __qtablewidgetitem3.setIcon(icon4);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        icon5 = QIcon()
        icon5.addFile(u":/Icons/ResourcesFolder/featherIcons/clock.svg", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        __qtablewidgetitem4.setBackground(QColor(217, 225, 243));
        __qtablewidgetitem4.setIcon(icon5);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 600, 350))
        font3 = QFont()
        font3.setFamilies([u"Rockwell"])
        font3.setPointSize(10)
        font3.setWeight(QFont.Medium)
        self.tableWidget.setFont(font3)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet(u"QHeaderView:section\n"
"{\n"
"background-color: rgb(237, 245, 255);\n"
"}")
        self.tableWidget.setLineWidth(2)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        historialWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(historialWindow)

        QMetaObject.connectSlotsByName(historialWindow)
    # setupUi

    def retranslateUi(self, historialWindow):
        historialWindow.setWindowTitle(QCoreApplication.translate("historialWindow", u"Historial de Inicios de Sesi\u00f3n - Abaxfem", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("historialWindow", u"Usuario", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("historialWindow", u"Funci\u00f3n", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("historialWindow", u"Nombre", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("historialWindow", u"Fecha", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("historialWindow", u"Hora", None));
    # retranslateUi

