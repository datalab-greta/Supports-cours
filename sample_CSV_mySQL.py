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

# Définition des accès
user='team'
password='DataLab@2019'
host='172.20.152.200'
mySQLengine = create_engine("mysql://%s:%s@%s/?charset=utf8" % (user, password, host))

# Ici, on execute directement du SQL: "USE XXX"
DBname='goudot_test'
mySQLengine.execute("USE `goudot_test`;")

# Lecture du CSV par pandas, noter le format du fichier (local sur /home/goudot/movies/data)
URL = "file:///home/goudot/movies/data/people.csv"
tbl = pd.read_csv(URL, encoding = 'utf8', sep=';', header=None)
print(tbl.head())

# Ecriture des données dataframe -> mySQL
# Après avoir supprimé (si existante) la table 'people'
Tname="people"
mySQLengine.execute('DROP TABLE IF EXISTS %s' % Tname)
tbl.to_sql(Tname, mySQLengine, if_exists='replace', index=False)
print("CSV sauvé dans table '%s'" % Tname)

'''
import pymysql
conn = pymysql.connect(host=host, user=user, password=password, db=DBname, charset='utf8mb4')
with conn.cursor() as cursor:
    cursor.execute("SELECT * FROM %s;" % Tname)
    for row in cursor:
        print(row)

'''