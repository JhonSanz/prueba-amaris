import { useState, useEffect } from 'react';
import '../styles/fundsTable.css';


const FundsTable = ({
  userId,
  clientSubscriptions,
  getCurrentClient,
  getHistory,
  setModalOpen,
  setModalMessage
}) => {
  const [funds, setFunds] = useState([]);

  async function getFunds() {
    try {
      const response = await fetch(`/fund/list`);
      if (!response.ok) {
        throw new Error(`Error: ${response.status} - ${response.statusText}`);
      }
      const data = await response.json();
      setFunds(data.result);
    } catch (error) {
      setModalOpen(true);
      setModalMessage('Error fetching investment funds');
      return null;
    }
  }

  useEffect(() => {
    async function init() {
      await getFunds();
    }
    init();
  }, []);

  async function subscribeToFund(fundId) {
    const data = {
      userId: userId,
      fundId: fundId,
      amount: 0,
      type: "subscription"
    }
    try {
      const response = await fetch(
        `/fund/subscribe`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
      const result = await response.json();
      if (!result.success) {
        setModalOpen(true);
        setModalMessage(result.message);
      }
      await getCurrentClient();
      await getHistory();
    } catch (error) {
      setModalOpen(true);
      setModalMessage('Error fetching investment funds');
      return null;
    }
  }

  async function desubscribeToFund(fundId) {
    const data = {
      userId: userId,
      fundId: fundId,
      amount: 0,
      type: "unsubscription"
    }
    try {
      const response = await fetch(
        `/fund/unsubscribe`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
      if (!response.ok) {
        setModalOpen(true);
        setModalMessage('Error fetching investment funds');
      }
      const result = await response.json();
      console.log('Success:', result);
      await getCurrentClient();
      await getHistory();
    } catch (error) {
      setModalOpen(true);
      setModalMessage('Error fetching investment funds');
      console.error('Error:', error);
    }
  }

  return (
    <div className="funds-table-container">
      <table className="funds-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Monto Mínimo de Vinculación</th>
            <th>Categoría</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {funds.map((fund) => (
            <tr key={fund.fundId}>
              <td>{fund.fundId}</td>
              <td>{fund.name}</td>
              <td>${fund.amount}</td>
              <td>{fund.category}</td>
              <td>
                {
                  !clientSubscriptions.includes(fund.fundId) && <button
                    onClick={() => subscribeToFund(fund.fundId)}
                  >Suscribirse</button>
                }
                {
                  clientSubscriptions.includes(fund.fundId) && (
                    <button
                      className="unsubscribe-button"
                      onClick={() => desubscribeToFund(fund.fundId)}
                    >Desuscribirse</button>
                  )
                }
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default FundsTable;