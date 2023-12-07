# -*- coding: utf-8 -*-
"""Actividad repaso - Webscrapping.ipynb
"""
from bs4 import BeautifulSoup as bs
import requests as req
import pandas as pd
from io import StringIO


#EJERCICIO 1 API: consultar en el endpoint de Berries por la que corresponde al "id" = 7.


# URL del endpoint de la baya con ID 7
api_code = 'https://pokeapi.co/api/v2/berry/7/'

# Realizar la solicitud GET a la API
response = req.get(api_code)
json_code = response.json()


df_berry = pd.json_normalize(json_code)

df_berry_2 = pd.json_normalize( df_berry["flavors"][0])
print(df_berry_2)