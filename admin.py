# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boton = QtWidgets.QPushButton(self.centralwidget)
        self.boton.setGeometry(QtCore.QRect(80, 80, 171, 71))
        self.boton.setObjectName("boton")
        self.boton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.boton_2.setGeometry(QtCore.QRect(330, 80, 171, 71))
        self.boton_2.setObjectName("boton_2")
        self.boton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.boton_3.setGeometry(QtCore.QRect(570, 80, 171, 71))
        self.boton_3.setObjectName("boton_3")
        self.boton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.boton_4.setGeometry(QtCore.QRect(330, 230, 171, 71))
        self.boton_4.setObjectName("boton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.boton.setText(_translate("MainWindow", "Ver reportes"))
        self.boton_2.setText(_translate("MainWindow", "Establecer Parametros"))
        self.boton_3.setText(_translate("MainWindow", "Usuarios "))
        self.boton_4.setText(_translate("MainWindow", "Regresar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
