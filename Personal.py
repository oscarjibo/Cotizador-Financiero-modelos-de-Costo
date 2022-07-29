# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Personal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Personal(object):
    def setupUi(self, Personal):
        Personal.setObjectName("Personal")
        Personal.resize(480, 388)
        self.centralwidget = QtWidgets.QWidget(Personal)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 320, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 111, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 47, 13))
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(180, 30, 251, 21))
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(180, 80, 251, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(180, 120, 71, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(180, 160, 71, 21))
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 210, 47, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 260, 121, 16))
        self.label_6.setObjectName("label_6")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(180, 210, 71, 21))
        self.spinBox_3.setObjectName("spinBox_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 260, 251, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.tablapersonal = QtWidgets.QListWidget(self.centralwidget)
        self.tablapersonal.setGeometry(QtCore.QRect(50, 370, 371, 91))
        self.tablapersonal.setObjectName("tablapersonal")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 470, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        Personal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Personal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        Personal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Personal)
        self.statusbar.setObjectName("statusbar")
        Personal.setStatusBar(self.statusbar)

        self.retranslateUi(Personal)
        QtCore.QMetaObject.connectSlotsByName(Personal)

    def retranslateUi(self, Personal):
        _translate = QtCore.QCoreApplication.translate
        Personal.setWindowTitle(_translate("Personal", "MainWindow"))
        self.pushButton.setText(_translate("Personal", "Añadir "))
        self.label.setText(_translate("Personal", "Rol"))
        self.label_2.setText(_translate("Personal", "Perfil"))
        self.label_3.setText(_translate("Personal", "Meses ejecutados "))
        self.label_4.setText(_translate("Personal", "Cantidad "))
        self.comboBox.setItemText(0, _translate("Personal", "Analista"))
        self.comboBox.setItemText(1, _translate("Personal", "Analista +"))
        self.comboBox.setItemText(2, _translate("Personal", "Profesional Junior"))
        self.label_5.setText(_translate("Personal", "Recargos "))
        self.label_6.setText(_translate("Personal", "Ubicación del recurso"))
        self.comboBox_2.setItemText(0, _translate("Personal", "SONDA Portatil"))
        self.pushButton_2.setText(_translate("Personal", "LISTO "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Personal = QtWidgets.QMainWindow()
    ui = Ui_Personal()
    ui.setupUi(Personal)
    Personal.show()
    sys.exit(app.exec_())

