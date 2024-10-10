import React, { useState, useEffect } from 'react';
import Modal from './components/modal';
import FundsTable from "./components/fundTable";
import HistoryTable from './components/historyTable';

const API_URL = process.env.REACT_APP_API_URL;
console.log('API URL:', API_URL);

function App() {
  const [isModalOpen, setModalOpen] = useState(false);
  const [modalMessage, setModalMessage] = useState('');
  const [currentClient, setCurrentClient] = useState(null);
  const [history, setHistory] = useState([]);

  async function getCurrentClient(params) {
    try {
      const response = await fetch(`/fund/get_client?client_id=user_001`);
      if (!response.ok) {
        throw new Error(`Error: ${response.status} - ${response.statusText}`);
      }
      const data = await response.json();
      setCurrentClient(data.result);
    } catch (error) {
      console.error('Error fetching investment funds:', error);
      return null;
    }
  }

  useEffect(() => {
    async function init() {
      await getCurrentClient();
    }
    init();
  }, []);

  async function getHistory() {
    try {
      const response = await fetch(`/fund/history`);
      if (!response.ok) {
        throw new Error(`Error: ${response.status} - ${response.statusText}`);
      }
      const data = await response.json();
      setHistory(data.result);
    } catch (error) {
      console.error('Error fetching investment funds:', error);
      return null;
    }
  };


  return (
    <div style={{ padding: 50 }}>
      <h1>{currentClient?.name} - {currentClient?.money}</h1>
      <br />
      <h5>Mis Fondos</h5>
      {
        currentClient && <FundsTable
          setModalOpen={setModalOpen}
          setModalMessage={setModalMessage}
          clientSubscriptions={currentClient.subscriptions.map((item) => item.fundId)}
          userId={currentClient.userId}
          getCurrentClient={getCurrentClient}
          getHistory={getHistory}
        />
      }
      <br />
      <h5>Mi Historial</h5>
      <HistoryTable
        history={history}
        setHistory={setHistory}
        setModalOpen={setModalOpen}
        setModalMessage={setModalMessage}
        getHistory={getHistory}
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
