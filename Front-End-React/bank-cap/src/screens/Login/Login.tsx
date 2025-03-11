import React, { useState } from "react";
import {
  View,
  Text,
  TouchableOpacity,
  ImageBackground,
  Keyboard,
  TouchableWithoutFeedback,
} from "react-native";
import { StackNavigationProp } from "@react-navigation/stack";
import { RouteProp } from "@react-navigation/native";
import Title from "../../components/Title";
import SubTitleText from "../../components/SubTitleText";
import InputText from "../../components/InputText";
import ButtonTextCenter from "../../components/ButtonTextCenter";
import ErrorMessage from "../../components/ErrorMessage";
import StyleLogin from "./StyleLogin";
import { loginApi } from "../../services/authService";

// Definição dos tipos de navegação
type RootStackParamList = {
  Login: undefined;
  Register: undefined;
  Main: undefined;
  Start: { userId: string };
};

type LoginScreenNavigationProp = StackNavigationProp<RootStackParamList,"Login">;
type LoginScreenRouteProp = RouteProp<RootStackParamList, "Login">;

type Props = {
  navigation: LoginScreenNavigationProp;
  route: LoginScreenRouteProp;
};

const Login: React.FC<Props> = ({ navigation }) => {
  const [email, setEmail] = useState("");
  const [emailError, setEmailError] = useState("");
  const [password, setPassword] = useState("");
  const [apiError, setApiError] = useState("");

  async function handleLogin() {
    if (emailError) return;

    const data = await loginApi(email, password);

    if (!data) {
      setApiError("Credenciais Invalídas.");
      return;
    }

    navigation.navigate("Start", { userId: String(data.id_usuario) });
  }

  function validateEmail(text: string) {
    setEmail(text);
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    setEmailError(emailRegex.test(text) ? "" : "E-mail inválido");
  }

  return (
    <ImageBackground
      source={require("../../assets/background.jpg")}
      style={StyleLogin.background}
    >
      <TouchableWithoutFeedback onPress={Keyboard.dismiss} accessible={false}>
        <>
          <View style={StyleLogin.container}>
            <Title>Bank Cap</Title>
            <SubTitleText>Login</SubTitleText>

            <View style={{ alignSelf: "flex-start", width: "85%" }}>
              <Text style={StyleLogin.textSmall}>Email:</Text>
            </View>

            <InputText
              onChangeText={validateEmail}
              keyboardType="email-address"
              autoCapitalize="none"
            />

            <View style={{ alignSelf: "flex-start", width: "85%" }}>
              <Text style={StyleLogin.textSmall}>Senha:</Text>
            </View>

            <InputText
              secureTextEntry={true}
              value={password}
              onChangeText={setPassword}
            />

            <ErrorMessage message={emailError} />
            <ErrorMessage message={apiError || ""} />

            <ButtonTextCenter title="Entrar" onPress={handleLogin} />

            <TouchableOpacity onPress={() => navigation.navigate("Register")}>
              <Text style={StyleLogin.linkText}>Não tem conta? Registre-se</Text>
            </TouchableOpacity>
          </View>
        </>
      </TouchableWithoutFeedback>
    </ImageBackground>
  );
};

export default Login;