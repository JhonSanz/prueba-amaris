import { useState, useEffect } from 'react';


const FundsTable = ({ userId, clientSubscriptions, setModalOpen, setModalMessage }) => {
  const [funds, setFunds] = useState([]);

  async function getFunds() {
    try {
      const response = await fetch('http://localhost:8000/fund/list');
      if (!response.ok) {
        throw new Error(`Error: ${response.status} - ${response.statusText}`);
      }
      const data = await response.json();
      console.log(data)
      setFunds(data.result);
    } catch (error) {
      console.error('Error fetching investment funds:', error);
      return null;
    }
  };

  useEffect(() => {
    async function init() {
      await getFunds();
    }
    init();
  }, []);


  async function subscribeToFund(fundId) {
    const data = {
      "userId": userId,
      "fundId": fundId,
      "amount": 0,
      "type": "subscription"
    }
    try {
      const response = await fetch(
        'http://localhost:8000/fund/subscribe', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
      const result = await response.json();
      console.log('Success:', result);
    } catch (error) {
      console.error('Error:', error);
    }
  }

  async function desubscribeToFund(fundId) {

  }

  return (
    <div style={{ overflowX: 'auto' }}>
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th style={styles.th}>ID</th>
            <th style={styles.th}>Nombre</th>
            <th style={styles.th}>Monto Mínimo de Vinculación</th>
            <th style={styles.th}>Categoría</th>
            <th style={styles.th}>actions</th>
          </tr>
        </thead>
        <tbody>
          {funds.map((fund) => (
            <tr key={fund.fundId}>
              <td style={styles.td}>{fund["fundId"]}</td>
              <td style={styles.td}>{fund["name"]}</td>
              <td style={styles.td}>${fund["amount"]}</td>
              <td style={styles.td}>{fund["category"]}</td>
              <td style={styles.td}>
                {
                  !clientSubscriptions.includes(fund.fundId) && <button
                    onClick={() => subscribeToFund(fund.fundId)}
                  >suscribirse</button>
                }
                {
                  clientSubscriptions.includes(fund.fundId) && (
                    <button
                      style={{ marginLeft: 5, backgroundColor: "red" }}
                      onClick={() => desubscribeToFund(fund.fundId)}
                    >desuscribirse</button>
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

const styles = {
  th: {
    border: '1px solid #dddddd',
    textAlign: 'left',
    padding: '8px',
  },
  td: {
    border: '1px solid #dddddd',
    textAlign: 'left',
    padding: '8px',
  },
};

export default FundsTable;
