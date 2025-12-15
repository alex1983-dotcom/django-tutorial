import React from 'react';

function App() {
  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial, sans-serif' }}>
      <h1>Мой первый React + Vite</h1>
      <div
        style={{
          border: '1px solid #ccc',
          borderRadius: '8px',
          padding: '1rem',
          maxWidth: '300px',
          boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
        }}
      >
        <h2>Карточка товара</h2>
        <p>Описание товара — просто тестовая карточка.</p>
        <button>Купить</button>
      </div>
    </div>
  );
}

export default App;