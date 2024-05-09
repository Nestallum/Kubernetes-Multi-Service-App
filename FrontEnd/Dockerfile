# Utilisation de l'image de base Python
FROM python:3.12.2-alpine3.18

# Définition du répertoire de travail pour le service 2
WORKDIR /app

# Copie des fichiers de dépendances pour le service 2
COPY requirements.txt .

# Installation des dépendances pour le service 2
RUN pip install -r requirements.txt

# Copie du code source pour le service 2
COPY . .

# Exposition du port 8080 pour le service 2
EXPOSE 8080

# Définition de la commande par défaut pour le service 2
CMD ["python", "app.py"]
