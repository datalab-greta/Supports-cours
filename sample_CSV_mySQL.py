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
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", action="store_true", help="Verbose SQL")
#~ parser.add_argument("--cred", help="Credentials (myDatalab, pgDatalab)")
parser.add_argument("--base", help="Répertoire de movies")
parser.add_argument("--bdd", help="Base de donnée")
args = parser.parse_args()

# Définition des accès
user='team'
password='DataLab@2019'
host='127.0.0.1'
DBname=args.bdd # ex: BDD_Emmanuel?charset=utf8
mySQLengine = create_engine("mysql://%s:%s@%s/%s" % (user, password, host, DBname))
rs=mySQLengine.execute("SELECT * FROM people LIMIT 10;")
for x in rs:
    print(x)

# Ici, on execute directement du SQL: "USE XXX"
#mySQLengine.execute("USE %s;" % DBname)

# Lecture du CSV par pandas, noter le format du fichier (local sur /home/goudot/movies/data)
URL = args.base+"/people.csv"
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