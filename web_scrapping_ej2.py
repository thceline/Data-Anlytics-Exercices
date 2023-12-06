# -*- coding: utf-8 -*-
"""Actividad repaso - Webscrapping.ipynb
"""
from bs4 import BeautifulSoup as bs
import requests as req
import pandas as pd
from io import StringIO



#EJERCICIO 2 Beautiful Soup: scrapear la tabla de lenguajes de programación más utilizados (https://lenguajesdeprogramacion.net/) 
   # creando un dataframe con una columna llamada "lenguaje" y otra columna llamada "porcentaje_uso".



# Obtener la página web y crear el objeto BeautifulSoup
url = 'https://lenguajesdeprogramacion.net/'
html = req.get(url)
soup = bs(html.text, 'html.parser')

# Encontrar la tabla de lenguajes de programación más utilizados
#table = soup.find('table', {'id': 'example'})
soup.find_all('table')

tabla=soup.find_all('table')[0]

elem = tabla.find('a')




lenguajes=[]

# Bucle por filas
for f in tabla.find_all('tr'):

    fila=[e for e in f.find_all('td')]


    if len(fila)>0:
    
        language = fila[1].text.strip()
        porcentaje = fila[2].text.strip()
        lenguajes.append([language, porcentaje])

df = pd.DataFrame(lenguajes, columns=['Lenguaje', 'Porcentaje_Uso'])
print(df)


# Leer la tabla y crear un DataFrame

#print(df)


