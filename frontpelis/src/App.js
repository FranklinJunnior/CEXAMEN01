import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'; // Importar Bootstrap
import './App.css'; // Importar los estilos personalizados

function App() {
  const [title, setTitle] = useState('');
  const [recommendations, setRecommendations] = useState([]);

  const fetchRecommendations = async () => {
    try {
      const response = await fetch(`http://back:5180/recommend?title=${title}`);
      if (!response.ok) {
        throw new Error('La respuesta de la red no fue correcta');
      }
      const data = await response.json();
      setRecommendations(data);
    } catch (error) {
      console.error('Error al obtener recomendaciones:', error);
    }
  };

  return (
    <div className="App container mt-5">
      <h1 className="text-center mb-4">Recomendaciones de Películas</h1>
      <div className="input-group mb-3">
        <input
          type="text"
          className="form-control"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Introduce el título de la película"
        />
        <button className="btn btn-primary" onClick={fetchRecommendations}>
          Obtener Recomendaciones
        </button>
      </div>
      {recommendations.length > 0 ? (
        <ul className="list-group">
          {recommendations.map((rec, index) => (
            <li key={index} className="list-group-item">
              {rec}
            </li>
          ))}
        </ul>
      ) : (
        <p className="text-center">No hay recomendaciones disponibles.</p>
      )}
    </div>
  );
}

export default App;
