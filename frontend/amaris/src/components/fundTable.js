import { useState, useEffect } from 'react';


const FundsTable = ({ setModalOpen, setModalMessage }) => {
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
            <tr key={fund.id}>
              <td style={styles.td}>{fund["fundId"]}</td>
              <td style={styles.td}>{fund["name"]}</td>
              <td style={styles.td}>${fund["amount"]}</td>
              <td style={styles.td}>{fund["category"]}</td>
              <td style={styles.td}>
                <button>suscribirse</button>
                <button style={{ marginLeft: 5, backgroundColor: "red" }}>desuscribirse</button>
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
