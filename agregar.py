# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 388)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boton_opex1t = QtWidgets.QPushButton(self.centralwidget)
        self.boton_opex1t.setGeometry(QtCore.QRect(250, 60, 191, 101))
        self.boton_opex1t.setObjectName("boton_opex1t")
        self.boton_capex = QtWidgets.QPushButton(self.centralwidget)
        self.boton_capex.setGeometry(QtCore.QRect(250, 190, 191, 101))
        self.boton_capex.setObjectName("boton_capex")
        self.boton_personal = QtWidgets.QPushButton(self.centralwidget)
        self.boton_personal.setGeometry(QtCore.QRect(40, 60, 191, 101))
        self.boton_personal.setObjectName("boton_personal")
        self.boton_otroopex = QtWidgets.QPushButton(self.centralwidget)
        self.boton_otroopex.setGeometry(QtCore.QRect(40, 190, 191, 101))
        self.boton_otroopex.setObjectName("boton_otroopex")
        self.boton_regresar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_regresar.setGeometry(QtCore.QRect(200, 310, 91, 31))
        self.boton_regresar.setObjectName("boton_regresar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_opex1t.setText(_translate("MainWindow", "OPEX 1T"))
        self.boton_capex.setText(_translate("MainWindow", "CAPEX"))
        self.boton_personal.setText(_translate("MainWindow", "Personal"))
        self.boton_otroopex.setText(_translate("MainWindow", "Otro OPEX"))
        self.boton_regresar.setText(_translate("MainWindow", "Regresar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

