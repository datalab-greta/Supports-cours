
# ------------------------------------------------------------------------------
# FAIRE UN RESUME STATISTIQUE D'UN JEU DE DONNEES
# LANCER AU PREALABLE LE SCRIPT "CONNEXION API" CAR
# LA DATA FRAME 'df' EST UTILISEE DANS LA SUITE DE CE SCRIPT
# ------------------------------------------------------------------------------


# df est la data frame crée par le script de connexion à l'API
# selection de la variable numérique ''
x <- df$attributes.valeur

# Calculs de statistiques de position
mean(x)
median(x)


# Calculs de statistiques de dispersion
min(x)
max(x)
range(x)
var(x)
sd(x)


# Résumé statistique du jeu de données partiel ou complet
summary(x)
summary(df)


# Résumé graphique des données
hist(x)
boxplot(x)


# ------------------------------------------------------------------------------------------------------
# Analyse statistique avancée
library(dplyr)

# Résumé statistique des valeurs par type de polluants
stat_polluant <- df %>%
  group_by(attributes.nom_polluant) %>%
  summarise(moyenne = mean(attributes.valeur),
            mediane = median(attributes.valeur),
            mini = min(attributes.valeur),
            maxi = max(attributes.valeur))

View(stat_polluant)

# Résumé statistique des valeurs par type de polluants et commune
stat_polluant_commune <- df %>%
  group_by( attributes.nom_com, attributes.nom_polluant) %>%
  summarise(moyenne = mean(attributes.valeur),
            mediane = median(attributes.valeur),
            mini = min(attributes.valeur),
            maxi = max(attributes.valeur))

View(stat_polluant_commune)


# Graphique boxplot avancé
boxplot(attributes.valeur ~ attributes.nom_polluant, data = df)
boxplot(attributes.valeur ~ attributes.nom_com + attributes.nom_polluant, data = df)
boxplot(attributes.valeur ~ attributes.nom_dept + attributes.nom_polluant, data = df)


# Graphique des moyennes par polluant
barplot(height = stat_polluant_commune$moyenne,
        names.arg = paste0(stat_polluant_commune$attributes.nom_com, " - ", stat_polluant_commune$attributes.nom_polluant))


# Bonus : utilisation de la librairie 'ggplot2', une librairie incontournable pour la visualisation de données
# Les notions ci-dessous n'ont pas encore été introduites en cours, nous y reviendront dessus largement plus tard
require(ggplot2)
graph1 <- ggplot2::ggplot(data=df, aes(x=attributes.nom_polluant, y=attributes.valeur, color=attributes.nom_polluant)) +
  ggplot2::geom_boxplot() +
  ggplot2::facet_wrap(~ attributes.nom_com) + xlab('Type polluant') + ylab('Concentration observée (µg/m3)') + labs(colour = "Polluant")
print(graph1)  


graph2 <- ggplot2::ggplot(data=df, aes(x=attributes.nom_com, y=attributes.valeur, color=attributes.nom_polluant)) +
  ggplot2::geom_boxplot() +
  ggplot2::coord_flip() +
  ggplot2::facet_wrap(~ attributes.nom_polluant) + xlab('Commune') + ylab('Concentration observée (µg/m3)') + labs(colour = "Polluant")
print(graph2)  

