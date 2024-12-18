## Tests Techniques DataBeez
## Projet : Scoring de Risque avec German Credit Dataset

Projet : Credit Scoring

   ## Données : https://www.google.com/url?q=https://b2s2j.r.sp1-brevo.net/mk/cl/f/sh/6rqJfgq8dINmOJvCzGV2lprJOBK/QNMAs_gFSitZ&source=gmail&ust=1734543143038000&usg=AOvVaw0_AJA62_OmDqX6u633Z_ET.
   ## Tâches :
      * Explorer les données pour chercher les plus grandes corrélations avec l'octroi ou non de crédit 
      * Développer un modèle de prédiction de scoring crédit.
      * Créer un Dockerfile pour le déploiement.
      * Héberger le code sur GitHub ou GitLab.
      * Créer un tableau de bord interactif via Power BI ou Looker Studio pour visualiser les résultats du modèle.

---

## Technologies utilisées

- **Python 3.12** : Langage principal pour toutes les étapes.
- **Pandas** : Manipulation et analyse des données.
- **Scikit-learn** : Préparation des données, construction de pipelines, et modélisation.
- **PowerBi** : Visualisations des résultats de la modélisation et un tableau de bord dynamique et interactif.
- **Docker** : Création d'une image pour le deploiement du modèle sur un serveur (Continiuous Integration/Continuous Deployment)
- **FastAPI** : Mise en place d’une API RESTful.
- **Streamlit** : Création d’une interface utilisateur pour la visualisation.
- **Matplotlib, Seaborn, Plotly** : Génération de visualisations interactives et statiques.

---

## Étapes du projet

### 1. Analyse des données

Le dataset contient des informations socio-économiques et financières sur les clients, notamment :
- **Variables numériques :**
  - Age
  - Job
  - Credit amount
  - Duration
- **Variables catégoriques :**
  - Sex
  - Housing
  - Saving accounts
  - Checking account
  - Purpose

#### Explorations réalisées :
- Distribution des variables numériques (histogrammes).
- Analyse des fréquences pour les variables catégoriques (count plots).
- Relations entre les variables avec des scatter plots.

### 2. Préparation des données

Un pipeline de transformation a été mis en place :
- **Variables numériques :**
  - Standardisation avec `StandardScaler`.
- **Variables catégoriques :**
  - Imputation des valeurs manquantes avec `SimpleImputer` (méthode "most_frequent").
  - Encodage avec `OneHotEncoder`.

La transformation des données conserve la structure initiale du dataset pour garantir une interprétation directe des résultats.

### 3. Modélisation

Lors de la modélisation plusieurs étapes ont été faites:
      ** Création d'une fonction de modelisation qui prend en entrée une liste de modèle ,les données d'entrainement et les données de test.Cette fonction peut etre utilise à des fins utiles pour la classification binaire.(voir le notebook)
      ** Mise en place d'un pipeline de modelisation et transformation des données automatiquement et rapide pour obtenir les résultats. Ce pipeline de modélisation est sauvégardé dans le dossier ../models_risque_credit/final_model_pipeline. Pour mettre en place ce pipeline il vous suffira de vous référer à :
         -- https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer
         -- https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline
      ** Recherche des meilleurs paramètres des modèles et du modèle performant avec GridSearchCV(qui applique une validation croisée de 5/lots). 
   ** Le modèle principal utilisé est un **XGBOOST Classifier**, sélectionné pour sa robustesse et sa capacité à gérer des données hétérogènes.

#### Métriques d’évaluation :
- **Précision globale.**
- **F1-score.**
- **Courbe ROC et AUC.**
- **Matrice de confusion.**

A partir des résultats du modèle, les prédictions sont générées dans le fichier (predict_df.csv) avec les probabilités associées à chaque prédiction sont ajoutées, ainsi qu’une variable "normale(du donnée source) " pour l’interprétation.

### 4. Dashboard dynamique

Un dashboard dynamique et interactif est mis en place pour visualiser les resultats de la modélisation (Databeez.)

### 5. DockerFile
Pour tout projet data science ou de machine learning, il est conseillé de deployer ce modèle afin de permettre à des entreprises de le consommer et d'assurer la maintenance et la surveillance du performance. Donc un #Dockerfile est écrit pour servir d'image du modèle afin de le déployer correctement .

### 6- OPTIONELLE ****
#### A- Mise en place de l’API (Cette partie est OPTIONNELLE) car le dashboard est mis en place
Pour mettre aller plus loin et de rendre ce projet dynamique, nous avons mis en place une API avec deux routes (post/predict et get/results).
La première route servira à afficher la prediction et la probabilité : de nouvelle observation est fourni l'apiet nous obtenons une sortie parfaite.
La deuxième route servira à visualiser les résultats des données sorties obtenues.
   #### Routes principales :
   - **`POST /predict`** :
     - Entrée : Une nouvelle observation.
     - Sortie : La prédiction du risque (classe et probabilité).

  Exemple de requête :
  ```json
  {
      "Age": 35,
      "Sex": "Male",
      "Job": 1,
      "Housing": "own",
      "Saving accounts": "little",
      "Checking account": "moderate",
      "Credit amount": 1200,
      "Duration": 24,
      "Purpose": "car"
  }
  ```

  Exemple de réponse :
  ```json
  {
      "Predicted": "Good",
      "Probability": 0.85
  }
  ```

- **`GET /results`** :
  - Fournit les résultats de modélisation stockés pour exploration.

   ### B. Visualisation des résultats avec Streamlit
     L'api ainsi mise en place est intégrée dans une application streamlit qui sert d'interface utilisateur pour afficher les résultats.
     L'utilisateur soumet les données nouvelles à partir de l'app streamlit et une réquete est faite via l'api.
   Un tableau de bord interactif a été conçu pour :
   - **Afficher les données prédéfinies** et explorer les résultats.
   - **Explorer les visualisations :**
     - Histogrammes des variables numériques.
     - Scatter plots pour analyser les relations entre variables.
     - Pie charts pour les répartitions des classes prédites.
   - **Tester de nouvelles prédictions** directement dans l’interface.
   
   #### Exemple d’interface utilisateur :
   - Formulaire d’entrée pour soumettre de nouvelles données.
   - Graphiques interactifs avec Plotly et Seaborn.

   ### C. Commandes pour lancer l’application :

      1. Lancer l’API :
        '''
         uvicorn main:app --reload
        '''

      2. Lancer Streamlit :
         streamlit run dashboard.py
         ```

---

## Structure du projet

```
Test_Techniques_DATABEEZ/
|-riskenv          #environnement virtuel utiliseé
   |-Analyse_risque_credit/
       |-analyse_credit_risque.ipynb # notebook pour l'analyse.
   |-German_Data_Credit/
       |-predictions        #les données de predictions
       |-Train               #les données d'entrainement
       |-Test               #les données de test
   |-models_credit_risque/
       -pipeline_transformers.pkl  #pour transformer les données
       - final_model_pipeline.pkl  #  le pipeline pour la preparation des données et la modelisation
   |-ScoringApp                   #pour l'api et interface streamlit
       |— main.py               # API FastAPI
       |— dashboard.py          # Tableau de bord Streamlit
       # Données prédites sauvegardées
   |— requirements.txt      # Dépendances Python
   |-Dockerfile                #fichier docker pour le deploiement du modèle
```

---

## Conclusion

Ce projet fournit une solution complète pour le scoring de risque, incluant un dashbord interactif et dynamique des résultats de la modélisation. Il peut être étendu pour inclure davantage de types de modèles ou des analyses approfondies sur des données supplémentaires.
