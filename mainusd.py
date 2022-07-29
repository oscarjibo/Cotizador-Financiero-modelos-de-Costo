# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 12:31:34 2022

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

#Día actual
today = date.today()
c = canvas.Canvas("oferta.pdf", pagesize=A4)
s="SONDA Este  documento hace parte del Sistema de Gestión de Calidad de SONDA certificado por SGS bajo la NTC"
g="ISO 9001:2015 Este documento y la información contenida en él hacen parte y son propiedad de SONDA. "
g1="Ninguna parte de este documento puede ser utilizada, reproducida o transmitida en ninguna forma,"
c.drawString(50, h - 50, s+g+g1)
c.showPage()
c.save()




# para crear el excel

# importamos el submodulo "Workbook"


# ruta de nuestro archivo
filesheet = ".\ejercicio.xlsx"
miarchivo =".\ejercicio.xlsx"
archivo_adicion=".\\adicion.docx"
archivo_nuevo=".\\nuevo.docx"

archivo_reportes=".\df.xlsx"
mipdf=".\oferta.pdf"
#datos nombres
preventa=[]
comercial=[]
cliente=[]
# DATOS 
tasa_financiacion_general=[]
tasa_capex=[]
tasa_opex1t=[]
tasa_otroopex=[]
tasa_personal=[]
mesesfact=[]
TRM=[]
TRM_SERV=[]
riesgototal=[]
imprevistos_1=[]
ipc=[]
crm=[]
linea=["MDS"]
#empiezo a crear mi dataframe 
#TOTALEs
total_personal=[0]
total_otroopex=[0]
total_opex1t=[0]
total_capex=[0]
# datos para mi datafrma

articulos=[]
costos=[]
cantidades=[]
tipo=[]
seguro=[]
componente=[]
componente_status=[]

Analista1=1866052
Analista2=2428629
Analista3=3151944
Profesional1=4339889
Profesional2=5384677
Profesional3=7233148
Profesional4=9322724
Profesional5=11251564
Profesional6=12858930
Profesional7=14466297
Profesional8=21170544
Experto=21826484

En1=651900
En2=296150
En3=647500
En4=291750
En5=225800
En6=581550
En7=392630
En8=196315
En9=130877
En10=80550



#para mi dataframe



Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Ventana1(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.boton_iniciar.clicked.connect(self.Variables) # abro la ventana de variables
        self.boton_salir.clicked.connect(self.close)# boton salir 
        self.boton_iniciar_2.clicked.connect(self.admin) # abro la ventana de variables
   
    def Variables(self):
         self.hide()
         otraventana=Variables(self)
         otraventana.show()
         pre=self.lista_gente.currentText()
         pcom=self.lista_gente_2.currentText()
         preventa.append(pre)
         comercial.append(pcom)
    def admin(self):
        self.hide()
        otraventana=Admin(self)
        otraventana.show()
class Admin(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase de Opex 1t 
    def __init__(self,parent=None):
        super(Admin, self).__init__(parent)
        loadUi('admin.ui', self)
        self.boton_4.clicked.connect(self.Variables)#boton regresa
        self.boton_3.clicked.connect(self.usuarios)#boton regresa
        #self.boton.clicked.connect(self.reportes)#boton regresa
        
    
    def Variables(self):
         self.hide()
         otraventana=Variables(self)
         otraventana.show()
    def usuarios(self):
        os.startfile(archivo_usuarios)
    def reportes(self):
        os.startfile(archivo_reportes)
        
   

class Personal(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase del personal
 
    def __init__(self,parent=None):
        super(Personal, self).__init__(parent)
        loadUi('Personal.ui', self)
        self.boton_regresar.clicked.connect(self.agregar)#boton abre agregar
        self.boton_regresar1.clicked.connect(self.anadir)#boton abre agregar

    
    def agregar(self):
        self.hide()
        otraventana=agregar(self)
        otraventana.show() 
    def anadir(self):
        rol=self.c1.toPlainText()
        perfil=self.c3.currentText()
        meses_ejecutados=self.c2.value()
        cantidad=self.c4.value()
        recargos=self.c5.value()
        ubicacion=self.c6.currentText()
        mesesno=self.c22.value()
        costo=1
        print("#####")
        print(ubicacion)
        print(perfil)
        if perfil=="Analista":
            costo=Analista1
        elif perfil=="Analista +":
            costo=Analista2
        elif perfil=="Analista ++":
            costo=Analista3
        elif perfil=="Profesional Junior":
            costo=Profesional1
        elif perfil=="Profesional Pleno":
            costo=Profesional2
        elif perfil=="Profesional Pleno +":
            costo=Profesional3
        elif perfil=="Profesional Especialista ":
            costo=Profesional4
        elif perfil=="Profesional Especialista +":
            costo=Profesional5
        elif perfil=="Profesional Especialista ++":
            costo=Profesional6
        elif perfil=="Profesional Senior ":
            costo=Profesional7
        elif perfil=="Profesional Senior +":
            costo=Profesional8
        elif perfil=="Experto ":
            costo=Experto
        if ubicacion=="En Sonda Pc":
            ubi=En1
        elif ubicacion=="En Cliente Pc":
            ubi=En2
        elif ubicacion=="SONDA Portatil":
            ubi=En3
        elif ubicacion=="Cliente Portatil":
            ubi=En4
        elif ubicacion=="En cliente sin equipo ":
            ubi=En5
        elif ubicacion=="En Sonda sin equipo":
            ubi=En6
        elif ubicacion=="Zona Franca RU1":
            ubi=En7
        elif ubicacion=="Zona Franca RU2":
            ubi=En8
        elif ubicacion=="Zona Franca RU3":
            ubi=En9
        elif ubicacion=="Field Services EUS":
            ubi=En10
        P=(costo)+ubi
        print("#####")
        print("costo mensual personal")
        print(P)
        cuota=P*cantidad*(meses_ejecutados+mesesno)/mesesfact[0]
        print(cuota)
        cuota_total_personal_=npf.pmt(tasa_financiacion_general[0]/100,mesesfact[0]/(meses_ejecutados+mesesno),-1*P*cantidad,0,1)
        
        print(cuota_total_personal_)
        total_personal.append(cuota_total_personal_)
        articulos.append(rol)
        cantidades.append(cantidad)
        costos.append(cuota_total_personal_)
        tipo.append("personal")# aca empiezo a darle con los precios del personal 
        seguro.append("no")
        c=componente_status[-1]
        componente.append(c)
        componente_status.pop(-1)
class Otroopex(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase de otro opex
 
    def __init__(self,parent=None):
        super(Otroopex, self).__init__(parent)
        loadUi('Otroopex.ui', self)
        self.boton_regresar.clicked.connect(self.agregar)#boton abre personal
        self.boton_anadir.clicked.connect(self.anadir)
        
    
    def agregar(self):
        self.hide()
        otraventana=agregar(self)
        otraventana.show()
    def anadir(self):
    
        item=self.textEdit.toPlainText()
        meses_ejecutado=self.spinBox.value()
        cantidad=self.c.value()
        costo=self.c1.value()   
        iva=self.i.value()
        trm_servicio=self.c3.isChecked()
        if trm_servicio==True:
            costo=TRM_SERV[0]
        unit=costo*(1+iva/100)
        
        cuota_mensual_otropex=npf.pmt(tasa_financiacion_general[0]/100,mesesfact[0]/meses_ejecutado,-1*cantidad*unit,0,1)
        total_otroopex.append(cuota_mensual_otropex)
        articulos.append(item)
        cantidades.append(cantidad)
        costos.append(cuota_mensual_otropex)
        tipo.append("otroopex")
        seguro.append("no")
        c=componente_status[-1]
        componente.append(c)
        componente_status.pop(-1)
class opex1t(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase de Opex 1t 
 
    def __init__(self,parent=None):
        super(opex1t, self).__init__(parent)
        loadUi('opex1t.ui', self)
        self.boton_regresar.clicked.connect(self.agregar)#boton abre personal
        self.anadi.clicked.connect(self.anadir)
    def agregar(self):
        self.hide()
        otraventana=agregar(self)
        otraventana.show()
    def anadir(self):
    
        item=self.textEdit.toPlainText()
        veces_ejecutado=self.v.value()
        cantidad=self.c.value()
        nacio=self.n.value()
        costo=self.c1.value()
        iva=self.i.value()
        #p=(iva*costo)+costo
        #q=1-riesgototal[0]/100-tasa_otroopex[0]/100-imprevistos_1[0]/100
        
        #print("costo opex 1t total ")
        #tot=(p/q)
        #tot=round(tot,2)
        #print(tot)
        print("costo mensual opex 1t")
        #print(tot/mesesfact[-1])
        #total_opex1t.append(tot)
        unitario= costo*(1+nacio/100)*(1+iva/100)
        print(unitario)
        cuota_mensual_opex1t=npf.pmt(tasa_financiacion_general[0]/100,mesesfact[0]/veces_ejecutado,-1*unitario*cantidad,0,1)
        print(cuota_mensual_opex1t  )
        total_opex1t.append(cuota_mensual_opex1t)
        articulos.append(item)
        cantidades.append(cantidad)
        costos.append(cuota_mensual_opex1t)
        tipo.append("opex1t")
        seguro.append("no")
        c=componente_status[-1]
        componente.append(c)
        componente_status.pop(-1)
class Capex(QtWidgets.QMainWindow, Ui_MainWindow):# esta es la clase de Opex 1t 
         
    def __init__(self,parent=None):
        super(Capex, self).__init__(parent)
        loadUi('Capex.ui', self)
        self.boton_regresar.clicked.connect(self.agregar)#boton abre personal
        self.boton_anadir.clicked.connect(self.anadir)#boton añade
        
    
    def agregar(self):
        self.hide()
        otraventana=agregar(self)
        otraventana.show()
    def anadir(self):
        
        print("añadiendo")
        # aca empiezo a darle con los precios 
        item=self.c1.toPlainText()
        empresa_fabricante=self.q1.toPlainText()
        mesesnofact=self.c2.value()
        nacionalizacion=self.c3.value()
        plataforma=self.c4.value()
        iva=self.c5.value()
        tasa_financiacion=self.c6.value()
        cantidad=self.c7.value()
        costo=self.c8.value()
        dolar=self.c9.isChecked()
        seguro1=self.c10.isChecked()
        if dolar==True:
            costo=costo*TRM[0]
        if seguro1==True:
            v=(costo)*(1+nacionalizacion)
            s=v*0.01/mesesfact[0]
            total_otroopex.append(s)
            seguro.append("si")
            articulos.append("seguro plataforma")
            costos.append(s) #aca S debe llevar la formual 
            cantidades.append(1)
            tipo.append("seguro")
            c=componente_status[-1]
            componente.append(c)

            
        else:
            seguro.append("no")
            
        unitario=((1+nacionalizacion/100)*(1+iva/100))*((mesesfact[0]+mesesnofact)/mesesfact[0])
        unit=unitario*costo
        cuota = npf.pmt(tasa_financiacion/100, mesesfact[0], unit*-1*cantidad , 0,1)
        cuota_mensual_capex=round(cuota,3)
        total_capex.append(cuota_mensual_capex)
        articulos.append(item)
        cantidades.append(cantidad)
        costos.append(cuota_mensual_capex)
        tipo.append("capex")
        c=componente_status[-1]
        componente.append(c)
        componente_status.pop(-1)
class infocliente(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase de Opex 1t 
    def __init__(self,parent=None):
        super(infocliente, self).__init__(parent)
        loadUi('infocliente.ui', self)
        self.boton_regresar.clicked.connect(self.Variables)#boton abre personal
        self.boton_regresar_2.clicked.connect(self.Anadir)#boton abre personal
    
    def Variables(self):
         self.hide()
         otraventana=Variables(self)
         otraventana.show() 
    def Anadir(self):
         c=self.c1.toPlainText()
         crm.append(c)
class Parametros(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase de Opex 1t 


 
    def __init__(self,parent=None):
        super(Parametros, self).__init__(parent)
        loadUi('Parametros.ui', self)
        self.boton_regresar.clicked.connect(self.Variables)#boton abre la pagina de atras variables
        self.boton.clicked.connect(self.anadir)#s
        
    
    def Variables(self):
         self.hide()
         otraventana=Variables(self)
         otraventana.show()
    def anadir(self):
        riesgo=self.p20.value()
        riesgototal.append(riesgo)
        margencapex=self.p14.value()
        tasa_capex.append(margencapex)
        tasaoex1t=self.p13.value()
        tasa_opex1t.append(tasaoex1t)
        trm=self.p19.value()
        ipcg=self.p15.value()
        ipc.append(ipcg)
        TRM.append(trm)
        meses=self.p21.value()
        mesesfact.append(meses)
        imprevistos=self.p11.value()
        imprevistos_1.append(imprevistos)
        margenotro=self.p12.value()
        tasa_otroopex.append(margenotro)
        margenp=self.p10.value()
        tasa_personal.append(margenp)
        tasa_gnral=self.gg.value()
        tasa_financiacion_general.append(tasa_gnral)
        trm_serv=self.p24.value()
        TRM_SERV.append(trm_serv)
class ayudas(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase de Opex 1t 


 
    def __init__(self,parent=None):
        super(ayudas, self).__init__(parent)
        loadUi('ayudas.ui', self)
        self.boton_regresar.clicked.connect(self.Variables)#boton regresa
        self.boton_salarios.clicked.connect(self.salarios)#boton abre salarios 
    
    def Variables(self):
         self.hide()
         otraventana=Variables(self)
         otraventana.show()
         
    def salarios(self):
         self.hide()
         otraventana=salarios(self)
         otraventana.show()
    def riesgos(self):
        self.hide()
        otraventana=riesgos(self)
        otraventana.show()
class salarios(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase de Opex 1t 

    def __init__(self,parent=None):
        super(salarios, self).__init__(parent)
        loadUi('salarios.ui', self)
        self.boton_regresar.clicked.connect(self.ayudas)#boton abre personal
    
    def ayudas(self):
         self.hide()
         otraventana=ayudas(self)
         otraventana.show()
class DataFrameTable(tk.Frame):
    def __init__(self, parent=None, df=pd.DataFrame()):
        super().__init__()
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)
        self.table = Table(
            self, dataframe=df,
            showtoolbar=False,
            showstatusbar=True,
            editable=False)
        self.table.show()       
class agregar(QtWidgets.QMainWindow, Ui_MainWindow): # aca entran los 4 elementos 

    def __init__(self,parent=None):
        super(agregar, self).__init__(parent)
        loadUi('agregar.ui', self)
        self.boton_regresar.clicked.connect(self.Variables)#boton abre personal
        self.boton_otroopex.clicked.connect(self.Otroopex)#boton abre personal
        self.boton_opex1t.clicked.connect(self.opex1t)#boton abre personal
        self.boton_capex.clicked.connect(self.Capex)#boton abre personal
        self.boton_personal.clicked.connect(self.Personal)#boton abre personal
        self.boton_agregados.clicked.connect(self.agregados)#boton abre personal
        self.boton_agregados_2.clicked.connect(self.eliminar)#boton abre personal
    
    def eliminar(self):
        if tipo[-1]=="personal":
            total_personal.pop(-1)
        if tipo[-1]=="capex":
            total_capex.pop(-1)
        if tipo[-1]=="otroopex":
            total_otroopex.pop(-1)
        if tipo[-1]=="opex1t":
            total_opex1t.pop(-1)
        if seguro[-1]=="si":
            total_otroopex.pop(-1)
        articulos.pop(-1)
        cantidades.pop(-1)
        costos.pop(-1)
        tipo.pop(-1)
        componente.pop(-1)
         
    def Variables(self):
         self.hide()
         otraventana=Variables(self)
         otraventana.show()
    def Personal(self): 
         self.hide()
         status=self.comboBox.currentText()
         componente_status.append(status)
         otraventana=Personal(self)
         otraventana.show()
         
    def Otroopex(self):
         self.hide()
         status=self.comboBox.currentText()
         componente_status.append(status)
         otraventana=Otroopex(self)
         otraventana.show()
    def opex1t(self):
         self.hide()
         status=self.comboBox.currentText()
         componente_status.append(status)
         otraventana=opex1t(self)
         otraventana.show()
    def Capex(self):
         self.hide()
         status=self.comboBox.currentText()
         componente_status.append(status)
         otraventana=Capex(self)
         otraventana.show()
    def agregar(self):
        self.hide()
        otraventana=agregar(self)
        otraventana.show()
    def agregados(self):
            
        df = pd.DataFrame()
        df['Articulo']=articulos 
        df['Cantidad']=cantidades
        df['Costo']=costos
        df['Tipo']=tipo
        df['Componente']=componente
        root = tk.Tk()
        table = DataFrameTable(root, df)
        root.mainloop()
class Tipooferta(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase de Opex 1t 
    def __init__(self,parent=None):
        super(Tipooferta, self).__init__(parent)
        loadUi('tipooferta.ui', self)
        self.boton_regresar.clicked.connect(self.Variables)#boton regresa
        self.boton_regresar_2.clicked.connect(self.abrir_adicion)#boton regresa
        self.boton_regresar_3.clicked.connect(self.abrir_nuevo)#boton regresa
        
    
    def Variables(self):
         self.hide()
         otraventana=Variables(self)
         otraventana.show()
    def abrir_adicion(self):
        os.startfile(archivo_adicion)
    def abrir_nuevo(self):
        os.startfile(archivo_nuevo)
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



if __name__ == "__main__": # abre la pantalla principal
 
    app =  QtWidgets.QApplication(sys.argv)
    window = Ventana1()
    window.show()
    sys.exit(app.exec_())
    