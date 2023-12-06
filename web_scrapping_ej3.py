# -*- coding: utf-8 -*-
"""Actividad repaso - Webscrapping.ipynb
"""
from bs4 import BeautifulSoup as bs
import requests as req
import pandas as pd
from io import StringIO


#EJERCICIO 1 API: consultar en el endpoint de Berries por la que corresponde al "id" = 7.

#EJERCICIO 2 Beautiful Soup: scrapear la tabla de lenguajes de programación más utilizados (https://lenguajesdeprogramacion.net/) 
   # creando un dataframe con una columna llamada "lenguaje" y otra columna llamada "porcentaje_uso".


#EJERCICIO 3 Pandas: scrapear la tabla que contiene informacion sobre los álbums más vendidos por año en todo el 
#mundo (https://es.wikipedia.org/wiki/Anexo:%C3%81lbumes_musicales_m%C3%A1s_vendidos) generando un dataframe con 
#la información del año, nombre del álbum, artista y ventas. Ésta ultima columna deberá tener sus valores 
#en numeros enteros en millones.

url = 'https://es.wikipedia.org/wiki/Anexo:%C3%81lbumes_musicales_m%C3%A1s_vendidos' #url en variable 

html=req.get(url).text  #extraemos html

soup = bs(html, 'html.parser')  #sopa 
#print(len(soup.find_all('table')))
#table = soup.find_all('table', class_='wikitable')[0]
# table_str = str(table)
# table_io = StringIO(table_str)

# dfs = pd.read_html(table_io)
# df = dfs[0]  
tables = soup.find_all('table', class_='wikitable')  # Encontrar todas las tablas con esa clase
table = tables[0]

data = []
for row in table.find_all('tr')[1:]:
    cols = row.find_all(['td', 'th'])
    # Verificar si la fila tiene al menos 4 columnas
    if len(cols) >= 4:
        year = cols[0].get_text().strip()
        album = cols[1].get_text().strip()
        artist = cols[2].get_text().strip()
        sales = cols[3].get_text().strip()
        # Limpiar el formato de ventas y convertirlo a millones
        sales_millions = int(sales.replace('millones', '').replace(',', '').replace('.', '').strip()) if 'millones' in sales else 0
        data.append([year, album, artist, sales_millions])
  

# Crear el DataFrame
df = pd.DataFrame(data, columns=['Año', 'Álbum', 'Artista', 'Ventas (en millones)'])



print(df)




