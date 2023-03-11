import { useEffect, useState } from "react";
import Chart from "../Chart";
import NavBar from "./NavBar";
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
      <div className="grid items-stretch">
        <div className="max-w-xl">
          <div className="max-w-xl">{data && <Chart data={data} />}</div>
          <div className="relative left-11 max-w-xl">
            <p>
              Renowned author, historian, and theologian G.K. Chesterton once
              remarked, "Men did not love Rome because she was great. She was
              great because they had loved her." My fellow residents and I love
              our little home on Ravenna Blvd, for we wish for it to be as
              glorious as Rome once was. As victory is often the cause of the
              defeat of victors, I make it a point to extinguish anything that
              might endanger the sanctity of these precious grounds. I conducted
              a thorough analysis — I looked to the Germanic Tribes, but alas, I
              found them to pose no threat.
            </p>
            <br></br>
            <p>
              Indeed, the greatest risk to our well-being lay within our own
              ranks! Our housemates would leave dishes in the sink for weeks on
              end, enabling the proliferation of maleficent bacteria whose
              presence sullied these sacred grounds. However, I have been
              studying. Armed with the ancient secrets of computer vision, I set
              out on a course not just to detect who left the dishes in the
              sink, but also to ensure the prosperity of our great homestead for
              millennia to come!
            </p>
          </div>
        </div>
      </div>
      <NavBar />
    </div>
  );
}

export default HomePage;
