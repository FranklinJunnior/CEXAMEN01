# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt en el directorio de trabajo
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Descargar los recursos de NLTK necesarios
RUN python -m nltk.downloader stopwords punkt wordnet punkt_tab

# Copia el resto del código de la aplicación en el directorio de trabajo
COPY . .

# Copia el archivo CSV en el directorio de trabajo
COPY movie_dataset.csv /app/movie_dataset.csv

# Expone el puerto en el que correrá la aplicación
EXPOSE 5000

# Comando para correr la aplicación
CMD ["python", "app.py"]
