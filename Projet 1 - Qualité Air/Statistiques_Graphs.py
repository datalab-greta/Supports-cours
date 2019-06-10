# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:49:36 2019
@author: remij

FAIRE UN RESUME STATISTIQUE D'UN JEU DE DONNEES
LANCER AU PREALABLE LE SCRIPT "CONNEXION API" CAR
LA DATA FRAME 'df' EST UTILISEE DANS LA SUITE DE CE SCRIPT

"""

import pandas as pd
import numpy as np

# df est la data frame crée par le script de connexion à l'API
# selection de la variable numérique 'attributes.vleur' qui est
# la valeur mesurée des polluants
x = df["attributes.valeur"]

# Calculs de statistiques de position
np.mean(x)
np.median(x)


# Calculs de statistiques de dispersion
min(x)
max(x)
np.ptp(x)
np.var(x)
np.std(x)


# Résumé statistique du jeu de données partiel ou complet
df.describe(include='all')
x.describe(include='all')


# Résumé graphique des données
import matplotlib.pyplot as plt
plt.hist(x)
plt.boxplot(x)


# ------------------------------------------------------------------------------------------------------
# Analyse statistique 'avancée'

# Résumé statistique des valeurs par type de polluants
mean_polluant = df.groupby(by=['attributes.nom_polluant'])['attributes.valeur'].mean()
median_polluant = df.groupby(by=['attributes.nom_polluant'])['attributes.valeur'].median()
min_polluant = df.groupby(by=['attributes.nom_polluant'])['attributes.valeur'].min()
max_polluant = df.groupby(by=['attributes.nom_polluant'])['attributes.valeur'].max()
stat_polluant = pd.DataFrame([mean_polluant, median_polluant, min_polluant, max_polluant], index=['moyenne', 'mediane', 'mini', 'maxi'])
stat_polluant = stat_polluant.T

# Résumé statistique des valeurs par type de polluants et commune
mean_polluant_com = df.groupby(by=['attributes.nom_polluant', 'attributes.nom_com'])['attributes.valeur'].mean()
median_polluant_com = df.groupby(by=['attributes.nom_polluant', 'attributes.nom_com'])['attributes.valeur'].median()
min_polluant_com = df.groupby(by=['attributes.nom_polluant', 'attributes.nom_com'])['attributes.valeur'].min()
max_polluant_com = df.groupby(by=['attributes.nom_polluant', 'attributes.nom_com'])['attributes.valeur'].max()
stat_polluant_com = pd.DataFrame([mean_polluant_com, median_polluant_com, min_polluant_com, max_polluant_com], index=['moyenne', 'mediane', 'mini', 'maxi'])
stat_polluant_com = stat_polluant_com.T


# Graphique boxplot avancé
df.boxplot(column=['attributes.valeur'], by=['attributes.nom_polluant'])
df.boxplot(column=['attributes.valeur'], by=['attributes.nom_com', 'attributes.nom_polluant'])
df.boxplot(column=['attributes.valeur'], by=['attributes.nom_dept', 'attributes.nom_polluant'])



"""
# Bonus : utilisation de la librairie 'ggplot2', une librairie incontournable pour la visualisation de données
# Les notions ci-dessous n'ont pas encore été introduites en cours, nous y reviendront dessus largement plus tard
# l'import de la librairie 'plotnine' se fait comme décrit ici en commande linux :
https://plotnine.readthedocs.io/en/stable/installation.html
"""

import numpy as np
import pandas as pd
from plotnine import *

# We run this to suppress various deprecation warnings from plotnine - keeps our notebook cleaner
import warnings
warnings.filterwarnings('ignore')


# Au prealable on renomme certaines colonnes car l'operation de 'facetting' (fonction facet_wrap) est en défaut avec les noms d'origine
df2 = df
df2.rename(columns ={'attributes.nom_com' : 'commune',
                         'attributes.nom_polluant' : 'polluant',
                         'attributes.valeur' : 'valeur',
                         }, inplace=True)

graph1 = ggplot(df2, aes(x='polluant', y='valeur', color='polluant')) + \
    geom_boxplot() + \
    xlab('Type polluant') + ylab('Concentration observée (µg/m3)') + labs(colour = "Polluant") + \
    facet_wrap('~commune')
print(graph1)


graph2 = ggplot(df2, aes(x='commune', y='valeur', color='polluant')) + \
    geom_boxplot() + \
    coord_flip() + \
    xlab('Commune') + ylab('Concentration observée (µg/m3)') + labs(colour = "Polluant") + \
    facet_wrap('~polluant')
print(graph2)

