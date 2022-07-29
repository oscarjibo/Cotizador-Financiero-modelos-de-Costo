import pandas as pd
import os

from datetime import date
from datetime import datetime

now = date.today()
datos = {'comercial': [], 'preventa': [], 'fecha': [], 'cliente': [], 'TOTAL': [], 'CMR': []}
df = pd.DataFrame(data=datos)
nuevo_registro = {'comercial': "Mariem Espinoza", 'preventa': "Patricia Cuta", 'cliente': "avianca",
                  'TOTAL': "avianca", 'CMR': "111111",'fecha':now, "tipo" : "RFP"}
df = df.append(nuevo_registro, ignore_index=True)
print(df)
file_name = 'registros.xlsx'
df.to_excel(file_name, index=False)
print('DataFrame is written to Excel File successfully.')
os.startfile(file_name)
    
    
