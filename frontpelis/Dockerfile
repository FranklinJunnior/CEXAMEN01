# Utiliza la imagen base de Node.js para compilar la aplicación
FROM node:16 AS build

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de configuración y dependencias
COPY package.json package-lock.json ./

# Instala las dependencias, incluyendo Bootstrap
RUN npm install

# Copia el resto de los archivos del proyecto
COPY . .

# Construye la aplicación para producción
RUN npm run build

# Utiliza una imagen base de Nginx para servir los archivos estáticos de la aplicación
FROM nginx:alpine

# Copia los archivos de compilación desde la etapa anterior
COPY --from=build /app/build /usr/share/nginx/html

# Expone el puerto 80 para acceder a la aplicación
EXPOSE 80

# Comando por defecto para iniciar Nginx
CMD ["nginx", "-g", "daemon off;"]
