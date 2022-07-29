# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Variables.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Variables(object):
    def setupUi(self, Variables):
        Variables.setObjectName("Variables")
        Variables.resize(683, 515)
        self.centralwidget = QtWidgets.QWidget(Variables)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 30, 151, 71))
        self.label.setStyleSheet("border-image: url(:/logo/logo-sonda-final.png);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/logo/logo-sonda-final.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 210, 211, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 260, 211, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 310, 211, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 360, 211, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(430, 280, 211, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 130, 211, 61))
        self.label_2.setObjectName("label_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 210, 211, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(430, 350, 211, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        Variables.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Variables)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 683, 21))
        self.menubar.setObjectName("menubar")
        Variables.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Variables)
        self.statusbar.setObjectName("statusbar")
        Variables.setStatusBar(self.statusbar)

        self.retranslateUi(Variables)
        QtCore.QMetaObject.connectSlotsByName(Variables)

    def retranslateUi(self, Variables):
        _translate = QtCore.QCoreApplication.translate
        Variables.setWindowTitle(_translate("Variables", "MainWindow"))
        self.pushButton.setText(_translate("Variables", "Personal"))
        self.pushButton_2.setText(_translate("Variables", "Otro OPEX"))
        self.pushButton_3.setText(_translate("Variables", "OPEX 1T"))
        self.pushButton_4.setText(_translate("Variables", "CAPEX"))
        self.pushButton_5.setText(_translate("Variables", "Parametros "))
        self.label_2.setText(_translate("Variables", "Diseño del modelo de costos"))
        self.pushButton_6.setText(_translate("Variables", "Información del cliente "))
        self.pushButton_7.setText(_translate("Variables", "Ayudas "))

import logo_rc
