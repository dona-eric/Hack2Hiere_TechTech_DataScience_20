# Utiliser une image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers requis
COPY requirements.txt ./requirements.txt
COPY analyse_credit_risque.ipynb .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install jupyter
# Exposer le port pour l'API
EXPOSE 8888

# Commande pour démarrer l'application
CMD ["jupyter", "notebook", "analyse_credit_risque.ipynb", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]