from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec

app = Flask(__name__)
CORS(app)

# Ruta al archivo CSV (ruta relativa dentro del contenedor)
file_path = 'movie_dataset.csv'

# Cargar el archivo CSV
try:
    data = pd.read_csv(file_path)
    print("Archivo CSV cargado correctamente.")
except FileNotFoundError:
    print("Archivo CSV no encontrado. Asegúrate de que el archivo esté en la ubicación correcta.")
    data = pd.DataFrame()

# Modificar el DataFrame si se cargó correctamente
if not data.empty:
    data.drop(columns=["homepage", "status"], axis=1, inplace=True)
    data['Description'] = data['title'] + ' ' + data['overview'] + ' ' + data['tagline']

    # Importar stopwords en inglés
    nltk.download('stopwords')
    nltk.download('punkt_tab')
    nltk.download('wordnet')
    en_stopwords = stopwords.words("english")
    lemma = WordNetLemmatizer()

    # Definir una función para el preprocesamiento
    def clean(text):
        text = re.sub("[^A-Za-z0-9 ]", "", text)  # Eliminar signos de puntuación
        text = text.lower()  # Convertir a minúsculas
        tokens = word_tokenize(text)  # Tokenizar el texto
        clean_list = [lemma.lemmatize(token) for token in tokens if token not in en_stopwords]  # Lematizar y eliminar stopwords
        return " ".join(clean_list)  # Unir los tokens

    # Asegurarse de que todos los valores en 'Description' sean cadenas de texto
    data['Description'] = data['Description'].astype(str)

    # Aplicar la función "clean" en la columna Description
    data['Description'] = data['Description'].apply(clean)

    # Vectorización usando TF-IDF
    vectorizer = TfidfVectorizer()
    test_matrix = vectorizer.fit_transform(data['Description'])

    # Definir una función que devolverá las primeras cinco películas recomendadas
    def Recommendation_Cosine_similarity(matrix, title):
        similarity = cosine_similarity(matrix)
        movie_index = data[data['title'].str.contains(title, case=False, na=False)].index[0]
        similar_movies = list(enumerate(similarity[movie_index]))
        sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[:6]  # El primer elemento es la película que se está viendo
        recommendations = [f"{i+1}\t{data[data.index == item[0]]['title'].values[0]}" for i, item in enumerate(sorted_similar_movies)]
        return recommendations

    # Endpoint para obtener recomendaciones
    @app.route('/recommend', methods=['GET'])
    def recommend():
        title = request.args.get('title')
        if not title:
            return jsonify({"error": "No title provided"}), 400
        recommendations = Recommendation_Cosine_similarity(test_matrix, title)
        return jsonify(recommendations)

    # Preprocesamiento para Word2Vec
    def clean_for_word2vec(text):
        text = re.sub("[^A-Za-z0-9 ]", "", text)  # Eliminar signos de puntuación
        text = text.lower()  # Convertir a minúsculas
        tokens = word_tokenize(text)  # Tokenizar el texto
        clean_list = [lemma.lemmatize(token) for token in tokens if token not in en_stopwords]  # Lematizar y eliminar stopwords
        return clean_list

    # Limpiar los documentos para Word2Vec
    Description = data['Description'].apply(clean_for_word2vec)

    # Instanciar el modelo Word2Vec
    model = Word2Vec(vector_size=100, min_count=1, workers=4)

    # Construir el vocabulario
    model.build_vocab(Description)

    # Entrenar el modelo
    model.train(Description, total_examples=model.corpus_count, epochs=model.epochs)

# Ruta para la página principal
@app.route('/')
def home():
    return "<h1>¡Bienvenido a la aplicación de recomendaciones de películas!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
