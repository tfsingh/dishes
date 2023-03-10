import React from "react";
import { VictoryChart, VictoryBar, VictoryAxis, VictoryLabel } from "victory";

const Chart = ({ data }) => {
  return (
    <VictoryChart domainPadding={{ x: 40, y: 40 }} animate={{ duration: 1000 }}>
      <VictoryAxis
        tickValues={data.map((item) => item.name)}
        style={{
          tickLabels: {
            fontSize: 10,
            padding: 5,
            angle: -45,
            textAnchor: "end",
          },
        }}
      />
      <VictoryAxis
        dependentAxis
        domain={[0, Math.max(...data.map((item) => Number(item.count)))]}
      />
      <VictoryBar
        data={data.sort((a, b) => Number(a.count) - Number(b.count))}
        x="name"
        y="count"
      />
    </VictoryChart>
  );
};

export default Chart;
