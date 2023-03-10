import "./App.css";
import { useEffect, useState } from "react";
import Chart from "./Chart";

// import API_ENDPOINT from .env

function App() {
  const api_endpoint = process.env.REACT_APP_API_ENDPOINT;
  const [data, setData] = useState();

  useEffect(() => {
    async function fetchData() {
      const data = await callApi();
      setData(data);
    }
    fetchData();
  }, []);

  async function callApi() {
    const response = await fetch(api_endpoint, {
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    });
    const data = await response.json();
    return data;
  }

  return (
    <div>
      <div className="max-w-xl">{data && <Chart data={data} />}</div>
    </div>
  );
}

export default App;
