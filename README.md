# Netflix Insights

## AI Watch : L'intelligence artificielle au service de l'analyse de données

### 1. Qu'est-ce que l'intelligence artificielle ?

L'intelligence artificielle (IA) désigne l'ensemble des méthodes permettant à une machine d'imiter des facultés cognitives humaines – perception, raisonnement, prise de décision – via l'application d'algorithmes sophistiqués dans un environnement informatique. Son objectif est que l'ordinateur « pense » ou « agisse » comme un humain, notamment grâce à la collecte et au traitement de vastes quantités de données.

Trois piliers fondamentaux permettent ce fonctionnement :

- **Les systèmes informatiques** : architecture matérielle et logicielle capable de supporter des calculs intensifs.
- **Les données** : volumes croissants de données structurées et non structurées, gérées via des bases de données et entrepôts de données.
- **Les algorithmes d'IA** : réseaux de neurones, algorithmes évolutionnistes, logique floue, permettant l'apprentissage et l'adaptation.

### 2. Le Machine Learning (apprentissage automatique)

Le Machine Learning est un sous-domaine de l'IA où la machine acquiert automatiquement des connaissances à partir d'exemples, sans être explicitement programmée pour chaque tâche. Concrètement, l'algorithme « apprend » à partir d'un jeu de données d'entraînement et génère un modèle statistique qu'il utilise ensuite pour faire des prédictions ou classifications.

On distingue principalement :

- **L'apprentissage supervisé** (données étiquetées) : classification, régression.
- **L'apprentissage non supervisé** (données non étiquetées) : clustering, détection d'anomalies.
- **L'apprentissage semi-supervisé** : combinaison de données étiquetées et non étiquetées pour réduire le coût d'annotation.
- **L'apprentissage en ligne/continu** : le modèle s'améliore en continu dès qu'il reçoit de nouveaux retours.

### 3. Le pré-traitement des données

Avant toute analyse, les données brutes doivent être nettoyées, transformées et normalisées :

- Traitement des valeurs manquantes (imputation, suppression)
- Correction des incohérences et des doublons
- Encodage des variables catégorielles
- Mise à l'échelle (normalisation, standardisation)
- Détection et gestion des outliers (valeurs aberrantes)

Ce pré-traitement est essentiel pour garantir la qualité des modèles de ML et éviter que le bruit ou les biais n'entraînent des performances médiocres.

### 4. L'analyse descriptive des données

L'analyse descriptive consiste à résumer et visualiser les caractéristiques principales d'un jeu de données :

- **Statistiques univariées** : mesures de tendance centrale (moyenne, médiane), de dispersion (écart-type, variance).
- **Fréquences et pourcentages** : distribution des modalités pour les variables catégorielles.
- **Graphiques** : histogrammes, boîtes à moustaches, diagrammes en barres.

Cette phase permet de comprendre ce qui s'est déjà produit, d'identifier des tendances ou anomalies, et de formuler des hypothèses avant toute modélisation prédictive.

### 5. Focus sur le domaine : La Santé

Grâce à l'IA, le secteur médical connaît une véritable révolution :

#### a. Diagnostics précoces
- Reconnaissance d'images médicales (radiographies, IRM, scanners) : détection de cancers du poumon ou du sein avec une précision souvent supérieure à celle de l'œil humain.
- Dépistage automatisé de la rétinopathie diabétique à partir de photographies du fond d'œil, réduisant le temps d'attente pour les patients.

#### b. Médecine personnalisée
- Analyse de données génomiques et historiques médicaux pour adapter les traitements aux caractéristiques individuelles du patient (pharmacogénomique).
- Prédiction des réactions aux médicaments et optimisation des posologies via le ML.

#### c. Optimisation des opérations hospitalières
- Prédiction des flux de patients pour ajuster les effectifs, planifier les interventions chirurgicales et gérer les stocks de médicaments en temps réel, réduisant les coûts et les pénuries.
- Tri automatique des urgences selon la gravité des cas, améliorant la prise en charge.

#### d. Assistance en chirurgie
- Robots chirurgicaux (Da Vinci, etc.) offrant une précision extrême, guidés par des algorithmes d'IA pour minimiser les erreurs et accélérer la récupération des patients.
- Réalité augmentée pour superposer des données anatomiques en temps réel.

#### e. Suivi et télémédecine
- Plateformes de surveillance à distance utilisant des capteurs connectés et des IA de détection d'anomalies pour prévenir les complications avant qu'elles ne deviennent critiques.
- Chatbots médicaux capables de répondre à des questions de premiers secours ou d'orienter vers un professionnel.

#### f. Découverte de médicaments et alternatives à l'expérimentation animale
- Combinaison d'IA et de modélisation moléculaire pour explorer des milliards de composés, réduisant de moitié le temps et les coûts de développement de nouveaux traitements.
- Utilisation de « lab-on-a-chip » et d'organes-sur-puce simulés numériquement pour remplacer progressivement l'expérimentation animale.

## Contexte du Projet et Données Utilisées

Ce projet d'analyse exploratoire porte sur le catalogue de contenu de Netflix, leader mondial du streaming vidéo. Depuis sa transition du modèle de location de DVD par courrier vers le streaming en 2007, Netflix a révolutionné la consommation de contenu audiovisuel, particulièrement avec son expansion internationale accélérée depuis 2016.

**Source de données** : Le dataset `netflix_titles.csv` contient des informations détaillées sur 8807 titres disponibles sur Netflix jusqu'en septembre 2021. Chaque entrée comporte 12 attributs :

- `show_id` : Identifiant unique de chaque titre
- `type` : Catégorie (Film ou Série TV)
- `title` : Titre de l'œuvre
- `director` : Réalisateur(s)
- `cast` : Acteurs principaux
- `country` : Pays d'origine
- `date_added` : Date d'ajout au catalogue Netflix
- `release_year` : Année de sortie originale
- `rating` : Classification par âge (TV-MA, PG-13, etc.)
- `duration` : Durée (en minutes pour les films, en saisons pour les séries)
- `listed_in` : Genres/catégories
- `description` : Synopsis

L'analyse a été réalisée via Python et ses bibliothèques spécialisées (Pandas, Matplotlib, Seaborn, Plotly) pour extraire des insights pertinents sur l'évolution et la composition du catalogue Netflix.

## Observations et Conclusions de l'Analyse

**a. Type d'œuvres :** Le catalogue est dominé par les **films (69,6%)**, tandis que les **séries TV représentent 30,4%** du contenu. Cette répartition montre la stratégie de Netflix de privilégier les contenus unitaires tout en maintenant une offre significative de séries.

**b. Pays d'origine :** Forte prédominance des **États-Unis (33,7%)**, suivis par l'**Inde (9,1%)**, le **Royaume-Uni (4,7%)** et le **Canada (3,2%)**. Cette distribution reflète l'héritage anglo-saxon de la plateforme, malgré une diversification progressive vers d'autres marchés internationaux.

**c. Année d'ajout au catalogue :** Croissance exponentielle à partir de **2016 (429 contenus)**, atteignant un pic en **2019 (2016 contenus au total)** avec **1424 films** et en **2020 (595 séries)**. Un léger ralentissement est observé en 2021, probablement dû aux contraintes de production liées à la pandémie.

**d. Ratings :** Prédominance des contenus pour adultes et jeunes adultes avec **TV-MA (29%)** et **TV-14 (27%)** en tête. Les contenus familiaux et pour enfants sont moins nombreux, démontrant un positionnement clairement orienté vers un public mature.

**e. Durée des films :** La majorité des films se situe dans la fourchette **90-120 minutes**, respectant les standards de l'industrie. Seulement 8% des films dépassent les 130 minutes, confirmant une préférence pour des formats accessibles.

**f. Durée des séries :** **67% des séries ne comportent qu'une seule saison**, et seulement 12% dépassent les 3 saisons. Cette distribution suggère un fort renouvellement du catalogue et une préférence pour les mini-séries ou les contenus à durée limitée.

**g. Genres :** Les **drames (30%)**, **comédies (24%)** et **documentaires (14%)** dominent le catalogue. On note également une forte présence de contenus internationaux, témoignant de la stratégie globale de la plateforme.

**h. Réalisateurs prolifiques :** Quelques réalisateurs comme **Rajiv Chilaka (19 œuvres)** et **Raúl Campos/Jan Suter (18 œuvres)** se distinguent par leur nombre de productions, mais la grande majorité des créateurs n'ont qu'une seule œuvre sur la plateforme.

**i. Tendances temporelles :** L'année **2019** marque le sommet absolu pour les films avec **1424 ajouts**, tandis que **2020** représente le pic pour les séries avec **595 ajouts**. La période **2016-2020** constitue clairement l'âge d'or de l'enrichissement du catalogue.

## Conclusion Générale

L'analyse du catalogue Netflix révèle une stratégie d'acquisition massive et ciblée entre 2016 et 2020, période coïncidant avec l'internationalisation accélérée de la plateforme et sa transition vers un modèle de production originale. Le catalogue présente un profil clairement orienté vers un public adulte, avec une prédominance américaine mais une diversification internationale croissante.

L'architecture du catalogue privilégie les formats moyens pour les films et les séries courtes (1-2 saisons), permettant un renouvellement rapide et une consommation flexible adaptée aux habitudes modernes de visionnage. Cette approche reflète une compréhension fine des comportements des utilisateurs à l'ère du streaming.

Le ralentissement observé en 2021 pourrait marquer la fin d'une phase d'expansion frénétique et l'entrée dans une ère plus sélective, davantage axée sur la rétention et la qualité que sur la croissance quantitative. Cette évolution est cohérente avec la maturation du marché du streaming et l'intensification de la concurrence (Disney+, HBO Max, Amazon Prime Video), qui oblige Netflix à affiner sa stratégie de contenu.

Notre analyse confirme que Netflix a construit un catalogue diversifié tant en termes de formats que d'origines géographiques, tout en maintenant une identité éditoriale claire orientée vers un public adulte et international. Cette stratégie de catalogue constitue un pilier fondamental de son succès commercial global, avec plus de 220 millions d'abonnés dans le monde en 2022.
