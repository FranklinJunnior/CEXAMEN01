#!/bin/bash

# Crear una red de Docker personalizada si no existe
docker network inspect my_network >/dev/null 2>&1 || docker network create my_network

# Construir y levantar el contenedor de backpelis
cd backpelis
echo "Construyendo y levantando el contenedor de backpelis..."
docker build -t backpelis .
docker run -d --network=my_network -p 5180:8080 --name back backpelis

# Construir y levantar el contenedor de Flask
cd ../Flask
echo "Construyendo y levantando el contenedor de Flask..."
docker build -t flask .
docker run -d --network=my_network -p 5000:5000 --name flask-container flask

# Construir y levantar el contenedor de frontpelis
cd ../frontpelis
echo "Construyendo y levantando el contenedor de frontpelis..."
docker build -t frontpelis .
docker run -d --network=my_network -p 3000:3000 --name front frontpelis

echo "Todos los contenedores se han iniciado correctamente."
