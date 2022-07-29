import pandas as pd
import os

miarchivo = "./df.xlsx"
df = pd.read_excel(miarchivo)
print(df)
nuevo_registro = {'comercial': "patricia22", 'preventa': "marolyn22", 'cliente': "avianca22"}
df = df.append(nuevo_registro, ignore_index=True)
file_name = 'df.xlsx'
df.to_excel(file_name, index=False)
print(df)
    
miarchivo = ".\df.xlsx"
os.startfile(miarchivo)