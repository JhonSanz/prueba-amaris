import React, { useState, useEffect } from 'react';
import '../styles/fundsTable.css';


const HistoryTable = ({ history, setHistory, getHistory, setModalOpen, setModalMessage }) => {

  useEffect(() => {
    async function init() {
      await getHistory();
    }
    init();
  }, []);

  return (
    <div className="history-table-container">
      <table className="history-table">
        <thead>
          <tr>
            <th>Transaction ID</th>
            <th>User ID</th>
            <th>Fund ID</th>
            <th>Amount</th>
            <th>Type</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {history.map((fund) => (
            <tr key={fund.id}>
              <td>{fund.transactionId}</td>
              <td>{fund.userId}</td>
              <td>{fund.fundId}</td>
              <td>{fund.amount}</td>
              <td>{fund.type}</td>
              <td>{fund.timestamp}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default HistoryTable;