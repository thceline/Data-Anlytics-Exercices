# -*- coding: utf-8 -*-
"""Actividad repaso - Webscrapping.ipynb
"""

import requests as req
import pandas as pd



#EJERCICIO 3 Pandas: scrapear la tabla que contiene informacion sobre los álbums más vendidos por año en todo el 
#mundo (https://es.wikipedia.org/wiki/Anexo:%C3%81lbumes_musicales_m%C3%A1s_vendidos) generando un dataframe con 
#la información del año, nombre del álbum, artista y ventas. Ésta ultima columna deberá tener sus valores 
#en numeros enteros en millones.



url = 'https://es.wikipedia.org/wiki/Anexo:%C3%81lbumes_musicales_m%C3%A1s_vendidos'

tables = pd.read_html(url) #leeo el HTML 


# for index, table in enumerate(tables): #busco todas las tablas de la pagina y me quedo con en el índice de cada tabla
#     print(f"Tabla {index}:")
#     print(table)

last_table = tables[-1]

last_table = last_table.iloc[:, :-1]

# Limpiar y renombrar las columnas
last_table.columns = ['Año', 'Álbum', 'Artista', 'Ventas']

# Convertir las ventas a números enteros en millones
def convert_to_millions(sales):
    try:
        return int(float(sales) * 1000000)  # Convertir a millones
    except ValueError:
        return 0 

last_table['Ventas'] = last_table['Ventas'].apply(convert_to_millions)

# Mostrar el DataFrame resultante
print(last_table.to_string())