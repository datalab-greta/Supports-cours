
# # ---------------------------------------------------------------------------------
# ATELIER CARTOGRAPHIE
# OBJECTIF : DECOUVRIR ET SE FAMILIARISER AVEC LA VISUALISATION DE DONNEES SUR CARTES
# DEROULEMENT :
# - UTILISATION DE PHOTON, API D'OPEN STREET MAP POUR CONNAITRE LES COORDONNEES D'UNE LOCALISATION CONNUE
# - CHARGEMENT D'UN FOND DE CARTE OPEN STREET MAP
# - AJOUT D'INFORMATIONS SUR LA CARTE
# # -----------------------------------------------------------------------------------

# Chargement des librairies
library("leaflet")
require(devtools)  
devtools::install_github(repo = 'rCarto/photon')


# Requete sur PHOTON pour connaitre les coordonnees spatiales d'une adresse postale
add_MAME <- "49 Boulevard Preuilly 37000 Tours France"
add_MAME <- gsub(" ", "+", add_MAME)
geo_MAME <- photon::geocode(add_MAME, limit = 1, key = "place")


# Chargement du fond de carte
carte <- leaflet::leaflet() %>%
  leaflet::addTiles() %>%
  leaflet::setView(lng = geo_MAME$lon, lat = geo_MAME$lat, zoom = 13)
print(carte)


# Ajout d'information sur la carte
carte <- carte %>%
  leaflet::addMarkers(geo_MAME$lon, geo_MAME$lat)
print(carte)

carte <- carte %>%
  leaflet::addCircles(lng = geo_MAME$lon, lat = geo_MAME$lat, weight = 3, radius = 100)#, color = "blue", fillColor = "blue", fillOpacity = 0.95)
print(carte)


# Personnalisation des informations restituées
msg <- "DataLab 2019, c'est ici ! On s'éclate et nos formateurs sont géniaux !"
carte <- carte %>%
  leaflet::addPopups(geo_MAME$lon, geo_MAME$lat, popup = msg, options = popupOptions(closeButton = FALSE))
print(carte)





