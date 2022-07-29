# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 12:02:51 2022

@author: oscar
"""

"""
Created on Thu Mar 17 14:26:59 2022

@author: OSCAR DAVID JIMENEZ BONILLA     1015478830 SONDA COLOMBIA 
"""
import tkinter as tk
from pandastable import Table, TableModel
import numpy as np
import numpy_financial as npf
import pathlib
import os
from PyQt5 import QtCore

import pandas as pd
from PyQt5.QtWidgets import (QApplication, QTableView)
from PyQt5.QtCore import (QAbstractTableModel, Qt)
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QLCDNumber
from PyQt5.uic import loadUi
qtCreatorFile = "principal.ui" 
# para crear el PDF
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
w, h = A4
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
from datetime import date
from datetime import datetime
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class Variables(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase de las variables 
 
    def __init__(self,parent=None):
        super(Variables, self).__init__(parent)
        loadUi('Variables.ui', self)
        self.boton_infocliente.clicked.connect(self.infocliente)# boton abre info cliete
        self.boton_parametros.clicked.connect(self.Parametros)# boton abre info parametros
        self.boton_ayudas.clicked.connect(self.ayudas)# boton abre info parametros
        self.boton_salir.clicked.connect(self.close)# boton salir
        self.boton_agregar.clicked.connect(self.agregar)# boton salir 
        self.boton.clicked.connect(self.generar)# GENERAR
        self.boton_2.clicked.connect(self.generarofer)# GENERAR
    
    def generarofer(self):
         self.hide()
         otraventana=Tipooferta(self)
         otraventana.show()
    def infocliente(self):
         self.hide()
         otraventana=infocliente(self)
         otraventana.show()
    def Parametros(self):
         self.hide()
         otraventana=Parametros(self)
         otraventana.show()
    def ayudas(self):
         self.hide()
         otraventana=ayudas(self)
         otraventana.show()
    def agregar(self):
        self.hide()
        otraventana=agregar(self)
        otraventana.show()
    def generar(self):
        a=sum(total_capex)
        b=sum(total_opex1t)
        c=sum(total_otroopex)
        d=sum(total_personal)
        a1=(a/(1-(riesgototal[0]/100)-(tasa_capex[0]/100)-(imprevistos_1[0]/100)))*(1+(ipc[0]/100))
        b1=(b/(1-(riesgototal[0]/100)-(tasa_opex1t[0]/100)-  (imprevistos_1[0]/100)))*(1+(ipc[0]/100))
        c1=(c/(1-(riesgototal[0]/100)-(tasa_otroopex[0]/100)-(imprevistos_1[0]/100)))*(1+(ipc[0]/100))
        d1=(d/(1-(riesgototal[0]/100)-(tasa_personal[0]/100)-(imprevistos_1[0]/100)))*(1+(ipc[0]/100))
        
        wb = load_workbook(filesheet)

        # Seleccionamos el archivo
        sheet = wb.active

        # Ingresamos el valor 56 en la celda 'A1'
        sheet['A4'] = "VALOR Mensual"
        # Ingresamos el valor 1845 en la celda 'B3'
        sheet['B2']=today
        sheet['B3'] = "Capex"
        sheet['C3'] = "Otro opex"
        sheet['D3'] = "Opex 1t"
        sheet['E3'] = "Personal"
        sheet['B4'] = a1
        sheet['C4'] = c1
        sheet['D4'] = b1
        sheet['E4'] = d1
        sheet['A5'] = "TOTAL mensual"
        sheet['B5'] = (a1+b1+c1+d1)

        sheet['A6'] = "TOTAL PROYECTO"
        sheet['B6'] = (a1+b1+c1+d1)*mesesfact[0]
        # 
        sheet['A10'] = "Preventa"
        sheet['B10'] = preventa[0]
        sheet['A11'] = "Comercial"
        sheet['B11'] = comercial[0]
        sheet['B17'] = ipc[0]
        sheet['B18'] = riesgototal[0]
        sheet['B19'] = imprevistos_1[0]
        sheet['B20'] = crm[0]
        sheet['B21'] = linea[0]
        
        #vamos a crear el segundo excel de la base de datos 
        # Guardamos el archivo con los cambios
        wb.save(filesheet)
        
        os.startfile(miarchivo)
        os.startfile(mipdf)