# -*- coding: utf-8 -*-
"""
Created on Fri May 17 15:18:52 2019

@author: remij
"""


# CHARGEMENT DES LIBRAIRIES
import requests
from pandas.io.json import json_normalize

# DEFINITION DE LA REQUETE (SELON API)
requete = "https://services1.arcgis.com/HzzPcgRsxxyIZdlU/arcgis/rest/services/mes_centre_val_de_loire_annuel_poll_princ_1/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"


# CONNEXION AVEC L'API
reponse = requests.get(requete)


# EVALUATION DE LA CONNEXION ET DU TYPE DE REPONSE
reponse.status_code
reponse.content


# EXTRACTION DES DONNEES
contenu_json = reponse.json()
contenu_json
print(type(contenu_json))


# TRANSFORMATION EN OBJET EN PYTHON INTERPRETABLE (DATA FRAME)
#import pandas as pd
df = json_normalize(contenu_json['features'])
print(df.shape)
print(df.head())

# Plus d'infos sur les data frames emboitées ici :
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.json.json_normalize.html
# https://www.kaggle.com/jboysen/quick-tutorial-flatten-nested-json-in-pandas
