import { useEffect, useState } from "react";
import Chart from "../Chart";
// import API_ENDPOINT from .env

function HomePage() {
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
    /*
    const response = await fetch(api_endpoint, {
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    });
    const data = await response.json();
*/

    return [
      {
        name: "adrian",
        count: "1",
      },
      {
        name: "jordan",
        count: "1",
      },
      {
        name: "atri",
        count: "2",
      },
      {
        name: "tej",
        count: "2",
      },
      {
        name: "jonathan",
        count: "3",
      },
      {
        name: "adrien",
        count: "4",
      },
      {
        name: "sammy",
        count: "4",
      },
      {
        name: "ian",
        count: "5",
      },
      {
        name: "julian",
        count: "5",
      },
    ];
  }

  return (
    <div>
      <div className="grid items-stretch">
        <div className="max-w-xl">
          <div className="max-w-xl">{data && <Chart data={data} />}</div>
          <div className="relative left-11 max-w-xl">
            <p>
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged. It was
              popularised in the 1960s with the release of Letraset sheets
              containing Lorem Ipsum passages, and more recently with desktop
              publishing software like Aldus PageMaker including versions of
              Lorem Ipsum.
            </p>
          </div>
        </div>
      </div>
      <div className="absolute top-10 right-12">
        <a>home</a>
        <br />
        <a href="/summary">summary</a>
        <br />
        <a>video</a>
        <br />
        <a>other</a>
      </div>
    </div>
  );
}

export default HomePage;
