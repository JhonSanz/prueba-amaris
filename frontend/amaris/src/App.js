import React, { useState, useEffect } from 'react';
import Modal from './components/modal';
import FundsTable from "./components/fundTable";
import HistoryTable from './components/historyTable';

function App() {
  const [isModalOpen, setModalOpen] = useState(false);
  const [modalMessage, setModalMessage] = useState('');

  const handleShowMessage = () => {
    setModalMessage('¡Este es un mensaje para el usuario!');
    setModalOpen(true);
  };


  return (
    <div style={{ padding: 50 }}>
      <h1>Cliente feliz</h1>
      <br />
      <button onClick={() => handleShowMessage()}>X</button>
      <h5>Mis Fondos</h5>
      {/* <FundsTable
        setModalOpen={setModalOpen}
        setModalMessage={setModalMessage}
      /> */}
      <br />
      <h5>Mi Historial</h5>
      <HistoryTable
        setModalOpen={setModalOpen}
        setModalMessage={setModalMessage}
      />
      <Modal
        isOpen={isModalOpen}
        onClose={() => setModalOpen(false)}
        message={modalMessage}
      />
    </div>
  );
}

export default App;
