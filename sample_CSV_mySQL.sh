# On execute tout...

# https://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux
RED='\033[0;31m'
NC='\033[0m' # No Color
#printf "I ${RED}love${NC} Stack Overflow\n"

# On change de répertoire (home)
printf "\n${RED}Récupération des données${NC}\n"
cd 
# Suppression movies si existant
rm -rf movies

# clone du projet movies
git clone https://github.com/cernoch/movies.git

# Affichage du répertoire
printf "\n${RED}Liste des CSV${NC}\n"
ls -l movies/data/*.csv

# Execution du programme python:
python3 < sample_CSV_mySQL.py