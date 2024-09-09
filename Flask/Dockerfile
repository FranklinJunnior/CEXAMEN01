FROM python:3.9-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación
COPY . /app

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Descargar recursos de NLTK
RUN python -m nltk.downloader stopwords punkt wordnet

# Exponer el puerto
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
