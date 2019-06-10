library(httr)
library(RMySQL)

# lecture du CSV
df <- read.csv2(file="~/movies/data/people.csv", header=FALSE)

# Affichage de qqe lignes
head(df)
    
# Connection à mysql
# https://www.r-bloggers.com/accessing-mysql-through-r/
mydb = dbConnect(MySQL(), user='team', password='DataLab@2019', dbname='BDD_Emmanuel', host='localhost')

# AJOUT du dataframe df dans la table 'peopleR', la table est créee si besoin
dbWriteTable(mydb, name='peopleR', df, overwrite=FALSE, append=TRUE)

