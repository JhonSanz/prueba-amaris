import React from 'react';

const InvestmentFundsTable = ({ funds }) => {
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
              <td style={styles.td}>{fund.id}</td>
              <td style={styles.td}>{fund.nombre}</td>
              <td style={styles.td}>${fund.montoMinimo}</td>
              <td style={styles.td}>{fund.categoria}</td>
              <td style={styles.td}>
                <button>sus</button>
                <button>uns</button>
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

export default InvestmentFundsTable;
