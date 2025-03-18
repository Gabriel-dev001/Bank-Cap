import React from "react";
import { TouchableOpacity, Image, Text, StyleSheet } from "react-native";
import { googleApi } from "../../services/authService";

const GoogleLoginButton: React.FC = () => {
  const { request, promptAsync, handleGoogleLogin } = googleApi();

  return (
    <TouchableOpacity
      style={styles.button}
      onPress={() => {
        if (request) {
          promptAsync();
        } else {
          console.error("Erro ao iniciar autenticação com Google");
        }
      }}
    >
      <Image source={require("../../assets/google.png")} style={styles.icon} />
      <Text style={styles.text}>Continuar com Google</Text>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
button: {
    width: "85%",
    height: 50,
    backgroundColor: "rgb(0, 71, 187)",
    flexDirection: "row",
    alignItems: "center",
    borderRadius: 12,
    marginTop: 10,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 3 },
    shadowOpacity: 0.3,
    shadowRadius: 4,
    paddingVertical: 12,
    paddingHorizontal: 20,
  },
  icon: {
    width: 35,
    height: 35,
    marginRight: 15,
  },
  text: {
    fontSize: 15,
    color: "#FFF",
    fontWeight: "bold",
    textAlign: "center",
    opacity: 0.8,
  },
});

export default GoogleLoginButton;
