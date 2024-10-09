import React, { useState, useEffect } from 'react';


const HistoryTable = ({ history, setHistory, getHistory, setModalOpen, setModalMessage }) => {

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
            <th style={styles.th}>transactionId</th>
            <th style={styles.th}>userId</th>
            <th style={styles.th}>fundId</th>
            <th style={styles.th}>amount</th>
            <th style={styles.th}>type</th>
            <th style={styles.th}>timestamp</th>
          </tr>
        </thead>
        <tbody>
          {history.map((fund) => (
            <tr key={fund.id}>
              <td style={styles.td}>{fund["transactionId"]}</td>
              <td style={styles.td}>{fund["userId"]}</td>
              <td style={styles.td}>{fund["fundId"]}</td>
              <td style={styles.td}>{fund["amount"]}</td>
              <td style={styles.td}>{fund["type"]}</td>
              <td style={styles.td}>{fund["timestamp"]}</td>
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
