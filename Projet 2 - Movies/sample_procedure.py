# -*- coding: utf-8 -*-
"""
Created 05/06/2019

@author: EGo

conda activate py27
pip install MySQL-python

"""

# Import librairies
import pandas as pd
from sqlalchemy import create_engine

URL = "~/movies/data/people.csv"
tbl = pd.read_csv(URL, encoding = 'utf8', sep=';', header=None)
tbl.columns = ["Ref_name", "codes", "Did", "years", "last_n", "first_n", "V7", "V8"]
print(tbl.columns)
print(tbl.head(20))

# Les producteurs : nombre & 10 premiers ?
# print(tbl[tbl.codes=='P'])

# Les Acteurs Directeurs: nombre et 10 derniers ?