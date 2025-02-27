import React from "react";
import { Text, StyleSheet } from "react-native";

interface ErrorMessageProps {
  message?: string; 
}

const ErrorMessage: React.FC<ErrorMessageProps> = ({ message }) => {
  if (!message) return null; // Se não houver erro, não renderiza nada

  return <Text style={styles.errorText}>{message}</Text>;
};

const styles = StyleSheet.create({
  errorText: {
    color: "red",
    fontSize: 14,
    marginTop: 5,
  },
});

export default ErrorMessage;
