import React from "react";
import { View, Text, Dimensions } from "react-native";
import { PieChart } from "react-native-chart-kit";

interface DonutChartProps {
  receitaTotal: number;
  despesas: number;
}

const DonutChart: React.FC<DonutChartProps> = ({ receitaTotal = 0, despesas = 0 }) => {
  const saldo = receitaTotal - despesas;
  console.log(saldo)

  const data = [
    {
      name: "Despesas",
      population: despesas,
      color: "rgba(199, 0, 0, 0.9)",
      legendFontColor: "#7F7F7F",
      legendFontSize: 15,
    },
    {
      name: "Saldo",
      population: saldo > 0 ? saldo : 0,
      color: "rgba(255, 255, 255, 0.5)",
      legendFontColor: "#7F7F7F",
      legendFontSize: 15,
    },
  ];

  return (
    <View style={{ alignItems: "center" }}>
      <PieChart
        data={data}
        width={200}  
        height={250} 
        chartConfig={{
          backgroundGradientFrom: "transparent",
          backgroundGradientTo: "transparent",
          color: () => "rgba(0, 0, 0, 0)", 
        }}
        accessor={"population"}
        backgroundColor={"transparent"}
        paddingLeft={"0"}
        hasLegend={false} 
        center={[50, 0]} 
        absolute
        />

        <View
            style={{
            position: "absolute",
            width: 150, 
            height: 150,
            borderRadius: 80,
            backgroundColor: "black", 
            top: 50,
            left: 25,
            alignItems: "center",
            justifyContent: "center",
        }}
        >
        <Text style={{ color: "white", fontSize: 18, fontWeight: "bold" }}>
          R$ {saldo.toFixed(2)}
        </Text>
      </View>

    </View>
  );
};

export default () => <DonutChart receitaTotal={5000} despesas={3000} />;
