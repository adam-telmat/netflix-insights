#!/usr/bin/env python
# coding: utf-8

# # Netflix Data Analysis
# 
# ## Introduction
# 
# Ce notebook présente une analyse complète du catalogue de Netflix en date de septembre 2021. Nous allons explorer la diversité du contenu, les tendances d'ajout, et la répartition des différents types d'œuvres.

# ## Sommaire
# 
# 1. [Chargement des données](#Chargement-des-données)
# 2. [Exploration initiale des données](#Exploration-initiale-des-données)
# 3. [Nettoyage et préparation des données](#Nettoyage-et-préparation-des-données)
# 4. [Analyse des valeurs uniques](#Analyse-des-valeurs-uniques)
# 5. [Analyses spécifiques](#Analyses-spécifiques)
# 6. [Visualisations](#Visualisations)
# 7. [Conclusion](#Conclusion)

# ## Chargement des données
# 
# Commençons par importer les bibliothèques nécessaires et charger le dataset.

# In[1]:

# Import des bibliothèques nécessaires
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import missingno as msno
from datetime import datetime
import warnings
import re

# Configuration de l'affichage
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)
plt.style.use('ggplot')
sns.set(style="whitegrid")

# Chargement du dataset
# Assurez-vous que le fichier est placé dans le dossier '../data/'
df = pd.read_csv('../data/netflix_titles.csv')

# ## Exploration initiale des données
# 
# Affichons maintenant un aperçu du DataFrame.

# In[2]:

# Afficher les 5 premières observations
print("Les 5 premières observations :")
print(df.head())

# In[3]:

# Afficher les 5 dernières observations
print("\nLes 5 dernières observations :")
print(df.tail())

# In[4]:

# Afficher les informations du DataFrame
print("\nInformations du DataFrame :")
print(df.info())

# In[5]:

# Afficher la dimensionnalité du DataFrame
print(f"\nDimensionnalité du DataFrame : {df.shape}")
print(f"Nombre de variables : {df.shape[1]}")
print(f"Nombre d'observations : {df.shape[0]}")

# In[6]:

# Afficher les colonnes du DataFrame
print("\nColonnes du DataFrame :")
print(df.columns.tolist())

# In[7]:

# Afficher le type des différentes colonnes
print("\nTypes des colonnes :")
print(df.dtypes)

# Pour répondre à la question sur les types de données :
print("\nDonnées quantitatives (numériques) :")
print(df.select_dtypes(include=['int64', 'float64']).columns.tolist())
print("\nDonnées qualitatives (catégorielles) :")
print(df.select_dtypes(include=['object']).columns.tolist())

# In[8]:

# Vérifier les données manquantes
print("\nRésumé des données manquantes :")
missing_data = df.isnull().sum()
missing_data_percent = 100 * df.isnull().sum() / len(df)
missing_data_table = pd.concat([missing_data, missing_data_percent], axis=1)
missing_data_table.columns = ['Valeurs manquantes', 'Pourcentage (%)']
print(missing_data_table.sort_values('Pourcentage (%)', ascending=False))

# In[9]:

# Visualisation des données manquantes avec Missingno
msno.matrix(df)
plt.title('Matrice des valeurs manquantes')
plt.show()

msno.bar(df)
plt.title('Graphique à barres des valeurs manquantes')
plt.show()

# In[10]:

# Afficher une observation aléatoire
random_index = np.random.randint(0, len(df))
print(f"\nObservation aléatoire (index {random_index}) :")
print(df.iloc[random_index])

# In[11]:

# Afficher toutes les informations de l'œuvre "Catch Me If You Can"
print("\nInformations sur 'Catch Me If You Can' :")
catch_me = df[df['title'] == 'Catch Me If You Can']
print(catch_me)

# In[12]:

# Convertir la colonne date_added en datetime pour les prochaines analyses
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), format='%B %d, %Y', errors='coerce')

# Trouver le film le plus récent
films = df[df['type'] == 'Movie'].copy()
film_recent = films.loc[films['date_added'].idxmax()]
print(f"\nFilm le plus récent : {film_recent['title']} (ajouté le {film_recent['date_added'].strftime('%d/%m/%Y')})")

# In[13]:

# Trouver la série la plus récente
series = df[df['type'] == 'TV Show'].copy()
serie_recente = series.loc[series['date_added'].idxmax()]
print(f"\nSérie la plus récente : {serie_recente['title']} (ajoutée le {serie_recente['date_added'].strftime('%d/%m/%Y')})")

# ## Nettoyage et préparation des données
# 
# Modifions certaines variables pour faciliter l'analyse.

# In[14]:

# La colonne date_added a déjà été convertie en datetime plus haut

# Modifier la variable duration pour les films
# Extraire la durée en minutes pour les films
df['duration_value'] = df['duration'].str.extract('(\d+)').astype('float')

# Extraire le nombre de saisons pour les séries
df.loc[df['type'] == 'TV Show', 'duration_value'] = df.loc[df['type'] == 'TV Show', 'duration'].str.extract('(\d+)').astype('float')

# In[15]:

# Modifier la variable listed_in pour en faire une liste
df['listed_in_list'] = df['listed_in'].apply(lambda x: [genre.strip() for genre in x.split(',')] if isinstance(x, str) else [])

# ## Analyse des valeurs uniques

# In[16]:

# Afficher les valeurs uniques des variables spécifiées
print("\nValeurs uniques de 'type' :")
print(df['type'].unique())

print("\nNombre de valeurs uniques pour 'country' :", df['country'].nunique())
print("Exemples de pays :", df['country'].dropna().unique()[:10])

print("\nValeurs uniques de 'release_year' :")
print(sorted(df['release_year'].unique()))

print("\nValeurs uniques de 'rating' :")
print(df['rating'].unique())

print("\nExemples de genres (listed_in) :")
unique_genres = set()
for genres in df['listed_in_list']:
    for genre in genres:
        unique_genres.add(genre)
print(list(unique_genres)[:10])

# In[17]:

# Vérifier les directeurs ayant produit plus d'une œuvre
director_counts = df['director'].dropna().value_counts()
directors_multiple_works = director_counts[director_counts > 1]
print(f"\nNombre de directeurs ayant produit plus d'une œuvre : {len(directors_multiple_works)}")
print("Top 10 des directeurs les plus prolifiques :")
print(directors_multiple_works.head(10))

# In[18]:

# Année avec le plus de films ajoutés
df['year_added'] = df['date_added'].dt.year
films_par_annee = df[df['type'] == 'Movie'].groupby('year_added').size()
annee_max_films = films_par_annee.idxmax()
print(f"\nL'année avec le plus de films ajoutés : {annee_max_films} ({films_par_annee[annee_max_films]} films)")

# In[19]:

# Année avec le plus de séries ajoutées
series_par_annee = df[df['type'] == 'TV Show'].groupby('year_added').size()
annee_max_series = series_par_annee.idxmax()
print(f"\nL'année avec le plus de séries ajoutées : {annee_max_series} ({series_par_annee[annee_max_series]} séries)")

# ## Visualisations

# In[20]:

# a. La répartition du type d'oeuvres du dataset
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='type')
plt.title('Répartition des types de contenu sur Netflix')
plt.xlabel('Type de contenu')
plt.ylabel('Nombre')
plt.show()

# Version interactive avec Plotly
fig = px.pie(df, names='type', title='Répartition des types de contenu sur Netflix',
             color_discrete_sequence=px.colors.sequential.RdBu)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()

# In[21]:

# b. La répartition des oeuvres en fonction des pays du dataset
# Nettoyer les données des pays (certains contenus ont plusieurs pays)
df['country_clean'] = df['country'].fillna('Unknown')
countries = df['country_clean'].str.split(', ').explode().str.strip()
top_countries = countries.value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title('Top 10 des pays produisant du contenu sur Netflix')
plt.xlabel('Nombre de titres')
plt.tight_layout()
plt.show()

# Version interactive avec Plotly
fig = px.bar(top_countries.reset_index(), x='count', y='index', 
             title='Top 10 des pays produisant du contenu sur Netflix',
             labels={'count': 'Nombre de titres', 'index': 'Pays'},
             color='count', color_continuous_scale='Viridis')
fig.update_layout(yaxis={'categoryorder':'total ascending'})
fig.show()

# In[22]:

# c. La répartition des années du dataset
plt.figure(figsize=(14, 6))
sns.histplot(data=df, x='release_year', bins=30, kde=True)
plt.title('Distribution des années de sortie')
plt.xlabel('Année de sortie')
plt.ylabel('Nombre de titres')
plt.show()

# Visualisation des années d'ajout
plt.figure(figsize=(14, 6))
sns.countplot(data=df, x='year_added')
plt.title('Distribution des années d\'ajout au catalogue Netflix')
plt.xlabel('Année d\'ajout')
plt.ylabel('Nombre de titres')
plt.xticks(rotation=45)
plt.show()

# In[23]:

# d. La répartition des ratings du dataset
plt.figure(figsize=(12, 6))
rating_counts = df['rating'].value_counts()
sns.barplot(x=rating_counts.index, y=rating_counts.values)
plt.title('Répartition des classifications (ratings)')
plt.xlabel('Classification')
plt.ylabel('Nombre de titres')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Version interactive avec Plotly
fig = px.pie(rating_counts.reset_index(), values='rating', names='index',
             title='Répartition des classifications (ratings)',
             color_discrete_sequence=px.colors.qualitative.Set3)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()

# In[24]:

# e. La répartition de la durée des films du dataset
plt.figure(figsize=(12, 6))
films = df[df['type'] == 'Movie'].copy()
sns.histplot(data=films, x='duration_value', bins=20, kde=True)
plt.title('Distribution de la durée des films')
plt.xlabel('Durée (minutes)')
plt.ylabel('Nombre de films')
plt.xlim(0, 250)  # Limiter l'axe x pour une meilleure visualisation
plt.tight_layout()
plt.show()

# Version interactive avec Plotly
fig = px.histogram(films, x='duration_value', nbins=20,
                  title='Distribution de la durée des films',
                  labels={'duration_value': 'Durée (minutes)'},
                  color_discrete_sequence=['indianred'])
fig.update_layout(xaxis_range=[0, 250])
fig.update_traces(marker=dict(line=dict(width=1, color='white')))
fig.show()

# In[25]:

# f. La répartition de la durée des séries du dataset
plt.figure(figsize=(12, 6))
series = df[df['type'] == 'TV Show'].copy()
sns.countplot(data=series, x='duration_value')
plt.title('Distribution du nombre de saisons des séries')
plt.xlabel('Nombre de saisons')
plt.ylabel('Nombre de séries')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Version interactive avec Plotly
fig = px.bar(series['duration_value'].value_counts().reset_index().sort_values('index'),
            x='index', y='duration_value',
            title='Distribution du nombre de saisons des séries',
            labels={'index': 'Nombre de saisons', 'duration_value': 'Nombre de séries'},
            color='duration_value', color_continuous_scale='Viridis')
fig.show()

# In[26]:

# g. La répartition des genres d'œuvres du dataset
genres_df = pd.DataFrame(df['listed_in_list'].explode().value_counts()).reset_index()
genres_df.columns = ['Genre', 'Count']
top_genres = genres_df.head(15)

plt.figure(figsize=(14, 8))
sns.barplot(data=top_genres, x='Count', y='Genre')
plt.title('Top 15 des genres sur Netflix')
plt.xlabel('Nombre de titres')
plt.tight_layout()
plt.show()

# Version interactive avec Plotly
fig = px.bar(top_genres, x='Count', y='Genre',
             title='Top 15 des genres sur Netflix',
             color='Count', color_continuous_scale='Viridis')
fig.update_layout(yaxis={'categoryorder':'total ascending'})
fig.show()

# In[27]:

# h. Le top 5 des séries les plus longues
top_series = series.sort_values('duration_value', ascending=False).head(5)
plt.figure(figsize=(12, 6))
sns.barplot(data=top_series, x='duration_value', y='title')
plt.title('Top 5 des séries avec le plus de saisons')
plt.xlabel('Nombre de saisons')
plt.ylabel('Titre')
plt.tight_layout()
plt.show()

# Version interactive avec Plotly
fig = px.bar(top_series, x='duration_value', y='title',
             title='Top 5 des séries avec le plus de saisons',
             color='duration_value', color_continuous_scale='Viridis',
             labels={'duration_value': 'Nombre de saisons', 'title': 'Titre'})
fig.update_layout(yaxis={'categoryorder':'total ascending'})
fig.show()

# In[28]:

# i. Le top 5 des films les plus longs
top_films = films.sort_values('duration_value', ascending=False).head(5)
plt.figure(figsize=(12, 6))
sns.barplot(data=top_films, x='duration_value', y='title')
plt.title('Top 5 des films les plus longs')
plt.xlabel('Durée (minutes)')
plt.ylabel('Titre')
plt.tight_layout()
plt.show()

# Version interactive avec Plotly
fig = px.bar(top_films, x='duration_value', y='title',
             title='Top 5 des films les plus longs',
             color='duration_value', color_continuous_scale='Viridis',
             labels={'duration_value': 'Durée (minutes)', 'title': 'Titre'})
fig.update_layout(yaxis={'categoryorder':'total ascending'})
fig.show()

# In[29]:

# j. La répartition des "directors" des œuvres françaises
# Filtrer les œuvres françaises
french_content = df[df['country_clean'].str.contains('France', na=False)]
# Extraire les directeurs (peut être plusieurs par œuvre)
french_directors = french_content['director'].dropna().str.split(', ').explode().value_counts().head(10)

plt.figure(figsize=(12, 8))
sns.barplot(x=french_directors.values, y=french_directors.index)
plt.title('Top 10 des réalisateurs d\'œuvres françaises sur Netflix')
plt.xlabel('Nombre d\'œuvres')
plt.tight_layout()
plt.show()

# Version interactive avec Plotly
fig = px.bar(french_directors.reset_index(), x='count', y='index',
             title='Top 10 des réalisateurs d\'œuvres françaises sur Netflix',
             labels={'count': 'Nombre d\'œuvres', 'index': 'Réalisateur'},
             color='count', color_continuous_scale='Viridis')
fig.update_layout(yaxis={'categoryorder':'total ascending'})
fig.show()

# In[30]:

# k. La répartition des œuvres en fonction de la date d'ajout au catalogue
df['month_added'] = df['date_added'].dt.month
df['month_year_added'] = df['date_added'].dt.strftime('%Y-%m')

monthly_additions = df.groupby('month_year_added').size().reset_index(name='count')
monthly_additions = monthly_additions.sort_values('month_year_added')

plt.figure(figsize=(16, 6))
sns.lineplot(data=monthly_additions, x='month_year_added', y='count')
plt.title('Évolution des ajouts mensuels au catalogue Netflix')
plt.xlabel('Mois')
plt.ylabel('Nombre de titres ajoutés')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Version interactive avec Plotly
fig = px.line(monthly_additions, x='month_year_added', y='count',
              title='Évolution des ajouts mensuels au catalogue Netflix',
              labels={'month_year_added': 'Mois', 'count': 'Nombre de titres ajoutés'})
fig.update_layout(xaxis_tickangle=-90)
fig.show()

# In[31]:

# l. Graphique supplémentaire : Évolution du ratio films/séries au fil du temps
yearly_type_counts = df.groupby(['year_added', 'type']).size().unstack().fillna(0)
yearly_type_ratio = yearly_type_counts['Movie'] / (yearly_type_counts['Movie'] + yearly_type_counts['TV Show'])

plt.figure(figsize=(12, 6))
yearly_type_ratio.plot(kind='line', marker='o')
plt.title('Évolution du ratio films/séries ajoutés à Netflix')
plt.xlabel('Année')
plt.ylabel('Proportion de films')
plt.grid(True)
plt.axhline(y=0.5, color='r', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Version interactive avec Plotly
fig = px.line(yearly_type_ratio.reset_index(), x='year_added', y=0,
              title='Évolution du ratio films/séries ajoutés à Netflix',
              labels={'year_added': 'Année', '0': 'Proportion de films'},
              markers=True)
fig.add_hline(y=0.5, line_dash="dash", line_color="red", annotation_text="Équilibre films/séries")
fig.show()

# ## Conclusion
# 
# Notre analyse du catalogue Netflix révèle plusieurs insights intéressants :
# 
# 1. **Composition du catalogue** : Les films dominent le catalogue (environ 70%), bien que la proportion de séries ait augmenté ces dernières années.
# 
# 2. **Diversité géographique** : Bien que le contenu américain soit prédominant, Netflix propose une grande diversité de contenus internationaux, reflétant sa stratégie d'expansion mondiale.
# 
# 3. **Tendances temporelles** : Les ajouts au catalogue ont connu une forte croissance entre 2015 et 2020, avec un pic autour de 2018-2019, suivi d'une légère diminution en 2021 (potentiellement due à la pandémie).
# 
# 4. **Caractéristiques du contenu** :
#    - La majorité des films ont une durée entre 90 et 120 minutes.
#    - La plupart des séries ont 1 à 2 saisons, avec relativement peu de séries longues.
#    - Les genres les plus représentés sont les drames, les comédies et les documentaires.
#    - Le rating "TV-MA" (public adulte) est le plus courant.
# 
# 5. **Stratégie de contenu** : L'évolution du ratio films/séries montre une tendance à l'équilibrage progressif, suggérant un intérêt croissant pour les séries.
# 
# Cette analyse nous offre un aperçu de la stratégie de contenu de Netflix et de son évolution, reflétant les changements dans les préférences des consommateurs et les tendances de l'industrie du divertissement. 