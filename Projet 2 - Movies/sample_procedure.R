# Exemple de procedures fonctions en R

#~ R --no-save -q < sample_procedure.R

library(httr)
#library(RMySQL)

# lecture du CSV
df <- read.csv2(file="~/movies/data/people.csv", header=FALSE)
colnames(df) <- c("Ref_name", "codes", "Did", "years", "last_n", "first_n", "V7", "V8")
str(df)

# Affichage de qqe lignes
head(df)

# Les producteurs dans df: nombre & 10 premiers ?
# print(df[df$codes == "P",])

# Les Acteurs Directeurs de df: nombre et 10 derniers ?

# Meme question à partir de la BBD

#library(RMySQL)
library('RPostgreSQL')
df <- read.csv2(file="~/movies/data/people.csv", header=FALSE)
colnames(df) <- c("Ref_name", "codes", "Did", "years", "last_n", "first_n", "V7", "V8")
drv <- dbDriver("PostgreSQL")
pgdb = dbConnect(drv, user='team', password='DataLab@2019', dbname='Datalab', host='localhost')

dbGetQuery(pgdb, 'TRUNCATE "peopleR"')
dbWriteTable(pgdb, name='peopleR', df, overwrite=FALSE, append=TRUE)
