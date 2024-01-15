# Étape 1: Construire l'app Angular
FROM node:18.13 as build-step
WORKDIR /app
COPY package.json /app
RUN npm install
COPY . /app
RUN npm run build
# Étape 2: Servir l'app avec Nginx
FROM nginx:alpine
COPY --from=build-step /app/dist/frontend /usr/share/nginx/html
# COPY ./nginx.conf /etc/nginx/nginx.conf