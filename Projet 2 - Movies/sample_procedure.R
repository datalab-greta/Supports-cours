# Exemple de procedures fonctions en R

#~ R --no-save -q < sample_procedure.R

library(httr)
library(RMySQL)

# lecture du CSV
df <- read.csv2(file="~/movies/data/people.csv", header=FALSE)
colnames(df) <- c("Ref_name", "codes", "Did", "years", "last_n", "first_n", "V7", "V8")
str(df)

# Affichage de qqe lignes
head(df)
    
# Les producteurs : nombre & 10 premiers ?
# print(df[df$codes == "P",])

# Les Acteurs Directeurs: nombre et 10 derniers ?