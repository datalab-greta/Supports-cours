# -*- coding: utf-8 -*-
"""
Created on Fri May 24 10:47:09 2019
@author: remij

ATELIER CARTOGRAPHIE
OBJECTIF : DECOUVRIR ET SE FAMILIARISER AVEC LA VISUALISATION DE DONNEES SUR CARTES
DEROULEMENT :
- UTILISATION DE NOMINATIM, API DE GEOPY POUR CONNAITRE LES COORDONNEES D'UNE LOCALISATION CONNUE
- CHARGEMENT D'UN FOND DE CARTE OPEN STREET MAP
- AJOUT D'INFORMATIONS SUR LA CARTE

Note : cet atelier nécessite les packages 'folium' (carte OSM) et 'geopy' (geolocalisation) qui ne sont pas dans la liste de base d'Anaconda,
il faut donc les installer au préalable : Anaconda / Environnements / search 'folium' - 'geopy' puis 'Apply'
"""


# Chargement des librairies
import folium
from geopy.geocoders import Nominatim


# Requete sur PHOTON pour connaitre les coordonnees spatiales d'une adresse postale
add_MAME = "49 Boulevard Preuilly 37000 Tours France"
geocoder = Nominatim(user_agent="trainee")
geo_MAME = geocoder.geocode(add_MAME, True, 30)


# Chargement du fond de carte
carte = folium.Map(location = [geo_MAME.latitude, geo_MAME.longitude], zoom_start = 13)
print(carte)


# Ajout d'information sur la carte
folium.Marker(location = [geo_MAME.latitude, geo_MAME.longitude]).add_to(carte)
print(carte)

folium.CircleMarker(location = [geo_MAME.latitude, geo_MAME.longitude], radius = 10).add_to(carte)
print(carte)


# Personnalisation des informations restituées
msg = "DataLab 2019, c'est ici ! On s'éclate et nos formateurs sont géniaux !"
carte = folium.CircleMarker(location = [geo_MAME.latitude, geo_MAME.longitude], radius = 10, popup = msg).add_to(carte)
print(carte)


# Sauvegarde de la carte au format 'html'
import os
import webbrowser
chemin = os.getcwd() + '/carte_py.html'
carte.save(chemin)
webbrowser.open('file://' + chemin)

