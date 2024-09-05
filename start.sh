#!/bin/bash

# Construir y levantar el contenedor de backpelis
cd backpelis
docker build -t backpelis .
docker run -d -p 5180:8080 --name back backpelis

# Construir y levantar el contenedor de Flask
cd ../Flask
docker build -t flask .
docker run -d -p 5000:5000 --name flask-container flask

# Construir y levantar el contenedor de frontpelis
cd ../frontpelis
docker build -t frontpelis .
docker run -d -p 3000:80 --name front frontpelis


