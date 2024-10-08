import React, { useState } from 'react';
import Modal from './components/modal';
import InvestmentFundsTable from "./components/table";


function App() {
  const [isModalOpen, setModalOpen] = useState(false);
  const [modalMessage, setModalMessage] = useState('');

  const handleShowMessage = () => {
    setModalMessage('¡Este es un mensaje para el usuario!');
    setModalOpen(true);
  };

  const investmentFunds = [
    { id: 1, nombre: 'Fondo A', montoMinimo: 1000, categoria: 'Renta Fija' },
    { id: 2, nombre: 'Fondo B', montoMinimo: 2000, categoria: 'Renta Variable' },
    { id: 3, nombre: 'Fondo C', montoMinimo: 1500, categoria: 'Alternativos' },
  ];

  return (
    <div style={{ padding: 50 }}>
      <h1>Cliente feliz</h1>
      <br />
      <button onClick={() => handleShowMessage()}>X</button>
      <h5>Fondos</h5>
      <InvestmentFundsTable funds={investmentFunds} />
      <br />
      <h5>historial</h5>

      <Modal
        isOpen={isModalOpen}
        onClose={() => setModalOpen(false)}
        message={modalMessage}
      />
    </div>
  );
}

export default App;
