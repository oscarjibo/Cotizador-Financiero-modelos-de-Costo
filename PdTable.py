# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:00:20 2022

@author: ojimeneb
"""

"""
Cosas interesantes 
 no termina todavía
2020/4/17 10:14
"""
import PdTable
import pandas as pd
from PyQt5.QtWidgets import (QApplication, QTableView)
from PyQt5.QtCore import (QAbstractTableModel, Qt)
 
 
class PdTable(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data
 
    def rowCount(self, parent=None):
        return self._data.shape[0]
 
    def columnCount(self, parent=None):
        return self._data.shape[1]
 
         # Mostrar datos
    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None
 
         # Mostrar encabezado de fila y columna
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self._data.axes[0][col]
        return None
 
 
def mostrartabla(a,b,c):
    import sys
    app = QApplication(sys.argv)
    df=pd.DataFrame()
    articulos=a
    costos=b
    cantidad=c
    df['articulo']=articulos 
    df['cantidad']=cantidad
    df['costo']=costos
    model = PdTable(df)
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle('Pandas')
    view.resize(410, 250)
    view.setAlternatingRowColors(True)
    view.show()
 
    sys.exit(app.exec_())
a=['rticul']
b=[34]
c=[54]
mostrartabla(a, b, c)