# Fase de construcción
FROM node:16 AS build

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo package.json y package-lock.json
COPY package*.json package-lock*.json ./

# Instalar dependencias
RUN npm install

# Copiar el resto del código fuente
COPY . .

# Construir la aplicación
RUN npm run build

# Fase de producción
FROM nginx:alpine

# Copiar la aplicación construida desde la fase anterior
COPY --from=build /app/build /usr/share/nginx/html

# Exponer el puerto 80
EXPOSE 80

# Iniciar Nginx
CMD ["nginx", "-g", "daemon off;"]