# Usa una imagen base de Nginx para servir la aplicación construida
FROM nginx:alpine

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el package.json y el package-lock.json
COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia el resto del código de la aplicación en el directorio de trabajo
COPY . .

# Construye la aplicación para producción
RUN npm run build

# Copia los archivos construidos desde la etapa de construcción anterior al servidor Nginx
COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80

# Comando para correr el servidor Nginx
CMD ["nginx", "-g", "daemon off;"]
