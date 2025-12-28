import React, { useEffect, useState } from 'react';

const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

function Activities() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        console.log('Activities API URL:', API_URL);
        console.log('Fetched data:', results);
        setData(results);
      });
  }, []);

  return (
    <div>
      <h2>Activities</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            {data[0] && Object.keys(data[0]).map(key => <th key={key}>{key}</th>)}
          </tr>
        </thead>
        <tbody>
          {data.map((item, idx) => (
            <tr key={idx}>
              {Object.values(item).map((val, i) => <td key={i}>{val?.toString()}</td>)}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Activities;
