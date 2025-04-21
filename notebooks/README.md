# Guide d'utilisation du notebook d'analyse Netflix

## Prérequis

1. Assurez-vous d'avoir Python installé (de préférence Python 3.8+)
2. Installez les dépendances nécessaires :
   ```
   pip install -r ../requirements.txt
   ```

## Instructions

1. **Préparation des données** :
   - Téléchargez le dataset Netflix (septembre 2021)
   - Placez le fichier CSV (`netflix_titles.csv`) dans le dossier `../data/`

2. **Utilisation du notebook** :
   - Option 1 : Créer un nouveau notebook Jupyter et copier-coller le contenu du fichier `netflix_analysis.py`
   - Option 2 : Convertir le script Python en notebook avec la commande suivante :
     ```
     jupyter nbconvert --to notebook --execute netflix_analysis.py
     ```
   - Option 3 : Ouvrir directement le script dans VS Code qui prend en charge l'exécution de cellules Python (avec l'extension Python installée)

3. **Exécution** :
   - Exécutez les cellules dans l'ordre pour reproduire l'analyse complète
   - Vous pouvez adapter et modifier le code selon vos besoins

## Notes importantes

- Certaines visualisations utilisent Plotly et nécessitent un environnement interactif pour être pleinement exploitées
- Les graphiques seront enregistrés dans le répertoire courant si vous exécutez toutes les cellules 