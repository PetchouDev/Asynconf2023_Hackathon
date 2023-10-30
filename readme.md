# Asynconf 2023 Hackathon

### Author: Petchou

### Description:
Ce repo constitue ma proposition de solution pour le hackaton Asynconf 2023. Il s'agit d'une application simmple, réalisée avec le framework PySide 2, qui permet de calculer un taux de prêt selon le type de voiture désiré.

### Lancement
Le projet requiert une version de python comprise entre 3.5 et 3.10 (Testé sur python 3.8 et 3.9, voir les compatibilités de PySide2)

#### 1. Création de l'environnement virtuel
L'application à besoin de certains modules pour fonctionner, il est donc recommandé de créer un environnement virtuel pour l'installation de ces modules. Pour cela, il faut se rendre dans le dossier du projet et exécuter la commande suivante:
```bash
python3 -m venv venv
source venv/bin/activate # Linux/OSX
.\venv\Scripts\activate  # Windows
```

#### 2. Installation des dépendances
Le script vérifie la présence des dépendances et les installe si besoin. Il peut quand même être une bonne idée de les installer manuellement pour éviter les erreurs. Cela se fait avec :

```bash
python3 -m pip install -r requirements.txt
```

#### 3. Lancement de l'application
Pour lancer l'application, il suffit d'exécuter le script main.py avec python3:
```bash
python3 main.py
```