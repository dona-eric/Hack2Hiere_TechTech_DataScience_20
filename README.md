## Tests Techniques DataBeez
## Projet : Scoring de Risque avec German Credit Dataset

Projet : Credit Scoring

   Données : https://www.google.com/url?q=https://b2s2j.r.sp1-brevo.net/mk/cl/f/sh/6rqJfgq8dINmOJvCzGV2lprJOBK/QNMAs_gFSitZ&source=gmail&ust=1734543143038000&usg=AOvVaw0_AJA62_OmDqX6u633Z_ET.
    Tâches :
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

Le modèle principal utilisé est un **XGBOOST Classifier**, sélectionné pour sa robustesse et sa capacité à gérer des données hétérogènes.

#### Métriques d’évaluation :
- **Précision globale.**
- **Courbe ROC et AUC.**
- **Matrice de confusion.**

Des probabilités associées à chaque prédiction sont ajoutées, ainsi qu’une variable "normale" pour l’interprétation.

### 4. Dashboard dynamique

Un dashboard dynamique et interactive est mis en place pour visualiser les resultats de la modélisation (Databeez.)


### **** OPTIONELLE ****
####  5. Mise en place de l’API (Cette partie est OPTIONNELLE) car le dashboard est mise en place

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
      "Predicted": "Low Risk",
      "Probability": 0.85
  }
  ```

- **`GET /results`** :
  - Fournit les résultats de modélisation stockés pour exploration.

### 5. Visualisation des résultats avec Streamlit

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

### Commandes pour lancer l’application :

1. Lancer l’API :
   ```bash
   uvicorn main:app --reload
   ```

2. Lancer Streamlit :
   ```bash
   streamlit run dashboard.py
   ```

---

## Structure du projet

```
Test_Techniques_DATABEEZ/
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

