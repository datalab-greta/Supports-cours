
# ------------------------------------------------------

# CHARGEMENT DES LIBRAIRIES
require(httr)
require(jsonlite)


# DEFINITION DE LA REQUETE (SELON API)
requete <- "https://services1.arcgis.com/HzzPcgRsxxyIZdlU/arcgis/rest/services/mes_centre_val_de_loire_annuel_poll_princ_1/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"

# CONNEXION AVEC L'API
reponse <- httr::GET(requete)


# EVALUATION DU TYPE DE REPONSE
httr::http_type(reponse)
View(reponse)


# EXTRACTION DES DONNEES
contenu_json <- httr::content(reponse)


# TRANSFORMATION EN OBJET R INTERPRETABLE (DATA FRAME)
contenu_r <- jsonlite::fromJSON(contenu_json, flatten = TRUE)
df <- as.data.frame(contenu_r$features)
View(df)
