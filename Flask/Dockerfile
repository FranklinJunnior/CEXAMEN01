# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Instala los datos necesarios de NLTK
RUN python -m nltk.downloader stopwords punkt wordnet

# Expone el puerto en el que correrá la aplicación Flask
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
