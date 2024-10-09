import React, { useState, useEffect } from 'react';


const HistoryTable = ({ setModalOpen, setModalMessage }) => {
  const [history, setHistory] = useState([]);

  async function getHistory() {
    try {
      const response = await fetch('http://localhost:8000/fund/history');
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

  useEffect(() => {
    async function init() {
      await getHistory();
    }
    init();
  }, []);

  return (
    <div style={{ overflowX: 'auto' }}>
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th>PK</th>
            <th>SK</th>
            <th>TipoEntidad</th>
            <th>FondoID</th>
            <th>FondoNombre</th>
            <th>TipoTransaccion</th>
            <th>Monto</th>
            <th>SaldoRestante</th>
            <th>Fecha</th>
            <th>Notificacion</th>
          </tr>
        </thead>
        <tbody>
          {history.map((fund) => (
            <tr key={fund.id}>
              <td style={styles.td}>{fund["PK"]}</td>
              <td style={styles.td}>{fund["SK"]}</td>
              <td style={styles.td}>{fund["TipoEntidad"]}</td>
              <td style={styles.td}>{fund["FondoID"]}</td>
              <td style={styles.td}>{fund["FondoNombre"]}</td>
              <td style={styles.td}>{fund["TipoTransaccion"]}</td>
              <td style={styles.td}>{fund["Monto"]}</td>
              <td style={styles.td}>{fund["SaldoRestante"]}</td>
              <td style={styles.td}>{fund["Fecha"]}</td>
              <td style={styles.td}>{fund["Notificacion"]}</td>
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

export default HistoryTable;
