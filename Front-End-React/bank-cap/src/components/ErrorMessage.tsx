import React from "react";
import { Text, StyleSheet } from "react-native";

interface ErrorMessageProps {
  message?: string; 
}

const ErrorMessage: React.FC<ErrorMessageProps> = ({ message }) => {
  if (!message || typeof message !== "string") return null; // Evita renderizar algo inválido

  return <Text style={styles.errorText}>{message.toString()}</Text>;
};


const styles = StyleSheet.create({
  errorText: {
    color: "red",
    fontSize: 14,
    marginTop: 5,
  },
});

export default ErrorMessage;
