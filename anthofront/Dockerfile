# Utiliser une image de base Node.js
FROM node:latest

# Définir le répertoire de travail dans le conteneur
WORKDIR /vue

# Copier les fichiers de dépendances et installer les dépendances
# Assurez-vous que les fichiers package.json et package-lock.json (si existant) sont copiés dans le répertoire de travail
COPY anthofront/package*.json ./

# Installer les dépendances du projet
RUN npm install


# Copier le reste des fichiers du projet Vue.js dans le conteneur
COPY anthofront/ .

# Construire l'application pour la production
RUN npm run build

# Installer un serveur HTTP simple pour servir l'application
RUN npm install -g http-server

# Exposer le port sur lequel le serveur HTTP écoute
EXPOSE 80

# Servir l'application
CMD ["http-server", "dist", "-p", "80"]
