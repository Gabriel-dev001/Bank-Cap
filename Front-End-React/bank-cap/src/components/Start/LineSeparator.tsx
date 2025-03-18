import React from "react";
import { View, StyleSheet } from "react-native";

const LineSeparator = () => {
  return <View style={styles.line} />;
};

const styles = StyleSheet.create({
  line: {
    width: "90%", // Ocupa 90% da largura da tela
    height: 1, // Espessura da linha
    backgroundColor: "#ccc", // Cor cinza clara
    marginVertical: 10, // Espaçamento acima e abaixo
    alignSelf: "center", // Centraliza a linha na tela
  },
});

export default LineSeparator;
