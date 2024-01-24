# AlgoInvest-Trade
***Livrable du Projet 7 du parcours D-A Python d'OpenClassrooms : 
calcul de la meilleure combinaison d'actions en fonction de leurs bénéfices selon deux approches ;***

- ***Bruteforce***

- ***Programmation dynamique (algorithme du sac à dos)***

## Initialisation du projet

git clone https://github.com/A1zenAttaqi/AlgoInvest-Trade.git


    python -m venv env 
    env\scripts\activate
    pip install -r requirements.txt

## Exécution du programme

Le montant d'investissement par défaut est fixé à 500€

### Bruteforce

    python bruteforce.py

*Note : Le bruteforce ne traîte que les données du fichier "actions_data.csv", contenant 20 actions. Les datasets 1 et 2 résulteraient à un temps d'exécution extrêmement long.*

### Programmation dynamique

La version optimisée nécessite d'entrer le nom du fichier à traiter:
    python optimized.py dataset1.csv
    python optimized.py dataset2.csv
    python optimized.py actions_data.csv






