# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt en el directorio de trabajo
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Descargar los recursos de NLTK necesarios en una ubicación específica
RUN python -m nltk.downloader -d /usr/local/share/nltk_data stopwords punkt wordnet

# Establece la variable de entorno NLTK_DATA para que NLTK sepa dónde buscar los datos
ENV NLTK_DATA=/usr/local/share/nltk_data

# Copia el resto del código de la aplicación en el directorio de trabajo
COPY . .

# Expone el puerto en el que correrá la aplicación
EXPOSE 5000

# Comando para correr la aplicación
CMD ["python", "app.py"]
