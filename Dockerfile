# Utiliser une image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers requis
COPY requirements.txt .
COPY analyse_credit_risque.ipynb .
COPY credit_scoring_model.joblib .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port pour l'API
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["python", "analyse_credit_risque.ipynb"]